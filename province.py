import pygame
import math

class Province:
  def __init__(self, position, nation, population, gold):
    self.position = position
    self.radius = 40
    self.is_highlighted = False
    self.nation = nation
    self.population = population
    self.gold = gold

  
  def render(self, screen, color) -> None:
    """Renders the hexagon on the screen"""
    points = []
    x, y = self.position
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = angle_deg * (math.pi / 180)
        points.append((x + self.radius * math.cos(angle_rad),
                       y + self.radius * math.sin(angle_rad)))
    pygame.draw.polygon(screen, color, points)

  @property
  def small_radius(self) -> float:
      # https://en.wikipedia.org/wiki/Hexagon#Parameters
      return self.radius * math.cos(math.radians(30))