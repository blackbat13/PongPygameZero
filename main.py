import pgzrun
import random

""" CONFIGURATION """

WIDTH = 800
HEIGHT = 600

TITLE = "Pong Pygame Zero"

BG_COLOR = (64, 64, 64)
FG_COLOR = "yellow"

""" VARIABLES """

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


""" DRAW """


def draw():
    screen.fill(BG_COLOR)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color=FG_COLOR)

    left.draw()
    right.draw()
    ball.draw()

    draw_points()
    draw_result()


def draw_points():
    """Draws players points
    """
    screen.draw.text(f"Left: {left.points}",
                     color=FG_COLOR,
                     center=(WIDTH / 4 - 20, 20),
                     fontsize=48)

    screen.draw.text(f"Right: {right.points}",
                     color="yellow",
                     center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
                     fontsize=48)


def draw_result():
    """Draws results after finishing the game
    """
    if left.win:
        screen.draw.text("LEFT WINS!!!",
                         color=FG_COLOR,
                         center=(WIDTH / 2, HEIGHT / 2),
                         fontsize=96)

    if right.win:
        screen.draw.text("RIGHT WINS!!!",
                         color=FG_COLOR,
                         center=(WIDTH / 2, HEIGHT / 2),
                         fontsize=96)


""" UPDATE """


def update():
    if not (left.win or right.win):
        update_players()
        update_ball()


def update_players():
    """Updates players positions based on the pressed keys
    """
    if keyboard.w and left.top > 40:
        left.y -= left.vy

    if keyboard.s and left.bottom < HEIGHT - 40:
        left.y += left.vy

    if keyboard.up and right.top > 40:
        right.y -= right.vy

    if keyboard.down and right.bottom < HEIGHT - 40:
        right.y += right.vy


def update_ball():
    """Updates ball position
    """
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


""" HELPERS """


def reset_ball():
    """Resets ball position
    """
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 2
    ball.vx = random.choice([-5, 5])
    ball.vy = random.choice([-5, 5])


""" INITIALIZATION """

pgzrun.go()
