###

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That wasn't a valid number!")
else:
    print("Great! No errors.")
finally:
    print("This always runs.")
