#!/usr/bin/python3

import sqlite3

db = "demo.db"
conn = None
c = None

def connectDB(args):
    global conn 
    conn = sqlite3.connect(args)

def closeDB():
    global conn
    conn.close()

def query(args):
    c.execute(args)
    conn.commit()

def initDB():
    global conn, db, c
    connectDB(db)
    c = conn.cursor()
    query("CREATE TABLE users (userid text,passwd text)")
    query("INSERT INTO users VALUES ('mayank','mayank')")
    closeDB()

initDB()