succsessful = True
for number in range(3):
    print("Attempt")
    if succsessful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed.")