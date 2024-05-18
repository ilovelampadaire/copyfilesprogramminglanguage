import webbrowser
import string
import os
import subprocess


def typing():
    os.system('start "" typing.png')


def help():
    print('''List of all lampy extensions:\n
typing (Opens a typing image)\n
help (Shows this message)\n
emoji(emoji) (Prints any emoji's you want!)\n
github (See the copied files github repo (Yes, i used a github repo to download the files))\n
reverse (Reverse text)\n
discord(1, 2 or 3) (Choose between the main discord server, the new one or a special discord bot developement one)\n
notepad(text) (Open notepad with the specified text)\n
printall(dir) (Print all the files in a specified directory)\n''')

def emoji(emoji):
    print(emoji)

def github():
    webbrowser.open('https://github.com/ilovelampadaire/copyfilesprogramminglanguage')

def reverse(text):
    print(text[::-1])

def discord(number):
    if number == 1:
        webbrowser.open('https://discord.gg/t5JRvjxdm3')
    elif number == 2:
        webbrowser.open('https://discord.gg/AamP4yJmqA')
    elif number == 3:
        webbrowser.open('https://discord.gg/QnChuvXWSH')
    else:
        print('Invalid server!')

def notepad(text):
    with open('temp.txt', 'w') as f:
        f.write(text)
    os.system('start "" temp.txt')

def printall(dir):
    for file in os.listdir(dir):
        print(file)