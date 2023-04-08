import random

nameInput = input("type list of names here, make sure to use space to seperate\n").split(" ")
print(nameInput)

isNumber = False;

quantityOfNumbers = 0

while not isNumber:
    quantityOfNumbers = input("please type the amount of names to be selected here\n")
    if quantityOfNumbers.isnumeric():
        isNumber = True
        quantityOfNumbers = int(quantityOfNumbers)
    else:
        print("This is not a number")

results = random.sample(nameInput, quantityOfNumbers)

print(results)

