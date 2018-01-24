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


def confirm(updateOrDelete):
    while True:
        confirm = input("Are you sure you want to {} this record from the data? (Y/N)".format(updateOrDelete))
        if confirm.upper() == "Y" or confirm.upper() == "N":
            return confirm.upper()
        else:
            message("Please enter Y or N")

def message(message):
    '''Output for the user'''
    print(message)


def displayRow(data):
    ''' User friendly display of return data '''
    rowCount = len(data)

    if rowCount > 0:
        print("{:^6} {:15} {:10} {:7}".format("ID","Record Holder", "Country", "Catches") )
        for row in data:
            id = row[0]
            name = row[1]
            country = row[2]
            catches = row[3]

            print("{:^6} {:15} {:10} {:^7}".format(id, name, country, catches))

        print("{} record(s) has been found".format(rowCount))

    return rowCount
