def welcome():
    ''' Welcome message '''
    message('''
        *** Welcome to Chainsaw Juggling Records!!! ***
    ''')


def mainMenuSelection():
    ''' Main menu '''

    print('''
        0. Display all records
        1. Search record
        2. Add a record
        3. Update/modify a record
        4. Delete a record
        q. Quit
    ''')

    choice = input("Enter a selection: ")
    return choice


def searchBy():
    ''' Search option '''

    print('''
        Search record by...
        1. ID
        2. Record holder
        3. Country
        4. Number of catches
    ''')
    choice = 0
    while not (choice >= 1 and choice <= 4):
        try:
            choice = int(input("Enter a selection: "))
            if not (choice >= 1 and choice <= 4):
                message("Please enter a valid selection")
        except ValueError:
            message("Please enter a valid selection")

    if choice == 1:
        searchBy = "ID"
    elif choice == 2:
        searchBy = "Record holder"
    elif choice == 3:
        searchBy = "Country"
    else:
        searchBy = "Number of catches"

    return searchBy

def updateBy():
    ''' update column option '''
    print('''
        Update/modify...
        1. Record holder
        2. Country
        3. Number of catches
    ''')
    choice = 0
    while not (choice >= 1 and choice <= 3):
        try:
            choice = int(input("Enter a selection: "))
            if not (choice >= 1 and choice <= 3):
                message("Please enter a valid selection")
        except ValueError:
            message("Please enter a valid selection")

    if choice == 1:
        updateColumn = "Chainsaw_Juggling_Record_Holder"
    elif choice == 2:
        updateColumn = "Country"
    else:
        updateColumn = "Number_of_catches"

    updateValue = ""
    while updateValue == "":
        updateValue = input("Enter a new value: ")

    return updateColumn, updateValue


def message(message):
    '''Output for the user'''
    print(message)
