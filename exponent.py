number = input("Enter the number: ")

power = input("Enter the power: ")

result = 1

for index in range(int(power)):
    #print(index)
    result *= int(number)

print(result)