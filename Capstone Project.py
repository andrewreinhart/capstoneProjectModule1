#Dummy Data Address
address = {
    'Andy' : 'Jakarta',
    'Benny' : 'Bogor',
    'Charlie' : 'Depok'
}

#Dummy Data Scores
scores = {
    'Andy' : {
        'Math' : 80,
        'Physics' : 90,
        'Chemistry' : 70
    },
    'Benny' : {
        'Math' : 50,
        'Physics' : 70,
        'Chemistry' : 90
    },
    'Charlie' : {
        'Math' : 70,
        'Physics' : 80,
        'Chemistry' : 80
    },
}

#Main Menu Function
def mainMenu ():
    global mainMenuItem
    print ('''
        1. Display Student's Data
        2. Add New Student
        3. Update Student's Data
        4. Delete Student's Data
        5. Exit
    ''')
    mainMenuItem = int(input("Select menu: "))
    return mainMenuItem

#Read Menu Function
def readMenu():
    global readMenuItem
    print ('''
        1. Address
        2. Score
        3. Back to Main Menu
    ''')
    readMenuItem = int(input("Select menu: "))
    return readMenuItem

#Read Menu_1 Function
def readMenu_1():
    addressItem = int(input('''
    1. All Address
    2. Choose a student
    Select Address Menu: '''))
    if (addressItem == 1):
        print("\n")
        for key,val in address.items():
            print ("{} : {}".format(key,val))
    elif (addressItem == 2):
        studentAddress = input('''Name : ''').capitalize()
        print("\n{} lives in {}\n".format(studentAddress,address[studentAddress]))

#Read Menu_2 function
def readMenu_2(studentName):
    scoresItem = int(input('''
    1. All Scores
    2. Choose a student
    Select Scores Menu: '''))
    if (scoresItem == 1):
        print("\n")
        for key1 in scores.keys():
            print ("- {}".format(key1))
            for key2,val in scores[key1].items():
                print ("{} : {}".format(key2,val))
            print("\n")
        totalMath = 0
        totalPhysics = 0
        totalChemistry = 0
        n = 0
        for i in scores.keys():
            for key,val in scores[i].items():
                totalMath += scores[i]["Math"]
                totalPhysics += scores[i]["Physics"]
                totalChemistry += scores[i]["Chemistry"]
                n += 1
        averageMath = round(totalMath / n , 1)
        averagePhysics = round(totalPhysics / n , 1)
        averageChemistry = round(totalChemistry / n , 1)
        print('''Summary Average Score per Subject
Math : {}
Physics : {}
Chemistry : {}
        '''.format(averageMath,averagePhysics,averageChemistry))
    elif (scoresItem == 2):
        studentName = input ("Name : ").capitalize()
        if (studentName in scores):
            for key,val in scores[studentName].items():
                print("{} : {}".format(key,val))
            totalScore = 0
            n = 0
            for val in scores[studentName].values():
                totalScore += val
                n += 1
            averageScore = round(totalScore / n , 1)
            print("Average : {}".format(averageScore))
        else:
            print ("Data is unavailable!")
    else:
        print("your choice is invalid")

#Create Menu Function
def createMenu():
    global createMenuItem
    print ('''
        1. Add New Student's Address
        2. Add New Student's Scores
        3. Back to Main Menu
    ''')
    createMenuItem = int(input("Select menu: "))
    return createMenuItem

#Create Menu_1 Function
def createMenu_1():
    newStudent = str(input("Input new student's name : ").capitalize())
    if (newStudent in address):
        print("Data already exists!")
    else:
        newAddress = str(input("Input new student's address : ").capitalize())
        address[newStudent] = newAddress
        save = input ("\n save? (y/n) : ").capitalize()
        if (save == "Y"):
            print ("Data is successfully saved!")
        else:
            address.popitem()
            print("New Data has been removed")

#Create Menu_2 Function
def createMenu_2():
    newStudent = str(input("Input new student's name : ").capitalize())
    if (newStudent in scores):
        print("Data already exists!")
    else:
        scores[newStudent] = {}
        newMath = int(input("Math : "))
        newPhysics = int(input("Physics : "))
        newChemistry = int(input("Chemistry : "))
        scores[newStudent]["Math"] = newMath
        scores[newStudent]["Physics"] = newPhysics
        scores[newStudent]["Chemistry"] = newChemistry
        save = input("\n save? (y/n) : ").lower()
        if (save == "y"):
            print ("The file has been successfully saved!")
        else:
            scores.popitem()
            print ("The update has been removed!")

#Update Menu Function
def updateMenu():
    global updateMenuItem
    print ('''
        1. Update Student's Address
        2. Update Student's Scores
        3. Back to Main Menu
    ''')
    updateMenuItem = int(input("Select menu: "))
    return updateMenuItem

#Update Menu_1 Function
def updateMenu_1():
    studentName = input("Student's name : ").capitalize()
    if (studentName not in address):
        print("Data does not exist!")
    else:
        updateAddress = input("Update student's address : ").capitalize()
        save = input ("\n save? (y/n) : ").capitalize()
        if (save == "Y"):
            address[studentName] = updateAddress
            print ("File has been successfully updated!")
        else:
            print("Update has been removed")

#Update Menu_2 Function
def updateMenu_2():
    studentName = input("Student : ").capitalize()
    if (studentName not in scores):
        print("Data does not exist!")
    else:
        for key,val in scores[studentName].items():
            print("{} : {}".format(key,val))
        updateData = input("Do you want to update data? (y/n) : ").capitalize()
        if (updateData == "Y"):
            subjectName = input("Subject : ").capitalize()
            if(subjectName not in scores[studentName]):
                print("Data does not exist!")
            else:
                newScore = int(input("New Score: "))
                saveUpdate = input("Are you sure?(y/n): ").capitalize()
                if (saveUpdate == 'Y'):
                    scores[studentName][subjectName] = newScore
                    print ('''{}'s {} score has been updated'''.format(studentName, subjectName))

#Delete Menu Function
def deleteMenu():
    global deleteMenuItem
    print ('''
        1. Delete Student's Address
        2. Delete Student's Scores
        3. Back to Main Menu
    ''')
    deleteMenuItem = int(input("Select menu: "))
    return deleteMenuItem

#Delete Menu_1 Function
def deleteMenu_1():
    studentName = input("Student's name : ").capitalize()
    if (studentName not in address):
        print("Data does not exist!")
    else:
        deleteAddress = input("Are you sure you want to delete {}'s address? (y/n) : ".format(studentName)).capitalize()
        if (deleteAddress == "Y"):
            del address[studentName]
            print ("Student's Address has been deleted")
        else:
            print ("Delete is cancelled")

#Delete Menu_2 Function
def deleteMenu_2():
    studentName = input("Student's name : ").capitalize()
    if (studentName not in scores):
        print("Data does not exist!")
    else:
        for key,val in scores[studentName].items():
            print("{} : {}".format(key,val))
        deleteScores = input("Are you sure you want to delete it? (y/n) : ").capitalize()
        if (deleteScores == "Y"):
            del scores[studentName]
            print ("{}'s scores has been deleted".format(studentName))
        else:
            print ("Delete is cancelled")

#Exit Menu Function
def exitMenu():
    print("Thank you!")

#Program Execution
print ("\nWelcome to School Database!")
while (True):
    mainMenu()
    while (mainMenuItem < 1 or mainMenuItem > 5):
        print ("\nThe choice you entered is not valid")
        mainMenu()
    while (mainMenuItem == 1):    
        readMenu()
        while (readMenuItem < 1 or readMenuItem > 3):
            print ("\nThe choice you entered is not valid")
            readMenu()
        if (readMenuItem == 1):
            readMenu_1()
        elif (readMenuItem == 2):
            studentName = '_'
            readMenu_2(studentName)
        elif (readMenuItem == 3):
            break

    while (mainMenuItem == 2):
        createMenu()
        while (createMenuItem < 1 or createMenuItem > 3):
            print ("\nThe choice you entered is not valid")
            createMenu()
        if (createMenuItem == 1):
            createMenu_1()
        elif (createMenuItem == 2):
            createMenu_2()
        else:
            break

    while (mainMenuItem == 3):
        updateMenu()
        while (updateMenuItem < 1 or updateMenuItem > 3):
            print ("\nThe choice you entered is not valid")
            updateMenu()
        if (updateMenuItem == 1):
            updateMenu_1()
        elif (updateMenuItem == 2):
            updateMenu_2()
        else:
            break        

    while (mainMenuItem == 4):
        deleteMenu()
        while (deleteMenuItem < 1 or deleteMenuItem > 3):
            print ("\nThe choice you entered is not valid")
            deleteMenu()
        if (deleteMenuItem == 1):
            deleteMenu_1()
        elif (deleteMenuItem == 2):
            deleteMenu_2()
        else:
            break                
    
    if (mainMenuItem == 5):
        exitMenu()
        break