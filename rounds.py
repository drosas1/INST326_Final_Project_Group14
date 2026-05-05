STUDENT_NAME = "Habeeb Kazeem"

class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        
    def generate_round(self):
        pass
    def __init__(self, round_number):
        """Initialize a Round with a given round number.

        Args:
            round_number (int): The round number to initialize.
        """
        self.round_number = round_number
        self.enemies = []
    def generate_enemies(self):
        """ Generates a list of enemies thats scaled to the round number.

        Uses a list comprehension to create Enemy objects. Each round increases
        the number of enemies and scales their health and attack power based on 
        the round number.

        Returns:
            list: A list of Enemy objects for this round.

        """
self.enemies = [
           Enemy(
                name=f"Enemy_{i + 1}",
                health_percentage=1 + (self.round_number * 0.1),
                speed=1 + (self.round_number * 0.05),
                attack_power=5 + (self.round_number * 2)
            )
            for i in range(self.round_number + 2)
        ]
        return self.enemies

class RoundManager:
    """Class to manage rounds and enemy waves in the game"""

    def __init__(self):
        """Initialize round manager with starting values"""
        self.current_round = 1
        self.active_enemies = []
        self.round_over = False

    def generate_wave(self, round_num):
        """
        Generate a list of enemies based on the round number

        Args:
            round_num (int): current round number

        Returns:
            list: list of Enemy objects
        """
        enemies = []
 def __init__(self):
        """Initialize the RoundManager with default starting values."""
        self.current_round = 1
        self.active_enemies = []
        self.round_over = False
        self.rounds_history = []

    def start_round(self):
        """Start the current round by generating and activating enemies.

        Creates a Round object, generates its enemies using a comprehension,
        and sets them as the active enemies. Prints a summary using the
        Round's __str__ magic method.

        Returns:
            list: The list of active enemies for this round.
        """
        round_obj = Round(self.current_round)
        self.active_enemies = round_obj.generate_enemies()
        self.round_over = False
        print(f"\n{'='*40}")
        print(round_obj)
        print(f"{'='*40}")
        return self.active_enemies

    def get_alive_enemies(self):
        """Return a filtered list of enemies that are still alive.

        Uses a list comprehension to filter out defeated enemies
        from the active enemies list.

        Returns:
            list: Enemy objects that have not been defeated yet.

        Technique: comprehension / generator expression
        """
        return [enemy for enemy in self.active_enemies if not enemy.is_defeated()]
  def check_round_over(self):
        """Check if all enemies have been defeated to end the round.

        If no alive enemies remain, marks the round as over, logs it,
        and advances to the next round number.

        Returns:
            bool: True if the round is over, False otherwise.
        """
        if len(self.get_alive_enemies()) == 0:
            self.round_over = True
            self.rounds_history.append(self.current_round)
            print(f"\nRound {self.current_round} complete! All enemies defeated.")
            self.current_round += 1
        return self.round_over

  def __str__(self):
        """Return a summary of the RoundManager's current state.

        Magic method that displays current round, alive enemy count,
        and total rounds completed so far.

        Returns:
            str: A formatted status string for the RoundManager.

        Technique: magic method other than __init__()
        """
        alive = len(self.get_alive_enemies())
        completed = len(self.rounds_history)
        return (f"[RoundManager] Current Round: {self.current_round} | "
                f"Alive Enemies: {alive} | "
                f"Rounds Completed: {completed}")


        
if __name__ == "__main__":
    manager = RoundManager()

    for _ in range(3):
        manager.start_round()
        print(f"\nEnemies this wave: {[e.name for e in manager.active_enemies]}")

        while not manager.check_round_over():
            manager.apply_damage_to_enemies(damage_per_enemy=50)

        print(manager)
