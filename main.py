
class Calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def add(self):
        return self.number1+self.number2
    def subract(self):
        return self.number1-self.number2
    def multiply(self):
        return self.number1*self.number2
    def divide(self):
        return self.number1/self.number2
    def operation(self,user_Operation):
        if user_Operation == '+':
            return self.add()

        elif user_Operation == '-':
            return self.subract()
        elif user_Operation== '*':
            return self.multiply()
        elif user_Operation == '/':
            return self.divide()
        else:
            print("Invalid input")

user_input=input("Enter the inputs ")
user_input=user_input.strip().split()


number1=int(user_input[0])
number2=int(user_input[2])
user_operation=user_input[1]
calc= Calculator(number1,number2)
result=calc.operation(user_operation)
print(result)










