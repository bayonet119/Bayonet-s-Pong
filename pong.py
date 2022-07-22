import pygame
from pygame import mixer
import random

def main():
    # Variables
    score1 = 0
    score2 = 0

    ball_rect = pygame.Rect(640, 360 ,10, 10)
    ball_vel_y = 5
    ball_vel_x = -5

    paddle_vel_y = 13
    paddle1 = pygame.Rect(50, 360, 10, 50)
    paddle2 = pygame.Rect(1205, 360, 10, 50)

    line = pygame.image.load('data/images/line.png')
    line_rect = line.get_rect()
    line_rect.y = 0
    line_rect.x = 638

    # Initializing pygame
    pygame.init()

    # Font
    font = pygame.font.Font('data/fonts/bit5x3.ttf', 64)

    # Creating the window
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Bayonet's Pong")

    # Colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    # Game loop
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bouncing the ball
        ball_rect.y += ball_vel_y
        ball_rect.x += ball_vel_x

        # Controls
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_w] and paddle1.y > 0:
            paddle1.y -= paddle_vel_y
        if userInput[pygame.K_s] and paddle1.y < 670:
            paddle1.y += paddle_vel_y
        if userInput[pygame.K_UP] and paddle2.y > 0:
            paddle2.y -= paddle_vel_y
        if userInput[pygame.K_DOWN] and paddle2.y < 670:
            paddle2.y += paddle_vel_y

        # Drawing the paddles and the balls
        screen.blit(line, line_rect)
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.rect(screen, WHITE, ball_rect)

        # Ball changing direction after colliding with one of the paddles or one of the screen border

        if ball_rect.x == 1280:
            score_sfx = mixer.Sound('data/audio/score.wav')
            score_sfx.play()
            score1 += 1
            ball_vel_y = 5
            ball_vel_x = random.choice((-5, 5))
            ball_rect.y = random.randint(0, 720)
            ball_rect.x = 640
            print(ball_vel_x)
            print(ball_rect.y)

        if ball_rect.x == 0:
            score_sfx = mixer.Sound('data/audio/score.wav')
            score_sfx.play()
            score2 += 1
            ball_vel_y = 5
            ball_vel_x = random.choice((-5, 5))
            ball_rect.y = random.randint(0, 720)
            ball_rect.x = 640
            print(ball_vel_x)
            print(ball_rect.y)

        if ball_rect.y > 720 or ball_rect.y < 0:
            wall_hit = mixer.Sound('data/audio/wall.wav')
            wall_hit.play()
            ball_vel_y *= -1

        if ball_rect.colliderect(paddle1) or ball_rect.colliderect(paddle2):
            paddle_hit = mixer.Sound('data/audio/paddle.wav')
            paddle_hit.play()
            ball_vel_x *= -1
            ball_vel_y *= -1

        # Text
        gscore1 = font.render(str(score1), True, WHITE)
        gscore2 = font.render(str(score2), True, WHITE)
        screen.blit(gscore1, (314, 20))
        screen.blit(gscore2, (942, 20))

        # Some other stuff
        pygame.time.delay(7)
        pygame.display.update()

if __name__ == "__main__":
    main()
