# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Crack File

# Imports
import Hash
import Menus
import time
from rich.console import Console
console = Console()

# Cracking
class Crack():
       def __init__(self, hash, library, common, progress, milestones):
              self.hash = hash
              self.common = common
              self.library = library
              self.progress = progress
              self.milestones = milestones

       def Crack(self):
              def getString(number, library):
                     base = len(library)
                     result = ""
              
                     while number > 0:
                            remainder = (number - 1) % base
                            result = library[remainder] + result
                            number = (number - 1) // base
              
                     return result

              Menus.Menu(10, self.hash, self.progress, self.milestones, self.library, self.common).print()

              if (isinstance(self.hash, list) == True):
                     crackHash = []
                     for i in range(len(self.hash)):
                            cracked = False

                            Menus.Menu(11, self.hash).print()

              else:
                     crackHash = ""
                     cracked = False
                     hashType = Hash.Hash(self.hash).GetType()
                     starttime = time.time()
                     Menus.Menu(11, self.hash).print()

                     if (self.progress == "S"):
                            attempts = 0
                            while (cracked == False):
                                   attempts = attempts + 1
                                   generated = getString(attempts, self.library)
                                   generatedHash = Hash.Hash(generated, hashType).HashData()
                                   print(f"┃  {generated} = {generatedHash}")

                                   if (generatedHash == self.hash):
                                          endtime = time.time()
                                          timetaken = endtime - starttime

                                          break

                     elif (self.progress == "F"):
                            attempts = 0
                            while (cracked == False):
                                   attempts = attempts + 1
                                   generated = getString(attempts, self.library)
                                   generatedHash = Hash.Hash(generated, hashType).HashData()
                                   console.print(f"[#6EB6FF]┃[/]  [bold][#6EB6FF]{generated}[bold][#99B0C8] = {generatedHash}")

                                   if (generatedHash == self.hash):
                                          endtime = time.time()
                                          timetaken = endtime - starttime

                                          break

                     else:
                            attempts = 0
                            milestone = 0
                            milestonecounter = 0
                            while (cracked == False):
                                   attempts = attempts + 1
                                   milestone = milestone + 1
                                   generated = getString(attempts, self.library)
                                   generatedHash = Hash.Hash(generated, hashType).HashData()
                                   
                                   if (milestone == self.milestones):
                                          milestone = 0
                                          milestonecounter = milestonecounter + 1
                                          console.print(f"[#6EB6FF]┃[/]  [bold][#6EB6FF]{milestonecounter}.[bold][#99B0C8] milestone reached ([bold][#6EB6FF]{attempts}[bold][#99B0C8] attempts)")

                                   if (generatedHash == self.hash):
                                          endtime = time.time()
                                          timetaken = endtime - starttime

                                          break
                     
                     Menus.Menu(12,generatedHash, attempts=attempts, result=generated, time=timetaken).print()
