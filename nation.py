from province import Province

class Nation:
  def __init__(self, name, color, provinces):
    self.name = name
    self.color = color
    self.provinces = provinces
  
  def to_dict(self):
    color_list = list(self.color)
    highlight_color_list = list(highlight_color)
    return {
      "name": self.name,
      "color": color_list,
      "provinces": [province.to_dict() for province in self.provinces]
    }
  
  @classmethod
  def from_dict(cls, data):
    color_tuple = tuple(data["color"])

    name = data["name"]
    color = color_tuple
    provinces_list = data["provinces"]
    provinces = [Province.from_dict(province_data) for province_data in provinces_list]
    
    nation = cls(name, color, provinces)

    for province in nation.provinces:
      province.set_nation(nation)
    return nation