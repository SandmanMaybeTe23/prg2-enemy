

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
         while True:
            if self.hp >= 0:
                 print(f"{self.name} dead")
                 break
            else:
                pass


slime=Enemy(100,5,"Slumbery")
goblin= Enemy(50,5,"Glen")

slime.print_status()

goblin.print_status()

slime.are_you_alive()
goblin.are_you_alive()

goblin.attacks()
while True:
    slime.take_dmg(goblin.atk)
    goblin.take_dmg(slime.atk)
    