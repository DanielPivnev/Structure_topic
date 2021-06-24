import string

edge1, edge2 = input('Enter please the edges: ').split()
alphabet = string.ascii_lowercase

print(f'The position of {edge1} in alphabet is {alphabet.index(edge1.lower()) + 1}. \n'
      f'The position of {edge2} in alphabet is {alphabet.index(edge2.lower()) + 1}. \n'
      f'And between them are {(alphabet.index(edge2.lower()) + 1) - (alphabet.index(edge1.lower()) + 1) - 1} letters.')
