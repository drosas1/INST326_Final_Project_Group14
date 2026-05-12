STUDENT_NAME = "Deirick Rosas & Alex Yogiaveetil"

from grid import Grid
from rounds import RoundManager
from units import Tower

class Game:
    def __init__(self):
        """Intialize the game with a grid, round manager and units together
        """
        
        self.grid = Grid(10)
        self.grid.add_row()
        self.manager = RoundManager()
        self.tower = Tower("Tower1", 100, 200, 3, 50)
        self.currency = 0

    
    def show_round_summary(self, round_number, enemies):
        """Display a summary of the round results after each wave.
        """
        defeated = [e for e in enemies if e.is_defeated()]
        surviving = [e for e in enemies if not e.is_defeated()]
        total_damage = sum(e.attack_power for e in defeated)
    
        print(f"\n{'='*40}")
        print(f"ROUND {round_number} SUMMARY")
        print(f"{'='*40}")
        print(f"Enemies Defeated: {len(defeated)}/{len(enemies)}")
        print(f"Enemies Remaining: {len(surviving)}")
        print(f"Total Damage Dealt: {total_damage}")
        print(f"{'='*40}\n")

    def award_currency(self, enemies):
        """Award currency to the player based on enemies defeated in the round.
        """
        defeated = [e for e in enemies if e.is_defeated()]
        currency_earned = len(defeated) * 10
        self.currency += currency_earned
    
        print(f"Enemies defeated: {len(defeated)}")
        print(f"Currency earned this round: {currency_earned}")
        print(f"Total currency: {self.currency}")
        
    def start(self):
        """Start the game, have a tower be placed and run through rounds
        
        Each round will spawn enemies, the tower will deal damage and the round 
        ends when all enemies are defeated
        """
        print("Welcome to Tower Defense")
        self.grid.place_tower(3)
        self.grid.display()
        
        for i in range(3):
            self.manager.start_round()
            self.manager.apply_damage_to_enemies(self.tower.attack_power)
            self.manager.check_round_over()
            self.show_round_summary(i + 1, self.manager.active_enemies)
            self.award_currency(self.manager.active_enemies)
            self.grid.display()
            
if __name__ == "__main__":
    game = Game()
    game.start()
