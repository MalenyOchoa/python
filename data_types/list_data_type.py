#************ List Data Type ************
# - Storing the diferent data type values in order and list is changeable in run time. 
# it allows duplicate values
# - Values should assing to a variable in square brackets []

my_list = [1, "python", 2.3, 4, "last"] #this is not recomended, you never should use diferent data types on a list
print(my_list)
print(type(my_list))

#access the valus on a list listName[indexValue]
index_1 = my_list[1]
print(index_1)

#Update a value in the list
my_list[1] = 2
print(f"The list is updated, the new value is: {my_list[1]}")

#Knowing the length od a list using the function len()
print(f"Your list has: {len(my_list)} items")

#To print from the last item of the list you can use minus nmbers and it will print from the last
index_negative = my_list[-1]
print(index_negative)

#add elements to the list
my_list.extend(["added items", "new item"])
print(my_list)

#Remove an item from the list
print(f"The list is currently: {my_list}")
my_list.remove(2.3)
print(f"The value has beein removed, the list is now: {my_list}")

#Inserting a value insert(index, "Value")
my_list.insert(2,3)
print(f"The value has beein inserted, the list is now: {my_list}")

#Find a value in the list using membership operators and validated with if/else statement
element = "perro" in my_list
if element:
    print(f"{element}: Your element exists in the list")
else:
    print(f"{element}: Your element does not exists in the list")


#index beyond the index will return an error "list index out of range"
#index_error = my_list[7]
#print(index_error)

#Nested lists
first_list = ["item1, item2, item3"]
second_list = ["item4, item5, item5"]
nested_list = [first_list, second_list]
print(f"This are the lists inside the list:")
for list in nested_list:
    print(list)

#Join lists items
jointed_lists = first_list + second_list
print(f"Merged: {jointed_lists}")

#Delete list
del second_list
print("List deleted, you will receive an error if try to print it")
#print(second_list)