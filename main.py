import pygame
import sys
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player  
from asteroid import Asteroid
from logger import log_event
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    player = Player(x,y)



    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt =  clock.tick(60) / 1000.0    
        #Fills in the screen with black
        screen.fill("black")
        #Updates and draws player groups
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        for drawing in drawable:
            drawing.draw(screen)
        #Renders the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

