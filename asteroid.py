from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        split_vector_1 = self.velocity.rotate(angle)
        split_vector_2 = self.velocity.rotate(-angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_1.velocity = split_vector_1 * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_2.velocity = split_vector_2 * 1.2

        