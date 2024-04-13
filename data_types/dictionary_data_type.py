#************ Dictionary Data Type ************
# - Dictionaries are the key and value pairs. Wich written with curly brackets. '{}'
# Example:
# employeeData = {
#   "name": Maleny,
#   "Id": 6808,
#   "DOB": 1993
#}

#Create Dictionary
employeeData = {
    "name": "Maleny",
    "Id": 6808,
    "DOB": 1993
}
print(employeeData)
print(type(employeeData))

#Access the value
employeeId = employeeData["Id"]
print(f"Id of employee: {employeeId}")
print(employeeData.get("name")) #more eficcient way of access a value
print(employeeData.get("huevoDePato", "noHay")) #the second value is going to be returned if the first is not found

#Update/Change value
employeeData["name"] = "Maleny Ochoa"
print(f"The data was updated: {employeeData}")

#Add key value
employeeData["address"] = "Mexico"
print(employeeData)

#Length
print(f"Your dictionary has {len(employeeData)} key:values")

#Copy dictionary to other variable
employeeIfo = employeeData.copy()
print(employeeIfo) #all the data is cloned and this varible is dict type of data also

#Iterate just the values in dictionary 
for data in employeeData.keys():
    print(employeeData[data])

#Iterate keys and values in dictionary 
for key,value in employeeData.items():
    print(f"{key}: {value}")

#Remove a key value
employeeData.pop("address")
print(f"Key value removed:{employeeData}")

#Clear the data on the dictionary
employeeData.clear()
print(employeeData) #this will print an empty {}, all data was clear

#Delete the dictionary
del employeeData
print(employeeData) #--> this will trow and error because it no longer exists