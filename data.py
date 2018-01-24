''' sqlite3 related codes references from Lab3 slides/examples
cursor.fetchall() reference from https://stackoverflow.com/questions/34463901/how-to-iterate-through-cur-fetchall-in-python'''

from ui import message, displayRow
import sqlite3
import traceback
import os
import sys

dbFolder = "Data"
dbFile = os.path.join(dbFolder, "juggling.db")

''' makedirs referenced from https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist '''
try:
    os.makedirs(dbFolder)
except OSError as e:
    pass #Do nothing if directory exists

db = sqlite3.connect(dbFile) # Creates or opens database file
cur = db.cursor() # Need a cursor object to perform operations
''' Initial records '''
initialRecords = [  (1, 'Ian Stewart', 'Canada', 94),
                    (2, 'Aaron Gregg', 'Canada', 88),
                    (3, 'Chad Taylor', 'USA', 78)]

def setup():
    ''' initial setup to create table and insert intial records'''
    global db
    global cur
    global initialRecords

    try:
        cur.execute('CREATE table if not exists records ("Chainsaw_Juggling_Record_Holder" TEXT, Country TEXT, "Number_of_catches" INT)')
        cur.executemany('INSERT OR REPLACE INTO records(ROWID, Chainsaw_Juggling_Record_Holder, Country, Number_of_catches) values(?,?,?,?)', initialRecords)
        db.commit() # Ask the database to save changes!

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def allRecords():
    ''' Display all records in the table '''
    global db
    global cur

    try:
        cur.execute('SELECT ROWID, * FROM records')
        data = cur.fetchall()
        displayRow(data)

    except sqlite3.Error as e:
        print("{} error has occured".format(e))


def search(searchOption, searchValue):
    ''' search for records '''
    global db
    global cur

    try:
        if searchOption == "ID":
            cur.execute("SELECT ROWID, * FROM records WHERE ROWID = ?", (searchValue,))

        elif searchOption == "Record holder":
            cur.execute("SELECT ROWID, * FROM records WHERE Chainsaw_Juggling_Record_Holder = ?  COLLATE NOCASE", (searchValue,))
            print(searchValue)

        elif searchOption == "Country":
            cur.execute("SELECT ROWID, * FROM records WHERE Country = ? COLLATE NOCASE", (searchValue,))
            print(searchValue)
        elif searchOption == "Number of catches":
            cur.execute("SELECT ROWID, * FROM records WHERE Number_of_catches = ?", (searchValue,))
            print(searchValue)

        data = cur.fetchall()
        rowCount = displayRow(data)

        if rowCount == 0:
            message("There are no record with matching {}". format(searchOption))

    except sqlite3.Error as e:
        print("{} error has occured".format(e))


def add(recordHolder, country, catches):
    ''' Add a new record '''
    global db
    global cur

    try:
        cur.execute("INSERT INTO records values(?,?,?)", (recordHolder, country, catches,))
        db.commit()
        message("Record ({}, {}, {}) has been added to the database".format(recordHolder, country, catches))
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def checkID(id):
    ''' Checks if matching ID exists in the record. Used for update/delete '''
    global db
    global cur

    try:
        cur.execute("SELECT ROWID, * FROM records WHERE ROWID = ?", (id,))
        data = cur.fetchall()
        rowCount = displayRow(data)

        if rowCount > 0:
            return True

        else:
            message("There are no record with matching ID")
            return False

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        return False


def update(updateColumn, updateValue, id):
    ''' Update/modify a record
    update reference from https://stackoverflow.com/questions/25387537/sqlite3-operationalerror-near-syntax-error'''
    global db
    global cur

    try:
        cur.execute("UPDATE records SET {} = (?) WHERE ROWID = (?)".format(updateColumn), (updateValue, id,))
        db.commit()
        message("New value {} has been updated".format(updateValue))

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def delete(id):
    ''' delete a row by id '''
    global db
    global cur

    try:
        cur.execute("DELETE FROM records WHERE ROWID =(?)", (id,))
        db.commit()
        message("ID {} has been deleted from the database".format(id))

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def quit():
    ''' Close DB '''
    global db

    message("Closing database")
    db.close
