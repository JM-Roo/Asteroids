import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        right_vector = self.velocity.rotate(angle)
        left_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = right_vector * 1.2

        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left_vector * 1.2

