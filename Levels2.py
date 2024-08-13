''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import os, time, random, keyboard
import Player,Banner, Dice, FoodASCII, FoodItems, Weapons, GhostASCII, Floor1_Map,Floor2_Map, Rooms_MAP, Win_Lose
from Ghost import Ghost_List
from TrapASCII import TrapText
from sty import fg, bg, ef, rs

_PositionCell = 321 ### CURRENT PLAYER CELL NUMBER - START POSITION FOR THE GAME
Moves_Made = [] ### EACH TURN LIST OF MOVES - CELL NUMBER AND ITEM IN CELL
Game_Level = 1
room_number = 0
Exit_Cell = 0

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
    global _PositionCell, Exit_Cell
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
        _PositionCell = int((Rooms_MAP.WIDTH * Rooms_MAP.HEIGHT) - (Rooms_MAP.WIDTH / 2))
        Exit_Cell = _PositionCell
        Rooms_MAP.CELL_DRAW[_PositionCell][0] = Rooms_MAP.CELLS[11][0]
        Rooms_MAP.CELL_DRAW[_PositionCell][1] = Rooms_MAP.CELLS[11][1]
        Rooms_MAP.CELL_DRAW[_PositionCell][2] = Rooms_MAP.CELLS[11][2]
    elif Level == 4: ### FLOOR 2 ROOM START POSITION = ((WIDTH * HEIGHT) - (WIDTH / 2)
        _PositionCell = int((Rooms_MAP.WIDTH * Rooms_MAP.HEIGHT) - (Rooms_MAP.WIDTH / 2))
        Exit_Cell = _PositionCell
        Rooms_MAP.CELL_DRAW[_PositionCell][0] = Rooms_MAP.CELLS[11][0]
        Rooms_MAP.CELL_DRAW[_PositionCell][1] = Rooms_MAP.CELLS[11][1]
        Rooms_MAP.CELL_DRAW[_PositionCell][2] = Rooms_MAP.CELLS[11][2]

### GET 25% OF THE TIME PLAYER FALLS INTO A TRAP ###
def Percentage():
    if random.random() * 100 < 25:
        return True
    return False
### DISPLAY PLAYER FALLS INTO TRAP AND GET IF PLAYER HEALTH REDUCED ###
def EncounterTrap():
    trap = Percentage()
    if trap:
        DrawHeader()
        print("\n" * 4 + fg(250,100,100))
        for line in TrapText:
            print(line.center(208, " "))
        print("\n" * 3 + fg(255,255,50))
        print(" You fell into a trap....".center(208, " "))
        print(" Are you strong enough to escape, roll the die to find out".center(208, " "))
        print(" Roll a 1,2,3, or 4 - and you escape unharmed".center(208, " "))
        print(" Roll a 5,6,7,8 or 9 - and escape with injuries".center(208, " "))

        result = DiceMove2()  ### ROLL DICE TO SEE IF PAYER WILL LOSE HP - 9 SIDED DICE
        Banner.Clear_Line(1)
        if (result == 1) or (result == 2) or (result == 3) or (result == 4): # 9 SIDED DICE - PLAYER ROLL < 5
            print(fg(100, 250, 100))
            print(f"{Player.PlayerInfo.PlayerName} you escape unharmed!".center(208, " "))
            input("PRESS ENTER TO CONTINUE".rjust(115))
        elif (result == 5) or (result == 6) or (result == 7) or (result == 8) or (result == 9): # 9 SIDED DICE  - PLAYER ROLL > 4
            HPloss = random.randint(1, int(Player.PlayerInfo.PlayerCurrentHealth / 5)) # PLAYER CAN ONLY LOSE 1/5th OF HEALTH AT A TIME FOR TRAP
            Player.PlayerInfo.PlayerCurrentHealth -= HPloss
            print(fg(255,25,25))
            print(f"You have lost {HPloss} HP and your current HP is {Player.PlayerInfo.PlayerCurrentHealth}.".center(208, " "))
            input("PRESS ENTER TO CONTINUE".rjust(115))
            print(fg.rs)

### IF CELL CONTAINS A GHOST DRAW GHOST AND GIVE OPTION TO FEED OR FIGHT
def EnounterGhost(move):
    print("\n" * 10)
    story = ""
    name = ""
    Hp = 0
    ghost_info = []
    ### SELECT CORRECT GHOST AND GET IT'S INFORMATION
    for ghost in Ghost_List:
        if ghost.location == move[0]:
            story = ghost.story
            name = ghost.name
            Hp = ghost.Ghost_HP
            story_Lines = ghost.story_lines
            ghost_info.append([name, story, Hp])

            ### DRAW GHOST AND STORY
    ### GIVE OPTION TO FIGHT OR FEED
    x, z = 0, 0  ### X = GHOST LINES, Z = STORY LINES
    story_length = len(story_Lines)
    
    Ghost_length = len(GhostASCII.printBasicGhost)
    where_to_Start = 0 if story_length == 0 else int(Ghost_length / story_length)  ### GET LINE TO START GHOST INFORMATION IN REFERENCE TO THE GHOST ASCII
    for i in GhostASCII.printBasicGhost:
        if z == 1:
            print(i.rjust(45) + f" YOU HAVE ENCOUNTERED THE GHOST OF {name}".center(150, " "))
            z += 1
        elif z == 2:
            print(i.rjust(45) + f" HEALTH: {Hp}".center(150, " "))
            z += 2
        elif (z == where_to_Start) and (x < story_length):
            print(i.rjust(45) + story_Lines[x].center(150, " "))
            x += 1
            where_to_Start += 1
            z += 1
        elif z == 10:
            print(i.rjust(45) + fg(255, 255, 0) + "1. FEED GHOST".center(150, " ") + fg.rs)
            z += 1
        elif z == 12:
            print(i.rjust(45) + fg(255, 255, 0) + "2. FIGHT GHOST".center(150, " ") + fg.rs)
            z += 1
        else:
            print(i.rjust(45))
            z += 1

            # print (f"\033[38;5;{227}m")
    Banner.Clear_Line()
    option = input("SELECT OPTION: ".rjust(125))
    if option == "1":
        FeedingGhost() ### CALL TO FEED THE GHOST
    elif option == "2":
        FightingGhost(ghost_info)  ### CALL GHOST FIGHT SCRIPT
    else:
        EnounterGhost(move)  ### RESTART IF NOT ONE OF THE OPTIONS

def GhostFight_Percentage(amount):
    if random.random() * 100 < amount:
        return True
    return False

### DISPLAY GHOST FIGHT
def FightingGhost(ghost_info):
    Banner.Clear_Line(int(12 * 3.9))

    avail_Weapons = {}
    # region DRAW WEAPONS AVAILABLE
    print("\n" * 15 + fg(255, 255, 0))
    print("❚█══SELECT WEAPON══█❚".center(208, " "))
    print("\n\n")
    x = 1
    for W in Player.PlayerInfo.PlayerWeapons:
        avail_Weapons[x] = W
        print((str(x) + ". " + str(W[1]) + " - " + str(W[0])).center(208, " "))
        win_chance = W[2]
        print("\n")
        x += 1
    item = input("SELECT A WEAPON TO USE: ".rjust(115))
    win_chance = avail_Weapons[int(item)][2]
    # endregion

    # region DRAW FIGHTING SEQUENCE
    Banner.Clear_Line(int(12 * 3.9))
    print("\n" * 30)
    color = 255
    while color > -5:
        Banner.Clear_Line(len(GhostASCII.printFight) + 1)
        print(fg.rgb_call(color, color, color))
        for i in GhostASCII.printFight:
            print(i.center(208, " "))

        time.sleep(0.1)
        color -= 17

    color = 0
    Banner.Clear_Line(len(GhostASCII.printFight) + 1)
    print("\n" * (30 - len(GhostASCII.printFight)))
    while color < 255:
        Banner.Clear_Line(len(GhostASCII.printFight2) + 1)
        print(fg.rgb_call(color, color, color))
        for i in GhostASCII.printFight2:
            print(i.center(208, " "))

        time.sleep(0.1)
        color += 17

    color = 255
    Banner.Clear_Line(len(GhostASCII.printFight2))
    print("\n" * (30 - len(GhostASCII.printFight2)))
    while color > -5:
        Banner.Clear_Line(len(GhostASCII.printFight) + 1)
        print(fg.rgb_call(color, color, color))
        for i in GhostASCII.printFight:
            print(i.center(208, " "))

        time.sleep(0.1)
        color -= 17

    # endregion

    # region DISPLAY FIGHT RESULTS
    print("\n" * 2 + fg(255, 255, 0))
    Ghost_Status = GhostFight_Percentage(win_chance)
    if Ghost_Status:
        print(fg(255, 255, 0) + "YOU HAVE BATTLED WITH THE GHOST....".center(208, " "))
        print(fg(255, 255, 0) + f"YOU HAVE DEFEATED THE GHOST !!!!!!!".center(208, " "))
        amount = random.randint(25, 75)
        Player.PlayerInfo.AddHealth(amount)
        print(fg(255, 255,0) + f"YOU HAVE GAINED {amount} HP".center(208, " ") + "\n\n")
        input("PRESS ANY KEY TO CONTINUE...".rjust(120))
    else:
        print(fg(255, 255, 0) + "YOU HAVE BATTLED WITH THE GHOST.....".center(208, " "))
        ghost_info[0][2] -= random.randint(10, 75)
        print(fg(255, 255, 0) + f"YOU HAVE REDUCED THEIR HEALTH TO {ghost_info[0][2]}".center(208, " "))
        amount = random.randint(0, 50)
        Player.PlayerInfo.RemoveHealth(amount)
        print(fg(255, 255,0) + f"YOU HAVE LOST {amount} HP".center(208, " ") + "\n\n")
        input("PRESS ANY KEY TO CONTINUE...".rjust(120))

    # endregion

### DISPLAY GHOST FIGHT
def FightingBoss():

    # region DRAW FIGHTING SEQUENCE
    Banner.Clear_Line(int(12 * 3.9))
    x = 0
    y = 0
    while x <= 20:
        z = random.randint(0,145)
        Banner.ClearScreen()
        print("\n" * random.randint(0,45))
        for i in GhostASCII.printBoss1Face:
            print(" " * z + i)
        
        time.sleep(0.1)
        x += 1

    # endregion

    # region DISPLAY FIGHT RESULTS
    print("\n" * 2 + fg(255, 255, 0))
    Ghost_Status = True
    if Ghost_Status:
        Win_Lose.DisplayWINGame()
        quit()
    else:
        print(fg(255, 255, 0) + "YOU HAVE BATTLED WITH THE ALISTOR.....".center(208, " "))
        print(fg(255, 255, 0) + f"AND LOST".center(208, " "))
        amount = random.randint(int(Player.PlayerInfo.PlayerCurrentHealth / 2), Player.PlayerInfo.PlayerCurrentHealth)
        Player.PlayerInfo.RemoveHealth(amount)
        print(fg(255, 255,0) + f"YOU HAVE LOST {amount} HP".center(208, " ") + "\n\n")
        input("PRESS ANY KEY TO CONTINUE...".rjust(120))
        return False

    # endregion

### DISPLAY FEEDING GHOST 
def FeedingGhost():
    Banner.ClearScreen()
    for i in FoodASCII.NomNom:
        print(i.center(208, " "))
    input("PRESS ANY KEY TO CONTINUE".rjust(135))

### COLLECTS PLAYER INPUT FOR SELECTED MOVES EACH TURN ###
### PLAYER CAN ALSO VIEW THEIR FOOD ITEMS AND WEAPONS  ###
def PlayerMove(num_Moves):
    global _PositionCell,Moves_Made
    move = 0
    while move < num_Moves:
        Banner.ChangeFOREcolor(255,255,0)
        Banner.Clear_Line()
        MoveSelection = input(f"You have {num_Moves - move} moves left (8: UP,  4: LEFT, 2: DOWN, 6: RIGHT️): ".rjust(130, " "))
        if MoveSelection == "8":
            move += 1
            MovePlayer("UP")

        elif MoveSelection == "2":
            move += 1
            MovePlayer("DOWN")

        elif MoveSelection == "4":
            move += 1
            MovePlayer("LEFT")

        elif MoveSelection == "6":
            move += 1
            MovePlayer("RIGHT")

        elif (MoveSelection.upper() == "FOOD"): ### FIXME - needs to display food items and be able to select item to use
            x = 1
            print(f"LIST OF YOUR FOOD ITEMS:".center(208, " "))
            for item in Player.PlayerInfo.PlayerFood:
                print((str(x) + ": " + i).center(208," ")) 
            
            option = input("SELECT ITEM TO USE OR TYPE NONE LEAVE WITH OUT USING ITEM")
            if option.upper() == "NONE":
                pass
            elif int(option) in itemslist:
                confirm = input(f"CONFIRM THAT YOU WOULD LIKE TO EAT A {} : (Y/N)")
                if confirm.upper() == 'Y':
                    del Player.PlayerInfo.PlayerFood[x-1]
                elif confirm.upper() == 'N':
                    pass
                else:
                    pass 
        elif (MoveSelection.upper() == "WEAPON"): 
            x = 1
            print(f"LIST OF YOUR WEAPONS:".center(208, " "))
            for item in Player.PlayerInfo.PlayerWeapons:
                print((str(x) + ": " + i).center(208," "))
            input("PRESS ENTER TO CONTINUE".rjust(135))

        Banner.EndColor()
        Banner.Clear_Line()

### MOVES PLAYER BASED ON SELECTED DIRECTION ###
def MovePlayer(direction):
    global _PositionCell,Moves_Made
    if Game_Level == 1:
        CELL_DRAW = Floor1_Map.CELL_DRAW
        CELLS = Floor1_Map.CELLS
    if Game_Level == 2:
        CELL_DRAW = Floor2_Map.CELL_DRAW
        CELLS = Floor2_Map.CELLS
    if Game_Level == 3:
        CELL_DRAW = Rooms_MAP.CELL_DRAW
        CELLS = Rooms_MAP.CELLS
    if Game_Level == 4:
        CELL_DRAW = Rooms_MAP.CELL_DRAW
        CELLS = Rooms_MAP.CELLS

    CELL_DRAW[_PositionCell] = [CELLS[1][0], CELLS[1][1], CELLS[1][2]]

    if(Game_Level == 1) or (Game_Level == 2):
        if direction == "UP":
            _PositionCell -= 28
        elif direction == "DOWN":
            _PositionCell += 28
        elif direction == "LEFT":
            _PositionCell -= 1
        elif direction == "RIGHT":
            _PositionCell += 1
    elif(Game_Level == 3) or (Game_Level == 4):
        if direction == "UP":
            _PositionCell -= Rooms_MAP.WIDTH
        elif direction == "DOWN":
            _PositionCell += Rooms_MAP.WIDTH
        elif direction == "LEFT":
            _PositionCell -= 1
        elif direction == "RIGHT":
            _PositionCell += 1

    Moves_Made.append([_PositionCell, CELL_DRAW[_PositionCell][1]])
    CELL_DRAW[_PositionCell] = [CELLS[11][0], CELLS[11][1], CELLS[11][2]]
    Banner.Clear_Line()
    time.sleep(0.3)
  
### DRAW GAME BOARD GRID ###
def DrawGameBoard(Level):
    global Game_Level, room_number
    if Level == 1:
        Floor1_Map.Draw_Cells2()
    if Level == 2:
        if len(Floor2_Map.CELL_DRAW) == 0:
            Floor2_Map.SetupCells()
            Floor2_Map.Assign_Ghost(False)
            Floor2_Map.Assign_Bosses()
            DrawStartPosition(2)
        Floor2_Map.Assign_Ghost(True)
        Floor2_Map.Draw_Cells2()
    if (Level == 3): # Floor 1 Rooms
        if len(Rooms_MAP.CELL_DRAW) == 0:
            Rooms_MAP.SetupCells()
            Rooms_MAP.AssignItems(False)
            room_number = Rooms_MAP.AssignRoom()
            DrawStartPosition(3)
        Rooms_MAP.Draw_Room(room_number)
        # Game_Level = 1
    if Level == 4: # Floor 2 Rooms
        if len(Rooms_MAP.CELL_DRAW) == 0:
            Rooms_MAP.SetupCells()
            Rooms_MAP.AssignItems(False)
            room_number = Rooms_MAP.AssignRoom()
            DrawStartPosition(4)
        Rooms_MAP.Draw_Room(room_number)

### GAME LOOP Floor 1 - LOOP UNTIL PLAYER HEALTH REACHES 0 OR PLAYER BEATS MAIN BOSS ###
def PlayGame():
    global Game_Level, _PositionCell
    while True:
        if Player.PlayerInfo.PlayerCurrentHealth >= 0:
            DrawHeader()
            DrawGameBoard(Game_Level)
            Banner.ChangeFOREcolor(255, 255, 0)
            print("Using Number Pad Select your move.".center(208, " "))
            result = DiceMove()  ### RETURNED NUMBER FOR PLAYER MOVES
            Banner.Clear_Line(1)
            PlayerMove(result)  ### COLLECTS PLAYER TURN MOVES
            Check_if_Room()
            # Blockedcell()  ### IS PART OF PREVIOUS COMMAND - CHECKS TO SEE IF ANY MOVE ENCOUNTERED OBJECT
            if Game_Level == 1:
                Floor1_Map.AssignItems(True)  ### MOVES GHOST EACH TURN
            if Game_Level == 3:
                if _PositionCell == Exit_Cell:
                    Game_Level = 1
                    for cell in len(Floor1_Map.CELL_DRAW):
                        if Floor1_Map.CELL_DRAW[cell][0] == '   O  ':
                            _PositionCell == cell
            elif Game_Level == 4:
                if _PositionCell == Exit_Cell:
                    Game_Level = 2
        else:
            break

    Win_Lose.DisplayLOSEGame()  ### DISPLAYS PLAYER DIE SCREEN AND REUTNS TO CMD PROMPT

def Check_if_Room():
    global Game_Level
    fellintotrap = False
    ### IF PLAYER ENTERS A ROOM
    if Game_Level == 1:
        rooms = Floor1_Map.Room_List
    elif Game_Level == 2:
        rooms = Floor2_Map.Room_List
    try:
        for room in rooms:
            if _PositionCell == room:
                if Game_Level == 1:
                    Game_Level = 3
                elif Game_Level == 2:
                    Game_Level = 4

            elif _PositionCell == 13:
                Game_Level = 2    
    except:
        pass

    Blockedcell()

### CHECK TO SEE IF PLAYER ENTERS ROOM OR ITEM IN EACH CELL PLAYER WAS IN ###
def Blockedcell():
    global Moves_Made
    fellintotrap = False

    for move in Moves_Made:
        ### IF A CELL CONTAINED A FOOD ITEM - ***FIXME***
        if (move[1] == '  🥖  '):
            Banner.Clear_Line(int(12 * 3.9) + 12)          
            print("\n" * 10)
            fooditem = random.choice(FoodItems.FoodItemList)
            print(f"YOU FOUND A {fooditem[0]} !!!".center(208, " "))
            print("\n" * 2)
            for i in fooditem[5]:
                print(i.center(208," "))
            print("\n" * 3)
            print((fg(255, 255, 0) + "1. EAT".center(208," ") + fg.rs))
            print((fg(53, 53, 53) + "2. SAVE FOR LATER".center(208," ") + fg.rs))
            option = input((fg(255, 255, 0) + "Select Option 1 only: " + fg.rs).rjust(135))
            if option == '1':
                Banner.Clear_Line(int(12 * 3.9) + 12)
                for i in FoodASCII.NomNom:
                    print(i.center(208," "))
            Player.PlayerInfo.AddHealth(int(fooditem[3]))
            del Player.PlayerInfo.PlayerFood[fooditem]
                
        ### IF A CELL CONTAINED A GHOST - PLAYER SELECTS TO FEED OR FIGHT
        elif (move[1] == '  👻  '):
            Banner.Clear_Line(int(12 * 3.9) + 12)
            # SlidingGhost()
            Banner.Clear_Line(4)
            print("\n")
            EnounterGhost(move)
            pass
        ### IF A CELL CONTAINED A WEAPON - ***FIXME***
        elif (move[1] == '  ⚔️  '):
            Banner.Clear_Line(int(12 * 3.9) + 12)          
            print("\n" * 10)
            Weaponitem = random.choice(Weapons.WEAPONLIST)
            print(f"YOU FOUND A {Weaponitem[0]} !!!".center(208, " "))
            print("\n" * 2)
            for i in Weapons.Weapon:
                print(i.center(208," "))
            print("\n" * 3)
            option = input((fg(255, 255, 0) + "PRESS ENTER TO CONTINUE ..." + fg.rs).rjust(135))
            print()
            Player.PlayerInfo.AddWeapon(Weaponitem)
        elif (move[1] == '  😡  '):
            DrawHeader()
            Banner.ChangeFOREcolor(250, 100, 100)
            print("YOU HAVE ENCOUNTERED ALISTOR THE MAIN BOSS")         
            results = FightingBoss()
            if results:
                Win_Lose.DisplayWINGame()
                quit()
            else:
                pass
        elif (move[1] == '  👿  '):
            print("YOU HAVE ENCOUNTERED ALISTOR'S HENCHMEN")
            input()
        ### DOES PLAYER FIND A TRAP?
        else: 
            if not fellintotrap:
                EncounterTrap()
                fellintotrap = True
    
    Moves_Made.clear()  ### CLEAR LIST FOR NEXT PLAYER TURN








