STUDENT_NAME = "Deirick Rosas"

class Unit:
    def __init__(self, name, health, attack_power):
        """Intialize Unit class for game with name, health and attack power
        
        Args:
            name (str): the name of unit like tower or enemy
            health (int): amount of health for unit as int
            attack_power (int): attack power for unit as int
        """
            
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack (self, target):
        """attack method to deal damage to a target unit
        
        Args:
            target: the unit being attacked
        """
        
        pass
    
    def damage_taken (self, amount):
        """damage taken method to show how much a unit has been damaged
        
        Args:
            amount (int): amount of damage taken by unit
        """
        
        pass
    
class Tower(Unit):
    def __init__(self, name, health, attack_power, attack_range, cost):
        """Intialize Tower class that inherits from Unit class
        
        Args:
            name (str): name of the tower 
            health (int): health of the tower
            attack_power (int): amount of attack power for tower
            attack_range (int): effective range of tower
            cost (int): the cost of the tower
        """
        
        super().__init__(name, health, attack_power)
        self.attack_range = attack_range
        self.cost = cost
        
    def get_enemy(self, enemies):
        """get enemy method to get a list of enemies within range of the tower
        
        Args:
            enemies (list): list of enemy object on the grid
            
        Returns:
            list: the enemies within the range of the tower
        """
         
        pass
            