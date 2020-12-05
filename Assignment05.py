# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot, 1.1.2030, Created started script
# Tim Shore, 11.15.2020, Added code to complete assignment 5
# Tim Shore, 12.06.2020, Added this comment to check GitHub Desktop
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
# objFile = "ToDoList.txt"
# An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
task = ""  # A Capture of the key element in a dictionary row
priority = ""  # A Capture of the value element in a dictionary row
strDel = ""  # A Capture of the key element to delete

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "w")
dicRow = {"Task": "Feed the Dog", "Priority": "Twice a Day"}
objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + "\n")
dicRow = {"Task": "Pet the Dog", "Priority": "Often"}
objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + "\n")
dicRow = {"Task": "Take the Dog to the Vet", "Priority": "Yearly"}
objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + "\n")
objFile.close()

objFile = open("ToDoList.txt", "r")
for row in objFile:
    strData = row.split(", ")
    dicRow = {"Task": strData[0], "Priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    - Tasks and Priorities for Taking Care of a Dog -
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open("ToDoList.txt", "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            print(dicRow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = str(input("What is the new task?: "))
        priority = str(input("How often should you do the new task?: "))
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        for objRow in lstTable:
            print(objRow)
        print("\n", task, "has been added, to be done", priority)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strDel = str(input("Which task do you want to remove?: "))
        for row in lstTable:
            if strDel in row["Task"]:
                lstTable.remove(row)
                print(strDel, "has been removed")
        if strDel not in row["Task"]:
            print("Task not in file")
            print(lstTable)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + ',' + row["Priority"] + "\n")
        objFile.close()
        print("Tasks saved to file")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You're done with making your list (for now)")
        break  # and Exit the program

    else:
        print("That is not one of the options available here.")
