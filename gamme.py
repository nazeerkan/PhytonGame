import sys,time, random

#function for defining typewriting text
def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  
def typinginput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  
  return value  
#Making sure we put all the functions first so we can call them later

#This is the intro (Done by Everyone)

def start_game():
    typingprint()
    


typingprint("""\033[1;31;40m
 _______ _    _ ______   _____          _____  _  __  ____  ______ _      ______          __        # Tyler Graphic
|__   __| |  | |  ____| |  __ \   /\   |  __ \| |/ / |  _ \|  ____| |    / __ \ \        / /                       
   | |  | |__| | |__    | |  | | /  \  | |__) | ' /  | |_) | |__  | |   | |  | \ \  /\  / /                        
   | |  |  __  |  __|   | |  | |/ /\ \ |  _  /|  <   |  _ <|  __| | |   | |  | |\ \/  \/ /                         
   | |  | |  | | |____  | |__| / ____ \| | \ \| . \  | |_) | |____| |___| |__| | \  /\  /                          
   |_|  |_|  |_|______| |_____/_/    \_\_|  \_\_|\_\ |____/|______|______\____/   \/  \/                           
                                                                                                                   \033[1;31;40m\n""")
print("")
typingprint("Chapter 1 ") # Group
print("")
typingprint("In the Beginning:\n")
typingprint("....................Eyes Open...................\n")
typingprint("As you awaken in an unknown place, your body trembles with fear and confusion.\n")
typingprint("Memories of strange occurrences and conspiracy theories flood your mind.\n")
typingprint("You try to push off the debris from the crashed plane as quickly as possible.\n")
typingprint("Struggling up the mountain path, you finally survey your surroundings.\n")
typingprint("All you see is forest and valley beyond, and the eerie feeling of emptiness sends shivers down your spine.\n")
typingprint("Your heart races as you suddenly jolt backwards, feeling like a defeated soul.\n")
typingprint("-----------------------------------------------------------------------------------------------\n")
name = input("Your eyes dart towards the bush, and as it opens up, a face appears, making you feel even more nervous. Hey there, I'm Tolund Owen! What's your name?: \n")

if len(name) > 3:
    typingprint("Welcome to the Kingdom of Throne\n")
else:
    typingprint("How dare you insult me!\n")

player = name

typingprint(f"There is nothing to be afraid of, {name}. Welcome to the Throne World;\n")
typingprint("We have suffered from the disease-ridden hand of the wicked queen.\n")
typingprint("This is an opportune time you came, for Throne World is beset by the ancient peril.\n")
typingprint("My people require your assistance in reclaiming our land from the clutches of the witch queen.\n")
typingprint("We must destroy her reign of terror and restore peace to our people.\n")
typingprint("-----------\n")
quest = input("Will you offer your hand in combat, killing the witch queen? You ponder to yourself for a moment, do you wish to proceed? Yes or No: \n")

if quest.lower() == 'yes':
    typingprint("With a beaming smile, Tolund declares that we are about to embark on an amazing adventure. We will journey to Thorne Schulze Castle where we can relax and rejuvenate.\n")
else:
    typingprint("YOU ARE DEAD! As fast as a Thunderfist, the Gods of Throne World act swiftly and harshly. Refusing aid to the people of Throne World may result in swift and harsh action from the Gods of the Throne World, resulting in the snuffing out of one's life as quickly as a Thunderfist.\n")
    typingprint("""\033[1;31;40m
       _____          __  __ ______    ______      ________ _____  
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
      
      \033[1;31;40m\n""")
     
    quit()



                                                                                                                                                    
typingprint("----------------------------------------------------------------------\n")
typingprint("  _______ _                              _____          _   _       \n")    
typingprint(" |__   __| |                            / ____|        | | | |      \n")  
typingprint("    | |  | |__   ___  _ __ _ __   ___  | |     __ _ ___| |_| | ___  \n") 
typingprint("    | |  | '_ \ / _ \| '__| '_ \ / _ \ | |    / _` / __| __| |/ _ \ \n")    
typingprint("    | |  | | | | (_) | |  | | | |  __/ | |___| (_| \__ \ |_| |  __/ \n")  
typingprint("    |_|  |_| |_|\___/|_|  |_| |_|\___|  \_____\__,_|___/\__|_|\___| \n") 
print("")
typingprint("Chapter 2\n") 
typingprint("Thorne Castle:\n")
typingprint("----------------------------------------------------------------------\n")
print("")
typingprint("Priest Tolund Owen's expression turns to joy - 'Praise be to the deities. You please the Gods for your good sense,'\n")
typingprint("I have rewarded you with a map, armor, and weapons. Venture Eastward to Thorne Schulze Castle in Neomuna to defeat the hell that plagues this land.\n")
typingprint("Priest Tolund makes one last gesture; you fill your goblet, and off you travel on your quest to Neomuna in the nearing dark.\n")
typingprint("Days of travel, the moon penetrates the leafy canopy, and from afar, you can hear the strains of flutes and high pitch.\n")
typingprint("You move cautiously towards Thorne Schulze Castle. You gaze in wonder at the scene before you.\n")
print("----------------------------------------------------------------------------------\n")
typingprint("   /\                                                        /\ \n")
typingprint("  |  |                                                      |  | \n")
typingprint(" /----\                                                    /----\ \n")
typingprint("[______]                                                  [______] \n")
typingprint(" |    |         _____                        _____         |    | \n")
typingprint(" |[]  |        [     ]                      [     ]        |  []| \n")
typingprint(" |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    | \n")
typingprint(" |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    | \n")
typingprint(" |             |     |/'    ____..____    '\|     |             | \n")
typingprint("  \  []        |     |    /'    ||    '\    |     |        []  / \n") 
typingprint("   |      []   |     |   |o     ||     o|   |     |  []       | \n")
typingprint("   |           |  _  |   |     _||_     |   |  _  |           | \n")
typingprint("   |   []      | (_) |   |    (_||_)    |   | (_) |       []  | \n")
typingprint("   |           |     |   |     (||)     |   |     |           | \n")
typingprint("   |           |     |   |      ||      |   |     |           | \n")
typingprint(" /''           |     |   |o     ||     o|   |     |           ''\ \n")
typingprint("[_____________[_______]--'------''------'--[_______]_____________] \n")
print("--------------------------------------------------------------------------------------\n")
typingprint("Do you wish to enter through the MAIN GATE? Press a\n")
typingprint("Do you want to go around to the BROKEN WALL? Press b\n")
typingprint("Do you wish to go through the DUNGEONS? Press c\n")
typingprint("----------------------------------------------------------------------------------------\n")

choice = input("How to you wish to proceed? Press a, b, or c: \n")

player_HP = 100

if choice.lower() == "a":
    typingprint("Main Gate\n")
    dice1 = random.randint(1, 6)
    typingprint(dice1)
    typingprint(player_HP)
    total = (dice1 * 100) - player_HP
    typingprint(total)
    if total <= 600:
        typingprint("YOU ARE DEAD! Overwhelmed by 30 ballista turrets, you find yourself gazing at the sky and taking your final exhale. Death is just the beginning.\n")

elif choice.lower() == "b":
    typingprint("Broken Wall\n")
    
    def sneak_or_attack():
        typingprint("After assessing the situation, you approach the broken wall cautiously and carefully enter through it. You weigh your options and decide if to sneak past the two guards undetected or engage in combat and try to take them down. The choice is yours, but it is essential to consider your safety and decide to align with your goals and values.\n")
        choice = input("What would you like to do? Do you sneak past the guards or attack them? (Sneak/Attack): \n").lower()
        
        if choice == "sneak":
            typingprint("You took your chances and decided to take a risk and stumbled upon a group of guards...\n")
            typingprint("As you approach the broken wall, you carefully assess the situation and choose the safest entry point. Once inside, you weigh your options and consider the risks of sneaking past the two guards versus confronting them head-on. After careful consideration, you make your decision and either stealthily make your way past the guards undetected or engage them in combat and emerge victorious. However, if luck is not on your side and the guards discover your presence, they may overpower you and ultimately lead to your demise. It is important to stay vigilant and always be prepared for any outcome. YOU ARE DEAD, you have made the wrong choice.\n")
            typingprint("   _____          __  __ ______    ______      ________ _____  \n")
            typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
            typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
            typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
            typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
            typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
            quit()

        elif choice == "attack":
            typingprint("In the dark corner, you approach the Elite Guard Soldiers of Thorne Schulze Castle, punctuated by the openings to the left and the right. You spot a weapon on the ground, glistening in its glory, and you seize it. You are ready for battle. Do you invoke your mighty Ultimate Mighty Fist of Destruction - Heavy Attack or Muck ill frenzy - Light Attack?\n")
            attack_choice = input("How do you wish to attack? (Heavy/Light): ").lower()
            
            if attack_choice == "heavy":
                typingprint("You unleash the Ultimate Mighty Fist of Destruction, a heavy attack.\n")
                typingprint("Despite your valiant effort to execute the swing of the Ultimate Mighty Fist of Destruction against the Elite Guard Soldiers of Thorne Schulze Castle, your pride got the better of you, and you were unable to match their skill. With an effortless counter-attack, they were able to crush you. Although your journey has come to an end, your bravery and determination will be an inspiration for others to follow. You are Dead!\n")
                typingprint("   _____          __  __ ______    ______      ________ _____  \n")
                typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
                typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
                typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
                typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
                typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
                quit()

            elif attack_choice == "light":
                typingprint("With your dexterity, you execute a quick and light attack, Muck ill frenzy.\n")
                typingprint("Sweating and trembling from the terrible experience, you find silence to invoke Muck's ill frenzy - You mumble from your soul and strike in honor of Muck. Victory swiftly comes beneath your blade. For now, the Patron God is favorable to you. You continue your journey.\n")

            else:
                typingprint("Invalid attack choice. Please try again.\n")
                sneak_or_attack()
        else:
            typingprint("Invalid choice. Please try again.\n")
            sneak_or_attack()

    sneak_or_attack()

elif choice.lower() == "c":
    typingprint("Dungeons entrance\n")
    typingprint("As you approach the dungeon's entrance, you must remain vigilant of the knight of shadows who stands guard.  With a concerned look, the Smog Bringer cautions you, this is no place for the faint-hearted.  Either leave while you still can or prepare to meet your demise. Engaging in a battle with the knight of shadows entails a high risk of losing your life.  Alternatively, fleeing would only lead you back to the castle entrance. What is your decision?\n")
    typingprint("You must weigh your options carefully before making a decision. You ignore the warning of Smog Bringer, the knight of Shadows, and engage in combat or retreat, such as this is hardly an act of a coward. You have a 50/50 chance:\n")
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    
    if total % 2 == 0:
        typingprint("As you strategically retreat from the danger, you realize this is not the end of your journey but a necessary step towards securing your survival. Memories of the brave heroes of old fill your mind, inspiring you to press on despite the challenges ahead. With renewed vigor, you break free from Smog Bringer's dark magic clutches and feel grateful for the chance to continue your quest. Now, as you approach the castle gates, you stand ready to face whatever challenges may come your way. You get to live another day.\n")

    else:
        typingprint("Despite the warning from Smog Bringer, the renowned Knight of Shadows, you recklessly engaged in combat. Unfortunately, this led to your untimely demise, as you met a gruesome and dishonorable end. You were impaled in the treacherous and intricate labyrinth of Thorne Schulze, where many have lost their lives before you. You are Dead and Disgraced!\n")
        typingprint("   _____          __  __ ______    ______      ________ _____  \n")
        typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
        typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
        typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
        typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
        typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
        quit()

          
typingprint("--------------------------------------------\n")
typingprint("   _____ _____   ____ _______       \n")
typingprint("  / ____|  __ \ / __ \__   __|/\    \n")
typingprint(" | |    | |__) | |  | | | |  /  \   \n")
typingprint(" | |    |  _  /| |  | | | | / /\ \  \n")
typingprint(" | |____| | \ \| |__| | | |/ ____ \ \n")
typingprint("  \_____|_|  \_\\_____/  |_/_/    \_\\\n")
typingprint("--------------------------------------------\n")
typingprint("Chapter 3\n")
typingprint("Son of Oryx:\n")
typingprint("--------------------------------------------\n")

def fight_son_of_oryx(name):
    son_of_oryx_HP = 1
    player_HP = 100
    player_damage = random.randint(2,12)

    while son_of_oryx_HP > 0 and player_HP > 0:
        typingprint(f"{name}, you engage in battle with the Son of Oryx!\n")
        typingprint(f"The Son of Oryx has {son_of_oryx_HP} HP.\n")
        typingprint(f"{name}, you have {player_HP} HP.\n")

        attack_choice = input(f"{name}, enter 'attack' to attack the Son of Oryx: \n")

        if attack_choice.lower() == "attack":
            son_of_oryx_HP -= player_damage
            typingprint(f"{name}, you deal {player_damage} damage to the Son of Oryx.\n")

            if son_of_oryx_HP <= 0:
                return True

            son_of_oryx_damage = random.randint(3, 18)
            player_HP -= son_of_oryx_damage
            typingprint(f"The Son of Oryx counterattacks and deals {son_of_oryx_damage} damage to you.\n")

    return False

def main():
    
    typingprint("As you arrived at the enigmatic Hive deity's abode, Crota, you found yourself standing in the depths of the imposing Thorne Schulze Castle. At the end of a seemingly endless abyss, the formidable Crota, Son of Oryx, loomed before you. The overwhelming powers of sleep threatened to overtake you, almost closing your eyelids. However, with unwavering determination, you knelt and called upon the favor of Patron God Throne, fully aware of the perilous risk to your life. With trepidation cast aside, you emerged and charged valiantly towards the mighty Oryx.\n")

    choice = input(f"Prepare for battle, {name}! Are you ready to face the Son of Oryx? (Yes or No): ").lower()

    if choice == "yes":
        if fight_son_of_oryx(name):
            typingprint(f"Congratulations, {name}! You defeated the Son of Oryx.\n")
            typingprint(".............................................................................................................\n")        
            typingprint("As your blade strikes through the body of Oryx, his final screams echo through the halls. Through your swift and precise swordsmanship, you have accomplished the complete and utter destruction of Oryx, leaving behind nothing but a pile of scorched, earthy armor and weaponry.\n")

            typingprint(f"{name}, the fiery aftermath has scorched the ground of the Gods' Favor citadel, leaving smoldering imtypingprints in its wake. On the floor lie armor, weapons, and accessories that appear suited to your size, causing one to question their origin and purpose. Which looks suspicious.\n")
            item_choice = int(input("Do you Not pick up Press 1. Yes, please Press 2 to pick up the items: "))

            if item_choice == 1:
                typingprint("After careful consideration, you concluded that it wasn't worth your time to pick up the items. You are currently carrying a heavy load, and adding more to your burden would not be wise. You made a logical decision and decided to walk away without any regrets. You confidently left the discarded items behind you, knowing that they were not a valuable addition to your possessions.\n")
                player_HP = 100
                player_damage = random.randint(2, 12)

                typingprint(f"{name} has {player_HP} HP and has a damage potential of {player_damage} (2xD6).")
                
            elif item_choice == 2:
                typingprint("As you bow to the ground, praying for guidance and wisdom from the divine entity known as the God Hauteur of Neomuna, the hall emanates a radiant glow of celestial light. {player_name} confidently claims the 'Hubris, Favor of Grieving Widow Set' and proudly adorns it. As you reach out to pick up the Set, you feel the power of the God Hauteur's favor and blessings upon you. The gift bestows upon you an incredible increase in your statistics, multiplying them threefold.\n")
                player_HP = 300
                player_damage = random.randint(3, 18)

                typingprint(f"{name} has {player_HP} HP and has a damage potential of {player_damage} (3xD6).\n")
                typingprint("----------------------------------------------------------------------------------\n")
                typingprint("              /> \n")
                typingprint("             /< \n")
                typingprint("            /< \n")
                typingprint("  |\_______{o}----------------------------------------------------------_ \n")
                typingprint(" [\\\\\\\\\\\{*}:::<===============================================-       > \n")
                typingprint("  |/~~~~~~~{o}----------------------------------------------------------~ \n")
                typingprint("            \< \n")
                typingprint("             \< \n")
                typingprint("              \> \n")
                typingprint("----------------------------------------------------------------------------------\n")

            else:
                typingprint("Invalid choice. Exiting the game.\n")
                typingprint("   _____          __  __ ______    ______      ________ _____  \n")
                typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
                typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
                typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
                typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
                typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
               
        else:
            typingprint("AS EXPECTED, YOU ARE DEAD. Game over\n")
            typingprint("   _____          __  __ ______    ______      ________ _____  \n")
            typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
            typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
            typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
            typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
            typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
            

    else:
        typingprint(f"{name}, you coward! You decline the challenge. You are Dead! Bah....\n")

main()


typingprint("\n--------------------------------------------------------------------------------------------------\n")
typingprint("  _______ _             _____                 _ _                _                            \n")
typingprint(" |__   __| |           / ____|               (_) |              | |                          \n")
typingprint("    | |  | |__   ___  | |  __ _ __ __ ___   ___| |_ ___  _ __   | |     __ _ _ __   ___ ___  \n")
typingprint("    | |  | '_ \ / _ \ | | |_ | '__/ _` \ \ / / | __/ _ \| '_ \  | |    / _` | '_ \ / __/ _ \ \n")
typingprint("    | |  | | | |  __/ | |__| | | | (_| |\ V /| | || (_) | | | | | |___| (_| | | | | (_|  __/ \n")
typingprint("    |_|  |_| |_|\___|  \_____|_|  \__,_| \_/ |_|\__\___/|_| |_| |______\__,_|_| |_|\___\___| \n")

typingprint("Chapter 4\n") 
typingprint("The Graviton Lance:\n")
typingprint("---------------------------------------------------------------------------------------------------\n")

typingprint("Victory is ours!  I quickly return to Tolund, flashing a mysterious grin as I reveal my successful strikes against the unbeatable Oryx.  Tolund is astounded and asks how I managed to accomplish such a feat.  But I know the key to our successive victory lies in obtaining the mythical --The Graviton Lance--, a weapon of unparalleled power in this realm.  According to ancient legends, this weapon will help us weaken Queen Savathun and ultimately bring about her destruction.\n")
print("")
typingprint("Back in towards Thorne Schulze Castle to Neomuna to quest for --The Graviton Lance--, you and your companion  Priest Tolund venture into the castle.\n")
print("")
typingprint("You came to this magnificence of this Hall?  Within the Halls on the pointing mount, there lay 3 Statue upon which the chest lies Back in towards Thorne Schulze Castle, accompanied by Priest Tolund, your quest for --The Graviton Lance-- leads you into the heart of the fortress.  Day and night, you battle through the dungeon, leaving behind a trail of lifeless bodies. / After a long and gruelling fight, you land the final blow on a disease-ridden creature.  Its pained shrieks echo through the halls as it lashes out with its tail but eventually succumbs to your might. \n ")


def play_game():
    typingprint("As the iridescent green clouds dissipate, they reveal a doorway leading to a magnificent hall atop the pointing mount.  Inside, you find three status, each bearing a chest upon its pedestal.  The grandeur of the place leaves you in awe.\n")
    typingprint(f"{name} you have three chests before you. Which chest do you choose?: Chest 1, Chest 2, and Chest 3.\n")

    chest_choice = input("Enter the number of the chest you want to open (1, 2, or 3): \n")

    if chest_choice == "3":
        typingprint("Upon unlocking the chest, the very earth beneath Thorne Schulze Castle quakes, unleashing a powerful curse feard as --Shattered Majesty-- that shakes the very foundations of the castle. The ground begins to split apart before your eyes, leading you to tumble down into the dark abyss of --Jurlus Ruhrasnath-- with a sense of scepticism and uncertainty and hearing your voice echoing and the collapsing castle. YOU ARE DEAD!!\n")
        typingprint("   _____          __  __ ______    ______      ________ _____  \n")
        typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
        typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
        typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
        typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
        typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
        quit()
    elif chest_choice == "1":
        typingprint(f"{name} You have choosen Chest 1 and found a riddle!\n")
        riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (Type SECRET(a) , THE PAST(b) , AN ECHO(c)\n"
        typingprint("Riddle: " + riddle)
        answer_choice = input("Enter the correct answer (a, b, or c): \n")

        if answer_choice == "a" or answer_choice == "b":
            typingprint(f"{name} I am Death, Here to claim your soul! You are Dead!\n")
            typingprint("   _____          __  __ ______    ______      ________ _____  \n")
            typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
            typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
            typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
            typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
            typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
            quit()
        elif answer_choice == "c":
            typingprint("The Graviton Lance? Yes!\n")

            player_hp = random.choice([100, 300])
            typingprint("Player HP:", player_hp)
            typingprint("Your current HP is: " + str(player_hp))

            if player_hp == 100:
                typingprint("Congratulations on solving the riddle! As the chest opens, you are presented with a magnificent weapon - --The Graviton Lance-- - that lies before you. However, to obtain this mighty artifact, you must first purify the surrounding area with Divine Light to eliminate all traces of evil. Upon activation, the divine energy inflicts a devastating 150 points of damage in all directions, which proves to be too much for your frail body to endure. Yes, my child if you did pick up -Hubris, Favor of Grieving Widow Set-, well remember I am God! Now Die, You Are Dead!\n")
                typingprint("   _____          __  __ ______    ______      ________ _____  \n")
                typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
                typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
                typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
                typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
                typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
                quit()
            elif player_hp == 300:
                player_hp += 500
                typingprint("Congratulations on solving the riddle! As the chest unlocks, the legendary weapon, --The Graviton Lance--, is revealed before you. However, to claim this mighty artefact, the chest unleashes a purifying wave of divine light that eradicates all traces of evil from its surroundings. Upon activation, the divine energy deals a devastating 150 points of Devine Blessing and receiving damage in all directions, empowered by the --Hubris, Favor of Grieving Widow-- Enchanted Set. With heads held high, you have obtained --The Graviton Lance--, and the hall resounds with the triumphant laughter of those deemed worthy. “Go forth, my child, and honor me with this tremendous mythical item, for only the most deserving can acquire such a powerful treasure.\n")
                typingprint("Your final HP is: " + str(player_hp))

    elif chest_choice == "2":
        typingprint("As the chest opens, a Nymph-like bull emerges, its presence captivating and fearsome. The room fills with haunting melodies, growing louder and more chaotic. It is Zionysus, the Chest guardian, embodying both grace and primal strength. Your heartbeat matches the dissonant rhythm, preparing you for the battle against Oblivilian's rage. With determination, you face the creature, ready to confront the clash of opposing forces.\n")

        dice_roll = random.randint(1, 100)
        typingprint("You rolled a dice and got: " + str(dice_roll))

        if dice_roll <= 50:
            typingprint("Unfortunately, your lacking of strength and consistency more; it is no wonder you death knock on your door. However, you are Dead for definite. But don't worry; you'll get there after serving in Tartarus! It's always good to remember that we all have room for improvement. Keep striving to be your best self, and you'll see progress quickly. Onward and upward, my friend! YOU ARE DEAD!\n")
            typingprint("   _____          __  __ ______    ______      ________ _____  \n")
            typingprint("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
            typingprint(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
            typingprint(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /\n")
            typingprint(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
            typingprint("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
            quit()
        else:
            typingprint(f"{name} Congratulations! You have emerged victorious against Zionysus and now have the opportunity to select another chest. Best of luck to you!.\n")
            new_chest_choice = input("Choose another chest to open (1 or 3): \n")
            play_game()  # Recursive call to play the game again with the new chest choice

    else:
        typingprint(f"{name} Have you learn basic maths? Please enter a valid chest number (1, 2, or 3).\n")

play_game() 


typingprint("   ____                           _____                  _   _                 \n")
typingprint("  / __ \                         / ____|                | | | |                \n")
typingprint(" | |  | |_   _  ___  ___ _ __   | (___   __ ___   ____ _| |_| |__  _   _ _ __  \n")
typingprint(" | |  | | | | |/ _ \/ _ \ '_ \   \___ \ / _` \ \ / / _` | __| '_ \| | | | '_ \ \n")
typingprint(" | |__| | |_| |  __/  __/ | | |  ____) | (_| |\ V / (_| | |_| | | | |_| | | | |\n")
typingprint(" \_____\_\\__,_|\___|\___|_| |_| |_____/ \__,_| \_/ \__,_|\__|_| |_|\__,_|_| |_|\n")
typingprint("-------------------------------------------------------------------------------------\n")
typingprint("Chapter 5\n") 
typingprint("Queen Savathun:\n")
typingprint("-------------------------------------------------------------------------------------\n")

class Fight(object):
  def enter(self):
    # typingprint ()
    typingprint ("A maddening Wail that goes, My dear son Crota, Son of Oryx, you will be avenged.\n")
    typingprint ("A Distant Mist glows and surface........\n")
   
    typingprint ("As Priest Tolund Owen summons the patron Gods, Boldy prepares to journey towards the ever-growing mist.  Toland’s staff slams with great force, uprooting the red-rimmed eye mist, glowing like coals on a fire.  You glance at the pitiful queen, wondering what the future holds.  Priest Tolund commands with authority, -Surrender Savathun, sink to your knees and beg for mercy, or you shall feel the grim of Tartarus for Eternity!- In a resounding show of defiance, the queen firmly declares her unwavering stance, stating - NEVER! Let it be known that no mortal shall ever defeat me. With her talisman raised high, she begins to incant, calling forth the dark and mysterious realms of Death.  What will happen next?  Only time will tell.\n")
    typingprint (f"THE EPIC SHOWDOEN EVIL QUEEN SAVATHUM VS {name}\n")
    
    your_hit_points = 20
    queen_hit_points = 6
    
    queen = True
    
    while your_hit_points > 0 and (queen):
    #   typingprint ("\n", "-" * 10)
      your_attack = random.randint(4,12)
      queen_attack = random.randint(2,4)
   
      attack = int(input("Type 1 to attack QUEEN or Type 2 that QUEEN attacks you >\n"))
   
      if attack == 1:
        if queen:
          queen_hit_points = queen_hit_points - your_attack
          typingprint ("You hit QUEEN for %d hit points." % your_attack)
          if queen_hit_points <= 0:
            queen = False
            typingprint ("You step into the attack, and the Queen beaks off and enters a she-pup, anxious for her offspring. The retreat, you advance, bloodies but not beaten, you trust the -The Graviton Lance- shouting, -Behold, the vanquished darkness lies slain, Its monstrous reign forever in chains.- You bring low the Queen, unstringing the force that binds it's mighty sinews, with Queen Savathun one last Scream Echoes of despair, silenced at last, Evils demise, a defeated blast. My Leige Forgive Me Queen Savathun is defeated. You are victorious.\n")
        else:
            typingprint ("You step into the attack, and the Queen beaks off and enters a she-pup, anxious for her offspring. The retreat, you advance, bloodies but not beaten, you trust the -The Graviton Lance- shouting, -Behold, the vanquished darkness lies slain, Its monstrous reign forever in chains.- You bring low the Queen, unstringing the force that binds it's mighty sinews, with Queen Savathun one last Scream Echoes of despair, silenced at last, Evils demise, a defeated blast. My Leige Forgive Me Queen Savathun is defeated. You are victorious.\n")


      if queen:
        your_hit_points = your_hit_points - queen_attack
        typingprint ("QUEEN hits you for %d points, you have %d"
           " hit points left." %(queen_attack, your_hit_points))
        if your_hit_points <= 0:
          typingprint ("Felled by the Treacherous blow in the death chambers of Queen Savathun, your noble companion Priest Tolund Owen was slain in her Death. The spirit of -The Graviton Lance-, your ancestors cry. from the hall of Never Ever Knowing. The defeat voyage and the demise of the scourge threaten the survival of Throne World of Neomuna. You are Dead! You have brought shame to the kingdom.\n")
          break


a_fight = Fight()
a_fight.enter()


typingprint("  _______ _                           __          __        _     _                                                                    \n")
typingprint(" |__   __| |                          \ \        / /       | |   | | \n")
typingprint("    | |  | |__  _ __ ___  _ __   ___   \ \  /\  / /__  _ __| | __| | \n")
typingprint("    | |  | '_ \| '__/ _ \| '_ \ / _ \   \ \/  \/ / _ \| '__| |/ _` | \n")
typingprint("    | |  | | | | | | (_) | | | |  __/    \  /\  / (_) | |  | | (_| | \n")
typingprint("    |_|  |_| |_|_|  \___/|_| |_|\___|     \/  \/ \___/|_|  |_|\__,_| \n")
typingprint("------------------------------------------------------------------------------\n")
typingprint("Chapter 6\n")
typingprint("Kingdom of Throne world :\n")
typingprint("------------------------------------------------------------------------------\n")

typingprint("With the return of Thorne Schulze Castle to the Kingdom of Throne world, Priest Tolund Owen he was emerged as the revered guardian of the mythical Graviton Lance. His unwavering faith and wisdom united the kingdom, guiding them with teachings of compassion and justice. The castle resonated with sacred energy under his watchful presence. Generation after generation sought his counsel, inspired by his devotion. Songs and legends immortalised his noble deeds, forever intertwining his legacy with the castle. Priest Tolund Owen's unwavering belief in the Graviton Lance symbolised the bond between faith and power. His name echoed through history, celebrated as a paragon of righteousness. With his guidance, Thorne Schulze Castle and the Graviton Lance illuminated a future filled with unity and prosperity for the Kingdom of Throne world.\n")
typingprint("Long live Kingdom of Throne world\n")
typingprint(".........THE END.........\n")
print("\n")

typingprint("  _ _   _______ _            _____      _                       ____   __   _______ _            _____             _      ____       _                 _ _  \n")
typingprint(" ( | ) |__   __| |          |  __ \    | |                     / __ \ / _| |__   __| |          |  __ \           | |    |  _ \     | |               ( | )\n")
typingprint("  V V     | |  | |__   ___  | |__) |___| |_ _   _ _ __ _ __   | |  | | |_     | |  | |__   ___  | |  | | __ _ _ __| | __ | |_) | ___| | _____      __  V V \n")
typingprint("          | |  | '_ \ / _ \ |  _  // _ \ __| | | | '__| '_ \  | |  | |  _|    | |  | '_ \ / _ \ | |  | |/ _` | '__| |/ / |  _ < / _ \ |/ _ \ \ /\ / /      \n")
typingprint("          | |  | | | |  __/ | | \ \  __/ |_| |_| | |  | | | | | |__| | |      | |  | | | |  __/ | |__| | (_| | |  |   <  | |_) |  __/ | (_) \ V  V /       \n")
typingprint("          |_|  |_| |_|\___| |_|  \_\___|\__|\__,_|_|  |_| |_|  \____/|_|      |_|  |_| |_|\___| |_____/ \__,_|_|  |_|\_\ |____/ \___|_|\___/ \_/\_/        \n")
typingprint("Up Comming\n")
typingprint("The Return of the The Dark Bellow\n")
typingprint("December 2023\n")
typingprint("Olawale Ajayi , Pedram Aman , Tyler Beard-Owens , Zi Yun (Joanne) Liaw, Nazeer Rahimi - 28 June 2023 22:22\n") 
def end_game():
    typingprint("The Rock Stars - Olawale Ajayi, Pedram Aman, Tyler Beard-Owens, Zi Yun (Joanne) Liaw, Nazeer Rahimi - 28th June 2023 22:22 \n")
    typingprint("\n")
    typingprint('''                          ,-.
                                          _.|  '
                                        .'  | /
                                      ,'    |'
                                     /      /
                       _..----""---.'      /
 _.....---------...,-""                  ,'
 `-._  \                                /
     `-.+_            __           ,--. .
          `-.._     .:  ).        (`--"| 
               7    | `" |         `...'  
               |     `--'     '+"        ,". ,""-
               |   _...        .____     | |/    '
          _.   |  .    `.  '--"   /      `./     j
         \' `-.|  '     |   `.   /        /     /
         '     `-. `---"      `-"        /     /
          \       `.                  _,'     /
           \        `                        .
            \                                j
             \                              /
              `.                           .
                +                          
                |                           L
                |                           |
                |  _ /,                     |
                | | L)'..                   |
                | .    | `                  |
                '  \'   L                   '
                 \  \   |                  j
                  `. `__'                 /
                _,.--.---........__      /
               ---.,'---`         |   -j"
                .-'  '....__      L    |
              ""--..    _,-'       \ l||
                  ,-'  .....------. `||'
               _,'                /
             ,'                  /
            '---------+-        /
                     /         /
                   .'         /
                 .'          /
               ,'           /
             _'....----""""" ''')
    typingprint('''
  .▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
  ─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█\n''')
    
    typingprint("\n")
    typingprint("Look out for Pokomon - The Return of the Dark Below\n")
    typingprint("Showcase this Christmas 2023\n")
    typingprint("\n")
end_game()
