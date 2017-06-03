import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor ("grey")
    abcd = turtle. Turtle()
    abcd.shape("turtle")
    abcd.color("red")
    abcd.speed (2)
    
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)
    abcd.forward(200)
    abcd.right(90)

    efgh=turtle.Turtle()
    efgh.shape("arrow")
    efgh.color("green")
    efgh.circle (100)
    window.exitonclick()
draw_square()
    
    
