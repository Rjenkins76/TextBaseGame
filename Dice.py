''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random, time
import Banner

###### THIS CODE NOT MINE, INCOPRERATED FROM GITHUB, MODIFIED TO WORK HERE ######


def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)

### ASCII ART FOR THE DICE
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    7: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    8: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
    9: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = ""

### 6 sided dice
class DiceNormalRoller:
    def __init__(self):
        pass
    ### GET THE RANDOM NUMBER FOR A DICE TO LAND ON
    def roll_dice(self,num_dice):
        roll_results = []
        for _ in range(num_dice):
            roll = random.randint(1, 6)
            roll_results.append(roll)
        return roll_results
    def generate_dice_faces_diagram(self,dice_values):

        # Generate a list of dice faces from DICE_ART
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])

        # Generate a list containing the dice faces rows
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string.center(208, " "))

        dice_faces_diagram = "\n".join(dice_faces_rows)
        return dice_faces_diagram

    def diceroller(self,number: int):
        roll_results = self.roll_dice(number)
        result = 0
        for i in range(len(roll_results)):
            result += roll_results[i]
        dice_face_diagram = self.generate_dice_faces_diagram(roll_results)
        Banner.EndColor()
        print(f"{dice_face_diagram} ")
        # print(f"You rolled a {result}".center(208, " "))
        Banner.EndColor()

        return result

### 9 sided dice
class DiceTrapRoller:
    def __init__(self):
        pass
    ### GET THE RANDOM NUMBER FOR A DICE TO LAND ON
    def roll_dice(self,num_dice):
        roll_results = []
        for _ in range(num_dice):
            roll = random.randint(1, 9)
            roll_results.append(roll)
        return roll_results
    def generate_dice_faces_diagram(self,dice_values):

        # Generate a list of dice faces from DICE_ART
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])

        # Generate a list containing the dice faces rows
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string.center(208, " "))

        dice_faces_diagram = "\n".join(dice_faces_rows)
        return dice_faces_diagram

    def diceroller(self,number: int):
        roll_results = self.roll_dice(number)
        result = 0
        for i in range(len(roll_results)):
            result += roll_results[i]
        dice_face_diagram = self.generate_dice_faces_diagram(roll_results)
        Banner.EndColor()
        print(f"{dice_face_diagram} ")
        # print(f"You rolled a {result}".center(208, " "))
        Banner.EndColor()

        return result