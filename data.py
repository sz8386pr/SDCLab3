''' code references from Lab3 slides/examples '''

import message from ui
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
    ''' initial setup '''
    global db
    global cur
    global initialRecords

    try:
        cur.excute('CREATE table if not exists records ('Chainsaw Juggling Record Holder' VARCHAR(50), 'Country' VARCHAR(25), 'Number of catches' INTEGER'))
        cur.executemany('INSERT OR IGNORE INTO records values (?,?,?)', initialRecords)
        db.commit() # Ask the database to save changes!

    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        trackback.print_exc() # Displays a stack trace, useful for debugging
        db.rollback()    # Optional - depends on what you are doing with the db


def search(searchOption, searchValue):
    global db
    global cur


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
