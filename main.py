from __future__ import print_function       # for printing to stderr
import sys
import logging

#Create and configure logger
logging.basicConfig(filename="gamelog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

#Creating an object
logger = logging.getLogger()

#Setting threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug("Just a harmless debug Message")

# Global Variables
places = ["Treep city", "Hadem city", "Darnew city"]

def start_game():
    name = input("Hello, what's your name?\n")
    print("Welcome " + name)

def prompt_location(location):
    print("="*25)
    print("These are the places you can go to: ")
    i = 0
    for place in places:
        print(str(i) + ". " + place) 
        i += 1

    print("You are currently at: [ " + location + " ]")
    new_place = int(input("Where would you like to go next? "))
    if (new_place == 0):
        return 0
    elif (new_place == 1):
        return 1
    elif (new_place == 2):
        return 2
    else:
        return -1
    

def main():
    start_game()
    location = "new_world"
    while (True):
        option = prompt_location(location)        
        if (option == 0):
            location = "treep city"
            print("You are now at " + location)
            ("In option 0")
        elif (option == 1):
            location = "hadem city"
            print("You are now at " + location)
            print("In option 1")
        elif (option == 2):
            location = "darnew city"
            print("You are now at " + location)
            print("In option 2")
        else:
            print("You are currently at " + location)
            break

main()
