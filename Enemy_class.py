STUDENT_NAME="Romario Harrison"

class Enemy:
    def __init__(self, name, health_percentage, speed, attack_power):
        '''used init method to initialize enemy.'''
        self.name = name
        self.health = health_percentage*100  # Convert percentage to actual health value
        self.speed = speed
        self.attack_power = attack_power

    def movement_block(self):
        return self.speed  # Default speed for all enemies

    def damage_taken(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Health should not go below zero
    def attack_power(self):
        return self.attack_power  # Return the enemy's attack power towards tower

    def is_defeated(self):
        return self.health <= 0 # Enemy is defeated if health is 0 or less
    print('Wave complete!') #round results
    
    
    def number_of_enemies(self):
        return 1  
    #represents one enemy
    

    
    
    

    
