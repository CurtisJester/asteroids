import pygame
import sys
from pygame.display import update
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init section
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player init
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Asteroid init
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Shots init
    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            # Quit by close button
            if event.type == pygame.QUIT:
                return
            pass

        # Display update
        screen.fill("black")
        updatable.update(dt)

        # Collision Detection
        for asteroid in asteroids:
            for shot in shots:
                if not asteroid.collides_with(shot):
                    continue
                log_event("asteroid_shot")
                asteroid.kill()
                shot.kill()

            if not asteroid.collides_with(player):
                continue
            log_event("player_hit")
            print("Game over!")
            sys.exit()

        for item in drawable:
            item.draw(screen)

        # Display Flip
        pygame.display.flip()

        # Game clock update
        dt = clock.tick(60.0) / 1000
        print(f"dt: {dt}")


if __name__ == "__main__":
    main()
