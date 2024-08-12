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
FoodItemList.append(['SLICE OF CAKE','🍰',0,25,7,Cake])
FoodItemList.append(['CHEESE BURGER','🍔',0,30,10,Burger])
FoodItemList.append(['CONTAINER OF FRIES','🍟',0,20,10,GenericFood])
FoodItemList.append(['SLICE OF BACON','🥓',0,40,15,Bacon])
FoodItemList.append(['TURKEY LEG','🍗',0,30,15,GenericFood])
FoodItemList.append(['SODA','🥤',0,20,7,Drink])
FoodItemList.append(['SLICE OF PIZZA','🍕',0,35,7,Pizza])
FoodItemList.append(['TACO','🌮',0,25,7,GenericFood])
FoodItemList.append(['WEDGE OF CHEESE','🧀',0,20,7,Cheese])
FoodItemList.append(['CARTON OF ASIAN NOODLE','🍜',0,30,10,WokSpoon])
FoodItemList.append(['STAKE','🥩',0,40,15,GenericFood])

def SetupPlayerStartItems():
    items = []
    items.append(random.choice(FoodItemList))
    items.append(random.choice(FoodItemList))
    items.append(random.choice(FoodItemList))
    return items


