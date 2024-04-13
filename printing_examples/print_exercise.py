#this is the only thing you need to do to print on python
print("Hello Maleny")

#Print more values on one line
print("Hello" + " " + "Maleny")

#Print variables
name = "Maleny"
print("Hello " + name)
 
#print input data
print("Hello " + input("What is your name?"))
name = input("What is your name?")
print(name)

#Slicing: Getting a portion of the data [1:n-1]
data_slice = "Print based on index"
slice_of_data = data_slice[1:3] #ri will be printed since 0 is 'P' and the las char will be -1 position, so index 1 and 2 will be returned
print(slice_of_data)