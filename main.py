import pgzrun
import random


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

bg_color = (64, 64, 64)

left = Actor("left")
left.x = 20
left.y = HEIGHT / 2
left.vy = 5
left.points = 0
left.win = False

right = Actor("right")
right.x = WIDTH - 20
right.y = HEIGHT / 2
right.vy = 5
right.points = 0
right.win = False

ball = Actor("ball")
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.vx = 5
ball.vy = 5


def draw():
    screen.fill(bg_color)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    left.draw()
    right.draw()
    ball.draw()
    draw_points()
    draw_result()


def draw_points():
    screen.draw.text(f"Lewy: {left.points}",
                     color="yellow",
                     center=(WIDTH / 4 - 20, 20),
                     fontsize=48)

    screen.draw.text(f"Prawy: {right.points}",
                     color="yellow",
                     center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
                     fontsize=48)


def draw_result():
    if left.win:
        screen.draw.text("LEWY WYGRYWA!!!",
                            color="yellow",
                            center=(WIDTH / 2, HEIGHT / 2),
                            fontsize=96)

    if right.win:
        screen.draw.text("PRAWY WYGRYWA!!!",
                            color="yellow",
                            center=(WIDTH / 2, HEIGHT / 2),
                            fontsize=96) 
    

def update():
    if not (left.win or right.win):
        move_players()
        move_ball()


def move_players():
    if keyboard.w and left.top > 40:
        left.y -= left.vy

    if keyboard.s and left.bottom < HEIGHT - 40:
        left.y += left.vy

    if keyboard.up and right.top > 40:
        right.y -= right.vy

    if keyboard.down and right.bottom < HEIGHT - 40:
        right.y += right.vy
    

def move_ball():
    ball.x += ball.vx
    ball.y += ball.vy

    if ball.top <= 40:
        ball.vy *= -1

    if ball.bottom >= HEIGHT - 40:
        ball.vy *= -1

    if left.colliderect(ball):
        ball.vx *= -1

    if right.colliderect(ball):
        ball.vx *= -1

    if ball.left <= 0:
        reset_ball()
        right.points += 1

    if ball.right >= WIDTH:
        reset_ball()
        left.points += 1

    if right.points == 11:
        right.win = True
        ball.game_over = True

    if left.points == 11:
        left.win = True
        ball.game_over = True
    

def reset_ball():
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 2
    ball.vx = random.choice([-5, 5])
    ball.vy = random.choice([-5, 5])


pgzrun.go()