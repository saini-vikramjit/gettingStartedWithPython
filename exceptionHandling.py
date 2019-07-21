try: 
    #value = 10/0
    integer = int(input("Enter an integer: "))

except ZeroDivisionError as err:
    print(err)
except ValueError: 
    print("Invalid input")