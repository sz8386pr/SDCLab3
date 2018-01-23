import ui, data

def handleChoice(choice):
    ''' Main menu selection handling '''
    if choice == '1':
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


def searchRecord():
    ''' search for record '''
    searchOption = ui.searchBy()
    searchValue = input("")


def addRecord():


def updateRecord():


def deleteRecord():


def quit():
    data.quit()
    ui.message("End of program")


def main():

    data.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.mainMenuSelection()
        handleChoice(choice)


if __name__ == '__main__':
    main()
