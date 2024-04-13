# While loop will execute the statements until condition is true
# initialize the value
# while condition:
#   incremet the value

numero = None
while numero is None:
    try:
        numero = int(input("Input a number: "))
        break
    except Exception:
        numero = None
print(f"The number you typed is: {numero}")