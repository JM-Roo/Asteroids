import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable items
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                exit()


        # Wipe background to start fresh
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # Limit to 60FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
