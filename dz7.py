a, b, c = input('Enter the sites a, b, c of a triangle: ').split()
sites = [int(a), int(b), int(c)]

max_site = 0
short_site1 = 0
short_site2 = 0
for i in sites:
    if i > max_site:
        if short_site1 == 0:
            short_site1 = max_site
            max_site = i
        else:
            short_site2 = max_site
            max_site = i
    elif short_site1 == 0:
        short_site1 = i
    else:
        short_site2 = i

if short_site1 + short_site2 > max_site:
    if short_site1 == short_site2 == max_site:
        print('The triangel is equilateral.')
    elif short_site1 == short_site2:
        print('The triangel is isosceles.')
    else:
        print('The triangel is non-isosceles.')
else:
    print('It is not possible to draw a triangel with this sites.')