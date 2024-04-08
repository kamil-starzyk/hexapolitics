import pygame
import math

class Province:
  diameter = 40
  def __init__(self, coordinates, terrain, population, gold,):
    self.coordinates = coordinates
    self.screen_position = (0, 0)
    self.is_highlighted = False
    self.nation = None
    self.terrain = terrain # lowland, plateaus, highlands, mountains, sea
    self.population = population
    self.gold = gold

  
  def render(self, screen) -> None:
    """Renders the hexagon on the screen"""
    points = []
    x, y = self.screen_position
    color = self.nation.color
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = angle_deg * (math.pi / 180)
        points.append((x + self.diameter * math.cos(angle_rad),
                       y + self.diameter * math.sin(angle_rad)))
    pygame.draw.polygon(screen, color, points)

  def set_position(self, start_x, start_y):
    hex_diameter = self.diameter + 2
    row, col = self.coordinates
    y = start_y + col * hex_diameter * 1.5
    x = start_x + row * hex_diameter * math.sqrt(3) - (col % 2) * hex_diameter * math.sqrt(3) / 2
    self.screen_position = (x, y)
  
  def set_nation(self, nation):
    self.nation = nation

  @property
  def small_diameter(self) -> float:
      # https://en.wikipedia.org/wiki/Hexagon#Parameters
      return self.diameter * math.cos(math.radians(30))

  def to_dict(self):
    return {
      "name": self.name,
      "color": self.color,
      "highlight_color": self.highlight_color,
      "provinces": [province.to_dict() for province in self.provinces]
    }
  
  @classmethod
  def from_dict(cls, data):
    coordinates = data["coordinates"]
    terrain = data["terrain"]
    population = data["population"]
    gold = data["gold"]
    
    province = cls(coordinates, terrain, population, gold)
    return province