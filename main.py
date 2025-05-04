import pygame
from constants import *

def main():
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    # Handle exit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return
    
    screen.fill((0,0,0))
    
    # Draw/refresh
    pygame.display.flip()

# Only run main when main.py is executed
if __name__ == "__main__":
    main()
