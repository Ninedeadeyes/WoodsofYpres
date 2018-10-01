import random


class Enemy:
    def __init__ (self):
        raise NotImplementedError("Do not create raw Enemy objects")
    
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
        
        
class boss (Enemy):
    def __init__(self):
        self.name = "Grand Butcher of Ypres"
        self.hp = 550
        self.damage= 40
        self.gold=random.randint(20,40)
        self.exp =100

class RagMan (Enemy):
    def __init__(self):
        self.name = "Rag man"
        self.hp = 10
        self.damage= 10
        self.gold=random.randint(20,40)
        self.exp =15
        
class BogImp (Enemy):
    def __init__(self):
        self.name = "Bog Imp"
        self.hp = 30
        self.damage = 15
        self.gold=random.randint(40,60)
        self.exp =20
        
class DarkYoungofShubNiggurath (Enemy):
    def __init__(self) :
        self.name = "Dark Young of Shub-Niggurath"
        self.hp = 80
        self.damage = 15
        self.gold=random.randint(60,80)
        self.exp =30
        
class WarMachine(Enemy):
    def __init__ (self):
        self.name =" Rusty War Machine of Ypres "
        self.hp =70
        self.damage=20 
        self.gold=random.randint(80,100)
        self.exp =40
