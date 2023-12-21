import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Subway Surfers')

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_image = pygame.image.load('player.png')
player_x = screen_width / 2
player_y = screen_height - 100
player_speed_x = 0
player_speed_y = 0

# Set up the obstacles
obstacle_image = pygame.image.load('obstacle.png')
obstacles = []
obstacle_spawn_timer = 0

# Set up the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player_speed_x = 5
            elif event.key == pygame.K_UP:
                player_speed_y = -5
            elif event.key == pygame.K_DOWN:
                player_speed_y = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed_y = 0

    # Update the player's position
    player_x += player_speed_x
    player_y += player_speed_y

    # Keep the player on the screen
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_image.get_width():
        player_x = screen_width - player_image.get_width()
    if player_y < 0:
        player_y = 0
    elif player_y > screen_height - player_image.get_height():
        player_y = screen_height - player_image.get_height()

    # Spawn obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer >= 100:
        obstacle_x = random.randint(0, screen_width - obstacle_image.get_width())
        obstacle_y = -obstacle_image.get_height()
        obstacles.append((obstacle_x, obstacle_y))
        obstacle_spawn_timer = 0

    # Update the obstacles' positions
    for obstacle in obstacles:
        obstacle[1] += 5

    # Check for collisions between the player and the obstacles
    for obstacle in obstacles:
        if player_x + player_image.get_width() > obstacle[0] and player_x < obstacle[0] + obstacle_image.get_width() and player_y + player_image.get_height() > obstacle[1] and player_y < obstacle[1] + obstacle_image.get_height():
            pygame.quit()
            sys.exit()

    # Increment the score
    score += 1

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(player_image, (player_x, player_y))
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
