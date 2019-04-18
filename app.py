#!/usr/bin/python3
import logger
import os

def passwordInput():
    # switch off echo on keypress
    os.system("stty -echo")
    tmp = input()
    # switch on echo on keypress and go to next line
    os.system("stty echo;echo \n")
    return tmp

def loginForm():
    print(logger.heading("LOGIN"))
    print(logger.msg('Username'),logger.sep(),end="")
    uname = input()
    print(logger.msg('Password'),logger.sep(),end="")
    paswd = passwordInput()
    return(uname,paswd)

print(loginForm())