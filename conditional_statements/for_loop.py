fruits = ["Apple", "Peach", "Orange"]

for fruit in fruits:
   print(fruit) #this will print each element of the list individually
   print(fruit + " juice") #this will be printed concatenated to the element of the list

#For loop with range
for number in range(1, 11, 3): #the third number indicates the 'jump'
    print(number)
    
#Gauss problem solved
total = 0
for number in range(1, 101):
    total += number
print(f"Your total is {total}")