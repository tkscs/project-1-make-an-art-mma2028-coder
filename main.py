import turtle
turtle.speed(0)
for _ in range(4):      
    turtle.forward(100)  
    turtle.right(90) 
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def draw_sword():
    # Handle
    turtle.color("brown")
    turtle.begin_fill()
    for z in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)

    # Guard
    turtle.color("gold")
    turtle.begin_fill()
    for o in range(2):
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
    turtle.right(180)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    for o in range(2):
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
    turtle.end_fill()
    # turtle.forward(40)
    # turtle.left(90)
    # turtle.forward(15)
    # turtle.right(10)

    turtle.right(90)
    turtle.forward(15)
    turtle.color("silver")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(200)
    turtle.end_fill()

    turtle.left(90)


    # turtle.left(90)


    
x = 90 # shows that you can substitute 90 degree with x
y = 50 # shows that you can substitute 50 degree with y
turtle.right(x)
turtle.forward(100)
turtle.left(x)
turtle.forward(y)
turtle.right(x)

# left side
turtle.right(x)
turtle.forward(30)
turtle.left(x)
turtle.forward(y)
# reverse left side
turtle.right(180)
turtle.forward(y)
turtle.right(x)
turtle.forward(60)
turtle.right(x)
turtle.forward(y)
turtle.left(x)
turtle.forward(70)
turtle.right(x)
turtle.forward(200)
turtle.right(180)
turtle.forward(200)
turtle.left(x)
turtle.forward(70)
turtle.right(x)
turtle.forward(y)
turtle.left(x)
turtle.forward(60)
turtle.left(x)
turtle.forward(y)
turtle.right(90)
turtle.forward(70)
turtle.left(x)
turtle.forward(y)
turtle.right(45)
draw_rectangle(150, 60)
turtle.left(45)
turtle.forward(150)
turtle.left(x)
turtle.forward(200)
turtle.left(x)
turtle.forward(170)
turtle.right(y)
draw_rectangle(150,60)


turtle.forward(150)

draw_sword()
turtle.end_fill()
turtle.up()
turtle.goto(-50, -350)
turtle.down()
turtle.right(40)
draw_rectangle(100, 400)
turtle.forward(100)
draw_rectangle(100, 400)

turtle.exitonclick()