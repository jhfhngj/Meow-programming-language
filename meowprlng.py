import time
import os
print("Meow Programming Language")
while True:
    iput = input(":::")
    if iput == "wfile":
        print("The file will be in the folder it is in.")
        print("Writing file")
        fn = input("Filename ")
        fe = input("File extension (for example .txt or .py) ")
        fc = input("File contents (use \n for newline) ")
        with open(fn+fe, 'w') as file:
            file.write(fc)
    if iput == "rfile":
       pat = input("Which path? (Full path, for example: C:/Users/MainUser/Documents/readme.txt)")
       print("This is the contents of the file")
       try:
            with open(pat, 'r') as fread:
                fread.read(pat)
       except TypeError:
           print("Type not supported.")
       except FileNotFoundError:
           print("File not found.")
       except PermissionError:
           print("You don't have the permission to read that file!")
       except NotADirectoryError:
           print("Why the heck are you doing a nonexistant directory?! This isn't even for directories!")
    if iput == "atfile":
        pata = input("Which path? (Full path, for example: C:/Users/MainUser/Documents/readme.txt)")
        print("This is the contents of the file")
        with open(pata, 'r') as freadd:
                 freadd.read(pata)
        fca = input("File contents (use \n for newline) ")
        with open(pata, 'a') as filea:
               filea.append(fca)

       