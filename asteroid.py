from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            old_radius = self.radius
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity1 * 1.2
            Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity2 * 1.2
