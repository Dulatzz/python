import os

path = input("Insert your path to file: ")
name = input("Insert name of file you want to delete: ")

if os.access(path, os.F_OK):
    os.remove(f'{path}\\{name}.txt')
    print("File was successfully deleted")
else: 
    print("The path does not exist")