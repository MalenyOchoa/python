#************ Set Data Type ************
# - Storing the diferent data type values in order and Set is changeable in run time. 
# - It does NOT allows duplicated values
# - Values should be assigned in '{}'
#Used to clean data that has repeated values

#Create set
my_set = {1,3,2,5,4} #this will be ordered
print(my_set)
print(type(my_set))

#Can't insert value once created, but can add values
my_set.add(90)
print(f"Value added, your set is now: {my_set}")

#Length 
print(f"Your set has {len(my_set)} values")

#Remove value
my_set.remove(90)
print(f"Value removed, your set is now: {my_set}")

#you can have a list with repeated values that you want to clean
#you can cast the list into a set to clear de data.
my_list = ["Hello", "World", "Hello"]
print(set(my_list))
print(list(set(my_list))) #if needed you can make it a list again

#Discard()
my_set.discard(2)
print(f"Value discarded, your set is now: {my_set}")

#Pop() - for sets this will remove an element,
#however it's better tu use remove() / discard() to specify what to remove/discard
my_set.pop()
print(f"Value poped, your set is now: {my_set}")

#Join sets by using union() method not '+'
first_set = {4, 7, 9}
second_set = {10, 26, 2}
union_sets = first_set.union(second_set)
print(f"Your sets were united: {union_sets}")

#Iterate using membership operator
for value in union_sets:
    print(value)

#Find value present
data = 3 in my_set
if  data:
   print(f"{data}: This value exists.")
else:
    print(f"{data}: This value does not exist.")

#Clear
union_sets.clear()
print(union_sets) #this will print an empty set, it will run OK

#Delete
del first_set
print(first_set) #this will trow an error