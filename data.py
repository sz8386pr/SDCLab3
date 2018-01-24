''' code references from Lab3 slides/examples '''

from ui import message
import sqlite3
import traceback
import sys

db = sqlite3.connect("juggling.db") # Creates or opens database file
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

        for row in cur:
            message(row)

    except sqlite3.Error as e:
        print("{} error has occured".format(e))


def search(searchOption, searchValue):
    ''' search for records '''
    global db
    global cur

    try:
        if searchOption == "ID":
            cur.execute("SELECT * FROM records WHERE ROWID = (?)", (searchValue,))

        elif searchOption == "Record holder":
            cur.execute("SELECT * FROM records WHERE 'Chainsaw_Juggling_Record_Holder' = (?)", (searchValue,))

        elif searchOption == "Country":
            cur.execute("SELECT * FROM records WHERE 'Country' = (?)", (searchValue,))

        elif searchOption == "Number of catches":
            cur.execute("SELECT * FROM records WHERE 'Number_of_catches' = (?)", (searchValue,))

        rowCount = 0

        for row in cur:
            message(row)
            rowCount+= 1

        if rowCount == 0:
            message("There are no record that matches {}". format(searchOption))


    except sqlite3.Error as e:
        print("{} error has occured".format(e))


def add(recordHolder, country, catches):
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


def update(updateColumn, updateValue, id):
    global db
    global cur

    try:
        cur.execute("UPDATE records SET (?) = (?) WHERE ROWID = (?)", (updateColumn, updateValue, id,))
        db.commit()
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db

def delete(id):
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
    global db

    message("Closing database")
    db.close
