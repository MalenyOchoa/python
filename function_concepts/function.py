# A function is a block of code that it's executed when we call it.
# Types: Non-parameter function, parameter function, return type function.
# Using 'def' will create it and the name should be camel case:
# def functionName():

#Non-parameter
def myFirstFunction():
    print("This is my function")

myFirstFunction() #here i'm callin it

#Parameter function
def mySecondFunction(message):
    print(message)

mySecondFunction("this is the parameter i'm sending to the finction")

#Return type
def sumOfTwoNumbers(number1, number2):
    sum = number1 + number2
    return sum

result = sumOfTwoNumbers(10, 5) #here we call the function and sending the parameters expected
print(f"The result is: {result}")

#Default value in parameter type of function
def divisionOfTwoNumbers(number1, number2 = 10): #by default the second number is defined, if the user does not define it the function will continue running
    result = number1 / number2
    return result

result = divisionOfTwoNumbers(100) #here we send the expected parameter and using the default value
print(f"The result is: {result}")

#Pass list value to the function
def listValue(elements):
    for element in elements:     
        print(element, end = ',') #Use 'end' parameter to print all in one line
listValue(range(0,3)) #instead of a list i'm using a range of values

