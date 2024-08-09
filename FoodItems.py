''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random
from FoodASCII import *

####### Food Item Information ########
# Food_Name
# Food_EMOJI
# Foodt_location_on_Grid
# Food_Player_HP
# Food_Ghost_HP
# Food_ASCII_Art
###################################
FoodItemList = []
FoodItemList.append(['CAKE','🍰',0,15,7,Cake])
FoodItemList.append(['Burger','🍔',0,20,10,GenericFood])
FoodItemList.append(['Fries','🍟',0,20,10,GenericFood])
FoodItemList.append(['BACON','🥓',0,30,15,GenericFood])
FoodItemList.append(['TURKEY LEG','🍗',0,25,15,GenericFood])
FoodItemList.append(['SODA','🥤',0,15,7,Drink])
FoodItemList.append(['PIZZA','🍕',0,15,7,Pizza])
FoodItemList.append(['TACO','🌮',0,15,7,GenericFood])
FoodItemList.append(['CHEESE','🧀',0,15,7,GenericFood])
FoodItemList.append(['ASIAN NOODLE','🍜',0,20,10,WokSpoon])
FoodItemList.append(['STAKE','🥩',0,30,15,GenericFood])

def SetupPlayerStartItems():
    items = []
    items.append(random.choice(FoodItemList))
    items.append(random.choice(FoodItemList))
    items.append(random.choice(FoodItemList))
    return items


