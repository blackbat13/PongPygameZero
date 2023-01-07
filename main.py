import pgzrun
import random

""" CONFIGURATION """

WIDTH = 800
HEIGHT = 600

TITLE = "Pong Pygame Zero"

VERTICAL_MARGIN = 40
HORIZONTAL_MARGIN = 20
BG_COLOR = (64, 64, 64)
FG_COLOR = "yellow"
POINTS_TO_WIN = 11

""" VARIABLES """

left = Actor("left")
left.x = HORIZONTAL_MARGIN
left.y = HEIGHT / 2
left.vy = 5
left.points = 0
left.win = False

right = Actor("right")
right.x = WIDTH - HORIZONTAL_MARGIN
right.y = HEIGHT / 2
right.vy = 5
right.points = 0
right.win = False

ball = Actor("ball")


""" DRAW """


def draw():
    screen.fill(BG_COLOR)
    screen.draw.line((WIDTH / 2, VERTICAL_MARGIN), (WIDTH / 2,
                     HEIGHT - VERTICAL_MARGIN), color=FG_COLOR)

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
                     center=(WIDTH / 4 - HORIZONTAL_MARGIN, HORIZONTAL_MARGIN),
                     fontsize=48)

    screen.draw.text(f"Right: {right.points}",
                     color=FG_COLOR,
                     center=(WIDTH / 2 + WIDTH / 4 -
                             HORIZONTAL_MARGIN, HORIZONTAL_MARGIN),
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
        update_winner()


def update_players():
    """Updates players positions based on the pressed keys
    """
    if keyboard.w and left.top > VERTICAL_MARGIN:
        left.y -= left.vy

    if keyboard.s and left.bottom < HEIGHT - VERTICAL_MARGIN:
        left.y += left.vy

    if keyboard.up and right.top > VERTICAL_MARGIN:
        right.y -= right.vy

    if keyboard.down and right.bottom < HEIGHT - VERTICAL_MARGIN:
        right.y += right.vy


def update_ball():
    """Updates ball
    """
    update_ball_position()
    update_ball_collision()
    update_ball_exit()


def update_ball_position():
    """Updates ball position on the screen
    """
    ball.x += ball.vx
    ball.y += ball.vy


def update_ball_collision():
    """Checks for ball collisions and updates it movement
    """
    if ball.top <= VERTICAL_MARGIN or ball.bottom >= HEIGHT - VERTICAL_MARGIN:
        ball.vy *= -1

    if left.colliderect(ball) and ball.vx < 0:
        ball.vx *= -1

    if right.colliderect(ball) and ball.vx > 0:
        ball.vx *= -1


def update_ball_exit():
    """Checks if the ball exited on the left or right side and updates players points accordingly
    """
    if ball.left <= 0:
        reset_ball()
        right.points += 1

    if ball.right >= WIDTH:
        reset_ball()
        left.points += 1


def update_winner():
    """Checks if one of the players won the game
    """
    if right.points == POINTS_TO_WIN:
        right.win = True
        ball.game_over = True

    if left.points == POINTS_TO_WIN:
        left.win = True
        ball.game_over = True


""" HELPERS """


def reset_ball():
    """Resets ball position
    """
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 2
    ball.vx = random.choice([-6, -5, -4, 4, 5, 6])
    ball.vy = random.choice([-6, -5, -4, 4, 5, 6])


""" INITIALIZATION """

reset_ball()
pgzrun.go()
