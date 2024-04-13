number1 = 5
number2 = 10

suma = number1 + number2
print (f"El resultado de {number1} + {number2} es: {suma}")

resta = number1 - number2
print(f"El resultado de {number1} - {number2} es: {resta}")

multiply = number1 * number2
print(f"El resultado de {number1} * {number2} es: {multiply}")

division = number1 / number2 #division always returns a float data type
print(f"El resultado de {number1} / {number2} es: {division}")
#you can chop the numbers of a division to get a int by using // doble
 
#Find the string in a sentence using membership operators - (in, not in)
#If the string is present in the sentence then it will return True
sentence = "Hey this is a sentence"
hey = "Hey"
bee = "Bee"
is_it_there = hey in sentence 
is_not_there =  bee in sentence
print(f"Is '{hey}' present in the sentence: {sentence} : {is_it_there}")
print(f"Is '{bee}' present in the sentence: {sentence} : {is_not_there}")