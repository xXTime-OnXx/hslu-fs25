from src.renderer import Renderer
from src.vector import Vector

circle_radius = 100
circle_center = Vector(800 / 2, 600 / 2)
    
renderer = Renderer(width=800, height=600)
renderer.draw_circle(circle_center, circle_radius)
renderer.run()