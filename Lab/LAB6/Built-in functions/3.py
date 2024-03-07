def polindrome(string):
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")

string = input("Insert your string: ")
polindrome(string)