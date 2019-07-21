def spelloutDetails(name,age):
    print("Hello "+ name + ", you are " + str(age) + " years old")

username = input("Whats ur name: ")
userage = input("Whats ur age: ")
spelloutDetails(username, userage)

def findMaxNumber(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

maxNum = findMaxNumber(num1, num2, num3)
print(maxNum)


