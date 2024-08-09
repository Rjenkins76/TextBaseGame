''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import os, Player
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.utils.graphics import Color, Gradient
from sty import fg, bg



### USING BYTE CHARACTERS TO MOVE THE CARRET UP ONE AND ERASE LINE
def Clear_Line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)
### USING THE STY LIBRARY TO RESET BOTH BACKGROUND AND FOREGROUND
def EndColor():
    print(bg.rs + fg.rs)
### USING OS LIBRARY TO CLEAR THE SCREEN AND RESETTING TEXT COLOR
def ClearScreen():
    os.system('cls')
    EndColor()
### USING THE STY LIBRARY TO CHANGE THE TEXT COLOR - RGB VALUES
def ChangeFOREcolor(R, G, B):
    print(fg(R, G, B))


def BannerText():
    logo1 = "░▒█▀▀█░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▀▀█▀▀░░░▒█▀▀▄░▒█▀▀▀░░░▒█▀▀█░▒█▀▀▀█░▒█▄░▒█░▒█▀▀▀".center(206, " ")
    logo2 = "░▒█░▄▄░▒█▀▀█░▒█░░▒█░░▀▀▀▄▄░░▒█░░░░░▒█▀▀▄░▒█▀▀▀░░░▒█░▄▄░▒█░░▒█░▒█▒█▒█░▒█▀▀▀".center(206, " ")
    logo3 = "░▒█▄▄▀░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░░▒█░░░░░▒█▄▄█░▒█▄▄▄░░░▒█▄▄▀░▒█▄▄▄█░▒█░░▀█░▒█▄▄▄".center(206, " ")

    Line1 = ("│" + logo1 + "│").center(206, " ")
    Line2 = ("│" + logo2 + "│").center(206, " ")
    Line3 = ("│" + logo3 + "│").center(206, " ")
    BottomBorder = "─" * 208 

    return (logo1 + "\n" + logo2 + "\n" + logo3 + "\n" + BottomBorder + "\n")

def BannerText2():
    logo1 = "░▒█▀▀█░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▀▀█▀▀░░░▒█▀▀▄░▒█▀▀▀░░░▒█▀▀█░▒█▀▀▀█░▒█▄░▒█░▒█▀▀▀".center(206, " ")
    logo2 = "░▒█░▄▄░▒█▀▀█░▒█░░▒█░░▀▀▀▄▄░░▒█░░░░░▒█▀▀▄░▒█▀▀▀░░░▒█░▄▄░▒█░░▒█░▒█▒█▒█░▒█▀▀▀".center(206, " ")
    logo3 = "░▒█▄▄▀░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░░▒█░░░░░▒█▄▄█░▒█▄▄▄░░░▒█▄▄▀░▒█▄▄▄█░▒█░░▀█░▒█▄▄▄".center(206, " ")

### USED TO CREATE THE SAME GAME LOGO AS OPENING SCREEN
### WITH THE SAME COLOR EFFECT 
banner_text = ""
def RenderBanner():
    global banner_text
    ClearScreen()
    effect = Print(BannerText()) 
    effect.effect_config.final_gradient_stops = {Color("00ffa2"), Color("5bbeff")}
    effect.terminal_config.frame_rate = 2000 # SPEED OF THE EFFECT - NOT DISPLAYED TO USER - SET HIGH VALUE FOR QUICKER CALCULATIONS
    with effect.terminal_output() as terminal:
        for frame in effect:
            pass
    banner_text += frame # USES LAST FRAME OF EFFECT THAT CONTAINS THE FULL LOGO
    
    return ('\033[1A' + '\x1b[2K')*8 + banner_text
