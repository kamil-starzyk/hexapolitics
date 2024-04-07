import pygame
import math

class Province:
  diameter = 40
  def __init__(self, position, nation, population, gold):
    self.position = position
    self.is_highlighted = False
    self.nation = nation
    self.population = population
    self.gold = gold

  
  def render(self, screen) -> None:
    """Renders the hexagon on the screen"""
    points = []
    x, y = self.position
    color = self.nation.color
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = angle_deg * (math.pi / 180)
        points.append((x + self.diameter * math.cos(angle_rad),
                       y + self.diameter * math.sin(angle_rad)))
    pygame.draw.polygon(screen, color, points)

  @property
  def small_diameter(self) -> float:
      # https://en.wikipedia.org/wiki/Hexagon#Parameters
      return self.diameter * math.cos(math.radians(30))