from random import randint
import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
game_over = False
score = 0
FONT = ("Arial", 30, "bold")

#score turtle
score_turtle = turtle.Turtle()

def making_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()
    score_turtle.setposition(0, 350)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)

#Our main turtle. When clicked, it will reappear at a random location.
game_turtle = turtle.Turtle()

def making_turtle_clicked():
    game_turtle.color("green")
    game_turtle.shape("turtle")
    game_turtle.shapesize(2)
    game_turtle.penup()

def reset_position(x, y):
    global score
    score = score + 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)
    game_turtle.hideturtle()
    game_turtle.goto(randint(-225, 225), randint(-225, 225))  # The range of locations where it can reappear.
    game_turtle.showturtle()

# timer turtle
timer_turtle = turtle.Turtle()

def timer(time):
    global game_over
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.setposition(0, 300)
    timer_turtle.clear()

    if time > 0:
        timer_turtle.clear()
        timer_turtle.write(f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: timer(time - 1), 1000)

    else:
        game_over = True
        screen.clear()
        screen.bgcolor("light blue")
        timer_turtle.write("Game Over!", move=False, align="center", font=FONT)
        score_turtle.write(f"Your Total Score: {score}", move=False, align="center", font=FONT)

        if score >= 25:
            timer_turtle.color("red")
            timer_turtle.setposition(0, 0)
            timer_turtle.write(arg="Perfect!", move=False, align="center", font=FONT)

        elif score >= 21 and score <= 24:
            timer_turtle.color("orange")
            timer_turtle.setposition(0, 0)
            timer_turtle.write(arg="Very Good!", move=False, align="center", font=FONT)

        elif score >= 14 and score <= 20:
            timer_turtle.color("yellow")
            timer_turtle.setposition(0, 0)
            timer_turtle.write(arg="Good!", move=False, align="center", font=FONT)

        elif score >= 5 and score <= 13:
            timer_turtle.color("brown")
            timer_turtle.setposition(0, 0)
            timer_turtle.write(arg="Not Bad!", move=False, align="center", font=FONT)

        elif score < 5:
            timer_turtle.color("red")
            timer_turtle.setposition(0, 0)
            timer_turtle.write(arg="Very bad!", move=False, align="center", font=FONT)

def starting_game():
    global game_over
    game_over = False
    turtle.tracer(0)
    making_score_turtle()
    making_turtle_clicked()
    game_turtle.onclick(reset_position)
    turtle.tracer(1)
    screen.ontimer(lambda: timer(20), 20)  # Timer will start from the 20. second

starting_game()
screen.mainloop()