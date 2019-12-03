class Calculator():
    leftOperand = ""
    rightOperand = ""
    operator = ""
    output = ""


    def __init__(self, leftOperand, rightOperand, operator):
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.operator = operator 

    
    def calculate(self):
        if self.operator == "+":
            self.output = self.leftOperand + self.rightOperand

        if self.operator == "*":
            self.output = self.leftOperand * self.rightOperand

    
