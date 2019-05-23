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
    print("+" + "="*26 + "+")
    print("| Hello, what's your name? |\t")
    name = input("+" + "="*26 + "+\n")
    print("Welcome " + name)

def prompt_location(location):
    print("="*50)
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

class Location():
    def __init__(self, name = None):
        self.explored = False
        if not name is None:
            if (len(name) < 1):
                self.name = "Unknown"
                self.display ="༝";
            else:
                self.name = name
                self.display = self.name[0]
        else:
            self.name = "Unknown"
            self.display ="༝";

    def get_name():
        return self.name

def print_map(world_map):
    print("This is the world map currently")
    print("    - U = unknown territory")
    print("    - [letter] = Place/town/location")
    print("\t+" + "-"*((14+10)-1) + "+")
    #print("|" + " "*(14+10) + "|")
    for x in range(10):
        print("\t|" + " "*int(((14-10)/2)), end="")
        for y in range(9):
            print(world_map[x][y].display, end=" ")
        print(world_map[x][y + 1].display, end="")
        print(" "*int(((14-10)/2)), end="|")
        print()
    #print("|" + " "*(14+10) + "|")
    print("\t+" + "-"*((14+10)-1) + "+")

def main():
    start_game()
    location = "new_world"
    world_map = []
    for i in range(10):
        row = [] 
        for j in range(10):
            row.append(Location())
        world_map.append(row)
    print_map(world_map)

    while (True):
        option = prompt_location(location)        
        if (option == 0):
            location = "Treep City"
            print("You are now at " + location)
            ("In option 0")
        elif (option == 1):
            location = "Hadem City"
            print("You are now at " + location)
            print("In option 1")
        elif (option == 2):
            location = "Darnew City"
            print("You are now at " + location)
            print("In option 2")
        else:
            print("You are currently at " + location)
            break

main()
