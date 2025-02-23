import pygame
import random
import matplotlib

from vector import Vector

# Initialize pygame
pygame.init()

# Set window dimensions
window_width = 800
window_height = 600

RADIUS = 100
CIRCLE_CENTER = Vector(window_width / 2, window_height / 2)

# Create a window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Raster")

# Loop through each pixel and set its color randomly
for x in range(window_width):
    for y in range(window_height):
        position = Vector(x, y)
        
        # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color = (255, 0, 0)
        if position.__sub__(CIRCLE_CENTER).magnitude() <= RADIUS:
            window.set_at((x, y), color)

# Update the display with the random colors
pygame.display.update()

# Wait until the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()