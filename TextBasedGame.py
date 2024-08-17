''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import ctypes, os , keyboard
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.utils.graphics import Color, Gradient
from GameMenu import StartMenu
from sty import fg, bg, ef, rs

### USED TO DISPLAY A MESSAGEBOX TO USER FOR SETTINGS NEEDED TO PLAY GAME
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

Mbox('GHOST BE GONE', 'Please run game with the following setup:\n\n1. Windows Command Prompt\n2. Fullscreen - (columns=209, lines=51)\n3. Using fonts:\n          "Cascadia Mono" Size: 11                    \n                    OR\n          "Consolas" Size 12', 0)
#
keyboard.press('f11')

def ClearScreen():
    os.system('cls')
    # EndColor()

#region START GAME SCRIPTS
text = (
         "\n"*12 + "".ljust(70) + "░▒█▀▀█░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▀▀█▀▀░░░▒█▀▀▄░▒█▀▀▀░░░▒█▀▀█░▒█▀▀▀█░▒█▄░▒█░▒█▀▀▀"
             "\n" + "".ljust(70) +"░▒█░▄▄░▒█▀▀█░▒█░░▒█░░▀▀▀▄▄░░▒█░░░░░▒█▀▀▄░▒█▀▀▀░░░▒█░▄▄░▒█░░▒█░▒█▒█▒█░▒█▀▀▀"
             "\n" + "".ljust(70) +"░▒█▄▄▀░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░░▒█░░░░░▒█▄▄█░▒█▄▄▄░░░▒█▄▄▀░▒█▄▄▄█░▒█░░▀█░▒█▄▄▄"
             "\n\n"
             "\n" + "".ljust(77) +  r"                             ,-.                              "
             "\n" + "".ljust(77) +  r"        ___,---.__          /'|`\          __,---,___         "
             "\n" + "".ljust(77) +  r"     ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.      "
             "\n" + "".ljust(77) +  r"   ,'        |           ~'\     /`~           |        `.    "
             "\n" + "".ljust(77) +  r"  /      ___//              `. ,'          ,  , \___      \\  "
             "\n" + "".ljust(77) +  r" |    ,-'   `-.__   _         |        ,    __,-'   `-.    |  "
             "\n" + "".ljust(77) +  r" |   /          /\_  `   .    |    ,      _/\          \   |  "
             "\n" + "".ljust(77) +  r" \  |           \ \`-.___ \   |   / ___,-'/ /           |  /  "
             "\n" + "".ljust(77) +  r"  \  \           | `._   `\\  |  //'   _,' |           /  /   "
             "\n" + "".ljust(77) +  r"   `-.\         /'  _ `---'' , . ``---' _  `\         /,-'    "
             "\n" + "".ljust(77) +  r"      ``       /     \    ,='/ \`=.    /     \       ''       "
             "\n" + "".ljust(77) +  r"              |__   /|\_,--.,-.--,--._/|\   __|               "
             "\n" + "".ljust(77) +  r"              /  `./  \\`\ |  |  | /,//' \,'  \\              "
             "\n" + "".ljust(77) +  r"             /   /     ||--+--|--+-/-|     \   \\             "
             "\n" + "".ljust(77) +  r"            |   |     /'\_\_\ | /_/_/`\     |   |             "
             "\n" + "".ljust(77) +  r"             \   \__, \_     `~'     _/ .__/   /              "
             "\n" + "".ljust(77) +  r"              `-._,-'   `-._______,-'   `-._,-'               "
             "\n\n" + "".ljust(37) +  "AS A RENOWNED PARANORMAL INVESTIGATOR, YOU ARE HIRED TO EXPLORE THE LONG-ABANDONED RAVENSWOOD HOSPITAL, RUMORED TO BE HAUNTED BY THE MALEVOLENT"
             "\n" + "".ljust(37) +  "SPIRIT OF ALASTOR, A FORMER PATIENT WHO DIED UNDER MYSTERIOUS CIRCUMSTANCES. YOUR TEAM CAPTURES EVIDENCE OF ALASTOR'S PRESENCE, BUT SOON REALIZES THAT"
             "\n" + "".ljust(37) +  "HE'S NOT THE ONLY ENTITY LURKING IN THE SHADOWS." 
             "\n\n" + "".ljust(37)+ "AS YOU DIG DEEPER, YOU UNCOVER A DARK HISTORY OF PATIENT ABUSE AND EXPERIMENTATION BY THE HOSPITAL'S FORMER STAFF. YOU BECOMES OBSESSED WITH UNCOVERING"
             "\n" + "".ljust(37) +  "THE TRUTH, CONVINCED THAT ALASTOR'S SPIRIT IS A MANIFESTATION OF THE HOSPITAL'S DARK PAST. HOWEVER, YOU START TO EXPERIENCE STRANGE AND TERRIFYING"
             "\n" + "".ljust(37) +  "OCCURRENCES,HINTING THAT ALASTOR MAY NOT BE THE ONLY THREAT.")

text2 = ("\n"*12 + "".ljust(70) + "░▒█▀▀█░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▀▀█▀▀░░░▒█▀▀▄░▒█▀▀▀░░░▒█▀▀█░▒█▀▀▀█░▒█▄░▒█░▒█▀▀▀"
             "\n" + "".ljust(70) +"░▒█░▄▄░▒█▀▀█░▒█░░▒█░░▀▀▀▄▄░░▒█░░░░░▒█▀▀▄░▒█▀▀▀░░░▒█░▄▄░▒█░░▒█░▒█▒█▒█░▒█▀▀▀"
             "\n" + "".ljust(70) +"░▒█▄▄▀░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░░▒█░░░░░▒█▄▄█░▒█▄▄▄░░░▒█▄▄▀░▒█▄▄▄█░▒█░░▀█░▒█▄▄▄"
             "\n\n\n\n\n" +        
            "".ljust(37) + "As you explore this hospital, you will find many ghost and 3 demonic spirits. You must fight the 3 demonic spirits (Bosses) to win the game."
            "\n\n" + "".ljust(37) + "Along the way, you will find food that you can use to increase your health, or you can use it to feed the ghost. If you feed the ghost they may"
            "\n" + "".ljust(37) + "just drop extra items to help defeat the bosses"
            "\n\n" + "".ljust(37) + "You will also uncover weapons that you can use to fight the ghost and spirits, if you are lucky enough to find the spirit catcher your job will be" 
            "\n" + "".ljust(37) + "easier to kill the ghost and will help killing the spirit of Alastor."
            "\n\n" + "".ljust(37) + "You will make your moves using the number pad arrow keys, you may press the ‘F’ Button to see your food items or the ‘W’ Button to list your weapons at any time.")

printBasicGhost = ( "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿   ⢿⣿⡿⣿⣿⡆⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀ ⣿⡇⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀" + "\n" + "".rjust(87) +
                    "      ⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀" + "\n" + "".rjust(87) +
                    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + "\n" +  "".rjust(87) +
                    "          ⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
#endregion

#region START SCREEN
ClearScreen()
effect = Print(text)
effect.effect_config.final_gradient_stops = {Color("00ffa2"), Color("5bbeff")}
effect.terminal_config.frame_rate = 1000  # SPEED FOR THE ANIMATION
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)
    # terminal.print(text)

print("\n" * 9)
print(fg(255,255,0)) # CHANGE TEXT COLOR TO YELLOW
input("Press Enter to Continue...".rjust(120))
print(fg.rs) # RESET TEXT COLOR TO DEFAULT
#endregion

#region RULES

ClearScreen()
effect = Print(text2 + "\n\n\n" + printBasicGhost)
effect.effect_config.final_gradient_stops = {Color("00ffa2"), Color("5bbeff")}
effect.terminal_config.frame_rate = 1000 # SPEED FOR THE ANIMATION
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)
    # terminal.print(text)


print("\n\n\n")
print(fg(255,255,0)) # CHANGE TEXT COLOR TO YELLOW
input("Press Enter to Continue...".rjust(115))
print(fg.rs) # RESET TEXT COLOR TO DEFAULT
#endregion

StartMenu()




