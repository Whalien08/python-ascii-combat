import time
import random
import os

# Hitpoints and weapons organized into a dictionary for easy access
WEAPONS = {
    "1": {"name": "Machine Gun", "damage": [5, 6, 7, 7, 8]},
    "2": {"name": "Pistol",      "damage": [2, 3, 3, 4, 5]},
    "3": {"name": "Grenade",     "damage": [5, 6, 7, 7, 8]},
    "4": {"name": "Fireball",    "damage": [6, 7, 8, 9, 10]},
    "5": {"name": "Health",      "heal":   [4, 4, 5, 5, 5]},
    "motorcycle": {"name": "Motorcycle", "damage": [3, 4, 5, 6, 7]},
    "bomb": {"name": "Bomb",             "damage": [3, 3, 4, 5, 6]}
}

ENEMY_WEAPONS = ["motorcycle", "bomb"]

NAMES = ["Steve Jobs", "Crazy Henry", "Corn Eater", "Ayachi Master", "Jason Voorhees", "Jelle", "Abbe", "Rembrandt", "Jesus", "Captain", "Cobra", "Driver", "Gert-Jan Meijer", "Golfball", "Pixel", "Pacboi", "LongBoi", "Calvin", "Redbeard", "Your Teacher", "Hyperboy", "Your Mom"]

SLEEP_TIMES = [0.5, 0.6, 0.7, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4]

#Helper Functions

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_frame(p_name, p_hp, e_name, e_hp, art_lines, delay=0.1):
    """Draws a single frame of the game to the console."""
    clear()
    print("                                ")
    print(f"  {p_name}")
    print(f"  {p_hp}hp")
    if e_name and e_hp is not None:
        print(f"                         {e_name}")
        print(f"                         {e_hp}hp")
    else:
        print("                                ")
        print("                                ")
    print("                                ")
    
    # Print the specific ASCII art for this frame
    for line in art_lines:
        print(line)
        
    time.sleep(delay)

def play_animation(p_name, p_hp, e_name, e_hp, frames, delay=0.1):
    """Plays a sequence of frames."""
    for frame in frames:
        draw_frame(p_name, p_hp, e_name, e_hp, frame, delay)

#Core Game Loop

def main():
    player_hp = 100
    enemy_hp = 100
    
    clear()
    print("\n\n\nGive your character a name.\n")
    name = input(": ")
    
    # Selection Spin
    spin = 0.005
    enemy = ""
    for _ in range(30):
        spin += 0.006
        enemy = random.choice(NAMES)
        default_stance = [
        "    @                      @    ",
        "   /|\                    /|\   ",
        "___/ \____________________/ \___" 
    ]
        draw_frame(name, player_hp, enemy, enemy_hp, default_stance, spin)
        print(f"\n\n\nYou are playing against {enemy}.")
    
    input("\nPress Enter to begin.")

    # Main Combat Loop
    while player_hp > 0 and enemy_hp > 0:
        #ENEMY TURN
        enemy_weapon_id = random.choice(ENEMY_WEAPONS)
        enemy_weapon = WEAPONS[enemy_weapon_id]
        damage = random.choice(enemy_weapon["damage"])
        
        default_stance = ["    @                      @    ", 
                          "   /|\                    /|\   ",
                          "___/ \____________________/ \___" ]
        draw_frame(name, player_hp, enemy, enemy_hp, default_stance, 1)
        print(f"\n\n\n{enemy}'s turn.")
        time.sleep(random.choice(SLEEP_TIMES))
        print(f"\n{enemy} uses their {enemy_weapon['name']}.")
        time.sleep(2)
        if enemy_weapon_id == "bomb":
            bomb_frames = [
                [
                 "    @                     _@    ", 
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                [
                 "    @                    ╥_@    ",
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["                         ╥      ", 
                 "    @                     \@    ",
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___" 
                ],

                ["    o                           ",
                 "                         ╥      ",
                 "    @                     \@    ",
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["    o                           ",
                 "    o                    ╥      ",
                 "    @                     \@    ",
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["    |                           ",
                 "    o                    ╥      ",
                 "    @                     \@    ",
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["    |                    ╥      ",
                 "    #*                    \@    ", 
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["    |                    ╥      ",
                 "   *#*                    \@    ", 
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ],

                ["                         ╥      ",
                 "    #                     \@    ", 
                 "   /|\                     |\   ",
                 "___/ \____________________/ \___"
                ]
            ]
            play_animation(name, player_hp, enemy, enemy_hp, bomb_frames, 0.4)
            player_hp -= damage
            
        elif enemy_weapon_id == "motorcycle":
            motorcycle_frames = [
                ["    @                   @__,    ", 
                 "   /|\                 ,>_/-_   ", 
                 "___/ \________________(*)`\(*)__"],

                ["    @_              @__,        ", 
                 "   /|              ,>_/-_       ", 
                 "___/ \____________(*)`\(*)______"],

                ["    @_          @__,            ", 
                 "   /|          ,>_/-_           ", 
                 "___/ \________(*)`\(*)__________"],
                 
                ["    @_      @__,                ", 
                 "   /|      ,>_/-_               ", 
                 "___/ \____(*)`\(*)______________"],

                ["    @_  @__,                    ", 
                 "   /|  ,>_/-_                   ", 
                 "___/ \(*)`\(*)__________________"],

                ["      @__,                      ", 
                 "     ,>_/-_                     ", 
                 "____(*)`\(*)____________________"],

                [
                    "    @@__,                       ", 
                    "   /|  /|\                      ",
                    "    # ,>_/-_                    ",
                    "____(*)`\(*)____________________"
                ],

                [
                    " #@__,                          ", 
                    " #  /|\                         ",
                    "  ,>_/-_                        ",
                    "_(*)`\(*)_______________________"
                ],

                [
                    " @__,                           ", 
                    "   /|\                          ",
                    "  ,>_/-_                        ",
                    "_(*)`\(*)_______________________"                   
                ]
            ]
            play_animation(name, player_hp, enemy, enemy_hp, motorcycle_frames, 0.15)
            player_hp -= damage

        #PLAYER TURN
        if player_hp <= 0:
            break
            
        draw_frame(name, player_hp, enemy, enemy_hp, default_stance, 1)
        print("\n\n\nIt's your turn.\n\nChoose your weapon:")
        print(" 1 Machine Gun\n 2 Pistol\n 3 Grenade\n 4 Fireball\n 5 Heal\n")
        
        choice = input(": ")
        if choice in WEAPONS:
            weapon = WEAPONS[choice]
            
            if choice == "5":
                heal_amount = random.choice(weapon["heal"])
                heal_frames = [
                    [
                        "   _@_                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    +                           ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "  +   +                         ",
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    +                           ",
                        "  +   +                         ",
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    |                           ",
                        "   + +                          ",
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    |                           ",
                        "   +|+                          ",
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    +                           ",
                        "  +   +                         ",
                        " +  +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    +  +                        ",
                        "   \@/                     @    ", 
                        "    |                     /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "    @                      @    ", 
                        "  +/|\+                   /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        "  + @ +                    @    ", 
                        "   /|\                    /|\   ",
                        "___/ \____________________/ \___"
                    ],
                    [
                        " +     +                        ", 
                        "    @                      @    ",
                        "   /|\                    /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @                      @    ", 
                        "   /|\                    /|\   ",
                        "___/ \____________________/ \___"
                    ]
                ]
                
                print(f"\nYou use {weapon['name']}...")
                play_animation(name, player_hp, enemy, enemy_hp, heal_frames, 0.3)
                player_hp += heal_amount
                print(f"You heal {heal_amount} HP!")
                time.sleep(1)
            
            elif choice == "4":
                damage = random.choice(weapon["damage"])
                
                fireball_frames = [
                    ["    @  O                   @    ", 
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @     O                @    ", 
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @        O             @    ",
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @           O          @    ",
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @              O       @    ",
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @                 O    @    ",
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @                    *@* ",
                     "   /|\                    /|\   ",
                     "___/ \____________________/ \___"
                    ],

                    ["    @                     *#*     ",
                     "   /|\                    /*\    ",
                     "___/ \____________________/ \____"
                    ],

                    ["    @                     *#*     ",
                     "   /|\                    /*\    ",
                     "___/ \____________________/ \____"
                    ],

                    ["    @                     *@*    ",
                     "   /|\                    /*\    ",
                     "___/ \____________________/ \____"
                    ],

                    ["    @                      @     ",
                     "   /|\                    /*\    ",
                     "___/ \____________________/ \____"
                    ],
                    ["    @                      @     ",
                     "   /|\                    /|\    ",
                     "___/ \____________________/ \____"
                    ]
                ]
                
                print(f"\nYou cast {weapon['name']}!")
                play_animation(name, player_hp, enemy, enemy_hp, fireball_frames, 0.15)
                
                enemy_hp -= damage
                print(f"Direct hit! {damage} damage.")
                time.sleep(1)

            elif choice == "3":
                damage = random.choice(weapon["damage"])
                
                grenade_frames = [
                    [
                     "  * @                      @    ", 
                     "   /|\                    /|\   ", 
                     "___/ \____________________/ \___"
                    ],

                    ["    @      *⌀              @    ", 
                     "   /|\                    /|\   ", 
                     "___/ \____________________/ \___"],

                    ["    @              *⌀      @    ", 
                     "   /|\                    /|\   ", 
                     "___/ \____________________/ \___"],

                    ["    @                   *⌀ @    ", 
                     "   /|\                    /|\   ", 
                     "___/ \____________________/ \___"],

                    ["    @               (( ))  @    ", 
                     "   /|\             ( (X) )#|\   ", 
                     "___/ \____________(__( )__) \___"],
                    
                    ["    @               (( )) *#*   ", 
                     "   /|\             ( (X) )#|\   ", 
                     "___/ \____________(__( )__) \___"],

                    ["    @               (( )) *@*  ", 
                     "   /|\             ( (X) )#|\   ", 
                     "___/ \____________(__( )__) \___"],

                    ["    @                ( )   @    ", 
                     "   /|\               (X)  #|\   ", 
                     "___/ \_______________( )__/ \___"],


                    ["    @             (o)      @    ", 
                     "   /|\           / X \    /|\   ", 
                     "___/ \____________________/ \___"]
                ]
                
                print(f"\nYou throw a {weapon['name']}!")
                play_animation(name, player_hp, enemy, enemy_hp, grenade_frames, 0.3)
                
                enemy_hp -= damage
                print(f"Boom! {damage} damage dealt.")
                time.sleep(1)

            elif choice == "2":
                damage = random.choice(weapon["damage"])

                piston_frames = [
                    [
                        "    @                      @    ", 
                        "   /|\                    /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_                     @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<-                  @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<----               @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<--------           @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<-----------        @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<--------------     @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<-----------------  @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔<-------------------#    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔     --------------*#*   ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔         ----------*#*    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔             ------*#*    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔                 --*#*    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔                    #    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_╔                    @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ]
                ]
                print(f"\nYou cast {weapon['name']}!")
                play_animation(name, player_hp, enemy, enemy_hp, piston_frames, 0.15)
                
                enemy_hp -= damage
                print(f"Direct hit! {damage} damage.")
                time.sleep(1)
            elif choice == "1":
                damage = random.choice(weapon["damage"])

                machine_frames = [
                    [
                        "    @                      @    ", 
                        "   /|\                    /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_                     @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<-               @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<----            @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<-------         @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<----------      @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<-------------   @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<--------------  @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─<---------------*@    ", 
                        "   /|                     /#\    ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─  -------------?*@   ", 
                        "   /|                     /#*   ",
                        "___/ \____________________*?\___" 
                    ],
                    [
                        "    @_⌐╦═─      ---------?*@   ", 
                        "   /|                     /#*   ",
                        "___/ \____________________*?\___"  
                    ],
                    [
                        "    @_⌐╦═─          -----?*@     ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─              --*@    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                    [
                        "    @_⌐╦═─                 @    ", 
                        "   /|                     /|\   ",
                        "___/ \____________________/ \___" 
                    ],
                ]
                print(f"\nYou cast {weapon['name']}!")
                play_animation(name, player_hp, enemy, enemy_hp, machine_frames, 0.15)
                
                enemy_hp -= damage
                print(f"Direct hit! {damage} damage.")
                time.sleep(1)
        else:
            print("\nInvalid choice! You lose your turn.")
            time.sleep(1)

    # Game Over State
    clear()
    if player_hp <= 0:
        print(f"\n\nGAME OVER. {enemy} has won.")
    else:
        print(f"\n\nYOU WIN! You have defeated {enemy}.")

if __name__ == "__main__":
    main()