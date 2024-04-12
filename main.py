import pygame
import math

from myjson import MyJson
from province import Province
from world import World
from nation import Nation

BLACK = (0,0,0)

def render(screen, hexagons):
  #screen.fill(BLACK)
  for province in hexagons:
    province.render(screen)
  
  pygame.display.flip()

def render_province_data(screen, font, highlighted_province):
  """Renders province data in a frame at the top-right position of the screen"""
  
  if highlighted_province:
    frame_width = 200
    frame_height = 130
    frame_x = screen.get_width() - frame_width
    frame_y = 0
    pygame.draw.rect(screen, (200, 200, 200), (frame_x, frame_y, frame_width, frame_height))
    
    text_color = (0, 0, 0)
    text_color_2 = (120, 10, 0)
    text_padding = 10
    
    # Render province data
    nation_text = font.render(f"Nation: {highlighted_province.nation.name}", True, text_color_2)
    population_text = font.render(f"Population: {highlighted_province.population}", True, text_color)
    gold_text = font.render(f"Gold: {highlighted_province.gold}", True, text_color)
    terrain_text = font.render(f"Terrain: {highlighted_province.terrain}", True, text_color)
    
    # Blit text to screen
    screen.blit(nation_text, (frame_x + text_padding, frame_y + text_padding))
    screen.blit(population_text, (frame_x + text_padding, frame_y + 30 + text_padding))
    screen.blit(gold_text, (frame_x + text_padding, frame_y + 60 + text_padding))
    screen.blit(terrain_text, (frame_x + text_padding, frame_y + 90 + text_padding))
    
    
    pygame.display.flip()


def main():
  """Main function"""
  pygame.init()
  screen = pygame.display.set_mode((1080, 720))
  pygame.display.set_caption("HexaPolitics")
  clock = pygame.time.Clock()
  font = pygame.font.Font(None, 24)

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
        render_province_data(screen, font, province)
      else:
        province.is_highlighted = False

    render(screen, world.provinces) 
    
    clock.tick(50)
  
  pygame.display.quit()

if __name__ == "__main__":
    main()
