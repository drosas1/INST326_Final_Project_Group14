STUDENT_NAME = "Deirick Rosas"

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
            self.grid.display()
            
if __name__ == "__main__":
    game = Game()
    game.start()