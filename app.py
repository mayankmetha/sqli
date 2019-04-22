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
        if database.execute(query) is not None and re.findall('^\w$',passwd) and re.findall('^\w$',usrnam): 
            print(logger.tick(),logger.msg('Login successful'))
            print(usrnam, passwd)
        else:
            print(logger.cross(),logger.msg('Login failed'))
    except:
        print(logger.cross(),logger.msg('Login failed'))

def blacklist():
    return

def parametrizied():
    return

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
    blacklist()
else:
    parametrizied()