import enemies
import npc
import random
import player
import items

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

        
class LocationTile4(MapTile):
      def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)  

      def intro_text(self):
        print ("You find something etched onto a great oak tree")
        print("It looks like a map of the Woods !!")
        print ("It provides your location (H)")
        print ("and something else is marked (?)")
        print ("""
               |  | H|  |  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|xx|
               |  |  |  |xx|  |  |  | ?|xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |
               |  |  |  |  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|  |
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |         
        
                """)          
        
        
        
        
class LocationTile3(MapTile):
      def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)  

      def intro_text(self):
        print ("You find some markings etched onto the chest of a crucified corpse ")
        print("It looks like a map of the Woods !!")
        print ("It provides your location (H)")
        print ("and something else is marked (?)")
        print ("""
               |  |  |  |  |  |  |  |  |  | ?|
               |  |xx|xx|xx|  |  |xx|xx|xx|xx|
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |
               |  |  |  |  |  | H|  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|  |
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |         
        
                """)  
class LocationTile2(MapTile):
      def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)  

      def intro_text(self):
        print ("You found something etched onto a old tombstone")
        print("It looks like a map of the Woods !!")
        print ("It provides your location (H)")
        print ("and something else is marked (?)")
        print ("""
               |  |  |  |  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|xx|
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx| H|  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |
               |  |  | ?|  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|  |
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |        
        
        
        """)        
        
        
class LocationTile(MapTile):
      def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)  

      def intro_text(self):
        print ("You see an old wooden sign ahead of you")
        print("It looks like a map of the Woods !!")
        print ("It provides your location (H)")
        print ("and something else is marked (?)")
        print ("""
               |  |  |  |  |  |  |  |  |  | ?|
               |  |xx|xx|xx|  |  |xx|xx|xx|xx|
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |
               |  |  |  |  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|  |
               |  |  |  |xx|  |  |  | H|xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |        
        
        
        """)
        
            
        
class RagManTile(MapTile):
    def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)
 
        
    def modify_player(self, player):
   
        if not self.Item_claimed:
            
            action_input=input("Action:")  
            if action_input =="Y" or action_input =="y":
               print("Wonderful, make a note little one.. ")
               input(".....")
               print ("Go south 5,east 4 then south 4 ")
               input(".....")
               print("You will find a weapon of great power and fear.. ")
               input(".....")
               print ("I will let you have a look at my map ")
               print("H=HERE T=Treasure ")
               
               self.Item_claimed = True
               player.hp=int(player.hp/2)
               
               print("")
               print("""
               
               |  |  |  |  |  | H|  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|xx|
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|  |
               |  |  |  |  |  |  |  |  |  |  |
               |  |xx|xx|xx|  |  |xx|xx|xx|  |
               |  |  |  |xx|  |  |  |  |xx|  |
               |  |  |  |  |  |  |xx|  |  |  |
               |  |xx|  |xx|  |  |xx|  |xx|T |
               
               """)
               print("Your hp {} ".format(player.hp))
               
            elif action_input =="N" or action_input =="n":
               print("You refuse the offer and continue on")
            else:
                print("(INVALID CHOICE) You leave without taking up the offer")
               
                
    def intro_text(self):
        if self.Item_claimed:
            return """
            This is the place where you met that friendly Rag man
            I wonder where he is now ? 
            """
            
        else:
            print("You see a rag man but he does not attack you ")
            print("He speaks 'Hello young one,I can tell you a secret of these dreaded woods'")
            input("     ")
            print("'If you offer me some 'life'.. Not all, mind you..Just enough'")
            input("     ")
            return """
            Do you accept the dark pact?  yes(Y) or No(N)
            
            """                  
        
        
        

class FindRingTile(MapTile):
    def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)
 
        
    def modify_player(self, player):
   
        if not self.Item_claimed:
            
            action_input=input("Action:")  
            if action_input =="Y" or action_input =="y":
               print ("You decide to put on the ring")
               input(".....")
               print("As you fit the ring around your finger")
               input(".....")
               print("Your flesh starts to become hard like rock")
               input(".....")
               print("You panic and attempt to remove it")
               input(".....")
               print ("It will not come off, it is cursed !!!")
               input(".....")
               print("You are disturbed, but have no choice but to continue")
               input(".....")
       
               
               self.Item_claimed = True
               player.armour=12
               player.sanity = player.sanity + 2
               print("Your sanity point {}".format(player.sanity))
               print("Your armour resist {}".format(player.armour))
               print("")
            elif action_input =="N" or action_input =="n":
               print("You decide to not to wear the ring")
            else:
                print("(INVALID CHOICE) You leave without wearing the ring")
                
    def intro_text(self):
        if self.Item_claimed:
            return """
            You see a stone alter, nothing interesting here  
            """
            
        else:
            print("You see a ring placed on a stone alter")
            input(".....")
            print("There is a short note beside the ring")
            input(".....")
            print("One man's curse is another man's saviour")
            input(".....")
            print( "You have a strange urge to put on the ring")
            input(".....")
            return """
            Will you wear the ring ? YES (y) or NO (n) 
            
            """            
    
class FindHammerTile(MapTile):
    def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)
 
        
    def modify_player(self, player):
   
        if not self.Item_claimed:
            
            action_input=input("Action:")  
            if action_input =="Y" or action_input =="y":
               print ("You decide to take the hammer")
               input(".....")
               print("As you pick the hammer up ")
               input(".....")
               print("A great sense of dread and horror fills your soul")
               input(".....")
               print ("You are now the bearer of the Doom Hammer")
               input(".....")
               print("GO FORTH AND BRING DOOM TO US ALL ")
               input(".....")
               self.Item_claimed = True
               player.inventory.append(items.DoomHammer())
               player.sanity = player.sanity + 5
               print("Your sanity point {}".format(player.sanity))
               print("")
            elif action_input =="N" or action_input =="n":
               print("You decide to not take the hammer")
            else:
               print("(INVALID CHOICE) You leave without the hammer")
               
    
    
    def intro_text(self):
        if self.Item_claimed:
            return """
            A place of great power and darkness...  
            """
            
        else:
            print("You see a large hammer before you")
            input(".....")
            print("It has a dark essence around it")
            input(".....")
            print("Yet, there is a undeniable aura of power too")
            input(".....")
            return """
            Will you take the doom hammer ? YES (y) or NO (n) 
            """     

        

class FindSwordTile(MapTile):
    def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        
        if not self.Item_claimed:
            
            action_input=input("Action:")  
            if action_input =="Y" or action_input =="y":
               print ("You retreive the Silver Sword" )
               input(".....")
               print ("You feel a sense of hope against the darkness")
               input(".....")
               self.Item_claimed = True
               player.inventory.append(items.SilverSword())
               player.sanity = player.sanity - 3
               print("Your sanity level is {}".format(player.sanity))
               
            elif action_input =="N" or action_input =="n":
               print("You decide not to free the sword")
            else:
               print(" (INVALID CHOICE) You leave without taking the sword") 
               

    def intro_text(self):
        if self.Item_claimed:
            return """
            You see a large rock with a big crack in the middle 
            """
            
        else:
            print("You see a sword stuck in a large rock ")
            input(".....")
            print("The sword's glow devours the darkness around it ")
            return """
            Will you attempt to free the sword?   Yes (Y) or No (N)
            """        
        
        
        
        
class FindHealthTile(MapTile):
    def __init__(self, x, y):
        self.Item_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):  
    
        if not self.Item_claimed:
        
            action_input=input("Action:")  
            if action_input =="Y" or action_input =="y":
                print ("you gain a Greater Healing Potion" )
                self.Item_claimed = True
                player.inventory.append(items.GreaterHealingPotion())

               
            elif action_input =="N" or action_input =="n":
               print("You decide not to disturb the dead")
            else:
               print("(INVALID CHOICE) You walk away from the corpse")
   
                        

    def intro_text(self):
        if self.Item_claimed:
            return """
            You see a deady body slowly rotting away
            """
            
        else:
            print("You see a dead adventurer on the ground")
            print("There is something in his bag")
            return """
            will you search the dead adventurer ? YES(Y) or NO(N)
            """
        
        
class BossTile(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.boss()
        self.alive_text = """
                          You see a massive demonic creature with a 
                          gigantic cleaver.  
                          He smiles and speaks... 'Meat for the lady?'
                          """
                          
        self.dead_text = """
                         The great abomination falls to the ground
                         bleeding from every orifice. 
                         It has been a bloody battle. 
                         He reaches his right hand into the air 
                         and with his dying breath he whispers 
                        'No meat for supper tonight, my lady'. 
                         The butcher is dead                        
                         
                         """
                             
        super().__init__(x, y)  

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            enemydamage=self.enemy.damage-player.armour
            if enemydamage < 0:
                enemydamage=0                
            player.hp = player.hp-enemydamage
            print("Enemy does {} damage. You resisted {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.armour,player.hp))
        else:
            player.victory=True 
            print("You see a dim light on the edge of the woods")
            input(".....")
            print("You run to the light and the light becomes brighter")
            input(".....")
            print("As you reach the light, a sense of finality overcomes you")
            input(".....")
            print("You wake up")
            input(".....")
            print("You are surrounded by mangled bodies all with contorted faces of horror" )
            print("You can make out four paths.' ")
            input(".....")
            print ("You break down on the floor knowing you cannot do this again..")
            input(".....")
            print("You notice an old man with a pipe sitting in a chair ")
            print("beside a pile of mangled bodies")
            input(".....")
            print("The old man speaks 'No one truly escapes these woods ")
            print("without a clear conscious")
            input(".....")
            print ("As you begin to object. You start to remember")
            input(".....")
            print ("Something your mind has hid away from you until now " )
            input(".....")
            print ("You remember the butcher's daugther lying on the floor in a pool of blood" )
            input(".....")
            print ("The butcher rushes into the room and stares in horror")
            input(".....")
            print ("Your hands were around another woman's neck, her eyes drained of life")
            input(".....")
            print ("You remember a struggle with the enraged butcher ")
            input(".....")
            print("which ended with you throwing the butcher into a great cauldron of boiling water")
            input(".....")
            print("You remember the endless scream and rambling of the butcher")
            print("as you force the lid on top of the cauldron preventing his escape")
            input(".....")
            print ("Until silence")
            input(".....")
            print ("You start to cry uncontrollably feeling only the deepest of guilt and regret")
            input(".....")
            print ("The old man speaks again ' There, there.. Old Man Kwong will take care of you'")
            input(".....")
            print("You look up and suddenly, you are back in your prison cell ")
            print("before your trip to the Woods of Yrpes")
            input(".....")
            print("The old man continues 'Congratulations, you have escaped the Woods of Yrpes") 
            input(".....")
            print("'Now are you ready to confess, this time ?'")
            input(".....")
            print("You nod with approval and readily face your final judgement")
            input(".....")
            print("Sometimes redemption can only truly be found in death")
            print("All is forgiven in the eternal sleep ")
            input(".....")
            print(r"""
 
  _______ _            ______           _  
 |__   __| |          |  ____|         | |
    | |  | |__   ___  | |__   _ __   __| |
    | |  | '_ \ / _ \ |  __| | '_ \ / _` |
    | |  | | | |  __/ | |____| | | | (_| |
    |_|  |_| |_|\___| |______|_| |_|\__,_|
                                          
                                          
                                                          
            
            """)
            print("Final stats")
            print("Bones: {}".format(player.gold))
            print("Experience:{}".format(player.exp))
            attackpower=player.powerup+player.power
            print("Attack:{}".format(attackpower))
            print("Hp:{}".format(player.hp))
            print("Mark of the Beast {} out of 6 ".format(player.mark))
            print("Special thanks to Louise Shaw for proof reading ")
            print("Ascii by jg and jgs"  )
            print("""
            
             
            )
           (_)
          .-'-.
          |   |
          |   |
          |   |
          |   |
        __|   |__   .-.
     .-'  |   |  `-:   :
    :     `---'     :-'
     `-._       _.-'
         '""""""
            
            """)
            input("Press any button to escape")
            
        
class WestTile(MapTile):
    def intro_text(self):
        print ("You see a large cage hanging from a dead tree")
        print ("There seems to be a corpse inside with a sign")
        return """
        The Sign reads : Go West, my honey flower  
        """  

class EastTile(MapTile):
    def intro_text(self):
        print ("You see a large cage hanging from a dead tree")
        print ("There seems to be a corpse inside with a sign")
        return """
        The Sign reads : Go East, my sweet meat
        """          
        
        
class SouthTile(MapTile):
    def intro_text(self):
        print ("You see a large cage hanging from a dead tree")
        print ("There seems to be a corpse inside with a sign")
        return """
        The Sign reads : Go South, my butter cups
        """          
        
        
class NorthTile(MapTile):
    def intro_text(self):
        print ("You see a large cage hanging from a dead tree")
        print ("There seems to be a corpse inside with a sign")
        return """
        The Sign reads : Go North, my sugar plums  
        """        

        
class SleepTile(MapTile):
    def __init__(self, x, y):
        self.powerup =1
        self.powerup_claimed = False
        super().__init__(x, y)

    def modify_player(self, player): 
        if not self.powerup_claimed:    
            self.insanity=5
            player.hp=player.fullhp
            player.sanity=player.sanity-self.insanity
            print("Your sanity point{}".format(player.sanity))
            print("Your hp {} ".format(player.hp))
            self.powerup_claimed = True
    
    def intro_text(self):
        if self.powerup_claimed:
            return """
            You return to the church but you only see rubbles..
            Is there no safe space in this dreaded woods ?             
            """
            
        else:
            return """
            You find an abandon church, it has a holy aura around it.
            You decide to rest your exhausted body and find a 
            temperamental solace within this hell...             
                        
            """   

            

            
class MadTile(MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(3,5)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            self.dream_claimed = True
            player.mark=player.mark+1
            print("Your sanity level is {}".format(player.sanity))
            print ("Gain 1 Mark of the Beast") 
            print("")                                                                    
        else:
            player.sanity = player.sanity +1     
            print("Your sanity level is {}".format(player.sanity))                   
            print("") 

    def intro_text(self):
        
        if self.dream_claimed:
       
            return """
            You faintly remember a story about a mother's love for her child.  
            It terrifies you to the core.. 
             """
        else:
            r=random.random()
            if r< 1.0:
               
                print("You see a mother with two daughters.") 
                print("One in red and the other in blue.")
                input(".....")
                print("The mother first hugs the one in 'blue' with a sad sigh")
                input(".....")
                print("She then moves towards the one in 'red' and proceeds to strangle her")
                input(".....")
                print("As red's frantic body ceases of movement and her life becomes no more ")
                input(".....")
                print("the mother then stares wildly  at 'blue 'and moves towards her next ")
                input(".....")
                print("With great excitement she embraces the child")
                input(".....")
                print("She whispers in the sweet child's ear ") 
                input(".....")
                print("'Now, i can love you more'")
                input(".....")
                return """  """
                
                             
                
                
            
            else :
                return """ 
                bleak   """   


class MadTile2 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(3,5)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            player.mark=player.mark+1
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity))
            print ("Gain 1 Mark of the Beast")
            print("                                              ")
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("") 

    def intro_text(self):
        
        if self.dream_claimed:
       
            return """
             You feel that you have taken something important
             from someone here.
             """
        else:
            r=random.random()
            if r< 1.00:
                print("You see a man full of glee stepping up on a chair")
                print("and puts a noose around his neck")
                input(".....")
                print("He then jumps off the chair and hangs in the air for a while")
                input(".....")
                print("Suddenly he starts to cry uncontrollably")
                input(".....")
                print("You start to notice your throat begins to tighten ")
                input(".....")
                print("You struggle for breath frantically grasping at your throat")
                print("Attempting to tear away something that is not there.")
                input(".....")
                print("As you fall into unconsciousness")
                input(".....")
                print("You hear the man rambling angrily at you. ")
                print("Even though it is mostly incoherent")                
                print("It seems you have taken something precious from him")
                input("")
                return """ 
                 
                """
            else :
                return """
                   """                 
    
class MadTile3 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(2,3)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
             
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            player.mark=player.mark+1
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity)) 
            print ("Gain 1 Mark of the Beast")
            print("                                              ")
        
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("")  
          
    
    def intro_text(self):
        
        if self.dream_claimed:  
            return """
             Did you come here to escape from the horror or to face it ?  
             
       
                """
             
        else:
            r=random.random()
            if r< 1.0:
                print("You see the light at the end of the tunnel")
                input(".....")
                print("Your heart skips a beat as you run towards the light")
                input(".....")
                print ("As you reach the light") 
                input(".....")
                print ("You wake up")
                input(".....")
                print("You are surrounded by mangled bodies all with contorted faces of horror" )
                print("You can make out four paths.' ")
                input(".....")
                print ("You wake up..Again")
                return """
                           """
            else :
                return """
                Bleak   """                 

class MadTile4 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(3,5)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            player.mark=player.mark+1
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity)) 
            print ("Gain 1 Mark of the Beast")
            print("                                              ")
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("") 
            
    def intro_text(self):
        
        if self.dream_claimed:
            return """
             This place reminds you of a giant pot of meaty stew.     
             A noisy wailing meaty stew.. 
             """
             
        else:
            r=random.random()
            if r< 1.0:
                print("You see 12 men in rags in a giant pot")
                input(".....")
                print("Scambling over each other to get out")
                input(".....")
                print("But never succeeding and instead falling to the bottom")
                input(".....")
                print("They repeat the cycle until their broken bodies can no longer")
                input(".....")
                print("You notice a 13th man surrounded by bones gnarling on a human leg")
                input(".....")
                print("He looks at you with a menacing smile")
                input(".....")
                print("With a crackling voice he mutters 'I am complete'")
                input(".....")
                return """
                
                    """ 
               
            else :
                return """
                Bleak   """     

              
                        

class MadTile5 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(3,5)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            player.mark=player.mark+1
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity)) 
            print ("Gain 1 Mark of the Beast")
            print("                                              ")
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("")      
            
    def intro_text(self):      
        if self.dream_claimed:
            
            return """
             Somethings are best left unknown
             You quickly move away from this cursed place
             before your remember something you regret..             
             """
             
        else:
            r=random.random()
            if r< 1.0:
                print ("You see a book with a cover that displays a contorted demonic face")
                input(".....")
                print("It is both grotesque yet strangely alluring")
                input(".....")
                print("You can not resist this strange allure and open the book")
                input(".....")
                print("You pry open its heavy cover trembling with both fear and delight")
                input(".....")
                print("In an instant, your mind is consumed with an indescribable dark ecstasy")
                input(".....")
                print("Deeper and deeper you fall into the abyss, time becomes meaningless")
                input(".....")
                print("Yet, you continue until you notice a picture of someone being eaten by a book")
                input(".....")
                print("You panic and attempt to snap from your feverish dream")
                input(".....")
                print("But alas, it is too late, you cannot move, you cannot scream...")
                input(".....")
                return """
                  """  
               
            else :
                return """
                Bleak   """   
                

class MadTile6 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(3,5)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            player.gold= player.gold+30 
            player.mark=player.mark+1
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity)) 
            print("Bones: {}".format(player.gold))
            print ("Gain 1 Mark of the Beast")
            print("                                              ")
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("")      
    
    def intro_text(self):
        
        if self.dream_claimed:
        
       
                
            return """
             A great sense of guilt and regret overcomes you.   
             You continue on with burden on your shoulders 
             and heaviness in your heart.       
             
             """
             
        else:
            r=random.random()
            if r< 1.0:
                print("You see a woman advancing towards you with a Knife")
                input(".....")
                print("You prepare for combat but before you can react")
                input(".....")  
                print("She plunged the knife into her belly")
                input(".....")   
                print("With great struggle she begins to reach inside her body")
                input(".....")
                print("She begins to snap pieces of her ribs and place them on the floor")
                input(".....")
                print("Sobbing and wailing with each crack of her bones")
                input(".....")
                print("Until her body could no longer support her")
                input(".....")
                print("She collapses with exhaustion and with frantic breathes she whispers")
                input(".....")
                print("My loss is your gain")
                input(".....")
                
                return """
                
                
                             """  
               
            else :
                return """
                Bleak   """                   
                
                
class MadTile7 (MapTile):
    def __init__(self, x, y):
        self.sanity = random.randint(1,3)
        self.dream_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.dream_claimed:
            player.sanity = player.sanity + self.sanity
            self.dream_claimed = True
            print("Your sanity level is {}".format(player.sanity)) 
            print("                                              ")
        
        else:
            player.sanity = player.sanity +1
            print("Your sanity level is {}".format(player.sanity)) 
            print("") 

    def intro_text(self):
        
        if self.dream_claimed:
            
            return """
             Why do you return to a place of dead memories ?
             Do you enjoy being tormented by the ghost of the past ?             
       
             """
        else:
            r=random.random()
            if r< 0.5:
                return """
                You have been here for much too long.
                Your sanity is in ruins, you need to escape soon!!
                
                """
            else :
                return """
                Your minds starts to crack. 
                You only see your own damnation
                
                """         


                
class StartTile(MapTile):
    def intro_text(self):
        
        print("You are surrounded by mangled bodies all with contorted faces of horror")
        print("You can make out four paths.")
   
        return """        
        """

        
        
        

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.40:
            self.enemy = enemies.RagMan()
            self.alive_text =r"""
                               You hear a shout in the darkness.  
                               'More rags for the rag man !!' 
                                                                                
                                                      
                                                      """
                                                      
            self.dead_text = """
            
                             A battered corpse lays on floor.
                             Is this the fate fo those that 
                             enter the Woods of Yrpes ?
                                                     """
        elif r < 0.75:
            self.enemy = enemies.BogImp()
            self.alive_text = r"""  
                              A Bog Imp wants to play with you 
                              and your intestines !! 
                                                        
   
          
                              
                              
                                                           """
            self.dead_text = """ 
            
                              A splattered body of a Bog Imp
                              rots on the ground
                                                     """
        elif r < 0.85:
            self.enemy = enemies.DarkYoungofShubNiggurath()
            self.alive_text = r"""
                              A monster of unimaginable horror arrives.
                              Prepare for combat !!  
                              
         
                                """ 
                               
            self.dead_text = """
                              The abomination has been defeated but
                              what a mess it has left behind
                              
                                         """                  
        else:
            self.enemy = enemies.WarMachine()
            self.alive_text = r"""
                               You see a rusty mechanical beast.
                               Made for war, but the war is long over. 

                               
                                                        """                       
            self.dead_text = """
            
                             The Defeated mechanical beast can now find   
                             peace in these dreadful woods.
                                                    """

        super().__init__(x, y) # 3 lines below referring to this 

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            enemydamage=self.enemy.damage-player.armour
            if enemydamage < 0:
                enemydamage=0                
            player.hp = player.hp-enemydamage
            print("Enemy does {} damage. You resisted {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.armour,player.hp))

 #The line of code at the bottom will take the x-y coordinates for this tile and pass them to the 
#__init__method of the superclass (MapTile ). Not needed for the Start Tile because 
#we did not define an __init__ method for that class. (superclass initalizer will be auto called)

class VictoryTile(MapTile):
    
    def modify_player(self,player):
        player.victory=True 
    
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
    
    

        Victory is yours!
        """
    

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            
            print("+{} bones added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable part of the woods. You must continue.
            """
            
        else:
            return """
            You see a pile of bones. Maybe it was someone who failed 
            to escape ? You pick them up regardless. His loss, your gain.
            
            """


class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                print("You have Bones: {}".format(player.gold))
                self.trade(buyer=player, seller=self.trader)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Bones".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                    return            
                
                except ValueError:
                    print("Invalid choice!")
                    
                    

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")


    def intro_text(self):
        return """
        A shadowy figure cloaked in black stands before you
        He desires your bones and will trade for them. 
        He really likes bones..        
        """

world_dsl = """
|HT|LC|DM|EN|ED|RM|SL|TT|MM|BT|
|FG|  |  |  |EN|EN|  |  |  |  |
|EN|EN|EN|  |MT|AM|EN|RT|  |HT|
|ED|TT|EN|EN|ND|EN|  |LA|DM|EN|
|EN|  |EN|  |TT|DM|  |EN|  |EN|
|NT|EN|IT|EN|EN|LB|EN|TT|EN|CM|
|EN|  |  |  |EN|EN|  |  |  |EN|
|ND|EN|WD|  |EN|EN|EN|LT|  |EN|
|EN|EN|ST|EN|EN|BM|  |EN|EN|SL|
|HT|  |EN|  |EN|TT|  |EN|  |DT|

"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|BT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "MT": MadTile,
                  "NT": MadTile2,
                  "MM": MadTile3,
                  "AM": MadTile4,
                  "BM": MadTile5,
                  "CM": MadTile6,
                  "DM": MadTile7,
                  "TT": TraderTile,
                  "ND": NorthTile,
                  "ED": EastTile,
                  "SD": SouthTile,
                  "WD": WestTile,
                  "BT": BossTile,
                  "HT": FindHealthTile,
                  "IT": FindSwordTile,
                  "DT": FindHammerTile,
                  "RT": FindRingTile,
                  "RM": RagManTile,
                  "LT": LocationTile,
                  "LA": LocationTile2, 
                  "LB": LocationTile3, 
                  "LC": LocationTile4,                  
                  "SL": SleepTile,                   
                  "  ": None}
                  


world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x,y):      # function that locate the tile at a coordinate 
    if x< 0 or y<0:    # return non if smaller than bound of map 
        return None 
    try: 
        return world_map[y][x]  # y part select row, x select specific cell  
    except IndexError:          # return none if greater than bound of map           
        return None 
            
            
            
