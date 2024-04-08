import pygame
import math

class Province:
  radius = 40
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
    base_color = self.nation.color 
    brighter_color = tuple(min(255, c + 50) for c in base_color)
    color = self.nation.color if not self.is_highlighted else brighter_color # Brighter color when highlighted
    
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = angle_deg * (math.pi / 180)
        points.append((x + self.radius * math.cos(angle_rad),
                       y + self.radius * math.sin(angle_rad)))
    pygame.draw.polygon(screen, color, points)

  def set_position(self, start_x, start_y):
    hex_radius = self.radius + 2
    row, col = self.coordinates
    y = start_y + col * hex_radius * 1.5
    x = start_x + row * hex_radius * math.sqrt(3) - (col % 2) * hex_radius * math.sqrt(3) / 2
    self.screen_position = (x, y)
  
  def is_mouse_over(self, mouse_pos):
    """
    Checks if the mouse is over the hexagon
    """
    x, y = mouse_pos
    cx, cy = self.screen_position
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return distance < self.radius 
  
  def set_nation(self, nation):
    self.nation = nation

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