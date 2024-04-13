# if condition:
#   if true then it will execute
# else:
#   if false then else statement will execute

#Comparison operators   
#Equals: a == b         ⁄ Greater than: a > b
#Not Equals: a != b     ⁄ Greater or equal to: a >= b
#Less than: a < b       ⁄ Logical: and, or
#Identity: is, is not   ⁄ Membership: in, not in

number1 = 6
number2 = 44
number3 = 61

if number1 > number2:
    print(f"{number1} is greater than {number2}")

if number1 > number3:
    print(f"{number1} is greater than {number3}")
elif number3 > number2:
    print((f"{number3} is greater than {number2}"))
else:
    print("All the statements are False")