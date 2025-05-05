import pygame
from constants import *
from player import Player

def main():
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    # Handle exit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    screen.fill((0,0,0))
    player.update(dt)
    player.draw(screen)
    
    # Draw/refresh
    pygame.display.flip()
    dt = clock.tick(60) / 1000

# Only run main when main.py is executed
if __name__ == "__main__":
  main()
