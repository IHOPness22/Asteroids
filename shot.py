import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

        self.rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y

        self.rect.topleft = (self.position.x - self.radius, self.position.y - self.radius)

    def draw(self, screen):
        pygame.draw.circle(
        screen,
        "white",  # Color of the shot
        (self.position.x, self.position.y),  # Position
        self.radius  # Size
    )

    
