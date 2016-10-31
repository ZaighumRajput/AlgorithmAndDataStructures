import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()



def draw_spiral(myTurtle, line_length):
	if line_length > 0:
		myTurtle.forward(line_length)
		myTurtle.right(90)
		draw_spiral(myTurtle, line_length - 5)

draw_spiral(myTurtle, 100)
myWin.exitonclick()
