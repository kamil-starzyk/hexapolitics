import pygame
import math

from province import Province
from world import World
from nation import Nation

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
L_GREEN = (50, 255, 50)
L_RED = (255, 50, 50)

HEX_DIAMETER = 42

def init_provinces(cols, rows, nation):
  provinces = []
  start_x, start_y = 100, 100
  for row in range(rows):
    for col in range(cols):
      # Calculate position of hexagon center
      x = start_x + col * HEX_DIAMETER * 1.5
      y = start_y + row * HEX_DIAMETER * math.sqrt(3) + (col % 2) * HEX_DIAMETER * math.sqrt(3) / 2
      province = Province((x, y), nation, 10, 100)
      provinces.append(province)

  return provinces

def render(screen, hexagons):
  screen.fill(BLACK)
  for province in hexagons:
    province.render(screen, RED)
  

  pygame.display.flip()



def main():
  """Main function"""
  pygame.init()
  screen = pygame.display.set_mode((1080, 720))
  pygame.display.set_caption("HexaPolitics")
  clock = pygame.time.Clock()

  world = World()
  n1 = Nation("We", GREEN, L_GREEN)
  n2 = Nation("Enemy", RED, L_RED)
  
  world.provinces = init_provinces(3,3, n2)
  
  is_playing = True
  
  while is_playing:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        is_playing = False

    render(screen, world.provinces)
    
    clock.tick(50)
  
  pygame.display.quit()

if __name__ == "__main__":
    main()
