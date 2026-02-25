print("***The Adventure Game BETA***")
print("Created by: Patrik and Aiden")
print("Note: This game does not have a save feature yet")
print("You wake up in a field in the middle of nowhere...") 


## Core Mechanics
# These are the core mechanics of the game, they will be used in every area of the game

health = 10
stamina = 10
maxhealth = 10
maxstamina = 10
XP = 0
Level = 1
money = 0
player_inventory = ["Map"]
if health <= 0:
    print("You have fallen and never woke up again. Game Over.")
    exit()

def LevelUp():
    global Level, XP, maxhealth, maxstamina, health, stamina
    if XP >= 25:
        Level = Level + 1
        XP = XP - 25
        maxhealth = maxhealth + 2
        maxstamina = maxstamina + 2
        health = maxhealth
        stamina = maxstamina
        print("[[[[[***  Congratulations! You have leveled up to level ", Level, " your health and stamina have been fully restored and your maximum health and stamina have increased by 2! ***]]]]]")

def debug():
    debug = True
    while debug == True:
            
        print("Debug enabled...")
        print("ONE use per activation")
        debuginput = input("cmd//> ")
        if debuginput in ("DEBUG_OFF"):
            debug = False
        elif debuginput in ("goToVillage"):
            village()

def addToInventory(item):
    player_inventory.append(item)
    print("You have added", item, "to your inventory.")

def inventory():
    global player_inventory, health, stamina, maxhealth, maxstamina
    print("You have: ")
    for item in player_inventory:
                    print("-", item)
    check = input("Do you want to use anything? ")
    if check in ("Map" , "map"):
                        if "Map" in player_inventory: 
                            print("A map of Wildwood, It has the regions Kamaranda, Tigerclaw and Formandi, a piece of the map is ripped off")
                            return
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Old sword" , "old sword" , "Sword" , "sword"):
                        if "Old sword" in player_inventory:
                            print("An old rusty sword, not the best weapon in the world but will do so in a pinch")
                            return
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Shield" , "shield"):
                        if "Shield" in player_inventory:
                            print("A standard edition shield, if you didn't know already, its made of metal and is pretty heavy")
                            return
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Worn dagger" , "worn dagger" , "Dagger" , "dagger"):
                        if "Dagger" in player_inventory:
                            print("A small dagger, favorited by assassins that hide in hay carts")
                            return
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Ale" , "ale"):
                        if "Ale" in player_inventory:
                            print("A bottle of ale, it has a bitter and fruity taste, it is a little bit refreshing and can help you relax")
                            print("Restores 1 health and 1 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                stamina = stamina + 1
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Ale")
                                print("You drink the ale")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the ale")
                                return
                                  
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Wine" , "wine"):
                        if "Wine" in player_inventory:
                            print("A bottle of wine, it has a sweet and fruity taste, it makes you feel fancy at dinner parties")
                            print("Restores 2 health and 1 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 2
                                stamina = stamina + 1
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Wine")
                                print("You drink the wine")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the wine")
                                return
                                  
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Whiskey" , "whiskey"):
                        if "Whiskey" in player_inventory:
                            print("A bottle of whiskey, it has a strong and smoky taste, it has notes of vanilla and toasted oak")
                            print("Restores 3 health and 2 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 3
                                stamina = stamina + 2
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Whiskey")
                                print("You drink the whiskey")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the whiskey")
                                return
                                  
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Rum" , "rum"):
                        if "Rum" in player_inventory:
                            print("A bottle of rum, it has a sweet and strong taste, it can be drunk as is or put into chocolate to give it a ZING!")
                            print("Restores 4 health and 3 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 4
                                stamina = stamina + 3
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Rum")
                                print("You drink the rum")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the rum")
                                return
                                  
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Vodka" , "vodka"):
                        if "Vodka" in player_inventory:
                            print("A bottle of vodka, it has a strong and powerful taste, it gives you a strong buzz and a warm feeling in your stomach")
                            print("Restores 5 health and 4 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 5
                                stamina = stamina + 4
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Vodka")
                                print("You drink the vodka")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the vodka")
                                return
                                  
                        else:
                            print("You do not have that item")
                            return
    elif check in ("Water" , "water"):
                        if "Water" in player_inventory:
                            print("A bottle of water, it has a refreshing and clean taste, it is essential for survival and can help you stay hydrated, it has the potential to be made into many things but for now it's just water")
                            print("It has no effects on your stats but it is refreshing and can be used in crafting and cooking")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                player_inventory.remove("Water")
                                print("You drink the water")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the water")
                                return
                        else:
                            print("You do not have that item")
                            return

    elif check in ("Health potion" , "health potion"):
                        if "Health potion" in player_inventory:
                            print("A health potion, it has a bright red color and a sweet taste, it is used to restore health and can be very useful in combat")
                            print("Restores 5 health")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 5
                                health = min(health, maxhealth)
                                player_inventory.remove("Health potion")
                                print("You drink the health potion")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the health potion")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Stamina potion" , "stamina potion"):
                        if "Stamina potion" in player_inventory:
                            print("A stamina potion, it has a bright blue color and a sweet taste with the taste of energy so powerful great Elder Sebastian would argue with, it is used to restore stamina and can be very useful in combat")
                            print("Restores 5 stamina")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                stamina = stamina + 5
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Stamina potion")
                                print("You drink the stamina potion")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the stamina potion")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Bread" , "bread"):
                        if "Bread" in player_inventory:
                            print("A loaf of bread, it has a soft and fluffy texture with a slightly sweet taste, it is a staple food for any adventurer and can be used to restore health in a pinch")
                            print("Restores 2 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 2
                                health = min(health, maxhealth)
                                player_inventory.remove("Bread")
                                print("You eat the bread")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the bread")
                                return
                        else:
                            print("You do not have that item")
                            return
                            
    elif check in ("Apple" , "apple"):
                        if "Apple" in player_inventory:
                            print("A red apple, it has a crisp and juicy texture with a sweet and slightly tart taste, it is a healthy snack that can be used to restore health in a pinch")
                            print("Restores 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                health = min(health, maxhealth)
                                player_inventory.remove("Apple")
                                print("You eat the apple")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the apple")
                                return
                        else:
                            print("You do not have that item")
                            return
                        
    elif check in ("Cheese" , "cheese"):
                        if "Cheese" in player_inventory:
                            print("A block of cheese, it has a creamy and smooth texture with a mild and slightly tangy taste, it is a good source of protein and can be used to restore health in a pinch")
                            print("Restores 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                health = min(health, maxhealth)
                                player_inventory.remove("Cheese")
                                print("You eat the cheese")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the cheese")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Milk" , "milk"):
                        if "Milk" in player_inventory:
                            print("A bottle of milk, it has a smooth and creamy texture with a slightly sweet taste, it is a good source of calcium and can be used to restore health in a pinch")
                            print("Restores 1 health")
                            drink = input("Do you want to drink it? ")
                            if drink in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                health = min(health, maxhealth)
                                player_inventory.remove("Milk")
                                print("You drink the milk")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to drink the milk")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Eggs" , "eggs"):
                        if "Eggs" in player_inventory:
                            print("A small pack of eggs, they have a smooth and hard texture with a slightly sweet taste, they are a good source of protein but should not be eaten raw unless you want to try your chances with food poisoning")
                            print("Can drain 1 health if eaten raw but can restore 2 health if cooked")
                            eat = input("Do you want to eat them? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Eggs")
                                print("You eat the eggs")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the eggs")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Sweets" , "sweets"):
                        if "Sweets" in player_inventory:
                            print("A bag of sweets, they have a chewy and soft texture with a sweet and fruity taste, they are a good source of sugar and can be used to restore stamina in a pinch")
                            print("Restores 2 stamina")
                            eat = input("Do you want to eat them? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                stamina = stamina + 2
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Sweets")
                                print("You eat the sweets")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the sweets")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Biscuits" , "biscuits"):
                        if "Biscuits" in player_inventory:
                            print("A pack of biscuits, they have a crunchy and crumbly texture with a sweet and buttery taste, they are a good source of carbohydrates and can be used to restore stamina in a pinch")
                            print("Restores 2 stamina")
                            eat = input("Do you want to eat them? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                stamina = stamina + 2
                                stamina = min(stamina, maxstamina)
                                player_inventory.remove("Biscuits")
                                print("You eat the biscuits")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the biscuits")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Tomatoes" , "tomatoes"):
                        if "Tomatoes" in player_inventory:
                            print("A basket of tomatoes, they have a juicy and soft texture with a sweet and slightly tangy taste, they are a good source of vitamins and can be used to restore health in a pinch")
                            print("Restores 1 health")
                            eat = input("Do you want to eat them? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                health = min(health, maxhealth)
                                player_inventory.remove("Tomatoes")
                                print("You eat the tomatoes")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the tomatoes")
                                return
                        else:
                            print("You do not have that item")
                            return
                        
    elif check in ("Beans" , "beans"):
                        if "Beans" in player_inventory:
                            print("A humble bag of dried beans, they have a soft and mushy texture with a savory and slightly sweet taste, they are a good source of protein and can be used to restore health in a pinch, but can be cooked into a dish to restore more health")
                            print("Restores 1 health")
                            eat = input("Do you want to eat them? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health + 1
                                health = min(health, maxhealth)
                                player_inventory.remove("Beans")
                                print("You eat the beans")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the beans")
                                return
                            
    elif check in ("Beef" , "beef"):
                        if "Beef" in player_inventory:
                            print("A slab of raw beef packaged in butcher paper, it has a tender and juicy texture with a rich and savory taste, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Beef")
                                print("You eat the beef, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the beef")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Fish" , "fish"):
                        if "Fish" in player_inventory:
                            print("A whole raw fish, it has a tender and flaky texture with a mild and slightly sweet taste, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Fish")
                                print("You eat the fish, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the fish")
                                return
    
    elif check in ("Pork" , "pork"):
                        if "Pork" in player_inventory:
                            print("A slab of raw pork packaged in butcher paper, it has a tender and juicy texture with a rich and savory taste when cooked, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Pork")
                                print("You eat the pork, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the pork")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Chicken" , "chicken"):
                        if "Chicken" in player_inventory:
                            print("A whole raw chicken, it has a tender and juicy texture with a mild and slightly sweet taste when cooked, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Chicken")
                                print("You eat the chicken, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the chicken")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Lamb" , "lamb"):
                        if "Lamb" in player_inventory:
                            print("A slab of raw lamb packaged in butcher paper, it has a tender and juicy texture with a rich and savory taste when cooked, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Lamb")
                                print("You eat the lamb, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the lamb")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Sausage" , "sausage"):
                        if "Sausage" in player_inventory:
                            print("A raw sausage, it has a tender and juicy texture with a rich and savory taste when cooked, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Sausage")
                                print("You eat the sausage, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the sausage")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Bacon" , "bacon"):
                        if "Bacon" in player_inventory:
                            print("A tied stack of raw bacon rashers, it has a crispy and crunchy texture with a rich and savory taste when cooked, it is a good source of protein but can only be eaten safely if cooked, or you'll suffer the wrath of food poisoning")
                            print("Drains 1 health")
                            eat = input("Do you want to eat it? ")
                            if eat in ("Yes" , "yes" , "Y" , "y"):
                                health = health - 1
                                health = max(health, 0)
                                player_inventory.remove("Bacon")
                                print("You eat the bacon, it was raw and you got food poisoning, you lose 1 health")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                                return
                            else:
                                print("You decide not to eat the bacon")
                                return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Rope" , "rope"):
                        if "Rope" in player_inventory:
                            print("A sturdy rope, it is made of hemp and can be used for climbing, tying things up, or even as a makeshift weapon in a pinch")
                            return
                        else:
                            print("You do not have that item")
                            return
    
    elif check in ("Soap" , "soap"):
                        if "Soap" in player_inventory:
                            print("A bar of soap, it has a clean and fresh scent, it can be used to clean yourself or your equipment")
                            return
                        else:
                            print("You do not have that item")
                            return
             
    elif check in ("Lantern" , "lantern"):
                        if "Lantern" in player_inventory:
                            print("A lantern, it has a sturdy metal frame and a glass enclosure to protect the flame, it can be used to light up dark areas and can be very useful in caves or dungeons")
                            return
                        else:
                            print("You do not have that item")
                            return
    else:
                        print("That item doesn't exist in this universe")
                        return

# This is a village in the starting area of the game, this area does not have any connections to other areas yet

blacksmith_looted = False

def village():
    global health, stamina, money, inventory , maxhealth, maxstamina , XP , Level , blacksmith_looted

    while True:    
            
        
        print("You walk to the village and find out it's abandoned, there is a blacksmith shop, a tavern, a general store, and an inn")
        answervill = input("What do you do now? ")    
        
        if answervill in ("Leave" , "leave" , "Go back" , "go back"):
                print("There is not much of a point in going back")


        if answervill in ("Enter blacksmith" , "enter blacksmith" , "Go to blacksmith" , "go to blacksmith"):
            
            while True:
            
                print("You enter the blacksmith shop, it's completely abandoned...")
                if blacksmith_looted == True:
                    print("You already looted the blacksmith, there is nothing else to find")
                    print("Do you want to leave the blacksmith?")
                    leaveblacksm = input("Leave blacksmith? ")
                    if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                        print("You leave the blacksmith shop")
                        village()
                    else:
                        print("You stay in the blacksmith shop")
                        answerblacksm2 = input("What do you do now? ")
                        if answerblacksm2 in ("Look around" , "look around" , "Search" , "search" , "Search the blacksmith" , "search the blacksmith"):
                            print("You already searched the blacksmith, there is nothing else to find")
                            print("Do you want to leave the blacksmith?")
                            leaveblacksm = input("Leave blacksmith? ")
                            if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                                print("You leave the blacksmith shop")
                                village()
                            else:
                                print("You stay in the blacksmith shop")
                                answerblacksm2       
                answerblacksm = input("What do you do here? ")                    
                if answerblacksm in ("Look around" , "look around" , "Search" , "search" , "Search the blacksmith" , "search the blacksmith"):
                                print("You do find an Old sword , a Shield and a Dagger on the counter, as well as ξ25 in the cash register")
                                pickup = input("Do you want to pick them up? ")
                                if pickup in ("Yes" , "yes" , "Y" , "y"):
                                    addToInventory("Old sword")
                                    addToInventory("Shield")
                                    addToInventory("Dagger")
                                    money = money + 25
                                    print("You obviously take the money as well, you now have ξ" , money) 
                                    print("Do you want to leave the blacksmith?")
                                    leaveblacksm = input("Leave blacksmith? ")
                                    if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                                        print("You leave the blacksmith shop")
                                        blacksmith_looted = True
                                        village()
                                    else:
                                        print("You stay in the blacksmith shop")
                                        answerblacksm2 = input("What do you do now? ")
                                        if answerblacksm2 in ("Look around" , "look around" , "Search" , "search" , "Search the blacksmith" , "search the blacksmith"):
                                            print("You already searched the blacksmith, there is nothing else to find")
                                            print("Do you want to leave the blacksmith?")
                                            leaveblacksm = input("Leave blacksmith? ")
                                            if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                                                print("You leave the blacksmith shop")
                                                village()
                                            else:
                                                print("You stay in the blacksmith shop")
                                                answerblacksm2
                                else:
                                    print("You leave the items on the counter")
                                    print("Do you want to leave the blacksmith?")
                                    leaveblacksm = input("Leave blacksmith? ")
                                    if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                                        print("You leave the blacksmith shop")
                                        village()
                                    elif leaveblacksm in ("No" , "no" , "N" , "n"):
                                        print("You stay in the blacksmith shop")
                                        answerblacksm3 = input("What do you do now? ")
                                        if answerblacksm3 in ("Look around" , "look around" , "Search" , "search" , "Search the blacksmith" , "search the blacksmith"):
                                            print("You already searched the blacksmith, there is nothing else to find")
                                            print("Do you want to leave the blacksmith?")
                                            leaveblacksm = input("Leave blacksmith? ")
                                            if leaveblacksm in ("Yes" , "yes" , "Y" , "y"):
                                                print("You leave the blacksmith shop")
                                                village()
                                            else:
                                                print("You stay in the blacksmith shop")
                                                answerblacksm3 

                                if answerblacksm in ("Leave" , "leave" , "Exit" , "exit"):
                                    print("You leave the blacksmith shop")
                                    village()
        
                
        if answervill in ("Enter tavern" , "enter tavern" , "Go to tavern" , "go to tavern"):
            print("You enter the tavern, there is a bartender and a few patrons, as well as an angry drunkard")

            while True:
                    
                    answertav = input("What do you do here? ")
                    if answertav in ("Talk to bartender" , "talk to bartender"):
                        print("The bartender sympathizes with you and tells you that the village has been abandoned for a while, he says that the villagers left because of a monster that has been terrorizing the \nvillage, he also says that the monster is very strong and that you should be careful if you decide to go out and fight it")
                    elif answertav in ("Talk to patrons" , "talk to patrons"):
                        print("The patrons are all very drunk and don't have much to say, they just mumble incoherently and occasionally shout something about \'a monster\'")
                    elif answertav in ("Order a drink" , "order a drink" , "Buy a drink" , "buy a drink"):
                        print("The options are:")
                        print("-Ale: 2ξ")
                        print("-Wine: 3ξ")
                        print("-Whiskey: 5ξ")
                        print("-Rum: 7ξ")
                        print("-Vodka: 10ξ")
                        print("-Water: Free!")
                        print("You have ξ" , money)
                        order = input("What do you want to order?")
                        if order in ("Ale" , "ale"):                          
                            if money >= 2:
                                money = money - 2
                                choice = input("You order an ale, do you want to drink it? ")
                                if choice in ("Yes" , "yes" , "Y" , "y"):
                                    print("You drink the ale and feel a little bit better")
                                    health = health + 1
                                    stamina = stamina + 1
                                    health = min(health, maxhealth)
                                    stamina = min(stamina, maxstamina)
                                    print("Your health is now ", health, " and your stamina is now ", stamina)
                                else:
                                    print("You ask the bartender to bottle the ale for you, it goes into your inventory")
                                    addToInventory("Ale")
                            else:
                                print("You don't have enough money to buy that")
                        if order in ("Wine" , "wine"):
                            if money >= 3:
                                money = money - 3
                                choice = input("You order a wine, do you want to drink it? ")
                                if choice in ("Yes" , "yes" , "Y" , "y"):
                                    print("You drink the wine and feel a little bit better")
                                    health = health + 2
                                    stamina = stamina + 1
                                    health = min(health, maxhealth)
                                    stamina = min(stamina, maxstamina)
                                    print("Your health is now ", health, " and your stamina is now ", stamina)
                                else:
                                    print("You ask the bartender to bottle the wine for you, it goes into your inventory")
                                    addToInventory("Wine")
                            else:
                                print("You don't have enough money to buy that")
                        if order in ("Whiskey" , "whiskey"):
                            if money >= 5:
                                money = money - 5
                                choice = input("You order a whiskey, do you want to drink it? ")
                                if choice in ("Yes" , "yes" , "Y" , "y"):
                                    print("You drink the whiskey and feel a little bit better")
                                    health = health + 3
                                    stamina = stamina + 2
                                    health = min(health, maxhealth)
                                    stamina = min(stamina, maxstamina)
                                    print("Your health is now ", health, " and your stamina is now ", stamina)
                                else:
                                    print("You ask the bartender to bottle the whiskey for you, it goes into your inventory")
                                    addToInventory("Whiskey")
                            else:
                                print("You don't have enough money to buy that")
                        if order in ("Rum" , "rum"):
                            if money >= 7:
                                money = money - 7
                                choice = input("You order a rum, do you want to drink it? ")
                                if choice in ("Yes" , "yes" , "Y" , "y"):
                                    print("You drink the rum and feel a little bit better")
                                    health = health + 4
                                    stamina = stamina + 3
                                    health = min(health, maxhealth)
                                    stamina = min(stamina, maxstamina)
                                    print("Your health is now ", health, " and your stamina is now ", stamina)
                                else:
                                    print("You ask the bartender to bottle the rum for you, it goes into your inventory")
                                    addToInventory("Rum")
                            else:
                                print("You don't have enough money to buy that")
                        if order in ("Vodka" , "vodka"):
                            if money >= 10:
                                money = money - 10
                                choice = input("You order a vodka, do you want to drink it? ")
                                if choice in ("Yes" , "yes" , "Y" , "y"):
                                    print("You drink the vodka and feel a little bit better")
                                    health = health + 5
                                    stamina = stamina + 4
                                    health = min(health, maxhealth)
                                    stamina = min(stamina, maxstamina)
                                    print("Your health is now ", health, " and your stamina is now ", stamina)
                                else:
                                    print("You ask the bartender to bottle the vodka for you, it goes into your inventory")
                                    addToInventory("Vodka")
                            else:
                                print("You don't have enough money to buy that")
                        if order in ("Water" , "water"):
                            print("You order water, the bartender gives you a glass of water, do you want to drink it? ")
                            choice = input("Do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the water and feel a tiny bit better, not much but it is refreshing, your stats did not change")
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the bartender to bottle the water for you, it goes into your inventory")
                                addToInventory("Water")
                                                
                    elif answertav in ("Talk to angry drunkard" , "talk to angry drunkard"): 

                            print("Drunkard: oI yOu lIl bUgger, yOu aRe disTurBing me peAce, lEave me alOne uNless yoU're loOking fOr a fIght")
                            print("Hint: You will not have access to your equipment in the fight!")
                            answertav2 = input("Leave him alone and leave the tavern? ")
                            if answertav2 in ("Yes" , "yes" , "Y" , "y"):
                                print("You think it's best to leave the angry drunkard alone and leave the tavern...")
                                village()
                            elif answertav2 in ("No" , "no" , "N" , "n"):
                                print("\nYou decide to fight the angry drunkard")
                                print("\nTraveler, this is your first fight...")
                                print("Here is a simple tutorial...\n")
                                print("**************************** TUTORIAL: COMBAT **********************************")
                                print("\n-You and the enemy will take turns attacking and defending.")
                                print("-If you attack and the enemy defends, you will recoil and be unable to attack next turn.")
                                print("-If you defend and the enemy attacks, the enemy will recoil and be unable to attack next turn.")
                                print("-If you both defend, nothing will happen.")
                                print("-You both have an equal 33 percent chance to crit, which will do more damage than a normal attack.")
                                print("-If you both attack, you will both take damage, but if you get a crit, you will do more damage")
                                print("-The fight will continue until either you or the enemy runs out of health, good luck!\n")
                                print("************************************************************************\n")
                                
                                 # This part of the game was kindly made by Aiden, TYSM Aiden, you are a legend
                                
                                from random import randint
                                recoil = 0
                                playhealth = health
                                comphealth = 10

                                fighting1 = True

                                ComputerFightOptions1 = ["attack","defend","attack"]
                                ComputerFightOptions2 = ["attack","defend"]
                                Crit = ["a","b","c"]

                                hardmode = input("Would you like to turn on hard mode? [y/n]")
                                if hardmode == "y":
                                    print("\nHard mode enabled.\n")
                                    print("The drunkard drinks a full bottle of rum and becomes much more aggressive! He now has twice the health!\n")
                                    comphealth = 20
                                else:
                                    print()
                                while fighting1 == True:
                                    atkdmg = 1
                                    crtdmg = 3
                                    comdmg = 2
                                    comatk = ComputerFightOptions1[randint(0,2)]
                                    crit = Crit[randint(0,2)]
                                    if recoil == 1:
                                        print("You have recoiled and cannot do anything!\n")
                                    elif recoil == 2:
                                        print("They have recoiled and cannot do anything!\n")
                                        atk = input("What will you do? either 'attack' or 'defend' ")
                                    else:
                                        atk = input("What will you do? either 'attack' or 'defend' ")
                                    if atk == "a" or atk == "atk":
                                        atk = "attack"
                                        print()
                                    elif atk == "d" or atk == "def":
                                        atk = "defend"
                                        print()
                                    else:
                                        print()
                                    if atk == "attack" and comatk == "attack" and recoil == 0:
                                        if crit == "c":
                                            comphealth = comphealth - crtdmg
                                            print("A crit!")
                                            playhealth = playhealth - 1
                                            print("You get hit.\n")
                                        else:
                                            comphealth = comphealth - atkdmg
                                            print("You hit the enemy.")
                                            playhealth = playhealth - comdmg
                                            print("You got hit.\n")
                                    elif atk == "defend" and comatk == "defend" and recoil == 0:
                                        print("You both defend.\n")
                                    elif atk == "attack" and comatk == "defend" and recoil == 0:
                                        if crit == "c":
                                            print("They defend. but you crit!\n")
                                            comphealth = comphealth - 1
                                        else:
                                            print("They defend. You recoil!\n")
                                            recoil = 1
                                    elif atk == "defend" and comatk == "attack" and recoil == 0:
                                        print("You defended an attack. They recoil!\n")
                                        recoil = 2
                                    elif atk == "defend" and recoil == 2:
                                        print("You wasted your opportunity!")
                                        recoil = 0
                                    elif atk == "attack" and recoil == 2:
                                        if crit == "c":
                                            print("You get a free crit!")
                                            comphealth = comphealth - crtdmg
                                        else:
                                            print("You get a free hit!")
                                            comphealth = comphealth - atkdmg
                                        recoil = 0
                                    elif atk == "defend" or atk == "attack" and recoil == 1:
                                        if comatk == "defend":
                                            print("The drunkard wasted their free attack!")
                                        else:
                                            print("The drunkard gets a free hit!")
                                            playhealth = playhealth - comdmg
                                        recoil = 0
                                    elif atk == "debug":
                                        print("comphealth:", comphealth, "\n" , "playhealth:", playhealth, "\n" ,"recoil:", recoil)
                                    else:
                                        print("Invalid command.\n")
                                    if comphealth == 0 or comphealth == -1 or comphealth == -2:
                                            fighting1 = False
                                            print("You win!")
                                            print("Your health is now ",playhealth," and the drunkard's health is ",comphealth,"\n")
                                            health = health - playhealth
                                            money = money + 10
                                            XP = XP + 10
                                            print("The drunkard says that he's had a good fight and that he respects you, he then tells you to be careful out there and that the monster is no joke,\n along with giving you ξ10 for winning the fight as well as 10 XP")
                                            print("He also tells you that he is ready to fight you again if you want to test your strength")
                                            print("Do you want to leave the tavern?")
                                            leaveafterfight = input("Leave tavern? ")
                                            if leaveafterfight in ("Yes" , "yes" , "Y" , "y"):
                                                print("You leave the tavern")
                                                village()
                                            else:
                                                print("You decide stay in the tavern")
                                    elif playhealth == 0 or playhealth == -1 or playhealth == -2:                                   
                                            fighting1 = False
                                            print("You lose and you are dragged out of the bar")
                                            village()
                                    else:
                                        print("The fight continues.\n")
                                        print("*** Your health is now" , playhealth," and the drunkard's health is ",comphealth," ***" "\n")

                    elif answertav in ("Leave" , "leave" , "Exit" , "exit"):
                        print("You leave the tavern")
                        village()
                    else:
                        print("Doesn't look like that's working, you just stand there") 
                        answertav
            
        elif answervill in ("Check inventory" , "check inventory" , "Inventory" , "inventory"):
            inventory()
        
        elif answervill in ("Check stats" , "check stats" , "Stats" , "stats"):
                    print("\nHealth:", "♥ " * health , "or" , health , " out of " , maxhealth)
                    print("Stamina:", stamina , "out of" , maxstamina)
                    print("Money:", "ξ" , money , "\n")                           
    
        elif answervill in ("Go to general store" , "go to general store" , "Enter general store" , "enter general store"):
            
            while True:
            
                print("You enter the general store, there is a shopkeeper and a few shelves with items on them, he looks alsmost scared as if another \'attack\' may happen")
                answergs = input("What do you do here? ")
                if answergs in ("Talk to shopkeeper" , "talk to shopkeeper"):
                    print("The shopkeeper tells you that the monster has been terrorizing the village, he says that it is very strong and you may end up like the others if you try to fight it, he also says that he has some supplies for sale if you need them")
                if answergs in ("Buy supplies" , "buy supplies" , "Shop" , "shop" , "Buy" , "buy"):
                    print("\nThe shopkeeper shows you his supplies:")
                    print("\n***POTIONS***\n")
                    print("-Health potion: 5ξ")
                    print("-Stamina potion: 5ξ")
                    print("\n***ALCOHOL***\n")
                    print("-Ale: 2ξ")
                    print("-Wine: 3ξ")
                    print("-Whiskey: 5ξ")
                    print("-Rum: 7ξ")
                    print("-Vodka: 10ξ")
                    print("\n***SUPPLIES***\n")
                    print("-Bread: 2ξ")
                    print("-Apple: 1ξ")
                    print("-Cheese: 2ξ")
                    print("-Milk: 2ξ")
                    print("-Eggs: 3ξ")
                    print("-Sweets: 4ξ")
                    print("-Biscuits: 2ξ")
                    print("-Tomatoes: 2ξ")
                    print("-Beans: 1ξ")
                    print("-Water: Free!")
                    print("\n***MEATS***\n")
                    print("-Beef: 3ξ")
                    print("-Chicken: 2ξ")
                    print("-Pork: 2ξ")
                    print("-Fish: 3ξ")
                    print("-Lamb: 4ξ")
                    print("-Sausage: 3ξ")
                    print("-Bacon: 4ξ")
                    print("\n***MISC***\n")
                    print("-Rope: 5ξ")
                    print("-Soap: 3ξ")
                    print("-Lantern: 10ξ")
                    print("\nYou have ξ" , money)
                    buy = input("What do you want to buy? ")
                    if buy in ("Health potion" , "health potion"):
                        if money >= 5:
                            money = money - 5
                            addToInventory("Health potion")
                            print("You buy a health potion, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Stamina potion" , "stamina potion"):
                        if money >= 5:
                            money = money - 5
                            addToInventory("Stamina potion")
                            print("You buy a stamina potion, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Bread" , "bread"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Bread")
                            print("You buy a loaf of bread, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Water" , "water"):
                        addToInventory("Water")
                        print("You take the free water, it goes into your inventory")
                    elif buy in ("Apple" , "apple"):
                        if money >= 1:
                            money = money - 1
                            addToInventory("Apple")
                            print("You buy an apple, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Cheese" , "cheese"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Cheese")
                            print("You buy a piece of cheese, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Milk" , "milk"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Milk")
                            print("You buy a bottle of milk, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Eggs" , "eggs"):
                        if money >= 3:
                            money = money - 3
                            addToInventory("Eggs")
                            print("You buy a dozen eggs, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Sweets" , "sweets"):
                        if money >= 4:
                            money = money - 4
                            addToInventory("Sweets")
                            print("You buy a bag of sweets, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Biscuits" , "biscuits"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Biscuits")
                            print("You buy a pack of biscuits, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Tomatoes" , "tomatoes"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Tomatoes")
                            print("You buy a bunch of tomatoes, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Beans" , "beans"):
                        if money >= 1:
                            money = money - 1
                            addToInventory("Beans")
                            print("You buy a can of beans, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Beef" , "beef"):
                        if money >= 5:
                            money = money - 5
                            addToInventory("Beef")
                            print("You buy a piece of beef, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Chicken" , "chicken"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Chicken")
                            print("You buy a piece of chicken, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Pork" , "pork"):
                        if money >= 2:
                            money = money - 2
                            addToInventory("Pork")
                            print("You buy a piece of pork, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Fish" , "fish"):
                        if money >= 3:
                            money = money - 3
                            addToInventory("Fish")
                            print("You buy a piece of fish, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Lamb" , "lamb"):
                        if money >= 4:
                            money = money - 4
                            addToInventory("Lamb")
                            print("You buy a piece of lamb, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Sausage" , "sausage"):
                        if money >= 3:
                            money = money - 3
                            addToInventory("Sausage")
                            print("You buy a pack of sausage, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Bacon" , "bacon"):
                        if money >= 4:
                            money = money - 4
                            addToInventory("Bacon")
                            print("You buy a pack of bacon, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Rope" , "rope"):
                        if money >= 5:
                            money = money - 5
                            addToInventory("Rope")
                            print("You buy a rope, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Soap" , "soap"):
                        if money >= 3:
                            money = money - 3
                            addToInventory("Soap")
                            print("You buy a bar of soap, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Lantern" , "lantern"):
                        if money >= 10:
                            money = money - 10
                            addToInventory("Lantern")
                            print("You buy a lantern, it goes into your inventory")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Ale" , "ale"):
                        if money >= 2:
                            money = money - 2
                            choice = input("You buy an ale, do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the ale and feel a little bit better")
                                health = health + 1
                                stamina = stamina + 1
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the shopkeeper to bottle the ale for you, it goes into your inventory")
                                addToInventory("Ale")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Wine" , "wine"):
                        if money >= 3:
                            money = money - 3
                            choice = input("You buy a wine, do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the wine and feel a little bit better")
                                health = health + 2
                                stamina = stamina + 1
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the shopkeeper to bottle the wine for you, it goes into your inventory")
                                addToInventory("Wine")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Whiskey" , "whiskey"):
                        if money >= 5:
                            money = money - 5
                            choice = input("You buy a whiskey, do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the whiskey and feel a little bit better")
                                health = health + 3
                                stamina = stamina + 2
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the shopkeeper to bottle the whiskey for you, it goes into your inventory")
                                addToInventory("Whiskey")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Rum" , "rum"):
                        if money >= 7:
                            money = money - 7
                            choice = input("You buy a rum, do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the rum and feel a little bit better")
                                health = health + 4
                                stamina = stamina + 3
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the shopkeeper to bottle the rum for you, it goes into your inventory")
                                addToInventory("Rum")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Vodka" , "vodka"):
                        if money >= 10:
                            money = money - 10
                            choice = input("You buy a vodka, do you want to drink it? ")
                            if choice in ("Yes" , "yes" , "Y" , "y"):
                                print("You drink the vodka and feel a little bit better")
                                health = health + 5
                                stamina = stamina + 4
                                health = min(health, maxhealth)
                                stamina = min(stamina, maxstamina)
                                print("Your health is now ", health, " and your stamina is now ", stamina)
                            else:
                                print("You ask the shopkeeper to bottle the vodka for you, it goes into your inventory")
                                addToInventory("Vodka")
                        else:
                            print("You don't have enough money to buy that")
                    elif buy in ("Go back" , "go back"):
                        print("You stop looking at the supplies")
                        answergs
                elif answergs in ("Leave" , "leave" , "Exit" , "exit"):
                    print("You leave the general store")
                    village()
        else:
            print("Doesn't look like that's working, you just stand there")
        
        if answervill in ("DEBUG_ON"):
            debug()
        
# This is the starting area of the game, do not delete or move it in front of any functions or those areas will not be accessible (Code will be structurally unreachable)
 
while True:

    answer = input("What do you do? ")
                        
    if answer in ("Look around" , "look around" , "Observe" , "observe"):
                    print("Not much, mostly just grass, but you do see a very small village in the horizon") 
                    altanswer = input("What do you do next? " )
                    if altanswer in ("Walk to village" , "walk to village" , "Go to village" , "go to village"):
                                from time import sleep 
                                print("You start walking to the village...")
                                sleep(2)
                                print("You start wondering how you got here in the first place, but you can't remember anything...")
                                sleep(4)
                                print("You start to feel a little bit hungry and thirsty, but you don't have anything to eat or drink")
                                sleep(4)
                                print("You are getting closer...yawn")
                                sleep(2)
                                print("You arrive at the village and lose 3 stamina")
                                stamina = stamina - 3
                                village()
                    else:
                                print("Doesn't look like that's working, you just stand there")
    elif answer in ("Wake up" , "wake up"):
                    print("You are already awake, dummy")
    elif answer in ("Go back to sleep" , "go back to sleep" , "Go to sleep" , "go to sleep"):
                    print("You fall back asleep and never wake up again. Game Over.")
                    exit()
    elif answer in ("Check inventory" , "check inventory" , "Inventory" , "inventory"):
                    inventory()
    elif answer in ("Shout for help" , "shout for help" , "Yell for help" , "yell for help"):
                    print("No one answers, you are all alone")
    
    elif answer in ("Check stats" , "check stats" , "Stats" , "stats"):
                    print("\nHealth:", "♥ " * health , "or" , health , " out of " , maxhealth,)
                    print("Stamina:", stamina, "out of", maxstamina)
                    print("Money:", "ξ" , money , "\n")                           
    
    else:
                    print("Doesn't look like that's working, you just stand there")     

    if answer in ("DEBUG_ON"):
        debug()