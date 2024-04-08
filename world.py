from nation import Nation

class World:
  def __init__(self, nations):
    self.nations = nations
    self.provinces = []

  def to_dict(self):
    return {
      "nations": [nation.to_dict() for nation in self.nations]
    }
  
  @classmethod
  def from_dict(cls, data):
    nations = [Nation.from_dict(nation_data) for nation_data in data["nations"]]

    world = cls(nations)

    # Populate world.provinces with provinces from every nation
    for nation in world.nations:
      world.provinces.extend(nation.provinces)

    return world