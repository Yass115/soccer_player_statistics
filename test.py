import sys

import pygame
import random

# Define the screen size and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake"

# Define the colors to be used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the speed of the snake
SNAKE_SPEED = 10

# Define the size of the snake
SNAKE_SIZE = 10

# Define the initial position of the snake
SNAKE_X = SCREEN_WIDTH / 2
SNAKE_Y = SCREEN_HEIGHT / 2

# Define the initial direction of the snake
SNAKE_DIRECTION = "right"

# Define the size of the food
FOOD_SIZE = 10

# Define the initial position of the food
FOOD_X = random.randint(0, SCREEN_WIDTH - FOOD_SIZE)
FOOD_Y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE)

# Define the score
SCORE = 0

# Initialize the PyGame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the screen
pygame.display.set_caption(SCREEN_TITLE)

# Create the clock
clock = pygame.time.Clock()

# Create the snake
snake = pygame.Rect(SNAKE_X, SNAKE_Y, SNAKE_SIZE, SNAKE_SIZE)

# Create the food
food = pygame.Rect(FOOD_X, FOOD_Y, FOOD_SIZE, FOOD_SIZE)

# Create the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SNAKE_DIRECTION = "up"
            elif event.key == pygame.K_DOWN:
                SNAKE_DIRECTION = 'down'