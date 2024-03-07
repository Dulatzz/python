def upper_and_lower (list):
    lower_letters = 0
    upper_letters = 0
    for word in list:
        for letter in word:
            if letter.isupper():
                upper_letters += 1
            else:
                lower_letters += 1
    print (f'Amount of uppercase letters: {upper_letters}')
    print (f'Amount of lowercase letters: {lower_letters}')
    
list = list(input("Insert the string: ").split())
upper_and_lower(list)