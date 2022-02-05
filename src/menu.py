import inquirer
import os
from coke import *
import time
from location import *

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def cokeModuleSetup():

    email = input("Please enter your email: ")
    reps = int(input("Please enter how many codes you would like: "))
    venue = input("Please enter your venue ID: ")
    clear()
    print(title)
    for i in range(reps):
        cokeMain(email, venue, i)
        time.sleep(1.2) #Delay between each request
    print("\n")
    input("Press Enter to go back to main menu...")
    cokeSetup()

def locationSetup():
    clear()
    print(title)
    postcode = input("Please enter a postcode with a space: ")
    clear()
    print(title)
    locationModule(postcode)
    print("\n")
    input("Press Enter to go back to main menu...")
    cokeSetup()



def cokeSetup():
    print(title)
    questions = [
    inquirer.List('option',
                    message="Please select an option: ",
                    choices=['Free Coke', 'Location Finder'],),]
    answers = inquirer.prompt(questions)
    answer = answers["option"]
    if answer == "Free Coke":
        clear()
        cokeModuleSetup()
    if answer == "Location Finder":
        clear()
        locationSetup()
