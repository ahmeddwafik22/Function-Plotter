import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QLineEdit,QMessageBox,QPushButton,QLabel
from PySide2.QtCore import Qt
from PySide2.QtWebEngineWidgets import QWebEngineView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import eval_system
import re
import math

_not_testing=True

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.function_widget = FunctionInputWidget()
        self.layout.addWidget(self.function_widget)

        self.plot_widget = PlotWidget()
        self.layout.addWidget(self.plot_widget)

        self.function_widget.set_plot_widget(self.plot_widget)


class FunctionInputWidget(QWidget):

    def __init__(self):
        super(FunctionInputWidget, self).__init__()


        self.flag_test=0 ## this is used when testing the GUI

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.fun_textbox = QLineEdit(self)
        self.fun_textbox.setPlaceholderText("Enter a function (e.g., x**2 + 3*x)")
        self.fun_textbox.returnPressed.connect(self.plot_function)
        self.layout.addWidget(self.fun_textbox)

        self.x_min_label = QLabel("x_min", self)
        self.x_min_label.move(250,250)
        self.layout.addWidget(self.x_min_label)

        self.x_min_textbox = QLineEdit(self)
        self.x_min_textbox.move(250, 280)
        self.layout.addWidget(self.x_min_textbox)

        self.x_max_label = QLabel("x_max", self)
        self.x_max_label.move(280,250)
        self.layout.addWidget(self.x_max_label)

        self.x_max_textbox = QLineEdit(self)
        self.x_max_textbox.move(280, 280)
        self.layout.addWidget(self.x_max_textbox)

        self.plot_button = QPushButton("plot", self)
        self.plot_button.move(20, 80)
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

        self.eval_sys=eval_system.eval_service()


        self.plot_widget = None
        self.ax=None


    def set_plot_widget(self,plot_widget):
        self.plot_widget=plot_widget

    def plot_function(self):
        self.plot_widget.refresh()

        function_text=self.fun_textbox.text()
        x_min=self.x_min_textbox.text()
        x_max=self.x_max_textbox.text()

        if(len(function_text)==0):
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "please write your function")

        elif len(x_min)==0:
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "please write your x_min")

        elif not re.match(r'^-?\d+(?:\.\d+)?$', x_min):
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "Invalid x_min")

        elif len(x_max)==0:
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "please write your x_max")

        elif not re.match(r'^-?\d+(?:\.\d+)?$', x_max):
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "Invalid x_max")

        elif float(x_min)> float(x_max):
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "x_min is bigger than x_max")

        elif float(x_min) ==float(x_max):
            self.flag_test=1
            if _not_testing:
                QMessageBox.warning(self,"Warning", "x_min is equal x_max")

        else:
            self.valid,self.s=self.eval_sys.preprocess_text(function_text)

            if(self.valid==False):
                self.flag_test=1
                if _not_testing:
                    QMessageBox.warning(self,"Warning", self.s)

            else:
                try:
                    x,y=self.eval_sys.eval(self.s,float(x_min),float(x_max))
                    if math.inf in y:
                         self.flag_test=1
                         if _not_testing:
                            QMessageBox.warning(self,"Warning", "Invalid Function")
                    else:
                        self.ax=self.plot_widget.plot(x,y,self.s)

                except Exception as e:
                    self.flag_test=1
                    if _not_testing:
                        QMessageBox.warning(self,"Warning", "Invalid Function")

                    print("Error plotting function:", e)


class PlotWidget(QWidget):
    def __init__(self):
        super(PlotWidget, self).__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def refresh(self):
        self.layout.removeWidget(self.canvas)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def plot(self, x, y,fun_x):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')

        plt.title('Graph of f(x) = '+fun_x)
        self.canvas.draw()

        return ax


if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())
