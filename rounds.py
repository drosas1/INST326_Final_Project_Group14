STUDENT_NAME = "Habeeb Kazeem"

from Enemy_class import Enemy


class Round:
    def __init__(self, round_number):
        """Initialize a Round with a given round number."""
        self.round_number = round_number
        self.enemies = []

    def generate_round(self):
        pass

    def generate_enemies(self):
        """Generates a list of enemies that's scaled to the round number."""
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
        """Initialize the RoundManager with default starting values."""
        self.current_round = 1
        self.active_enemies = []
        self.round_over = False
        self.rounds_history = []

    def generate_wave(self, round_num):
        """Generate a list of enemies based on the round number"""
        round_obj = Round(round_num)
        enemies = round_obj.generate_enemies()
        return enemies

    def start_round(self):
        """Start the current round"""
        round_obj = Round(self.current_round)
        self.active_enemies = round_obj.generate_enemies()
        self.round_over = False

        print(f"\n{'='*40}")
        print(f"Round {self.current_round}")
        print(f"Enemies: {[e.name for e in self.active_enemies]}")
        print(f"{'='*40}")

        return self.active_enemies

    def get_alive_enemies(self):
        """Return a filtered list of enemies that are still alive"""
        return [enemy for enemy in self.active_enemies if not enemy.is_defeated()]

    def apply_damage_to_enemies(self, damage_per_enemy):
        """Apply damage to all active enemies"""
        for enemy in self.active_enemies:
            if not enemy.is_defeated():
                enemy.damage_taken(damage_per_enemy)
                print(
                    f"{enemy.name} took {damage_per_enemy} damage | "
                    f"HP remaining: {enemy.health:.1f}"
                )

    def check_round_over(self):
        """Check if all enemies have been defeated"""
        if len(self.get_alive_enemies()) == 0:
            self.round_over = True
            self.rounds_history.append(self.current_round)
            print(f"\nRound {self.current_round} complete! All enemies defeated.")
            self.current_round += 1
        return self.round_over

    def __str__(self):
        alive = len(self.get_alive_enemies())
        completed = len(self.rounds_history)
        return (
            f"[RoundManager] Current Round: {self.current_round} | "
            f"Alive Enemies: {alive} | "
            f"Rounds Completed: {completed}"
        )


if __name__ == "__main__":
    manager = RoundManager()

    for _ in range(3):
        manager.start_round()
        print(f"\nEnemies this wave: {[e.name for e in manager.active_enemies]}")
            manager.apply_damage_to_enemies(damage_per_enemy=50)

        print(manager)
