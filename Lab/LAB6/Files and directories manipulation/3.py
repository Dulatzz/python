import os

path = input("Insert your path: ")

if os.access(path, os.F_OK):
    print(os.listdir(path))
else: 
    print("The path does not exist")