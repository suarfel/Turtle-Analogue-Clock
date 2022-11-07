import turtle
import datetime
import time
#  screen leveling
window_screen=turtle.Screen()
window_screen.tracer(0)
window_screen.bgcolor("black")
#declaring the turtles 
writer=turtle.Turtle()
writer.hideturtle()
second_hand=turtle.Turtle()
second_hand.hideturtle()
minute_hand=turtle.Turtle()
minute_hand.hideturtle()
hour_hand=turtle.Turtle()
hour_hand.hideturtle()
#  read the current time
hour =datetime.datetime.now().hour
minute =datetime.datetime.now().minute
second=datetime.datetime.now()