
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display and game constants
ball = False
DISPLAYSURF = pygame.display.set_mode((700, 1100))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (207, 155, 59)
fps = 60
clock = pygame.time.Clock()

score = 0
miss = 0

# Load images and set up game objects
img3 = pygame.image.load('ni/rim.png')
court = pygame.image.load('ni/court.webp')
ball_img = pygame.image.load('ni/basketball.png')

ball_img = pygame.transform.scale(ball_img, (100, 100))
ball_rect = ball_img.get_rect()
ball_y = ball_rect.y

court = pygame.transform.scale(court, (700, 1100))
img = pygame.transform.scale(img3, (120, 120))
img_rect = img.get_rect()

img_rect.x = 200
img_rect.y = 150
y = 550
y2 = 570

score_rect = pygame.Rect((260, 145), (180, 100))
miss_left = pygame.Rect((0, 145), (255, 100))
miss_right = pygame.Rect((450, 145), (299, 100))

# Main game loop
while True:
    clock.tick(fps)

    # Draw game objects on the screen
    DISPLAYSURF.blit(court, (0, 0))
    DISPLAYSURF.blit(img, (img_rect.x, y))
    pygame.draw.rect(DISPLAYSURF, RED, score_rect)
    pygame.draw.rect(DISPLAYSURF, GREEN, miss_left)
    pygame.draw.rect(DISPLAYSURF, GREEN, miss_right)

    ball_rect.x = img_rect.x
    ball_rect.y = y2

    # Display score
    font = pygame.font.SysFont('Calibri', 55, True, False)
    text = font.render(f'SCORE: {score}', True, GREEN)
    DISPLAYSURF.blit(text, (160, 80))

    # Percentage calculator
    shots = score + miss
    if shots >= 1:
        percent = (score / shots) * 100
        percent = round(percent, 2)
    else:
        shots = 1
        percent = (score / shots) * 100
        percent = round(percent, 2)
    
    text = font.render(f'({percent}%)', True, GREEN)
    DISPLAYSURF.blit(text, (270, 150))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handle user input for ball movement and scoring
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ball = True
            while ball:
                y2 -= 10
                ball_rect.y = y2
                DISPLAYSURF.blit(ball_img, (img_rect.x, y2))
                pygame.display.update()

                DISPLAYSURF.blit(court, (0, 0))
                DISPLAYSURF.blit(img, (img_rect.x, y))

                text = font.render(f'SCORE: {score}', True, GREEN)
                DISPLAYSURF.blit(text, (160, 80))

                shots = score + miss
                if shots >= 1:
                    percent = (score / shots) * 100
                    percent = round(percent, 2)
                else:
                    shots = 1
                    percent = (score / shots) * 100
                    percent = round(percent, 2)

                text = font.render(f'({percent}%)', True, GREEN)
                DISPLAYSURF.blit(text, (270, 150))

                if y2 <= 0:  # Reset ball position if it reaches the top
                    ball = False
                    y2 = 570

        # Reset ball position if not in use
        if not ball:
            y2 = 570

    # Update the display
    pygame.display.update()