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
