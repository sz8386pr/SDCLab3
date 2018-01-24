import ui, data

def handleChoice(choice):
    ''' Main menu selection handling '''
    if choice == '0':
        displayTable()

    elif choice == '1':
        searchRecord()

    elif choice == '2':
        addRecord()

    elif choice == '3':
        updateRecord()

    elif choice == '4':
        deleteRecord()

    elif choice == 'q':
        quit()

    else:
        ui.message("Please enter a valid selection number")


def displayTable():
    ''' Display records table '''
    data.allRecords()


def searchRecord():
    ''' search for record '''
    searchOption = ui.searchBy()
    searchValue = ""
    while searchValue == "":
        searchValue = str(input("Enter a(n) {} to search the record with: ".format(searchOption)))

    data.search(searchOption, searchValue)


def addRecord():
    ''' add a new record '''
    recordHolder = input("Enter the name of the record holder: ")
    country = input("Enter the country of origin of the record holder: ")
    try:
        catches = int(input("Enter the number of catches: "))
    except ValueError:
        ui.message("Enter a valid number")

    data.add(recordHolder, country, catches)


def updateRecord():
    ''' update/modify a record '''
    try:
        id = int(input("Please enter an ID to update/modify: "))
    except ValueError:
        ui.message("Enter a valid number")

    updateColumn, updateValue = ui.updateBy()

    data.update(updateColumn, updateValue, id)


def deleteRecord():
    ''' Delete a record '''
    try:
        id = int(input("Please enter an ID to delete: "))
    except ValueError:
        ui.message("Enter a valid number")

    data.delete(id)


def quit():
    ''' Close db connection and end the program '''
    data.quit()
    ui.message("End of program")


def main():

    ui.welcome()
    data.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.mainMenuSelection()
        handleChoice(choice)


if __name__ == '__main__':
    main()
