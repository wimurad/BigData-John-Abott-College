import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor ("red")

    a = turtle. Turtle()

    for count in range (0,4):
    
        a.forward(200)
        a.right(90)
                
    b = turtle.Turtle ()
    b.shape("arrow")
    b.color ("blue")
    b.circle (100)

    c = turtle.Turtle ()
    c.shape ("arrow")
    c.color ("yellow")

    count = 0
    a.forward(200)
    for count in range (0,3):
    
        a.forward(200)
        a.left(120)
    
    
    window.exitonclick()

draw_square()
    
    
