class Move:
    def __init__(self, name: str, power: int, type: str):
        self.name = name
        self.power = power
        self.type = type

    def __repr__(self):
        return f"Move({self.name}, Power: {self.power}, Type: {self.type})"
