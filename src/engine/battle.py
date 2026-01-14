import random
from ..models.pokemon import Pokemon
from ..models.move import Move

class Battle:
    TYPE_CHART = {
        "Water": {"Fire": 2.0, "Grass": 0.5, "Water": 0.5},
        "Fire": {"Grass": 2.0, "Water": 0.5, "Fire": 0.5},
        "Grass": {"Water": 2.0, "Fire": 0.5, "Grass": 0.5},
        "Electric": {"Water": 2.0, "Electric": 0.5, "Grass": 0.5},
    }

    def __init__(self, p1: Pokemon, p2: Pokemon):
        self.p1 = p1
        self.p2 = p2

    def _get_type_multiplier(self, move_type: str, defender_type: str) -> float:
        return self.TYPE_CHART.get(move_type, {}).get(defender_type, 1.0)

    def _print_sprites(self):
        s1 = self.p1.sprite.strip("\n").split("\n")
        s2 = self.p2.sprite.strip("\n").split("\n")
        
        max_lines = max(len(s1), len(s2))
        s1 += [""] * (max_lines - len(s1))
        s2 += [""] * (max_lines - len(s2))
        
        print("\n")
        for l1, l2 in zip(s1, s2):
            print(f"{attacker_color(self.p1)}{l1:20}\033[0m   VS   {attacker_color(self.p2)}{l2}\033[0m")
        print("\n")

def attacker_color(p: Pokemon):
    return p.CYAN if p.name == "Pikachu" else p.YELLOW # Simple helper

class Battle:
    TYPE_CHART = {
        "Water": {"Fire": 2.0, "Grass": 0.5, "Water": 0.5},
        "Fire": {"Grass": 2.0, "Water": 0.5, "Fire": 0.5},
        "Grass": {"Water": 2.0, "Fire": 0.5, "Grass": 0.5},
        "Electric": {"Water": 2.0, "Electric": 0.5, "Grass": 0.5},
    }

    def __init__(self, p1: Pokemon, p2: Pokemon):
        self.p1 = p1
        self.p2 = p2

    def _get_type_multiplier(self, move_type: str, defender_type: str) -> float:
        return self.TYPE_CHART.get(move_type, {}).get(defender_type, 1.0)

    def _print_sprites(self):
        s1 = self.p1.sprite.strip("\n").split("\n")
        s2 = self.p2.sprite.strip("\n").split("\n")
        
        max_lines = max(len(s1), len(s2))
        s1 += [""] * (max_lines - len(s1))
        s2 += [""] * (max_lines - len(s2))
        
        mid = max_lines // 2
        print("\n")
        for i in range(max_lines):
            separator = "   VS   " if i == mid else "        "
            print(f"\033[96m{s1[i]:20}\033[0m{separator}\033[93m{s2[i]}\033[0m")
        print("\n")

    def start(self):
        print(f"\n--- Battle Start: {self.p1.name} vs {self.p2.name} ---")
        self._print_sprites()
        print(f"{self.p1.name} ({self.p1.type}): {self.p1.get_hp_bar()}")
        print(f"{self.p2.name} ({self.p2.type}): {self.p2.get_hp_bar()}\n")
        
        turn = 0
        while self.p1.is_alive() and self.p2.is_alive():
            turn += 1
            print(f"Turn {turn}")
            
            # Determine order based on speed
            if self.p1.speed >= self.p2.speed:
                attacker, defender = self.p1, self.p2
            else:
                attacker, defender = self.p2, self.p1

            self.execute_turn(attacker, defender)
            if not defender.is_alive():
                break
                
            self.execute_turn(defender, attacker)
            print("-" * 20)

        if self.p1.is_alive():
            print("\033[92m")
            print(r" __      __  _____  __    _ ")
            print(r" \ \    / / |_   _| |  \  | |")
            print(r"  \ \/\/ /    | |   |   \ | |")
            print(r"   \    /     | |   | |\  | |")
            print(r"    \__/     _| |_  |_| \___|")
            print("\033[0m")
            print(f"\nCongratulations! {self.p1.name} wins the battle!")
        else:
            print("\033[91m")
            print(r"  _        ____     _____   ______ ")
            print(r" | |      / __ \   / ____| |  ____|")
            print(r" | |     | |  | | | (___   | |__   ")
            print(r" | |     | |  | |  \___ \  |  __|  ")
            print(r" | |____ | |__| |  ____) | | |____ ")
            print(r" |______| \____/  |_____/  |______|")
            print("\033[0m")
            print(f"\n{self.p2.name} wins. Better luck next time!")

    def execute_turn(self, attacker: Pokemon, defender: Pokemon):
        if attacker == self.p1:  # Assuming p1 is always the player for now
            print(f"\nWhat will {attacker.name} do?")
            for i, move in enumerate(attacker.moves):
                print(f"{i + 1}: {move.name} ({move.type})")
            
            choice = -1
            while choice < 0 or choice >= len(attacker.moves):
                try:
                    choice = int(input(f"Select a move (1-{len(attacker.moves)}): ")) - 1
                except ValueError:
                    print("Please enter a valid number.")
            move = attacker.moves[choice]
        else:
            move = random.choice(attacker.moves)

        print(f"\n{attacker.name} uses {move.name}!")
        
        # Damage calculation with types
        multiplier = self._get_type_multiplier(move.type, defender.type)
        
        # Critical hit (10% chance)
        is_critical = random.random() < 0.1
        if is_critical:
            multiplier *= 2.0
            print("\033[1;93mCritical hit!\033[0m")

        if multiplier > 1.0 and not is_critical:
            print("\033[92mIt's super effective!\033[0m")
        elif multiplier < 1.0:
            print("\033[93mIt's not very effective...\033[0m")

        damage = int((attacker.attack / defender.defense) * move.power * multiplier)
        defender.take_damage(damage)
