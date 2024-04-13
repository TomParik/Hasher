# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Main File

# Imports
import os

# First Start
def start():
       requirements = open("Important/requirements.txt", "r")
       requirements = requirements.readlines()
       print(requirements[6])
       
       if (requirements[6] == "requirements/True\n"):
              return None
       
       else:
              if (requirements[9] == "rich/False\n"):
                     os.system("pip3 install rich")

              if (requirements[9] == "pyperclip/False\n"):
                     os.system("pip3 install pyperclip")

              if (requirements[9] == "hashlib/False\n"):
                     os.system("pip3 install hashlib")

              return None

if __name__ == "__main__":
       start()
