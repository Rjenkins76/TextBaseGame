''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random,Banner
from Rooms_ASCII import ROOM_NAMES, ROOM_NUMBER
from Ghost import Ghost_List
from sty import fg, bg, ef, rs

WIDTH =  random.randint(4,12)
HEIGHT = random.randint(3,7)

CELL_DRAW = []

CELLS = {
    1: (
        "      ",
        "      ",
        "      "
    ),
    2: (
        "     │",
        "     │",
        "     │"
    ),
    3: (
        "     │",
        "     │",
        "─────│"
    ),
    4: (
        "      ",
        "      ",
        "──────"
    ),
    5: (
        "│     ",
        "│     ",
        "│     "
    ),
    6: (
        "│     ",
        "│     ",
        "│─────"
    ),
    7: (
        "     │",
        "     │",
        "─────┼"
    ),
    8: (
        "      ",
        "  🥖  ",   # FOOD ITEM
        "      "
    ),
    9: (
        "      ",
        "  👻  ",   # GHOST
        "      "
    ),
    10: (
        "      ",
        "  ⚔️  ",   # WEAPON
        "      "
    ),
    11: (
        fg(0, 235, 0) + r"   O  " + fg.rs,
        fg(0, 235, 0) + r"  /|\ " + fg.rs,
        fg(0, 235, 0) + r"  / \ " + fg.rs
    ),
    12: (
        "      ",
        "  👿  ",  # WEAPON
        "      "
    ),
    13: (
        "      ",
        "  😡  ",   # WEAPON
        "      "
    ),
}

def SetupCells():
    for x in range((WIDTH * HEIGHT)):
        CELL_DRAW.append([CELLS[1][0], CELLS[1][1], CELLS[1][2]])

def AssignItems(reassign):
    if reassign:
        for _ghost in range(int(len(Ghost_List)/4)):
            current = Ghost_List[_ghost]
            current2 = current.location
            print(current2)
            CELL_DRAW[current2] = [CELLS[1][0], CELLS[1][1], CELLS[1][2]]
            Ghost_List[_ghost].location = 0
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[9][0], CELLS[9][1], CELLS[9][2]]
                Ghost_List[_ghost].location = z
    else:
        for _ghost in range(int(len(Ghost_List)/4)):
            print(int(len(Ghost_List)/4))
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[9][0], CELLS[9][1], CELLS[9][2]]
                Ghost_List[_ghost].location = z

        for _food in range(3):
            z = random.randrange(1, len(CELL_DRAW))
            test = CELLS[8][1]
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[8][0], test, CELLS[8][2]]

        for _fWeapon in range(1):
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[10][0], CELLS[10][1], CELLS[10][2]]

def AssignRoom():
    return random.randint(1,5)   

def Draw_Room(room_number):
    x, y = 1, 1
    Banner.EndColor()
    print("\n")
    for n in ROOM_NAMES[room_number]:
        print(fg(105,145, 145) + n.center(208, " ") + fg.rs)
    print("\n" * 2)
    get_header_Length = len(("┌─────" + "──────" * (WIDTH - 2) + "─────┐"))
    justif = int((208 / 2) - (get_header_Length / 2))
    print("".ljust(justif) + ("┌──────" + "──────" * (WIDTH - 2) + "──────┐"))
    line1 = "".ljust(justif) + "│"
    line2 = "".ljust(justif) + "│"
    line3 = "".ljust(justif) + "│"
    for i in range(len(CELL_DRAW)):
        if y < WIDTH:           
            
            line1 += CELL_DRAW[i][0]
            line2 += CELL_DRAW[i][1]
            line3 += CELL_DRAW[i][2]
            x += 1
            y += 1
        elif y == WIDTH:        
            line1 += CELL_DRAW[i][0] + "│"
            line2 += CELL_DRAW[i][1] + "│"
            line3 += CELL_DRAW[i][2] + "│"
            x += 1
            y=1

            print((line1 +  "\n" + line2+ "\n" + line3))
            line1 , line2, line3 = "".ljust(justif) + "│", "".ljust(justif) + "│", "".ljust(justif) + "│"
            
    if WIDTH % 2 == 0:
        print("".ljust(justif) + "└" + "──────" * int(WIDTH/2) + "      " + "──────" * (int(WIDTH/2) - 1) +"┘")
    else:
        print("".ljust(justif) + "└" + "──────" * int(WIDTH/2) + "      " + "──────" * (int(WIDTH/2)) +"┘")

