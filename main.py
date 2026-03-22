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

    # scoring: 1 point per asteroid destroyed
    score = 0
    font = pygame.font.Font(None, 36)

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
                    score += 1
                    asteroid.split()
                    shot.kill()
            if player.collides_with(asteroid):
                player.lives -= 1
                asteroid.split()
                if player.lives > 0:
                    log_event("player_hit")
                    player.invulnerable_timer = 3
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    print("Game Over")
                    sys.exit()
        for drawing in drawable:
            drawing.draw(screen)

        # score HUD
        score_surface = font.render(f"Score: {score}", True, pygame.Color("white"))
        screen.blit(score_surface, (10, 10))

        #Renders the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

