# While loop will execute the statements until condition is true
# initialize the value
# while condition:
#   incremet the value

numero = None
while numero is None:
    try:
        data = input("Input a number: ")
        numero = int(data)
        break
    except Exception:
        print(f"{data}:That's not valid, please input a valid number, it must be positive and integer")
        numero = None
print(f"The number you typed is: {numero}")

#Requirement: The client needs a system that allows to decide if the flow continues or not
#by input a "Yes/Y/yes/y", else, if the user types "No/N/no/n" it returns "Canceled execution"
#either way the loop will break when given a valid answer (Y o N)
#if the system does nor receive one of those options it needs to keep asking the user

while True:
    try:
        user_input = input("Please indicate if you want the system to continue 'Yes/No': ")
        user_input.lower()
        if  user_input == "yes" or user_input == "y": 
            print(f"You choose {user_input}, the system will continue executing.")
            break
        elif user_input == "no" or user_input == "n":
            print(f"You choose {user_input}, the system will cancel execution.")
            break
        else:
            print(f"{user_input}: is not a valid answer, please type one of the following options 'Yes/Y or No/N': ")
            continue
    except Exception:
        user_input = None
