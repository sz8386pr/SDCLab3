''' code references from Lab3 slides/examples '''

from ui import message
import sqlite3
import traceback
import sys

db = sqlite3.connect("juggling.db") # Creates or opens database file
cur = db.cursor() # Need a cursor object to perform operations
''' Initial records '''
initialRecords = [  ('Ian Stewart', 'Canada', 94),
                    ('Aaron Gregg', 'Canada', 88),
                    ('Chad Taylor', 'USA', 78)]

def setup():
    ''' initial setup to create table and insert intial records'''
    global db
    global cur
    global initialRecords

    try:
        cur.execute('CREATE table if not exists records ("Chainsaw_Juggling_Record_Holder" TEXT, Country TEXT, "Number_of_catches" INT)')
        cur.executemany('INSERT INTO records values (?,?,?) WHERE NOT EXISTS (SELECT * FROM records WHERE 'Chainsaw_Juggling_Record_Holder' = (?))' , initialRecords, initialRecords)
        db.commit() # Ask the database to save changes!

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        trackback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def search(searchOption, searchValue):
    ''' search for records '''
    global db
    global cur

    try:
        if searchOption == "ID":
            cur.execute('SELECT * FROM records WHERE ROWID = (?)', searchValue)
            for row in cur:
                print(row)

        elif searchOption == "Record holder":
            cur.execute("SELECT * FROM records WHERE 'Chainsaw_Juggling_Record_Holder' = (?)", str(searchValue))
            for row in cur:
                print(row)

        elif searchOption == "Country":
            cur.execute("SELECT * FROM records WHERE 'Country' = (?)", str(searchValue))
            for row in cur:
                print(row)

        elif searchOption == "Number of catches":
            cur.execute("SELECT * FROM records WHERE 'Number_of_catches' = (?)", int(searchValue))
            for row in cur:
                print(row)

    except sqlite3.Error as e:
        print("{} error has occured".format(e))


def add(recordHolder, country, catches):
    global db
    global cur


def update(id):
    global db
    global cur


def delete(id):
    global db
    global cur


def quit():
    global db

    ui.message("Closing database")
    db.close
