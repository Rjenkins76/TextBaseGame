''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random,Weapons,FoodItems

####### Player Information ########
# PlayerName = name of player
# PlayerMaxHealth = max health of the player
# PlayerCurrentHealth = current health player has
# PlayerWeapons = list of weapons player has collected
# PlayerFood = list of food items player has collected
###################################
class Player:
    def __init__(self,name):
        self.PlayerName = name
        self.PlayerMaxHealth = 250
        self.PlayerCurrentHealth = 75
        self.PlayerWeapons = self.StartWeapon()
        self.PlayerFood = FoodItems.SetupPlayerStartItems()

    def StartWeapon(self):
        weapon = random.choice(Weapons.WEAPONLIST)
        test = []
        test.append(weapon)
        return test

    def AddHealth(self,AmountGained):
        self.PlayerCurrentHealth += AmountGained

    def RemoveHealth(self,AmountLost):
        self.PlayerCurrentHealth -= AmountLost

    def AddWeapon(self,FoundWeapon):
        if not FoundWeapon in PlayerInfo.PlayerWeapons:
            self.PlayerWeapons[FoundWeapon] = 1
        else:
            self.PlayerWeapons[FoundWeapon] += 1

    def RemoveWeapon(self,LostWeapon):
        self.PlayerWeapons.pop(LostWeapon)

    def AddFood(self,FoundFood):
        if not FoundFood in PlayerInfo.PlayerFood:
            self.PlayerFood[FoundFood] = 1
        else:
            self.PlayerFood[FoundFood] += 1

    def RemoveFood(self,LostFood):
        self.PlayerFood.pop(LostFood)

def SetupPlayer(Name):
    global PlayerInfo
    PlayerInfo = Player(Name)

####### HEALTH BAR #######
bars = 20 ### NUMBER OF SPACES IN HEALTH BAR
remaining_health_symbols = '█'
lost_health_symbols = '░'

def display_health_bar():
    if PlayerInfo.PlayerCurrentHealth >= 1:
        remaining_health_bar = round(PlayerInfo.PlayerCurrentHealth / PlayerInfo.PlayerMaxHealth * bars)
        lost_health_bar = bars - remaining_health_bar
        return f"HEALTH {PlayerInfo.PlayerCurrentHealth} / {PlayerInfo.PlayerMaxHealth}: {remaining_health_symbols * remaining_health_bar}{lost_health_symbols * lost_health_bar}"
    else:
        return "QUIT GAME"

def TestCode():
    SetupPlayer("Adam")
    global PlayerInfo
    print(PlayerInfo.PlayerName)

    print(PlayerInfo.PlayerCurrentHealth)
    PlayerInfo.AddHealth(25)
    print(PlayerInfo.PlayerCurrentHealth)
    PlayerInfo.RemoveHealth(36)
    print(PlayerInfo.PlayerCurrentHealth)

    PlayerInfo.AddWeapon("BEER")
    print(PlayerInfo.PlayerWeapons)
    PlayerInfo.RemoveWeapon("BEER")
    print(PlayerInfo.PlayerWeapons)

    PlayerInfo.AddFood("PIZZA")
    print(PlayerInfo.PlayerFood)
    PlayerInfo.RemoveFood("PIZZA")
    print(PlayerInfo.PlayerFood)

# TestCode()


