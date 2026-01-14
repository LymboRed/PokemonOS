from src.models.pokemon import Pokemon
from src.models.move import Move
from src.engine.battle import Battle

def main():
    # ASCII Art Sprites
    pikachu_sprite = r"""
  (\_/)
  (o.o )
 (> ^ <)
    """
    
    squirtle_sprite = r"""
   ____
  /    \
 ( o  o )
  \ -- /
    """

    # Define some moves
    thunderbolt = Move("Thunderbolt", 90, "Electric")
    quick_attack = Move("Quick Attack", 40, "Normal")
    water_gun = Move("Water Gun", 40, "Water")
    bubble = Move("Bubble", 40, "Water")

    # Initialize Pokemons
    # Pikachu is Electric, Squirtle is Water
    pikachu = Pokemon("Pikachu", "Electric", hp=100, attack=55, defense=40, speed=90, moves=[thunderbolt, quick_attack], sprite=pikachu_sprite)
    squirtle = Pokemon("Squirtle", "Water", hp=110, attack=48, defense=65, speed=43, moves=[water_gun, bubble], sprite=squirtle_sprite)

    # Start Battle
    battle = Battle(pikachu, squirtle)
    battle.start()

if __name__ == "__main__":
    main()
