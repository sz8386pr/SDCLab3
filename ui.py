def mainMenuSelection():
    ''' Main menu '''

    print('''
        1. Search record
        2. Add a record
        3. Update/modify a record
        4. Delete a record
        5. Quit
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
        4. Number of catches(greater or equal to)
    ''')
    choice = None
    while not (choice >= '1' and choice <= '4'):
        choice = input("Enter a selection: ")
        if not (choice >= '1' and choice <= '4'):
            message("Please enter a valid selection")
    return choice


def message(message):
    '''Output for the user'''
    print(message)
