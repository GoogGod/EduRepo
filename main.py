import pygame
import sys
from random import choice
from time import sleep

# Initialize Pygame
pygame.init()

# Set up some constants and initialize variables
WIDTH, HEIGHT = 1280, 720
FPS = 144
PADDLE_WIDTH = 15
BALL_SIZE = 15
SPEED = 3

C_WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font('bahnschrift.ttf', 36)

# Define classes for paddle and ball
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, 100)

    def move(self, direction):
        if direction == 'up' and self.rect.y > 0:
            self.rect.y -= SPEED
        elif direction == 'down' and self.rect.y < HEIGHT - 100:
            self.rect.y += SPEED

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = SPEED * (choice([-1, 1]))
        self.speed_y = SPEED * (choice([-1, 1]))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

# Create paddles and ball instances
left_paddle = Paddle(50, HEIGHT // 2 - 50)
right_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - 50)
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Main game loop
running = True
wait_score = False
score_left = 0
score_right = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    left_paddle.move('up' if keys[pygame.K_w] else 'down' if keys[pygame.K_s] else None)
    right_paddle.move('up' if keys[pygame.K_UP] else 'down' if keys[pygame.K_DOWN] else None)

    # Update game objects
    ball.update()
    if wait_score: 
        wait_score = not wait_score
        text = font.render(f"{score_left} : {score_right}", True, C_WHITE)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, 30)))
        for i in range(30):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            clock.tick(FPS)
            sleep(0.1)
    
    # Check for collisions with screen boundaries and paddles
    if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
        ball.speed_y *= -1

    if ball.rect.left <= left_paddle.rect.right and \
       ball.rect.colliderect(left_paddle.rect):
        ball.speed_x *= -1

    if ball.rect.right >= right_paddle.rect.left and \
       ball.rect.colliderect(right_paddle.rect):
        ball.speed_x *= -1

    # Check for scoring
    if ball.rect.left <= 0:
        print("Right player scores!")
        ball.__init__(WIDTH // 2, HEIGHT // 2)
        left_paddle.__init__(50, HEIGHT // 2 - 50)
        right_paddle.__init__(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - 50)
        wait_score = True
        score_right += 1

    elif ball.rect.right >= WIDTH:
        print("Left player scores!")
        ball.__init__(WIDTH // 2, HEIGHT // 2)
        left_paddle.__init__(50, HEIGHT // 2 - 50)
        right_paddle.__init__(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - 50)
        wait_score = True
        score_left += 1

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, C_WHITE, left_paddle.rect)
    pygame.draw.rect(screen, C_WHITE, right_paddle.rect)
    pygame.draw.ellipse(screen, C_WHITE, ball.rect)

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
