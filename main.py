import pygame
import math

from myjson import MyJson
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



def init_provinces(cols, rows, nation):
  hex_diameter = Province.diameter + 2
  provinces = []
  start_x, start_y = 100, 60
  for col in range(cols):
    for row in range(rows + col % 2):  # Add extra hexagon for odd rows:
      # Calculate position of hexagon center
      y = start_y + col * hex_diameter * 1.5
      x = start_x + row * hex_diameter * math.sqrt(3) - (col % 2) * hex_diameter * math.sqrt(3) / 2
      province = Province(nation, 10, 100)
      province.set_coordinates(col, row)
      province.set_position(x, y)
      provinces.append(province)

  return provinces

def render(screen, hexagons):
  screen.fill(BLACK)
  for province in hexagons:
    province.render(screen)
  

  pygame.display.flip()



def main():
  """Main function"""
  pygame.init()
  screen = pygame.display.set_mode((1080, 720))
  pygame.display.set_caption("HexaPolitics")
  clock = pygame.time.Clock()

  data = MyJson.load_json("data/init/intro.json")
  nations = data["world"]
  world = World.from_dict(nations)

  start_x, start_y = 100, 60
  for province in world.provinces:
    province.set_position(start_x, start_y)
  
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
