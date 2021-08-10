# AUTHOR - HIMANK JESHWAR
# DATE - 10/08/21

# This just a normal calculator for beginners. Its a just a initiate.
# This calculator takes 2 number and it can add,divide,substract and multiply.
# It can be improved! 

# YOU ARE FREE TO IMPROVE AND CUSTOMIZE THIS CALCULATOR

print("WELCOME QUICK Z CALCULATOR !")
print("YOU CAN ADD,MULTIPLY,DIVIDE,SUBSTRACT UPTO 2 NUMBERS")
class Calculator:
    def __init__(self,num):
        self.num=num
    def total(self,num2):
        return (f"{self.num} + {num2.num} = {self.num+num2.num}")
    def mul(self,num2):
        return (f"{self.num} X {num2.num} = {self.num*num2.num}") 
    def div(self,num2):
        return (f"{self.num} / {num2.num} = {self.num/num2.num}")
    def subt(self,num2):
        return (f"{self.num} - {num2.num} = {self.num-num2.num}")
operation=input("Which Operation would you like to do (choose the operand) (+),(-),(/),(*) = ")                
if operation=="+" or operation=="-" or operation=="*":
    num1=int(input("Enter First Number = "))
    num2=int(input("Enter the Second Number = "))
    num3=int(input("Enter Third Number = "))
    num4=int(input("Enter the Fourth Number = "))
if operation=="+":
    num1=Calculator(num1)
    num2=Calculator(num2)
    print(num1.total(num2))
elif operation=="-":
    num1=Calculator(num1)
    num2=Calculator(num2)
    print(num1.subt(num2))
elif operation=="*":
    num1=Calculator(num1)
    num2=Calculator(num2)
    print(num1.mul(num2))
elif operation=="/":
    dividend=int(input("Enter Dividend = "))
    divisor=int(input("Enter Divisor = ")) 
    num1=Calculator(dividend)
    num2=Calculator(divisor)
    print(num1.div(num2))
else:
    print("INVALID OPERAND ! Please Try Again.")    
