import pygame
import math

from myjson import MyJson
from province import Province
from world import World
from nation import Nation


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

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if mouse is over any province
    #TODO optimize this monstrosity
    for province in world.provinces:
      if province.is_mouse_over(mouse_pos):
        province.is_highlighted = True
      else:
        province.is_highlighted = False

    render(screen, world.provinces)
    
    clock.tick(50)
  
  pygame.display.quit()

if __name__ == "__main__":
    main()
