import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor ("grey")
    abcd = turtle. Turtle()
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)
    turtle.color ("black","green")
    turtle.begin_fill()
    turtle.circle (100)
    turtle.end_fill()
    window.exitonclick()
draw_square()
    
    
