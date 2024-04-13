#************ Tuple Data Type ************
# - Storing the different data type values in order and tuple is unchangeable in run time.
# - It allows duplicated values
# - Values should be assignm to a variable in '()'
#   Example: name_tuple = (1, "python", 2.3, 1)
#Can't add value
#Can't update 
#Can't insert value
#Can't remove value

my_tuple = ( 1, 1, 2, 3, 4, 5)

#Access the values in a tuple tupleName[indexValue]
search_index_in_tuple = my_tuple[5]
print(f"Your value searched by index is: {search_index_in_tuple}")

#Slicing - [1:n-1]
slicing_tuple = my_tuple[3:5]
print(f"Your slice includes: {slicing_tuple}")

#Length of a tuple - len()
print(f"The length of your tuple is: {len(my_tuple)}")

#Find how many times a value is repeated
print(f"{my_tuple.count(1)}: is the number of times the value is repeated.")

#How to find value
finded_value = 1 in my_tuple
if finded_value:
    print(f"{finded_value}: the value you're searching exists in your tuple")
else:
    print(f"{finded_value}: the value you're searching is not in your tuple")
#Add tuple items '+'
first_tuple = (1, 1, 1)
second_tuple = (2, 2, 2)
third_tuple = first_tuple + second_tuple
print(f"Your tuples are merged: {third_tuple}")

#Iterate values
print("The values in your tuple are listed following:")
for value in my_tuple:
    print(value)