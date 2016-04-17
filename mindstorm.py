import turtle

def draw_square(some_turtle):
	for i in range(40):
		for x in range(4):
			some_turtle.forward(100)
			some_turtle.right(90)
		some_turtle.right(10)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	#create the turtle brad - draws a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(0.5)
	draw_square(brad)
	# create the turtle Angie - Draws a circle
	# angie = turtle.Turtle()
	# angie.shape("arrow")
	# angie.color("blue")
	# angie.circle(100)

	window.exitonclick()

draw_art()
