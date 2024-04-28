# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Menus File

# Imports
import Hash
import time
import pyperclip
import os
from rich.console import Console
console = Console()

# Menus
class Menu():
       def __init__(self, type, hash=None, progress=None, milestones=None, library=None, common=None, attempts=None, result=None, time=None):
              self.type = type

              self.hash = hash
              self.progress = progress
              self.milestones = milestones
              self.library = library
              self.common = common

              self.attempts = attempts
              self.result = result
              self.time = time


       def print(self):
              colors = {
                     "mainB": "[bold][#6EB6FF]",
                     "main": "[#6EB6FF]",
                     "secondaryB": "[bold][#99B0C8]",
                     "secondary": "[#99B0C8]",
                     "thirdB" : "[bold][#FF5A43]",
                     "third" : "[#FF5A43]",
                     "hasher" : "[#6EB6FF]┃[/]"
                     }

              while True:
                     # Screen
                     def HasherBanner():
                            os.system("clear")

                            console.print(f"")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}██╗░░██╗░█████╗░░██████╗██╗░░██╗███████╗██████╗░")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}██║░░██║██╔══██╗██╔════╝██║░░██║██╔════╝██╔══██╗")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}███████║███████║╚█████╗░███████║█████╗░░██████╔╝")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}██╔══██║██╔══██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}██║░░██║██║░░██║██████╔╝██║░░██║███████╗██║░░██║")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
                            time.sleep(0.1)
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Made by Tom Parik (Github @TomParik)")
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Welcome to {colors['mainB']}Hasher{colors['secondaryB']}!")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Best program for cracking hashes into strings.")  
                            console.print(f"")

                     # Main Menu
                     if (self.type == 1):
                            HasherBanner()
                            console.print(f"{colors['hasher']}  {colors['mainB']}Main Menu")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}C{colors['secondaryB']}' = for {colors['mainB']}cracking{colors['secondaryB']} hash")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}M{colors['secondaryB']}' = for {colors['mainB']}making{colors['secondaryB']} hash")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}E{colors['secondaryB']}' = for {colors['mainB']}exiting{colors['secondaryB']} program")
                            console.print(f"")

                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Choose what do you want to do ({colors['mainB']}C{colors['secondaryB']}/{colors['mainB']}M{colors['secondaryB']}/{colors['mainB']}E{colors['secondaryB']}): ")
                     
                            # Crack hash
                            if (choice == "C" or choice == "c"):
                                   action = "crack"
                                   choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Are you sure you want to {colors['mainB']}crack{colors['secondaryB']} hash ({colors['mainB']}Y{colors['secondaryB']}/{colors['mainB']}N{colors['secondaryB']}): ")
                            
                            # Make hash
                            elif (choice == "M" or choice == "m"):
                                   action = "make"
                                   choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Are you sure you want to {colors['mainB']}make{colors['secondaryB']} hash ({colors['mainB']}Y{colors['secondaryB']}/{colors['mainB']}N{colors['secondaryB']}): ")
                            
                            # Exit
                            else:
                                   action = "exit"
                                   choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Are you sure you want to {colors['mainB']}exit{colors['secondaryB']} program ({colors['mainB']}Y{colors['secondaryB']}/{colors['mainB']}N{colors['secondaryB']}): ")

                            if (choice == "Y" or choice == "y"):
                                   return action
                            
                     # Cracking Menu 1
                     if (self.type == 2):
                            HasherBanner()
                            console.print(f"{colors['hasher']}  {colors['mainB']}Cracking Menu")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}1{colors['secondaryB']}' = to crack {colors['mainB']}one{colors['secondaryB']} hash")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}2{colors['secondaryB']}' = to crack {colors['mainB']}multiple{colors['secondaryB']} hashes")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}E{colors['secondaryB']}' = for {colors['mainB']}exiting{colors['secondaryB']} to the main menu")
                            console.print(f"")

                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Choose what do you want to do ({colors['mainB']}1{colors['secondaryB']}/{colors['mainB']}2{colors['secondaryB']}/{colors['mainB']}E{colors['secondaryB']}): ")

                            # One hash
                            if (choice == "1"):
                                   action = "one"
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to crack {colors['mainB']}one{colors['secondaryB']} hash!")
                            
                            # Multiple Hashes
                            elif (choice == "2"):
                                   action = "multiple"
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to crack {colors['mainB']}multiple{colors['secondaryB']} hashes!")
                            
                            # Exit
                            else:
                                   action = "exit"

                            return action
                     
                     # Cracking Menu 2 for one hash
                     if (self.type == 3):
                            console.print(f"")
                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Put your {colors['mainB']}hash{colors['secondaryB']} here: ")

                            return choice

                     # Cracking Menu 2 for multiple hashes
                     if (self.type == 4):
                            console.print(f"")
                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Put your {colors['mainB']}hashes{colors['secondaryB']} into {colors['mainB']}Hashes/hashes.txt{colors['secondaryB']} file (then click enter) ")

                            hashes = open("Hashes/hashes.txt", "r")
                            hashes = hashes.readlines()

                            for i in range(len(hashes)):
                                   hashes[i] = hashes[i].replace("\n", "")

                            return hashes
                     
                     # Cracking menu 3
                     if (self.type == 5):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['mainB']}Types of progress")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}1{colors['secondaryB']}' = to crack {colors['mainB']}fast{colors['secondaryB']} without seeing progress")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}2{colors['secondaryB']}' = to crack {colors['mainB']}normaly{colors['secondaryB']} with seeing normal progress")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}3{colors['secondaryB']}' = to crack {colors['mainB']}slowly{colors['secondaryB']} with seeing fancy progress")
                            console.print(f"")

                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Choose what type of progress you want ({colors['mainB']}1{colors['secondaryB']}/{colors['mainB']}2{colors['secondaryB']}/{colors['mainB']}3{colors['secondaryB']}): ")        

                            # Without progress
                            if (choice == "1"):
                                   progress = "N"
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to not see {colors['mainB']}any{colors['secondaryB']} progress!")
                            
                            # Normal progress
                            elif (choice == "2"):
                                   progress = "S"
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to see {colors['mainB']}normal{colors['secondaryB']} progress!")              
                            
                            # Fancy progress
                            else:
                                   progress = "F"
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to see {colors['mainB']}fancy{colors['secondaryB']} progress!")  

                            return progress

                     # Cracking menu 4 for no progress
                     if (self.type == 6):
                            console.print(f"")
                            milestone = int(console.input(f"{colors['hasher']}  {colors['secondaryB']}Type how often do you want to see {colors['mainB']}milestones{colors['secondaryB']} that will tell you how many attempts tried: "))
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}You will see milestone every {colors['mainB']}{str(milestone)}{colors['secondaryB']} attempts!")  


                            return milestone
                     
                     # Cracking menu 5
                     if (self.type == 7):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['mainB']}Libraries")
                            mylibrary = []

                            # Numbers
                            def library(name, characters):
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}{name}{colors['secondaryB']}' = library including {colors['mainB']}{name}{colors['secondaryB']} {str(characters)}")
                                   choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Do you want to crack using this library ({colors['mainB']}Y{colors['secondaryB']}/{colors['mainB']}N{colors['secondaryB']}): ")
                                   if (choice == "Y" or choice == "y"):
                                          console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to {colors['mainB']}include{colors['secondaryB']} {name} library!")
                                          console.print(f"")
                                          return mylibrary + characters
                                   else:
                                          console.print(f"{colors['hasher']}  {colors['secondaryB']}You chose to {colors['mainB']}not include{colors['secondaryB']} {name} library!")
                                          console.print(f"")
                                          return mylibrary

                            mylibrary = library("numbers", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

                            mylibrary = library("lowercase letters", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",])

                            mylibrary = library("uppercase letters",["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

                            mylibrary = library("space",[" "])                

                            mylibrary = library("easy symbols", ["+", "-", "*", "=", "/"])

                            mylibrary = library("medium symbols", ["&", "$", "#", "~", "@", "%", "_"])

                            mylibrary = library("hard symbols", ["!", "?", "§", ";", ":", "." "[", "]", "(", ")", "^"]) 

                            console.print(f"")
                            
                            return mylibrary
                     
                     # Cracking menu 6
                     if (self.type == 8):
                            choice = console.input(f"{colors['hasher']}  {colors['secondaryB']}Do you want to crack hash first by trying {colors['mainB']}famously used{colors['secondaryB']} passwords ({colors['mainB']}Y{colors['secondaryB']}/{colors['mainB']}N{colors['secondaryB']}): ")

                            if (choice == "Y" or choice == "y"):
                                   use = True
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}We {colors['mainB']}will{colors['secondaryB']} first try {colors['mainB']}commonly used{colors['secondaryB']} passwords!")
                            
                            else:
                                   use = False
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}We {colors['mainB']}will not{colors['secondaryB']} first try {colors['mainB']}commonly used{colors['secondaryB']} passwords!")

                            return use
                     
                     if (self.type == 9):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}You have {colors['mainB']}successfuly setup{colors['secondaryB']} cracking!") 
                            console.input(f"{colors['hasher']}  {colors['secondaryB']}Press any key to {colors['mainB']}continue{colors['secondaryB']} to cracking ")

                            return None
                     
                     if (self.type == 10):
                            HasherBanner()
                            console.print(f"{colors['hasher']}  {colors['mainB']}Cracking Setup")

                            if (isinstance(self.hash, list) == True):
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}hash{colors['secondaryB']}' = hashes are taken from {colors['mainB']}Hashes/hashes.txt{colors['secondaryB']} file")   
                            else:
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}hash{colors['secondaryB']}' = {colors['mainB']}{self.hash}")
                            
                            if (self.progress == "N"):
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}progress{colors['secondaryB']}' = you will see {colors['mainB']}no{colors['secondaryB']} progress")
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}milestones{colors['secondaryB']}' = you will see milestone every {colors['mainB']}{str(self.milestones)}{colors['secondaryB']} attempts")
                            elif (self.progress == "S"):
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}progress{colors['secondaryB']}' = you will see {colors['mainB']}normal{colors['secondaryB']} progress")
                            else:
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}progress{colors['secondaryB']}' = you will see {colors['mainB']}fancy{colors['secondaryB']} progress")
                            
                            if (self.common == True):
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}common passwords{colors['secondaryB']}' = we {colors['mainB']}will{colors['secondaryB']} first try commonly used passwords")
                            else:
                                   console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}common passwords{colors['secondaryB']}' = we {colors['mainB']}will not{colors['secondaryB']} first try commonly used passwords")

                            console.print(f"{colors['hasher']}  {colors['secondaryB']}~ '{colors['mainB']}library{colors['secondaryB']}' = {colors['mainB']}{str(self.library)}")

                            console.print(f"")
                            console.input(f"{colors['hasher']}  {colors['secondaryB']}Press any key to {colors['mainB']}start{colors['secondaryB']} cracking ")

                            return None

                     if (self.type == 11):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Hash to crack: {colors['mainB']}{self.hash}")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Hash type: {colors['mainB']}{Hash.Hash(self.hash).GetType()}")
                            console.print(f"")

                            time.sleep(1)
                            console.print(f"{colors['hasher']}  {colors['mainB']}3{colors['secondaryB']}!")
                            time.sleep(0.75)
                            console.print(f"{colors['hasher']}  {colors['mainB']}2{colors['secondaryB']}!")
                            time.sleep(0.75)
                            console.print(f"{colors['hasher']}  {colors['mainB']}1{colors['secondaryB']}!")
                            console.print(f"")
                            time.sleep(0.75)
                            console.print(f"{colors['hasher']}  {colors['mainB']}GO{colors['secondaryB']}!")
                            console.print(f"")
                            time.sleep(0.75)

                            console.print(f"{colors['hasher']}  {colors['mainB']}Progress{colors['secondaryB']}:")
                            console.print(f"")
                            time.sleep(0.75)

                            return None
                     
                     if (self.type == 12):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['mainB']}Hash cracked{colors['secondaryB']}!")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Result: {colors['secondaryB']}'{colors['mainB']}{self.result}{colors['secondaryB']}' ({self.hash})")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Attempts: {colors['mainB']}{str(self.attempts)}")
                            console.print(f"{colors['hasher']}  {colors['secondaryB']}Time: {colors['mainB']}{str(self.time)}")
                            console.print(f"")

                            console.input(f"{colors['hasher']}  {colors['secondaryB']}Press any key to go {colors['mainB']}back{colors['secondaryB']} to main menu ")
                            console.input(f"{colors['hasher']}  {colors['secondaryB']}Press any key to go {colors['mainB']}back{colors['secondaryB']} to main menu ({colors['mainB']}Just to be sure you know your result{colors['secondaryB']}) ")

                            return None

                     # Bye Bye Menu
                     if (self.type == 13):
                            console.print(f"")
                            console.print(f"{colors['hasher']}  {colors['mainB']}Bye{colors['secondaryB']}, {colors['mainB']}Bye{colors['secondaryB']}!")

                            return None
