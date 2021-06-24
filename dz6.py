import string

position_of_the_letter = input('Enter please a position of a letter: ')
alphabet = string.ascii_lowercase

print(f'The letter at this position in alphabet is "{alphabet[int(position_of_the_letter) - 1]}".')
