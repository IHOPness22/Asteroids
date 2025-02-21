from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)        

        self.rect.topleft = (self.position.x - self.radius, self.position.y - self.radius)

    def split(self, asteroid_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
 
        new_radius = (self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)

        # Add the new asteroids to an existing group or list (asteroid_group):
        asteroid_group.add(new_asteroid1, new_asteroid2)
