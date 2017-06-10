import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor ("blue")
    
    a = turtle. Turtle()
    turtle.speed (0.1)
    a.color ("grey")

    for outersquare in range (0,4):

        a.forward(200)
        a.right(90)

        for innersquare in range (0,4):
            a.forward(100)
            a.left(90)
      
    window.exitonclick()

draw_square()
