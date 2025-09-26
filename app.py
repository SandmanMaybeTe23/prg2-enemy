
class Enemy:
    def __init__(self, health:int,attack:int,name:str):
        self.hp=health
        self.atk=attack
        self.name=name



    def print_status(self):
        print(f"The enemy name is {self.name} has {self.hp} hp")


    def attacks(self):
        print(f"{self.name} has attack you with {self.atk} dmg and it hurt so much")


    def take_dmg(self,dmg):
        self.hp -= dmg 
        print(f"{self.name} has taken {dmg} and has {self.hp} left")
        
    def are_you_alive(self):
         if self.hp<0:
             print(f"{self.name} dead")


enemy_1=Enemy(10,5,"slumbery")

enemy_1.print_status()

enemy_1.attacks()



