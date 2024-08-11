''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random
import Banner, Ghost
from sty import fg, bg, ef, rs

Width = 28
Height = 12
get_header_Length = 170
justif = int((208 / 2) - (get_header_Length / 2))
Room_List = [30,53,114,137,198,221,282,305]

#region Cell information
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
}
#endregion

def SetupCells():
    for x in range((Width * Height)):
        CELL_DRAW.append([CELLS[1][0], CELLS[1][1], CELLS[1][2]])

def AssignItems(reassign):
    if reassign:
        for _ghost in range(len(Ghost.Ghost_List)):
            current = Ghost.Ghost_List[_ghost]
            current2 = current.location
            CELL_DRAW[current2] = [CELLS[1][0], CELLS[1][1], CELLS[1][2]]
            Ghost.Ghost_List[_ghost].location = 0
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[9][0], CELLS[9][1], CELLS[9][2]]
                Ghost.Ghost_List[_ghost].location = z

        # for _food in range(15):
        #     z= random.randrange(1, len(CELL_DRAW))
        #     test = CELLS[5][1]        
        #     if CELL_DRAW[z][1] == "      ":
        #         CELL_DRAW[z] = [CELLS[5][0], test, CELLS[5][2]]

        
    else:
        Ghost.SetupGhost(15)
        for _ghost in range(len(Ghost.Ghost_List)):
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[9][0], CELLS[9][1], CELLS[9][2]]
                Ghost.Ghost_List[_ghost].location = z

        for _food in range(15):
            z= random.randrange(1, len(CELL_DRAW))
            test = CELLS[8][1]        
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[8][0], test, CELLS[8][2]]

        for _fWeapon in range(10):
            z= random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[10][0], CELLS[10][1], CELLS[10][2]]

def Draw_Cells2():
    x, y, z, a = 0, 1, 48, 73
    Banner.EndColor()
    ### DRAW TOP ROW ###
    print("".ljust(justif) + "┌" + "──────" * 12 + fg(255,255,0) + "┬────────────────┬" + fg.rs+ "──────" * 13 + "┐")
    line1, line2, line3 = "".ljust(justif) + "│", "".ljust(justif) + "│", "".ljust(justif) + "│"

    Empty_Cell_List = [0,1,28,29,84,85,112,113,168,169,196,197,252,253,280,281,308,309
                       ,26,27,54,55,110,111,138,139,194,195,222,223,278,279,306,307,334,335]
    
    Left_Cell_Border_List = [2,86,170,254,310]

    Leff_Cell_Corner_List = [58,142,226]

    Bottom_Cell_Border_List = [56,57,140,141,224,225,82,83,166,167,250,251]

    Right_Cell_Border_List = [25,109,193,277,333]

    Right_Cell_Corner_List = [81,165,249]

    ### DRAW CELLS ###
    for i in range(len(CELL_DRAW)):
        if y < Width:
            if (i ==12): #or (i ==11) or (i ==12)
                line1 += fg(255,255,0) + "│STAIR"
                line2 += fg(255,255,0) + "│     "
                line3 += fg(255,255,0) + "└─────"
            elif (i ==13): #or (i ==11) or (i ==12)
                # CELL_DRAW[i][0] = f"{"%03d" % x}   "
                line1 += CELL_DRAW[i][0]
                line2 += CELL_DRAW[i][1]
                line3 += CELL_DRAW[i][2]
            elif (i ==14): #or (i ==11) or (i ==12)
                line1 += fg(255,255,0) + " WAY │" + fg.rs
                line2 += fg(255,255,0) + "     │" + fg.rs
                line3 += fg(255,255,0) + "─────┘" + fg.rs

            elif i in Empty_Cell_List:
                line1 += CELLS[1][0]
                line2 += CELLS[1][1]
                line3 += CELLS[1][2]

            elif i in Left_Cell_Border_List:
                line1 += CELLS[2][0]
                line2 += CELLS[2][1]
                line3 += CELLS[2][2]
            
            elif i in Leff_Cell_Corner_List:
                line1 += CELLS[3][0]
                line2 += CELLS[3][1]
                line3 += CELLS[3][2]

            elif i in Bottom_Cell_Border_List:
                line1 += CELLS[4][0]
                line2 += CELLS[4][1]
                line3 += CELLS[4][2]

            elif i in Right_Cell_Border_List:
                line1 += CELLS[5][0]
                line2 += CELLS[5][1]
                line3 += CELLS[5][2]

            elif i in Right_Cell_Corner_List:
                line1 += CELLS[6][0]
                line2 += CELLS[6][1]
                line3 += CELLS[6][2]
            else:
                # CELL_DRAW[i][0] = f"{"%03d" % x}   "
                line1 += CELL_DRAW[i][0]
                line2 += CELL_DRAW[i][1]
                line3 += CELL_DRAW[i][2]
            x += 1
            y += 1
        elif y == Width:
            y = 1
            if i in Empty_Cell_List:
                line1 += CELLS[1][0]
                line2 += CELLS[1][1]
                line3 += CELLS[1][2]

            elif i in Bottom_Cell_Border_List:
                line1 += CELLS[4][0]
                line2 += CELLS[4][1]
                line3 += CELLS[4][2]


            else:
                # CELL_DRAW[i][0] = f"{"%03d" % x}   "
                line1 += CELL_DRAW[i][0]
                line2 += CELL_DRAW[i][1]
                line3 += CELL_DRAW[i][2]

            line1 += "│"
            line2 += "│"
            line3 += "│"
            x += 1

            print((line1 + "\n" + line2 + "\n" + line3))
            line1, line2, line3 = "".ljust(justif) + "│", "".ljust(justif) + "│", "".ljust(justif) + "│"

    print("".ljust(justif) + "└" + "──────" * 12 + "┘                └" + fg.rs+ "──────" * 13 + "┘")

# Banner.ClearScreen()
# SetupCells()
# Draw_Cells2()