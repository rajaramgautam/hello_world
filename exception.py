numbers = [1, 2]
# print(numbers[2])

try:
    file = open("exception.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) :
    print("You did not enter a valid age.")
    # print(ex)
    # print(type(ex))
    
except ZeroDivisionError:
    print("Division by zero not possible.")
    
else:
    print("No exception were thrown.")
# print('Exception Continues')

finally:
    file.close()
    