from typing import List
from .move import Move

class Pokemon:
    # ANSI Color Codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    CYAN = "\033[96m"

    def __init__(self, name: str, pokemon_type: str, hp: int, attack: int, defense: int, speed: int, moves: List[Move], sprite: str = ""):
        self.name = name
        self.type = pokemon_type
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves
        self.sprite = sprite

    def is_alive(self) -> bool:
        return self.hp > 0

    def get_hp_bar(self) -> str:
        bar_length = 20
        percentage = self.hp / self.max_hp
        filled_length = int(round(bar_length * percentage))
        
        # Determine color based on remaining HP
        if percentage > 0.5:
            color = self.GREEN
        elif percentage > 0.2:
            color = self.YELLOW
        else:
            color = self.RED
            
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        return f"[{color}{bar}{self.RESET}] {color}{self.hp}/{self.max_hp} HP{self.RESET}"

    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)
        print(f"{self.CYAN}{self.name}{self.RESET} took {self.RED}{damage}{self.RESET} damage!")
        print(f"{self.name}'s Health: {self.get_hp_bar()}")

    def __repr__(self):
        return f"Pokemon({self.name}, HP: {self.hp}/{self.max_hp})"
