import turtle

# --- Basic Functions ---
def draw_rectangle(width, height):
    """Draw a rectangle with given width and height."""
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def draw_square(size):
    """Draw a square of given size."""
    draw_rectangle(size, size)

# --- Character Drawing ---
turtle.speed(3)

# Head
turtle.penup()
turtle.goto(-50, 100)  # position head
turtle.pendown()
draw_square(50)

# Body
turtle.penup()
turtle.goto(-25, 100)  # start at bottom of head
turtle.pendown()
draw_rectangle(25, 100)  # long rectangle body

# Left Arm
turtle.penup()
turtle.goto(-50, 80)
turtle.pendown()
draw_rectangle(25, 80)

# Right Arm
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
draw_rectangle(25, 80)

# Left Leg
turtle.penup()
turtle.goto(-25, 0)
turtle.pendown()
draw_rectangle(25, 80)

# Right Leg
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
draw_rectangle(25, 80)

# --- Simple Sword Shape ---
turtle.penup()
turtle.goto(25, 40)  # position in right hand
turtle.pendown()
draw_rectangle(60, 10)  # sword blade
turtle.penup()
turtle.goto(25, 35)
turtle.pendown()
draw_rectangle(10, 30)  # sword handle

turtle.done()
