import collections


columns = ['h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'hA', 'hB', 'hC', 'hD', 'hE', 'hF']
HexaNumbers = collections.namedtuple('HexaNumbers', columns)
hexa_numbers = HexaNumbers('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
a = list(input('Pleas enter: ').upper())
b = list(input('Pleas enter: ').upper())
a_decimal = 0
b_decimal = 0
c_decimal = 0
c_mult = []
c_add = []


def get_hexa_number(n, nt=hexa_numbers):
    hexa_number = []

    while True:
        hexa_number.append(n % 16)
        n = int(n/16)
        if n < 16:
            hexa_number.append(n)
            break

    for x in hexa_number:
        hexa_number.append(nt[hexa_number[0]])
        del hexa_number[0]

    len_hexa_number = len(hexa_number)
    for _ in range(len_hexa_number):
        hexa_number.append(hexa_number[len_hexa_number - 1])
        del hexa_number[len_hexa_number - 1]
        len_hexa_number -= 1

    return hexa_number


j1 = len(a) - 1
j2 = len(b) - 1
for i in range(max(len(a), len(b))):
    if len(a) > i:
        a_decimal += int(hexa_numbers.index(a[i])) * 16**j1
        j1 -= 1
    if len(b) > i:
        b_decimal += int(hexa_numbers.index(b[i])) * 16**j2
        j2 -= 1
c_mult = get_hexa_number(a_decimal * b_decimal)
c_add = get_hexa_number(a_decimal + b_decimal)

print('Mult. : ', *c_mult, '\n', 'Add.  : ', *c_add, sep='')
