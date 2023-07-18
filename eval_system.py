import numpy as np

class _eval_service:

    _instance=None ## this variable is used to support singleton pattern

    # valid the function_of_x and preprocess it to be ready for evaluation
    def preprocess_text(self,function_text):

        """
        :param:
                function_text: this is the function of x that will take from the user

        :return:
                 valid --> boolean variable if it is true --> valid input , false --> invalid_input
                 s--> preprocessed_function_of_x if valid is true otherwise s--> warning_message
        """

        function_text=function_text.lower()

        function_text=function_text.replace(" ","") ## remove_spaces
        function_text=function_text.replace(",",".")


        if(len(function_text)==0):
            return False,"Your function is empty"

        s=""
        stack=[] ## this is used when validating the parenthesis
        paren_dic={")":"(","]":"[","}":"{"}
        oper={"*","/","+","-","^"}
        prev_oper="" ## this is used to know what is the previous operation in the loop
        prev_c=""
        count_oper=0 ## this is used to handle something like (5--x) to be (5++x)
        appear=False ## this is used to know that the digit or "x" appear at least once or not

        if function_text[-1] in oper:
            return False,"Invalid Function as you write: "+function_text[-1]+" without any digit"

        if function_text[-1] ==".":
            return False,"Invalid Function as you write: '.' operation at the end of the string"

        for c in function_text:
            if c in oper:
                if prev_c==".": ## this is to handle something like (5.) to be (5.0)
                    s+="0"
                    prev_c="0"

                if not appear and c in {"*","/","^"}: ## this is to check if there is invalid_example like that (*5)
                    return False,"Invalid function as you begin with "+c

                if prev_oper==c: ## this is to check if there is invalid_example like that (5^^2)
                    if c in {"/","^"}:
                        return False,"Invalid Function as you write invalid operation"
                    else:
                        count_oper+=1
                else:
                    if prev_c in oper:  ## this is to check if there is invalid_example like that (5+*X)
                        return False,"Invalid Function as you write invalid operation"
                    prev_oper=c
                    count_oper=1

            if(prev_oper!="") and c not in oper : ## this condition when that we count the operations to put it before digit or "x" or parenthesis

                if(prev_oper=="*"):
                    if(count_oper==1):
                        s+="*"
                    elif(count_oper!=2):
                        return False, "Invalid Function as you write invalid operation"
                    else:
                        s+="**"

                if(prev_oper=="^"):
                    s+="**"

                if(prev_oper=="/"):
                    s+="/"

                if(prev_oper=="+"):
                    s+="+"
                if(prev_oper=="-"):
                    if(count_oper%2==0):
                        s+="+"
                    else:
                        s+="-"
                prev_oper="" # this is made to not reach the condition again until we found another opeation

            if c.isnumeric():
                if(not appear):
                    appear=True
                if prev_c=="x" or prev_c in paren_dic: ## to handle example like (x5) to be (x*5)
                    s+="*"
                s+=c

            elif c.isalpha():
                if prev_c ==".":
                    s+="0"
                    prev_c="0"
                if(not appear):
                    appear=True
                if c  != "x":
                    return False,"Invalid Function as Your function are not function of x"
                else:
                    if(prev_c.isnumeric()):
                        s+="*"
                    s+=c

            elif c in paren_dic:
                if stack and stack[-1]==paren_dic[c]:
                    stack.pop()
                    s+=c
                else:
                    return False,"Invalid parenthesis"

                if(prev_c in oper or prev_c in paren_dic.values()):
                    return False,"Invalid function, please revise that you write between the parenthesis"


            elif c in paren_dic.values():
                stack.append(c)
                if prev_c ==".":
                    s+="0"
                    prev_c="0"
                if prev_c.isdigit() or prev_c=="x" or prev_c in paren_dic:
                    s+="*"

                s+=c

            else:
                prev_c=c
                if c in oper:
                    continue
                if(c=="."):
                    s+=c
                else:

                    return False,"Invalid Function"

            prev_c=c

        s=s.replace("[","(")
        s=s.replace("]",")")

        s=s.replace("{","(")
        s=s.replace("}",")")

        return (True,s) if not stack else (False,"Invalid Paraenthesis")


    def eval(self,function_text,x_min,x_max):
        """
        :param function_text: "preprocessed_function_of_x"
        :param x_min: "min range of the graph"
        :param x_max: "max range of the graph"
        :return: "x,y to be ready for plotting"
        """
        function = lambda x:  np.full_like(x, eval(function_text))
        x = np.arange(x_min, x_max,0.1)
        y = function(x)

        return x,y


## this service to support singleton pattern as we there is no more than one object to use
def eval_service():
    if _eval_service._instance is None:
        _eval_service._instance=_eval_service()
    return _eval_service._instance
