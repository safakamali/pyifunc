from sys import stdout
from os import system


def printf(data):
    stdout.write(data)

def cls():
    system('cls' or 'clear')

