def promptOptions():
    print("1. Calculate BMI\n2. Show History\n3. Filter BMIs\n4. Exit")
    userInput = int(input("Option: "))
    if userInput > 0 and userInput < 4:
        return userInput
    else:
        return -1

def showmenu():
    while True:
        choice = promptOptions()
        if (choice == -1):
            break
        
