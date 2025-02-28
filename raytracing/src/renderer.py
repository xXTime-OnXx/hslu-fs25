import pygame

from src.vector import Vector


class Renderer:
    """Handles pixel-based rasterization using pygame."""

    def __init__(self, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height

        # Create display window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Rendered Circle")

    def draw_circle(self, center: int, radius: int, color=(255, 0, 0)):
        """Draws a circle by setting pixel colors based on vector distance."""
        for x in range(self.width):
            for y in range(self.height):
                position = Vector(x, y)
                if (position - center).magnitude() <= radius:
                    prev_color = self.window.get_at((x, y))
                    new_color = (prev_color[0] + color[0], prev_color[1] + color[1], prev_color[2] + color[2])
                    self.window.set_at((x, y), new_color)
                    

        pygame.display.update()

    def run(self):
        """Runs the event loop to keep the window open until closed by the user."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()