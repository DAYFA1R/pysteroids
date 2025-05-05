import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  while True:
    # Handle exit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)
    
    for asteroid in asteroids:
      if player.collision(asteroid):
        print("Game over!")
        return 1
    
    screen.fill((0,0,0))
    
    for sprite in drawable:
      sprite.draw(screen)
    
    # Draw/refresh
    pygame.display.flip()
    dt = clock.tick(60) / 1000

# Only run main when main.py is executed
if __name__ == "__main__":
  main()
