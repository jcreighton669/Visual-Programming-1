# This program draws the stars of the Orion constellation,
# the names of the stars, and the constellation lines.
import turtle

# Set the window size.
turtle.setup(500, 600)
turtle.speed(10)

# setup the turtle.
turtle.penup()
turtle.shape('turtle')

# create named constants for the star coordinates.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw the stars.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Betegeuse')
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Meissa')
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Alnitak')
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Alnilam')
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Mintaka')
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Saiph')
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Rigel')

turtle.dot()

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.penup()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup

turtle.done()
