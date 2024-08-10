''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import os, time, random, keyboard
import Player,Banner, Dice, FoodASCII, Ghost, GhostASCII, Floor1_Map,Floor2_Map, Rooms_MAP, Win_Lose
from TrapASCII import TrapText
from sty import fg, bg, ef, rs

_PositionCell = 321 ### CURRENT PLAYER CELL NUMBER - START POSITION FOR THE GAME
Moves_Made = [] ### EACH TURN LIST OF MOVES - CELL NUMBER AND ITEM IN CELL
Game_Level = 1

### DRAW GAME LOGO AND STATUS BAR ###
def DrawHeader():
    Banner.ClearScreen()
    Banner.Clear_Line()
    print(Banner.banner_text)

    healthbar = Player.display_health_bar()
    ### HEALTH BAR CHANGES COLORS FOR LEVEL
    ### <= 50 -     COLOR RED
    ### 51 <> 199 - COLOR BLUE
    ### >= 200 -    COLOR GREEN
    if healthbar != "QUIT GAME":
        if Player.PlayerInfo.PlayerCurrentHealth <= 50:
            print(fg(250, 100, 100) + (healthbar + fg(122, 216, 213) + f"  # FOOD ITEMS: {len(Player.PlayerInfo.PlayerFood)}     WEAPONS: {len(Player.PlayerInfo.PlayerWeapons)}").center(225, " ") + fg.rs)
        elif Player.PlayerInfo.PlayerCurrentHealth >= 200:
            print(fg(100,250,100) + (healthbar + fg(122, 216, 213) + f"  # FOOD ITEMS: {len(Player.PlayerInfo.PlayerFood)}     WEAPONS: {len(Player.PlayerInfo.PlayerWeapons)}").center(225, " ") + fg.rs)
        else:
            print(fg(122, 216, 213) + (healthbar + f"  # FOOD ITEMS: {len(Player.PlayerInfo.PlayerFood)}     WEAPONS: {len(Player.PlayerInfo.PlayerWeapons)}").center(208, " ") + fg.rs)
        Banner.EndColor()
        Banner.Clear_Line()
    else:
        Win_Lose.DisplayLOSEGame()
        quit()

### DISPLAY DICE IMAGE AND ROLL NUMBER OF TIMES ###
def DiceMove():
    rolls = 25 ### NUMBER TIMES DICE SPIN
    rolling = 0 ### CURRENT SPIN NUMBER
    while rolling < rolls:
        test = Dice.DiceNormalRoller()
        test.diceroller(1)
        Banner.Clear_Line(7)
        rolling += 1
        time.sleep(random.uniform(0.0,0.15)) ### CREATE RANDOM ROLL SPEED
    return test.diceroller(1) ### RETURN NUMBER DICE LANDS ON

### DISPLAY DICE IMAGE AND ROLL NUMBER OF TIMES ###
def DiceMove2():
    rolls = 25 ### NUMBER TIMES DICE SPIN
    rolling = 0 ### CURRENT SPIN NUMBER
    while rolling < rolls:
        test = Dice.DiceTrapRoller()
        test.diceroller(1)
        Banner.Clear_Line(7)
        rolling += 1
        time.sleep(random.uniform(0.0,0.15)) ### CREATE RANDOM ROLL SPEED
    return test.diceroller(1) ### RETURN NUMBER DICE LANDS ON

### START GAME HERE
def start():
    global Game_Level
    Floor1_Map.SetupCells() ### CREATE CELLS FOR LEVEL BASED ON WIDTH * HEIGHT
    Floor1_Map.AssignItems(False) ### ASSIGN GHOST, FOOD, AND WEAPONS ON GRID
    Game_Level = 1
    DrawStartPosition(1) ### SET CELL THAT HAS PLAY TO START THE GAME
    PlayGame() ### START GAME LOOP

### PUT PLAYER IMAGE IN BOTTOM CENTER CELL ###
def DrawStartPosition(Level):
    if Level == 1: ### FLOOR 1 START POSITION = 321
        _PositionCell = 321
        Floor1_Map.CELL_DRAW[_PositionCell][0] = Floor1_Map.CELLS[11][0]
        Floor1_Map.CELL_DRAW[_PositionCell][1] = Floor1_Map.CELLS[11][1]
        Floor1_Map.CELL_DRAW[_PositionCell][2] = Floor1_Map.CELLS[11][2]
    elif Level == 2: ### FLOOR 2 START POSITION = 13
        _PositionCell = 13
        Floor2_Map.CELL_DRAW[_PositionCell][0] = Floor2_Map.CELLS[11][0]
        Floor2_Map.CELL_DRAW[_PositionCell][1] = Floor2_Map.CELLS[11][1]
        Floor2_Map.CELL_DRAW[_PositionCell][2] = Floor2_Map.CELLS[11][2]
    elif Level == 3: ### FLOOR 1 ROOM START POSITION = ((WIDTH * HEIGHT) - (WIDTH / 2))
        _PositionCell = ((Rooms_MAP.WIDTH * Rooms_MAP.HEIGHT) - (Rooms_MAP.WIDTH / 2))
        Rooms_MAP.CELL_DRAW[_PositionCell][0] = Rooms_MAP.CELLS[3][0]
        Rooms_MAP.CELL_DRAW[_PositionCell][1] = Rooms_MAP.CELLS[3][1]
        Rooms_MAP.CELL_DRAW[_PositionCell][2] = Rooms_MAP.CELLS[3][2]
    elif Level == 4: ### FLOOR 2 ROOM START POSITION = ((WIDTH * HEIGHT) - (WIDTH / 2)
        _PositionCell = ((Rooms_MAP.WIDTH * Rooms_MAP.HEIGHT) - (Rooms_MAP.WIDTH / 2))
        Rooms_MAP.CELL_DRAW[_PositionCell][0] = Rooms_MAP.CELLS[3][0]
        Rooms_MAP.CELL_DRAW[_PositionCell][1] = Rooms_MAP.CELLS[3][1]
        Rooms_MAP.CELL_DRAW[_PositionCell][2] = Rooms_MAP.CELLS[3][2]







