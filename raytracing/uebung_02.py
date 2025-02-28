from src.renderer import Renderer
from src.vector import Vector

WIDTH = 800
HEIGHT = 800

circle_radius = 200
red_circle_center = Vector(WIDTH / 3, HEIGHT / 3 * 2)
green_circle_center = Vector(WIDTH / 3 * 2, HEIGHT / 3 * 2)
blue_circle_center = Vector(WIDTH / 2, HEIGHT / 3)
    
renderer = Renderer(width=WIDTH, height=WIDTH)
renderer.draw_circle(red_circle_center, circle_radius, color=(255, 0, 0))
renderer.draw_circle(green_circle_center, circle_radius, color=(0, 255, 0))
renderer.draw_circle(blue_circle_center, circle_radius, color=(0, 0, 255))
renderer.run()