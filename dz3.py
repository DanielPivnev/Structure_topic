dot1_x, dot1_y = input('Enter please a random dot: ').split(' ')
dot2_x, dot2_y = input('Enter please a random dot: ').split(' ')

dot1_x, dot1_y, dot2_x, dot2_y = int(dot1_x), int(dot1_y), int(dot2_x), int(dot2_y)

pitch = (dot2_y - dot1_y) / (dot2_x - dot1_x)
y_axis_intersection = 0
if dot1_x > 0:
    y_axis_intersection = dot1_x * (- pitch) + dot1_y
else:
    y_axis_intersection = dot1_y - dot1_x * (- pitch)

if y_axis_intersection > 0:
    print(f'The function is: f(x) = {round(pitch, 2)}x + {round(y_axis_intersection, 2)}')
elif y_axis_intersection < 0:
    print(f'The function is: f(x) = {round(pitch, 2)}x - {round(y_axis_intersection, 2) * (-1)}')
else:
    print(f'The function is: f(x) = {round(pitch, 2)}x')
