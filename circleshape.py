import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, Circleshape):
        distance = self.position.distance_to(Circleshape.position)
        print(f"Distance: {distance}")
        print(f"Sum of radii: {self.radius + Circleshape.radius}")
        if distance <= (self.radius + Circleshape.radius):
            return True
        else:
            return False
 
