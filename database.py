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
    query("CREATE TABLE users (userid varchar unique primary key,passwd varchar)")
    query("INSERT INTO users VALUES ('mayank','mayank')")
    closeDB()

def execute(args):
    global conn, db, c
    connectDB(db)
    c = conn.cursor()
    query(args)
    tmp = c.fetchone()
    c.close()
    return tmp

def executeParameter(args,parameters):
    global conn, db,c
    connectDB(db)
    c = conn.cursor()
    c.execute(args,parameters)
    tmp = c.fetchone()
    c.close()
    return tmp