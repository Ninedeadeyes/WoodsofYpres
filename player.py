import items
import world 

class Player:
    def __init__(self):
        self.inventory= [items.Rock(),
                        items.Dagger(),                
                        items.HardTack(),
                        items.HardTack(),  
                        items.HardTack(),
                        items.LesserHealingPotion(),                        
                        items.LesserHealingPotion(),
                        items.GreaterHealingPotion()]
                        
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold= 10
        self.power = 4
        self.victory= False
        self.sanity = 10
        self.exp=0
        self.powerup=4
        self.fullhp = 100
        self.armour=0
        self.mark=0
        self.level2_claimed = True
        self.level3_claimed = True
        self.level4_claimed = True
        self.level5_claimed = True
        self.level6_claimed = True
        self.level7_claimed = True
        self.level8_claimed = True
        self.level9_claimed = True
        self.level10_claimed= True
        
    def is_alive(self):
        return self.hp >0
     
    def is_sane (self):     
        return self.sanity <40
     
    def print_inventory(self):
        print("Inventory/Stats:")
        for item in self.inventory: 
            print("*"+ str(item))
        print("Bones: {}".format(self.gold))
        print("Experience:{}".format(self.exp))
        print("Hp:{}".format(self.hp))
        attackpower=self.powerup+self.power        
        print("Attack:{}".format(attackpower))
        print("Sanity:{}".format(self.sanity))
        
    
    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]  #accept an object and a type and tells us if that obje
        if not consumables:                                    # object is that type or a subclass of that type. 
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))
        
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]   # translate to consumables[the index of the item]
                self.hp = min(self.fullhp, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.") 
     
    def pick(self):
        
        Weapons= [item for item in self.inventory
               if isinstance(item, items.Weapon)]  #accept an object and a type and tells us if that obje
        if not Weapons:                                    # object is that type or a subclass of that type. 
            print("You do not have any items to equip!")
            return
        
        print("Choose an item to equip: ")
        for i, item in enumerate(Weapons, 1):
            
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                best_weapon= Weapons[int(choice) - 1]   # translate to consumables[the index of the item]
                self.power=best_weapon.damage
                print("Current Weapon damage: {}".format(best_weapon.damage))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")
     
                            
    def move(self,dx,dy):   # this is a move method () defines dx and dy
        self.x += dx        # This accept a generic change of dx and dy
        self.y += dy        # and the specific methods 
                            # define the amount of change
    def move_north(self):
        self.move(dx=0, dy=-1)
        
    def move_south(self) :
        self.move(dx=0, dy=1)
     
    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)  


    def attack(self):
        room = world.tile_at(self.x, self.y)  
        enemy = room.enemy
        print ("You attack the {}!".format(enemy.name))    
        enemy.hp-=self.power+self.powerup 
        if not enemy.is_alive():
            print ("you killed {}!".format(enemy.name))
            self.gold=self.gold+enemy.gold
            self.exp=self.exp+enemy.exp
            print ("You gain {} bones ".format(enemy.gold))
            
            print ("You gain {} experience ".format(enemy.exp))
            
            
            
            
            if self.exp>30 and self.level2_claimed:
                self.powerup=6
                self.hp= 120 
                self.fullhp=120
                print("You are now level 2 'The Struggler'  ")
                print("Current HP: {}".format(self.hp))
                self.level2_claimed = False
                
                         
            if self.exp>60 and self.level3_claimed:
                self.powerup=8  
                self.hp= 130
                self.fullhp=130
                print("You are now level 3 'The Survivor'")
                print("Current HP: {}".format(self.hp))
                self.level3_claimed = False
                
            if self.exp>100 and self.level4_claimed:
                self.powerup=10  
                self.hp= 140 
                self.fullhp=140
                print("You are now level 4 'The Explorer' ")
                print("Current HP: {}".format(self.hp))
                self.level4_claimed = False 
                
            if self.exp>150 and self.level5_claimed:
                self.powerup=12
                self.hp= 150 
                self.fullhp=150
                print("You are now level 5 'The Hunter'")
                print("Current HP: {}".format(self.hp))
                self.level5_claimed = False
                
                
            if self.exp>210 and self.level6_claimed:
                self.powerup=14 
                self.hp= 200
                self.fullhp=200
                print("You are now level 6 'The Dissenter' ")
                print("Current HP: {}".format(self.hp))
                self.level6_claimed = False
           
            if self.exp>300 and self.level7_claimed:
               self.powerup=16 
               self.hp= 220
               self.fullhp=220
               print("You are now level 7 'The Death Stalker' ")
               print("Current HP: {}".format(self.hp))
               self.level7_claimed = False 
               
            if self.exp>400 and self.level8_claimed:
               self.powerup=18 
               self.hp= 240
               self.fullhp=240
               print("You are now level 8 'The Harbinger of Doom ' ")
               print("Current HP: {}".format(self.hp))
               self.level8_claimed = False    
             
            if self.exp>520 and self.level9_claimed:
               self.powerup=20 
               self.hp= 260
               self.fullhp=260
               print("You are now level 9 'The Nightmare In The Woods ")
               print("Current HP: {}".format(self.hp))
               self.level9_claimed = False              

            if self.exp>600 and self.level10_claimed:
               self.powerup=22 
               self.hp= 280
               self.fullhp=280
               print("You are now level 10 'The Master Killer of the Woods' ")
               print("Current HP: {}".format(self.hp))
               self.level10_claimed = False                             

            
            #print  ("Your exp level is {} ".format(self.powerup))   
            
              
        else:
            print("{} HP is {}.".format(enemy.name,enemy.hp))
            
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)            
