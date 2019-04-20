from collections import OrderedDict
from player import Player
import world
import time 

def play():
    print(r""" 



    
 
      _    _                    _           __  __   __                        
     | |  | |                  | |         / _| \ \ / /                        
     | |  | |  ___    ___    __| |   ___  | |_   \ V /  _ __   _ __   ___  ___ 
     | |/\| | / _ \  / _ \  / _` |  / _ \ |  _|   \ /  | '_ \ | '__| / _ \/ __|
     \  /\  /| (_) || (_) || (_| | | (_) || |     | |  | |_) || |   |  __/\__ \
      \/  \/  \___/  \___/  \__,_|  \___/ |_|     \_/  | .__/ |_|    \___||___/
                                                       | |                     
                                                       |_|                                                     

                                             v .   ._
                               `-._\/  .  \ /    |/_
                                   \\  _\, y | \//
                             _\_.___\\, \\/ -.\||
                               `7-,--.`._||  / / ,
                               /'     `-. `./ / |/_.'
                                         |    |//
                                         |_    /
                                         |-   |
                                         |   =|
                                         |    |
                              ----------/ ,  . \--------
                                         
           
                       The Woods of Ypres by Tommy Kwong (2018)
                              Dedicated to David Gold
                                                                                                """)     

    time.sleep(1)
    print("Falsely accused of heinous crimes ")
    print("You were sent south to the Woods Of Ypres ")
    time.sleep(1)
    print("On the way to the heart of the Woods ")
    print("Your caravan was attacked. You blacked out")
    time.sleep(1)
    print("You wake up surrounded by dead bodies")
    print("You gather some items and begin your quest to escape")
    print("The Woods Of Ypres..  ")
    time.sleep(1)
    print("                       ")                                 
    world.parse_world_dsl()
    player=Player()  #this is an object without this no action can be done. 
    while player.is_alive()and player.is_sane() and not player.victory:
        room=world.tile_at(player.x, player.y)  #because player()start at1,2
        print(room.intro_text())                 #this is the start position # and wil print its intro
        room.modify_player(player) #new line, this call the enemy as soon as player enter tiles 
        if player.is_alive()and player.is_sane() and not player.victory:
            choose_action(room,player)
        elif player.is_alive()and not player.is_sane() and not player.victory:
            print("The beast in your mind has tracked you down")
            print("Madness has consumed you, welcome to the family, my rag sibling ")
            input("Press enter to exit")
        elif not player.is_alive():
            print("You have been slain. Rest in Peace, fallen one !!")
            input("Press enter to exit")

        
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")
    
def get_available_actions(room, player):
    actions = OrderedDict()
    print(" Choose an action:")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Inventory/Stats")
    if player.inventory:
        action_adder(actions, 'p', player.pick, "Select Weapon")
    if isinstance(room, world.BossTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")        
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")  
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    
    
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north (Up)")
        if world.tile_at(room.x, room.y + 1):                       
            action_adder(actions, 's', player.move_south, "Go south (Down)")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east (Right)")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west (Left)")
    if player.hp < player.fullhp:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))



    

play()  #A simple call to the play function
