import pygame
from constants import *
from player import Player  
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}" )
    print(f"Screen height: {SCREEN_HEIGHT}" )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    running = True	
    while running:
        dt = clock.tick(60) / 1000
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
