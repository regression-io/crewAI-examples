import pygame
import time
import random

# Initialize the game
pygame.init()

# Set game parameters
width, height = 600, 400
cell_size = 20
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake parameters
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
snake_length = 3

# Food parameters
food_pos = [random.randrange(1, (width // cell_size)) * cell_size,
            random.randrange(1, (height // cell_size)) * cell_size]
food_spawn = True

# Scoring
score = 0


# Functions
def show_score(choice, score):
    score_font = pygame.font.SysFont('times new roman', 35)
    score_surface = score_font.render('Score : ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    game_display.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    game_display.fill(black)
    game_display.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Game loop
while True:
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pygame.quit()  # Added to quit the game when the window is closed
        #     quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously, we don't want the snake to move in the opposite direction
    if change_to == 'UP' and snake_direction != 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and snake_direction != 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_pos[0][1] -= cell_size
    if snake_direction == 'DOWN':
        snake_pos[0][1] += cell_size
    if snake_direction == 'LEFT':
        snake_pos[0][0] -= cell_size
    if snake_direction == 'RIGHT':
        snake_pos[0][0] += cell_size

    # Snake body growing mechanism
    snake_pos.insert(0, list(snake_pos[0]))
    if snake_pos[0] == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                    random.randrange(1, (height // cell_size)) * cell_size]
    food_spawn = True

    # Draw everything
    game_display.fill(blue)
    for pos in snake_pos:
        pygame.draw.rect(game_display, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    pygame.draw.rect(game_display, white, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    # Game over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        game_over()
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    # Score display
    show_score(1, score)

    # Update the display
    pygame.display.update()

    # Frame rate
    clock.tick(15)