class Resource:
  radius = 40
  def __init__(self, name, description, renewable, amount_max, amount_discovered, amount_left, extraction_rate, recovery_rate):
    self.name = name
    self.description = description
    self.is_renewable = renewable
    self.amout_max = amount_max
    self.amount_discovered = amount_discovered
    self.amount_left = amount_left
    self.extraction_rate = extraction_rate # how fast can it be extracted i.e. 1-iron 5-wood 0.2-gold
    self.recovery_rate = recovery_rate # how many units can regrow per round, for nonrenewables it is 0

  #amount_max           = 1000
  #amount_left          = 999
  #amount_discovered    = 200
  #amount displayed:    199/200
  
  def display_amount(self) -> str:
    amount_not_discovered = self.amout_max - self.amount_discovered
    amount_displayed = self.amount_left - amount_not_discovered
    amount_max_displayed = self.amout_max - amount_not_discovered
    text = f"( {amount_displayed} / {amount_max_displayed} )"
    return text

  def to_dict(self):
    return {
      "name": self.name,
      "description": self.description,
      "renewable": self.is_renewable,
      "amount_max": self.amount_max,
      "amount_discovered": self.amount_discovered,
      "amount_left": self.amount_left,
      "extraction_rate": self.extraction_rate,
      "recovery_rate": self.recovery_rate
    }

  @classmethod
  def from_dict(cls, data):
    name = data["name"]
    description = data["description"]
    renewable = data["renewable"]
    amount_max = data["amount_max"]
    amount_discovered = data["amount_discovered"]
    amount_left = data["amount_left"]
    extraction_rate = data["extraction_rate"]
    recovery_rate = data["recovery_rate"]

    return cls(name, description, renewable, amount_max, amount_discovered, amount_left, extraction_rate, recovery_rate)
