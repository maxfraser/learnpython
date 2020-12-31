class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1/num2

    def multiply(self, num1, num2):
        return num1*num2

    def power(self, num1, pownum2):
        return num1**pownum2

    def say_hello(self):
        print("Hello")

calc = Calculator()
calc.say_hello()
# print(calc.subtract(5, 2))


say_hello()