import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            neg_angle = new_angle * -1
            new_vector = self.velocity.rotate(new_angle)
            neg_vector = self.velocity.rotate(neg_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_1.velocity = new_vector
            child_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_2.velocity = neg_vector




