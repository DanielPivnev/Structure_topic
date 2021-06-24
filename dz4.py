import random

edge1, edge2 = input('Enter please the edges of the symbols or numbers: ').split()

if edge1[1:].isdigit() and edge1[0] == '-' or edge1.isdigit():
    print(random.random() * (int(edge2) - int(edge1)) + int(edge1))
elif '-' == edge1.split('.')[0][0] and edge1.split('.')[0][1:].isdigit() or edge1.split('.')[0].isdigit() \
        and edge1.split('.')[1].isdigit():
    print(random.random() * (float(edge2) - float(edge1)) + float(edge1))
else:
    print(chr(int(random.random() * (ord(edge2) - ord(edge1)) + ord(edge1))))
