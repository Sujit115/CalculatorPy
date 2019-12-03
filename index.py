import Calculator


leftOperand = int(input())
rightOperand = int(input())
operator = input()


calc = Calculator.Calculator(leftOperand,rightOperand,operator)
calc.calculate()
print(calc.output)