# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # INITIALIZATION
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    updatable.add(player)
    drawable = pygame.sprite.Group()
    drawable.add(player)
    player.containers = (updatable, drawable)

    # Asteroids
    print("!DEBUG! initializing asteroids")
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    #asteroids.add(Asteroid)
    #updatable.add(Asteroid)
    #drawable.add(Asteroid)

    # AsteroidField
    print("!DEBUG! initializing asteroid field")
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    #updatable.add(asteroid_field)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update
        #player.update(dt)
        for u in updatable:
            #print(f"!DEBUG! updating {u}")
            u.update(dt)

        # draw
        screen.fill(0)
        #player.draw(screen)
        for d in drawable:
            #print(f"!DEBUG! drawing {d}")
            d.draw(screen)
        pygame.display.flip()
        ms = clock.tick(60)
        dt = ms / 1000

if __name__ == "__main__":
	main()

