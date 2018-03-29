import turtle

def triangle(some_turtle):
	"""
	This function takes a turtle as an input
	and it draws a fractal. 
	"""
	for _ in range(3):
		some_turtle.fd(37.5)
		some_turtle.left(120)

def bigger_triangle(some_turtle_2 ):
	"""
	This funciton takes a turtle and draws a bigger fractal. 
	"""
	for _ in range(3):
		
		# Draw 3 triangle in a line
		# At the end it moves one side ahead of 
		# the startig point of the triangle
		for _ in range(3):
			some_turtle_2.color("black", "green")
			some_turtle_2.begin_fill()
			triangle(some_turtle_2)
			some_turtle_2.end_fill()
			some_turtle_2.fd(37.5)

		# At the end of the 3rd triangle
		# It moves one side ahead of the end point
		# i.e it is 2 sides ahead of the starting point of the 
		# 3rd triangle	
		some_turtle_2.left(120)
		some_turtle_2.fd(37.5)
	

def all_triangle():
	"""
	This functin sets the screen where
	the fractals is drawn and it also
	creates a turtle object.
	"""
	
	# Screen for the graphics
	window = turtle.Screen()
	
	# Turtle object as rohit
	rohit = turtle.Turtle()
	rohit.speed(10)

	# First part of the fractal
	bigger_triangle(rohit)
	
	# Adjustment for the 2nd part of the fractal
	rohit.fd(150)
	# Drawing Second part of the fractal
	bigger_triangle(rohit)
	
	# Adjustment for the final part of the fracral
	rohit.fd(150 - 37.5)
	rohit.left(120)
	rohit.fd(150 + 37.5)
	# Drawing final fractal
	bigger_triangle(rohit)

	window.exitonclick()

# Function Call
all_triangle()