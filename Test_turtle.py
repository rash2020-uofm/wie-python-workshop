# ------------------------------------------------------------------------------ #
# ----------------- WIE Winnipeg's High School Python Workshop ----------------- #
# ---------------------- An Introduction to Python Basics ---------------------- #
# ------------------------------- March 13, 2022 ------------------------------- #
# ------------------------------------------------------------------------------ #

# -------------------------------  Python turtle Library  ---------------------- #

# A Python library that consist of a set of predefined functions which enables us to draw pictures and shapes on a virtual canvas
# Onscreen pen that we use is called the turtle
# To use any kind of Python library, we need to import the library into the Python environment
import turtle

# turtle is a graphical library, hence we will need to create a separate window called the screen to carry out any drawing command.
# To create the screen we have to initializing a variable for the screen
sc = turtle.getscreen()

# The little black arrowhead in the middle of the screen is called the turtle.
# Note that in a virtual screen the distance is measured in pixels, like we measure distance in cm on using a ruler.
# Please refer the booklet for a detail diagram of the screen

# Lesson 1: Draw a shape using the turtle
# First so we need to assign a variable to the turtle.
my_turtle = turtle.Turtle()

# If you want to draw no lines on the screen you can use the command
# >>> my_turtle.up() >> It will put the pen down and nothing will be drawn on the screen
# or
# >>>my_turtle.penup()
# If you want to draw no lines on the screen you can use
# >>> my_turtle.down() >> the pen will start to draw
# or
# >>> my_turtle.pendown()
#
# We can use commands forward, backward, right, and left to move my_turtle  around the screen
# Using commands forward and backward you can move the turtle in the forward direction and backward direction
# Using commands right, and left  you can rotate my_turtle in certain angle

# Lesson 1.1 : Draw a square of size 100x100 pixels
# Step 1 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)
# Step 2 - Turn my_turtle 90 degrees to your left
my_turtle.left (90)
# Step 3 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)
# Step 4 - Turn my_turtle 90 degrees to your left
my_turtle.left (90)
# Step 5 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)
# Step 6 - Turn my_turtle 90 degrees to your left
my_turtle.left (90)
# Step 7 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)

# Lesson 1.2 : Draw a triangle that has equal sides (equilateral triangle) size 100 pixels
# Step 1 - Turn my_turtle 60 degrees to your left
my_turtle.left (60)
# Step 2 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)
# Step 3 - Turn my_turtle 120 degrees to your right
my_turtle.right (120)
# Step 4 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)
# Step 5 - Turn my_turtle 120 degrees to your right
my_turtle.right (120)
# Step 6 - Move my_turtle in the forward direction 100 pixels
my_turtle.forward (100)

# Another way to move my_turtle is using x and y coordinates.
# As we said earlier, the measurement we use on a virtual screen is pixels.
# So we can specify the x and y coordinate that we want my_turtle to move.
# Let’s move my_turtle to move to (x,y) = (150,100)
my_turtle.goto(150,100)



# We can draw the above shapes using this command too. Try it yourself!!

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
# Draw a square and a trangle using (x,y) coordinates                  #
# -------------------------------------------------------------------- #

# Apart from this we have so many commands that we can use.
# We can change the color of the screen, try "blue",  "green", "red"
# >>> sc.bgcolor(“color”)
# (Note: sc is the name of our screen variable)
# To clear whatever that you draw on your screen
# >>>sc.clear()

# We can change the size of the screen
# >>> sc.setup(width=1000, height=600)

# There are commands you can use to change the size, color, shape, speed of the pen my_turtle
# How to change the speed of the pen
# >>>my_turtle.speed(my_speed)
# my_speed  can take integer values from 0-10, and 10 is the highest speed you can assign



# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
# Can you write the first letter of your first name on the “screen”    #
# or maybe your first name !!                                          #
# -------------------------------------------------------------------- #

