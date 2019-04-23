#!/usr/bin/python3
import init
import logger
import os
import re
import database
from PyInquirer import style_from_dict, Token, prompt

style = style_from_dict({
    Token.QuestionMark: '#ff9d00 bold',
    Token.Selected: '#ff9d00',
    Token.Pointer: '#ff9d00 bold',
    Token.Answer: '#f44336 bold',
    Token.Question: '#ffffff bold'
})

def loginForm():
    print(logger.heading("LOGIN"))
    questions = [{
        'type': 'input',
        'name': 'username',
        'message': 'Username :',
    },{
        'type': 'password',
        'name': 'password',
        'message': 'Password :'
    }]
    answers = prompt(questions,style=style)
    return(answers['username'],answers['password'])

def basic(usrnam,passwd):
    query = "SELECT * FROM users where userid = '"+str(usrnam)+"' and passwd='"+str(passwd)+"'"
    try:
        if database.execute(query) is not None:
            print(logger.tick(),logger.msg('Login successful'))
        else:
            print(logger.cross(),logger.msg('Login failed'))
    except:
        print(logger.cross(),logger.msg('Login failed'))

def whitelist(usrnam,passwd):
    query = "SELECT * FROM users where userid = '"+str(usrnam)+"' and passwd='"+str(passwd)+"'"
    try:
        if database.execute(query) is not None and re.findall(r'^[A-Za-z0-9]+$',passwd) and re.findall(r'^[A-Za-z0-9]+$',usrnam): 
            print(logger.tick(),logger.msg('Login successful'))
        else:
            print(logger.cross(),logger.msg('Login failed'))
    except:
        print(logger.cross(),logger.msg('Login failed'))

def blacklist(usrnam,passwd):
    bFile = open('blacklist','r')
    blacklist = [_.strip() for _ in bFile.readlines()]
    query = "SELECT * FROM users where userid = '"+str(usrnam)+"' and passwd='"+str(passwd)+"'"
    flag = 0
    for _ in usrnam.split(' '):
        if _ in blacklist:
            flag = 1
    for _ in passwd.split(' '):
        if _ in blacklist:
            flag = 1
    if flag == 1:
        print(logger.cross(),logger.msg('Login failed'))
    else:
        try:
            if database.execute(query) is not None :
                print(logger.tick(),logger.msg('Login successful'))
            else:
                print(logger.cross(),logger.msg('Login failed'))
        except:
            print(logger.cross(),logger.msg('Login failed'))

def parametrizied(usrnam,passwd):
    query = "SELECT * FROM users where userid = ? and passwd= ?"
    args = (usrnam,passwd)
    try:
        if database.executeParameter(query,args) is not None:
            print(logger.tick(),logger.msg('Login successful'))
        else:
            print(logger.cross(),logger.msg('Login failed'))
    except:
        print(logger.cross(),logger.msg('Login failed'))

if not os.path.isfile('demo.db'):
    init.main()
else:
    print(logger.tick(),logger.level(1),logger.sep(),logger.msg('Database Creation'),end='\n')

level = [{
    'type': 'list',
    'name': 'lvl',
    'message': 'Select level of SQLi testing?',
    'choices': ['Basic','Whitelist','Blacklist','Parametrizied Query']
}]
choice = prompt(level,style=style)['lvl']
username, password = loginForm()

if choice == 'Basic':
    basic(username,password)
elif choice == 'Whitelist':
    whitelist(username,password)
elif choice == 'Blacklist':
    blacklist(username,password)
else:
    parametrizied(username,password)