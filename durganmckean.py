#turtle
import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

circle_color = input("What color do you want for the circles?")
painter.color(user_color)

painter.penup()
painter.goto(-40,20)
painter.pendown()

painter.begin_fill()
painter.circle(50,360)
painter.end_fill()

painter.penup()
painter.goto(40,20)
painter.penup()

painter.begin_fill()
painter.circle(50,360)
painter.end_fill()

painter.penup()
painter.goto(0,-100)
painter.pendown()

painter.circle(75,360)

wn = trtl.Screen() wn.mainloop()
