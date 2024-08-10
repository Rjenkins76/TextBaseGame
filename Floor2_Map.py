''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random
import Ghost, Banner
from sty import fg, bg, ef, rs

Width = 28
Height = 11
Room_List = []
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
       f"  🥖  ",   # FOOD ITEM
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

Walkable_Cells = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 59, 60, 67, 68, 75, 76, 83, 87, 88, 95, 96, 103, 104, 111, 115, 116, 123, 124, 131, 132, 139, 143, 144, 151, 152, 159, 160, 167, 171, 172, 179, 180, 187, 188, 195, 199, 200, 207, 208, 215, 216, 223, 227, 228, 235, 236, 243, 244, 251, 255, 256, 263, 264, 271, 272,  279, 283, 284, 291, 292, 299, 300, 307]

Room_Doors = [86,89,94,97,102,105,110,170,173,178,181,186,189,194,254,257,262,265,270,273,278]

def SetupCells():
    for x in range((Width * Height) + 4):
        CELL_DRAW.append([CELLS[1][0], CELLS[1][1], CELLS[1][2]])

def Draw_Cells2():
    x, y, z, a = 0, 1, 48, 73
    # Banner.ClearScreen()
    Banner.EndColor()
    get_header_Length = len("┌" + "──────" * 12 + "┬────────────────┬" + "──────" * 13 + "┐")
    justif = int((208 / 2) - (get_header_Length / 2))
    print("".ljust(justif) + "┌" + "──────" * 12 + fg(255,255,0) + "┬────────────────┬" + fg.rs+ "──────" * 13 + "┐")
    line1, line2, line3 = "".ljust(justif) + "│", "".ljust(justif) + "│", "".ljust(justif) + "│"

    Empty_Cell_List = [56,57,64,65,70,92,93,84,85,148,149,154,140,140,176,177,232,233,168,169,224,260,261,225,238,252,253,72,73,100,101,156,157,184,185,240,241,268,269,98,182,193,248,249,276,277,62,90,146,174,230,258,78,106,162,190,246,274]

    LEFT_BORDER_CELL = [58,91,142,175,226,259,66,150,234,74,158,242,82,166,250,63,147,231,71,99,155,183,239,267,79,107,163,191,247,275,119,203,287,127,211,295,135,219,303]

    LEFT_CORNER_CELL = [114,198,282,122,206,290,130,214,298,138,222,306]

    BOTTOM_BORDER_CELL = [112,113,196,197,280,281,120,121,204,205,288,289,128,129,212,212,296,297,136,137,220,221,118,202,286,126,210,294,134,218,302]

    RIGHT_BORDER_CELL = [61, 145, 229, 69, 153, 237, 77, 161, 245]

    RIGHT_CORNER_BORDER = [117, 201, 285, 125, 209, 293, 133, 217, 301]

    for i in range(len(CELL_DRAW)):
        if y < Width:

#region STAIRS
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
#endregion

#region RIGHT CORNER ROOMS
            elif i in Empty_Cell_List:
                line1 += CELLS[1][0]
                line2 += CELLS[1][1]
                line3 += CELLS[1][2]
            elif i in LEFT_BORDER_CELL:
                line1 += CELLS[2][0]
                line2 += CELLS[2][1]
                line3 += CELLS[2][2]
            elif i in BOTTOM_BORDER_CELL:
                line1 += CELLS[4][0]
                line2 += CELLS[4][1]
                line3 += CELLS[4][2]
            elif i in LEFT_CORNER_CELL:
                line1 += CELLS[3][0]
                line2 += CELLS[3][1]
                line3 += CELLS[3][2]


# endregion

#region LEFT CORNER ROOMS
            elif i in RIGHT_BORDER_CELL:
                line1 += CELLS[5][0]
                line2 += CELLS[5][1]
                line3 += CELLS[5][2]
            elif i in RIGHT_CORNER_BORDER:
                line1 += CELLS[6][0]
                line2 += CELLS[6][1]
                line3 += CELLS[6][2]
            elif i in LEFT_BORDER_CELL:
                line1 += CELLS[2][0]
                line2 += CELLS[2][1]
                line3 += CELLS[2][2]
            elif i in Empty_Cell_List:
                line1 += CELLS[1][0]
                line2 += CELLS[1][1]
                line3 += CELLS[1][2]
            elif i in BOTTOM_BORDER_CELL:
                line1 += CELLS[4][0]
                line2 += CELLS[4][1]
                line3 += CELLS[4][2]
            elif i in LEFT_CORNER_CELL:
                line1 += CELLS[3][0]
                line2 += CELLS[3][1]
                line3 += CELLS[3][2]
# endregion

            else:
                # CELL_DRAW[i][0] = f"{"%03d" % x}   "
                line1 += CELL_DRAW[i][0]
                line2 += CELL_DRAW[i][1]
                line3 += CELL_DRAW[i][2]

            x += 1
            y += 1
        elif y == Width:
            y = 1
            # CELL_DRAW[i][0] = f"{"%03d" % x}   "
            line1 += CELL_DRAW[i][0]
            line2 += CELL_DRAW[i][1]
            line3 += CELL_DRAW[i][2]

            line1 += "│"
            line2 += "│"
            line3 += "│"
            x += 1
            print((line1 + "\n" + line2 + "\n" + line3))
            if i == 55:
                print("".ljust(justif) + "├─────────────────┐            ┌────────────────┬─────────────────┐            ┌────────────────┬─────────────────┐            ┌────────────────┬─────────────────┐      │")
            line1, line2, line3 = "".ljust(justif) + "│", "".ljust(justif) + "│", "".ljust(justif) + "│"

    print("".ljust(justif) + "├─────────────────┴────────────┴────────────────┴─────────────────┴────────────┴────────────────┴─────────────────┴────────────┴────────────────┴─────────────────┴──────┘")

def Assign_Ghost(reassign):
    if not reassign:
        x = 0
        while x < len(Ghost.Ghost_List):
            ghost_cell = random.choice(Walkable_Cells)
            CELL_DRAW[ghost_cell][0] = CELLS[9][0]
            CELL_DRAW[ghost_cell][1] = CELLS[9][1]
            CELL_DRAW[ghost_cell][2] = CELLS[9][2]
            x += 1
        x = 0
        while x < 5:
            food_cell = random.choice(Walkable_Cells)
            CELL_DRAW[food_cell][0] = CELLS[8][0]
            CELL_DRAW[food_cell][1] = CELLS[8][1]
            CELL_DRAW[food_cell][2] = CELLS[8][2]

            x += 1
        x = 0
        while x < 5:
            weapon_cell = random.choice(Walkable_Cells)
            CELL_DRAW[weapon_cell][0] = CELLS[10][0]
            CELL_DRAW[weapon_cell][1] = CELLS[10][1]
            CELL_DRAW[weapon_cell][2] = CELLS[10][2]
            x += 1
    else:
        for _ghost in range(len(Ghost.Ghost_List)):
            current = Ghost.Ghost_List[_ghost]
            current2 = current.location
            CELL_DRAW[current2] = [CELLS[1][0], CELLS[1][1], CELLS[1][2]]
            Ghost.Ghost_List[_ghost].location = 0
            z = random.randrange(1, len(CELL_DRAW))
            if CELL_DRAW[z][1] == "      ":
                CELL_DRAW[z] = [CELLS[9][0], CELLS[9][1], CELLS[9][2]]
                Ghost.Ghost_List[_ghost].location = z

def Assign_Bosses():
    x = 1
    while x < 3:
        ghost_cell = random.choice(Room_Doors)
        CELL_DRAW[ghost_cell][0] = CELLS[12][0]
        CELL_DRAW[ghost_cell][1] = CELLS[12][1]
        CELL_DRAW[ghost_cell][2] = CELLS[12][2]
        x += 1

    while x == 3:
        ghost_cell = random.choice(Room_Doors)
        CELL_DRAW[ghost_cell][0] = CELLS[13][0]
        CELL_DRAW[ghost_cell][1] = CELLS[13][1]
        CELL_DRAW[ghost_cell][2] = CELLS[13][2]
        x += 1



