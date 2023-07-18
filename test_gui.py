import pytest
import gui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox,QApplication,QPushButton
from PySide2 import QtCore
import warnings
import os
import sys

@pytest.fixture
def app(qtbot):
    window = gui.MainWindow()
    qtbot.addWidget(window)
    return window

### if flag_test ==1 ---> means that the warning message appear and input is invalid

# test click plot without writing the functiom
def test_1(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test ==1

# test invalid_x_min
def test_2(app, qtbot):
    window = app
    window.function_widget.flag_test=0

    window.function_widget.fun_textbox.setText("2x") #edit
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)

    assert window.function_widget.flag_test ==1

# # test invalid_x_max
def test_3(app, qtbot):
    window = app
    window.function_widget.flag_test=0

    window.function_widget.fun_textbox.setText("2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

#test the graph is plotted or not
def test_4(app, qtbot):
    window = app
    window.function_widget.fun_textbox.setText("5") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert len(window.function_widget.ax.lines)>0

#test when x_min > x_max
def test_5(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x(2+)") #edit
    window.function_widget.x_min_textbox.setText("10")
    window.function_widget.x_max_textbox.setText("0")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

#test valid input
def test_6(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    assert window.function_widget.flag_test == 0

#test invalid input
def test_7(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)

    assert window.function_widget.flag_test == 1


def test_8(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("  ") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)

    assert window.function_widget.flag_test == 1


def test_9(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.5(x+2).") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1


def test_10(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.5(x+2)#") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1


def test_11(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.5!(x+2)") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1


def test_12(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_13(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2X") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_14(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_15(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2,x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_16(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.5(x+2)") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_17(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2.+x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_18(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("+2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_19(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("-2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_20(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("*2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_21(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("/2x") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_22(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x//2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_23(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x**2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_24(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x^2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_25(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x***2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_26(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x---2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_27(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x+++2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_28(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x++*2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_29(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x^^2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_30(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("+") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_31(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2y") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_32(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("x2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_33(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("(2+x)8") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0


def test_34(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("(2x+8") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_35(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("{2+x)8") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_36(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("[3x+3]2") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_37(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x(4+8)") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 0

def test_38(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("()") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_39(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("{}") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1

def test_40(app, qtbot):
    window = app
    window.function_widget.flag_test=0
    window.function_widget.fun_textbox.setText("2x(2+)") #edit
    window.function_widget.x_min_textbox.setText("0")
    window.function_widget.x_max_textbox.setText("10")
    qtbot.mouseClick(window.function_widget.plot_button, Qt.LeftButton)
    assert window.function_widget.flag_test == 1
