import pygame
import sys
from constants import *
from player import Player  
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot

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
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x, y)
    running = True	
    while running:
        dt = clock.tick(60) / 1000
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        for shot in shots:
            for asteroid in asteroids:
                if shot.rect.colliderect(asteroid.rect):
                    shot.kill()
                    asteroid.split(asteroids)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
