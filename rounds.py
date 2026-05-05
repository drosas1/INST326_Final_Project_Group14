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
