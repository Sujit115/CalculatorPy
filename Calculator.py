
class Calculator():
    __leftOperand = ""
    __rightOperand = ""
    __operator = ""
    __output = ""

    def __init__(self, leftOperand, rightOperand, operator):
        self.__leftOperand = leftOperand
        self.__rightOperand = rightOperand
        self.__operator = operator 

    def calculate(self):
        if self.__operator == "+":
            self.__output = self.__leftOperand + self.__rightOperand

        if self.__operator == "/":

            try:
                self.__output = self.__leftOperand / self.__rightOperand
            except:
                while self.__rightOperand == 0:
                    self.__rightOperand = int(input("The denominator should not be 0"))

    def getOutput(self):
        return self.__output
    
    
        

    
