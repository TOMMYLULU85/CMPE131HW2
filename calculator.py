def calculator(number1, number2, operator):
      """This function takes in 3 parameters because it needs the 3 parameters for the if statements"""
      if operator == '+':
        return float(number1)+float(number2)
      elif operator == '-':
        return float(number1)-float(number2)
      elif operator == '*':
        return float(number1)*float(number2)
      elif operator == '/':
        if number2 == 0:
           print("Can't divide by Zero")
        return float(number1)/float(number2)
      elif operator == '//':
        if number2 ==0:
           print("Can't divide by Zero")
        return float(number1)//float(number2)
      elif operator == '**':
        return float(number1)**float(number2)
      else:
        return False

      """These if statements are here because it goes through input_output and checks if its the right operation sign"""
      """The else statement is here because once the operation signs are not the ones listed above then it leaves"""

def input_output():
     """This function doesnt take any parameters due to it not needing it since it just prints out user inputs"""
     while True:
       number1 = input("Enter the first number: ")
       number2 = input("Enter the second number: ")
       operator = input("Enter the operation: ")
       calculator(number1,number2,operator)
       """The user inputs are here because you would need to ask the user input 2 numbers and an operation"""
       """The calculator(number1, number2, operator) calls on the function in order to do the operation"""
       answer = input("Do you wish to exit: ?")
       if answer == 'y':
          break
       """This if statement is here because it asks the user to exit the program and if the answer is yes then it stops the program"""

"""This whole function calls on the whole function because you would need to call on the function"""

