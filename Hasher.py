# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Main File

# Imports Libraries
import os

# Import Files
import Hash
import Menus
import Crack

# First Start
def start():
       requirements = open("requirements.txt", "r")
       requirements = requirements.readlines()
       
       if (requirements[6] == "requirements/True\n"):
              return None
       
       else:
              with open("requirements.txt", "w") as file:
                     downloadRequirements = False
                     downloadRich = False
                     downloadPyperclip = False
                     downloadHashlib = False

                     if (requirements[9] == "rich/False\n"):
                            os.system("pip3 install rich")
                            downloadRich = True
                     else:
                            downloadRich = True

                     if (requirements[10] == "pyperclip/False\n"):
                            os.system("pip3 install pyperclip")
                            downloadPyperclip = True
                     else:
                            downloadPyperclip = True

                     if (requirements[11] == "hashlib/False\n"):
                            os.system("pip3 install hashlib")
                            downloadHashlib = True
                     else:
                            downloadHashlib = True

                     if (downloadRich == True and downloadPyperclip == True and downloadHashlib == True):
                            downloadRequirements = True

                     file.write(f"""# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Requirements File
# Hasher require a few libraries
requirements/{downloadRequirements}

# Libraries:
rich/{downloadRich}
pyperclip/{downloadPyperclip}
hashlib/{downloadHashlib}
                            """)

              return None

if __name__ == "__main__":
       # Check if everything needed is instaled
       start()

       # Show the main menu and returns what user want to do
       while True:
              action = Menus.Menu(1).print()

              if (action == "crack"):
                     action = Menus.Menu(2).print()

                     if (action != "exit"):
                            if (action == "one"):
                                   myhash = Menus.Menu(3).print()
                            elif (action == "multiple"):
                                   myhash = Menus.Menu(4).print()

                            progress = Menus.Menu(5).print()

                            milestones = None
                            if (progress == "N"):
                                   milestones = Menus.Menu(6).print()

                            library = Menus.Menu(7).print()
                            common = Menus.Menu(8).print()

                            Menus.Menu(9).print()
                            Crack.Crack(myhash, library, common, progress, milestones).Crack()

              elif (action == "make"):
                     pass
              elif (action == "exit"):
                     Menus.Menu(13).print()
                     exit()
