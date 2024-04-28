# Hasher
# Made by Tom Parik (All rights reserved)
# Github @TomParik (https://github.com/TomParik/Hasher)

# The Hash File

# Imports
import hashlib

# Hashes
class Hash():
       def __init__(self, data, hashtype=None):
              self.data = data
              self.hashtype = hashtype

       def HashData(self):
              if (self.hashtype == "MD5"):
                     shaMD5_hash = hashlib.md5()
                     shaMD5_hash.update(self.data.encode("utf-8"))
                     return shaMD5_hash.hexdigest() 
              
              elif (self.hashtype == "SHA1"):
                     shaSHA1_hash = hashlib.sha1()
                     shaSHA1_hash.update(self.data.encode("utf-8"))
                     return shaSHA1_hash.hexdigest()
              
              elif (self.hashtype == "SHA224"):
                     shaSHA224_hash = hashlib.sha224()
                     shaSHA224_hash.update(self.data.encode("utf-8"))
                     return shaSHA224_hash.hexdigest() 
              
              elif (self.hashtype == "SHA256"):
                     shaSHA256_hash = hashlib.sha256()
                     shaSHA256_hash.update(self.data.encode("utf-8"))
                     return shaSHA256_hash.hexdigest()
              
              elif (self.hashtype == "SHA384"):
                     shaSHA384_hash = hashlib.sha384()
                     shaSHA384_hash.update(self.data.encode("utf-8"))
                     return shaSHA384_hash.hexdigest()
              
              elif (self.hashtype == "SHA512"):
                     shaSHA512_hash = hashlib.sha512()
                     shaSHA512_hash.update(self.data.encode("utf-8"))
                     return shaSHA512_hash.hexdigest()
       
       def GetType(self):
              if (len(self.data) == 32):
                     hashType = "MD5"
                            
              elif (len(self.data) == 40):
                     hashType = "SHA1"

              elif (len(self.data) == 56):
                     hashType = "SHA224"

              elif (len(self.data) == 64):
                     hashType = "SHA256"

              elif (len(self.data) == 96):
                     hashType = "SHA384"

              elif (len(self.data) == 128):
                     hashType = "SHA512"

              return hashType
