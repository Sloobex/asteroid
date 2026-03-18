from os import kill

import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event, log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
import shot  

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    Asteroid.containers = (asteroids, updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)  
    
    clock = pygame.time.Clock()
    dt = 0

    grupa = pygame.sprite.Group()

    #------------------------------------------------>
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        log_state()
        updatable.update(dt)
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player.update(dt)
        player.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for i in shots:
                if i.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()

    #------------------------------------------------->

if __name__ == "__main__":
    main()
    
