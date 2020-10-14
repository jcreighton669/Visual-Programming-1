# 2)	Areas of Rectangles The area of a rectangle is the rectangle’s length times its width.
# 		Write a program that asks for the length and width of two rectangles. The program should tell
# 		the user which rectangle has the greater area, or if the areas are the same.
# 		The Areas of Rectangles Problem

width1 = int(input('Enter the width of the first rectangle: '))
height1 = int(input('Enter the height of the first rectangle: '))

width2 = int(input('Enter the width of the second rectangle: '))
height2 = int(input('Enter the height of the second rectangle: '))

area1 = width1 * height1
area2 = width2 * height2

if area1 > area2:
    print('The area of the first rectangle is larger')
elif area2 > area1:
    print('The area of the second rectangle is larger')
else:
    print('The areas are equal')
