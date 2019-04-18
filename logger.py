#!/bin/bash

from termcolor import colored

def star():
    return colored(' ★ ','magenta',attrs=['bold','blink'])

def tick():
    return colored(' ✔ ','green',attrs=['bold','blink'])

def cross():
    return colored(' ✘ ','red',attrs=['bold','blink'])

def level(x):
    if x == 0:
        return colored("Executing",'yellow',attrs=['bold'])
    elif x == 1:
        return colored("Executed ",'yellow',attrs=['bold'])
    elif x == 2:
        return colored("Failed   ",'yellow',attrs=['bold'])

def sep():
    return colored(' : ','white',attrs=['bold'])

def msg(args):
    return colored(args,'cyan',attrs=['bold'])

def heading(args):
    return colored(args,'white',attrs=['bold','underline'])