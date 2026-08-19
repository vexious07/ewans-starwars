import os
import time
import random
from player_info import Player_info
run = True
main_menu = True
username = False
class_selection = False
play = False
rules = False
key = False
standing = True
in_battle = False
faction = False
totalstep = 0
step = 0 
level = 1

hp = 100 
maxhp = 100
mp = 100
maxmp = 100
gold = 0
Str = 0
Dex = 0
Def = 0
Int = 0 
Cha = 0
weapon = ""
chosenrace = ""
y = 0
x = 0

def start_page_art():
    print("==========================")
    print("ASCII STAR WARS ROGUELITE")
    print("==========================")

def style():
    print("==========================")

def clearsceen():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )

def battle():
    global hp, gold

    enemy = random.choice(e_list)

    enemy_hp = mobs[enemy]["hp"]
    enemy_maxhp = enemy_hp
    enemy_atk = mobs[enemy]["at"]
    reward = mobs[enemy]["go"]

    print(f"\nA wild {enemy} appeared!")

    while enemy_hp > 0 and hp > 0:

        print("----------------")
        print(enemy)
        print(f"Enemy HP: {enemy_hp}/{enemy_maxhp}")
        print(f"Your HP : {hp}/{maxhp}")
        print("----------------")
        print("1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":
            damage = Str / 3
            enemy_hp -= damage

            print(f"You hit the {enemy} for {damage} damage!")

            if enemy_hp <= 0:
                print(f"You defeated the {enemy}!")
                gold += reward
                print(f"You gained {reward} Galactic Credit Standards!")
                gold += reward
                for x in range(0, 2):
                    level_up()
                clearsceen()
                break

            hp -= enemy_atk
            print(f"The {enemy} attacks for {enemy_atk} damage!")
            clearsceen()
            if hp <= 0:
                print("You were defeated!")
                quit()

        elif choice == "2":
           if random.randint(1, 100) >= 50:
            print("You escaped!")
            clearsceen()
            break

        else:
            print("Invalid choice.")

def level_up():
    global level, Str, Dex, Def, Int, Cha, maxhp, maxmp

    level += 1
    Str += 3
    Dex += 3
    Def += 3
    Int += 3
    Cha += 3
    maxhp += 10
    maxmp += 10

    print(f"\nCongratulations! You've reached level {level}!")
    print("Your stats have increased:")
    print(f"Strength: {Str}")
    print(f"Dexterity: {Dex}")
    print(f"Defense: {Def}")
    print(f"Intelligence: {Int}")
    print(f"Charisma: {Cha}")
    print(f"Max HP: {maxhp}")
    print(f"Max MP: {maxmp}")


def boss():
    global hp, gold

    enemy = "Dragon"

    enemy_hp = mobs[enemy]["hp"]
    enemy_maxhp = enemy_hp
    enemy_atk = mobs[enemy]["at"]
    reward = mobs[enemy]["go"]

    print(f"\nA wild {enemy} appeared!")

    while enemy_hp > 0 and hp > 0:

        print("----------------")
        print(enemy)
        print(f"Enemy HP: {enemy_hp}/{enemy_maxhp}")
        print(f"Your HP : {hp}/{maxhp}")
        print("----------------")
        print("1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":
            damage = Str / 3
            enemy_hp -= damage

            print(f"You hit the {enemy} for {damage} damage!")

            if enemy_hp <= 0:
                print(f"You defeated the {enemy}!")
                gold += reward
                print(f"You gained {reward} Galactic Credit Standards!")
                gold += reward
                for x in range(0, 4):
                    level_up()
                clearsceen()
                break

            hp -= enemy_atk
            print(f"The {enemy} attacks for {enemy_atk} damage!")
            clearsceen()
            if hp <= 0:
                print("You were defeated!")
                quit()

        elif choice == "2":
           if random.randint(1, 100) >= 50:
            print("You escaped!")
            clearsceen()
            break

        else:
            print("Invalid choice.")

def shop():

    style()
    print("Welcome to the shop!")
    style()
    print("You have", gold, "Galactic Credit Standards.")
    style()
    available_items = random.sample(list(shop_items.keys()), k=min(3, len(shop_items)))

    for index, item_name in enumerate(available_items, start=1):
        item = shop_items[item_name]
        print(f"{index}. Buy {item['name']} ({item['price']} GCS)")

    print("4. Exit Shop")
    buy_choice = input("> ")
    if buy_choice in ["1", "2", "3"]:
        item_index = int(buy_choice) - 1
        if item_index < len(available_items):
            item_name = available_items[item_index]
            item = shop_items[item_name]
            if gold >= item["price"]:
                gold -= item["price"]
                print(f"You bought {item['name']} for {item['price']} GCS.")
            else:
                print("You don't have enough Galactic Credit Standards.")
    else:
        print("Exiting the shop.")
        play = True
#        x = 0        x = 1        x = 2         x = 3          x = 4         x = 5             x = 6
map = [["plains",    "plains",    "plains",     "plains",      "forest",     "mountains",         "cave",], # y = 0
       ["forest",    "forest",    "forest",     "forest",      "forest",     "hills",         "mountains",], # y = 1
       ["forest",    "feilds",    "bridge",     "plains",      "hills",     "forest",           "hills",], # y = 2
       ["plains",    "shop",       "town",      "major",       "plains",     "hills",         "mountains",], # y = 3
       ["plains",    "feilds",    "feilds",     "plains",      "hills",     "mountains",       "mountains",]] # y = 4

y_len = len(map)-1
x_len = len(map[0])-1


e_list = ["Goblin", "Orc", "Slime"]
shop_item = ["Health Potion", "Mana Potion", "Compass", "Random key"]
shop_items = {
    "Health Potion": {
        "price": 10,
        "name": "Health Potion",
    },
    "Mana Potion": {
        "price": 10,
        "name": "Mana Potion",
    },
    "Compass": {
        "price": 25,
        "name": "Compass",
    },
    "Random key": {
        "price": 100,
        "name": "Random key",
    }
}

mobs = {
    "Goblin":{
        "hp": 15,
        "at": 3,
        "go": 8
    },
     "Orc":{
        "hp": 35,
        "at": 5,
        "go": 18
    },
     "Slime":{
        "hp": 30,
        "at": 2,
        "go": 12
    },
     "Dragon":{
        "hp": 100,
        "at": 8,
        "go": 100
    }
}

biome = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "feilds": {
        "t": "FEILDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "major": {
        "t": "MAJOR",
        "e": False},
    "cave": {
        "t": "Cave",
        "e": False},
    "mountains": {
        "t": "MOUNTAINS",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True},
}

factionsgoals = {
    "Jedi": {
        "signature": "Force",
        "goal": " find peace"
    },
    "Sith": {
        "signature": "Force",
        "goal": "Rule-it-all"
    },
    "Mandalorian": {
        "signature": "Blaster",
        "goal": "Be the richest"
    }
}

while run:
    while main_menu:
        start_page_art()
        print("1. Play")
        print("2. continue")
        print("3. Quit")
        style()
        choice = input("> ")

       
        if choice == "1":
            main_menu = False
            username = True
        
        elif choice == "2":
            if "save" in globals():
                name = save.name
                hp = save.hp
                maxhp = save.maxhp
                mp = save.mp
                maxmp = save.maxmp
                gold = save.gold
                weapon = save.weapon
                chosenrace = save.chosenrace

                print("Welcome back", save.name)

                play = True
                main_menu = False
            else:
                print("No save found.")
                time.sleep(2)
                        
        elif choice == "3":
            run = False
            break
       
    while username:
        clearsceen()
        style()

        name = input("Please enter your player name: ")

        if len(name) > 1:
            confirm = input(f"Are you sure {name} is your name? (yes/no): ")

            if confirm.lower() == "yes":
                username = False
                class_selection = True
        else:
            print("Your username should be greater than 1 character.")
    
    while class_selection:
        clearsceen()
        print("-------------------------")
        print("Race Selector")
        print("--------------------------")
        print("welcome ",name,", this is the race selector")
        time.sleep(3)
        print("You get to select one of these races")
        print("1. Human")
        print("2. Droid")
        print("3. Wookie")
        print("4. Zabrak")
        print("5. Rodian")
        print("6. Togruta")
        race = input("> ")
        if race == "1":
            print("you have selected the Human race")
            chosenrace = "Human"
            hp = 50
            maxhp = 50
            Str = 50 
            Dex = 50
            Def = 50
            Int = 50
            Cha = 50
            class_selection = False
            faction = True
        elif race == "2":
            print("you have selected the Droid race")
            chosenrace = "Droid"
            hp = 50
            maxhp = 50
            Str = 75
            Dex = 50
            Def = 60
            Int = 30
            Cha = 10
            class_selection = False
            faction = True
        elif race == "3":
            print("you have selected the Wookie race")
            chosenrace = "Wookie"
            hp = 50
            maxhp = 50
            Str = 75
            Dex = 50
            Def = 60
            Int = 30
            Cha = 10
            class_selection = False
            faction = True
        elif race == "4":
            print("you have selected the Zabrak race")
            chosenrace = "Zabrak"
            hp = 40
            maxhp = 40
            Str = 65
            Dex = 50
            Def = 40
            Int = 45
            Cha = 50
            class_selection = False
            faction = True
        elif race == "5":
            print("you have selected the Rodian race")
            chosenrace = "Rodian"
            hp = 50
            maxhp = 50
            Str = 40
            Dex = 30
            Def = 35
            Int = 30
            Cha = 60
            class_selection = False
            faction = True
        elif race == "6":
            print("you have selected the Togruta race")
            chosenrace = "Togruta"
            hp = 50
            maxhp = 50
            Str = 55
            Dex = 70
            Def = 40
            Int = 50
            Cha = 50
            class_selection = False
            faction = True
        else:
            print("invalid choice")
    while faction:
        clearsceen()
        print("-------------------------")
        print("Faction Selector")
        print("--------------------------")
        print("welcome ",name,", this is the faction selector")
        time.sleep(3)
        print("You get to select one of these factions")
        print("1. Jedi")
        print("2. Sith")
        print("3. Mandalorian")
        print("4. Agnostic")
        race = input("> ")
        if race == "1":
            print("you have selected the Jedi faction")
            chosenfaction = "Jedi"
            Int = Int + 5
            weapon = "Lightsaber"
            faction = False
            play = True
        elif race == "2":
            print("you have selected the Sith faction")
            chosenfaction = "Sith"
            Str = Str + 5
            weapon = "Force"
            faction = False
            play = True
        elif race == "3":
            print("you have selected the Mandalorian faction")
            chosenfaction = "Mandalorian"
            Dex = Dex + 5
            weapon = "Blaster"
            faction = False
            play = True
        elif race == "4":
            print("you have selected the Agnostic faction")
            chosenfaction = "Agnostic"
            weapon = "Blaster"
            faction = False
            play = True
        
        else:
            print("invalid choice")

    while play:
        clearsceen()
        if biome[map[y][x]]["e"]:
            if random.randint(0, 100) <= 30:
                battle()
        if map[y][x] == "shop":
            shop()
        if step == 5:
            step = 0
            gold += 25
        if totalstep == 200:
            boss()
        style()
        print("LOCATION: " + biome[map[y][x]]["t"])
        style()
        print("Goals: " + factionsgoals[chosenfaction]["goal"])
        print("Name: " + name)
        print("Level: " + str(level))
        print("HP: " + str(hp) + "/" + str(maxhp))
        print("MP: " + str(mp) + "/" + str(maxmp) )
        print("Current Weapon: " + weapon)
        print("CLASS: " + chosenrace)
        print("Galactic Credit Standards: " + str(gold))
        print("0: SAVE & QUIT")
        if y > 0:
            print("1 NORTH")
        if x < x_len:
            print("2 EAST")
        if y < y_len:
            print("3 SOUTH")
        if x > 0:
            print("4 WEST")

        destination = input("> ")
        if destination == "0":
            save = Player_info(name,hp,maxhp,mp,maxmp,gold,weapon,chosenrace)
            # print(save.name)
            # print(save.hp)
            # print(save.maxhp)
            # print(save.mp)
            # print(save.maxmp)
            # print(save.gold)
            # print(save.weapon)
            # print(save.chosenrace)
            print("GOOD BYE", save.name)
            clearsceen()
            play = False
            main_menu = True

        elif destination == "1":
            step += 1
            totalstep += 1
            if y > 0:
                y -= 1
                    
                
        elif destination == "2":
            step += 1
            totalstep += 1
            if x < x_len:
                x += 1
                
        elif destination == "3":
            step += 1
            totalstep += 1
            if y < y_len:
                y += 1
                
        elif destination == "4":
            step += 1
            totalstep += 1
            if x > 0:
                x -= 1
else:
    quit