number = input('Enter please a number')

a = ''
for i in range(len(number)):
    i += 1
    a += number[-i]

print(a)
