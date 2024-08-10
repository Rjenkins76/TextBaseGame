''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import os
import Banner, Player, Levels2

PlayerASCII = ( r"                  __....._             ",
                r"                ,', ,-_  `'.           ",
                r"               ;//  , _,-.\\\          ",
                r"              ;/ //,-'    '._\         ",
                r"             ; // /          \         ",
                r"             |/,-'  ~~~~  ~~~|         ",
                r"             |(( :  <o > \<o |         ",
                r"              \\-        _\  |         ",
                r"               \|            '         ",
                r"                |\    `---- /          ",
                r"               /| '._      /           ",
                r"           ___//|    `----'____        ",
                r"     _,--''      `-._____,'    ```-.   ",
                r"    /                               \  ",)

### GAME MENU FOR GAME AND TO EXIT
def StartMenu():
    Banner.ClearScreen()
    print(Banner.RenderBanner())

    print("\n\n\n")
    Banner.ChangeFOREcolor(91, 190, 254)
    print( "1: Start New Game".center(208, " "))
    Banner.ChangeFOREcolor(53, 53, 53)
    print("2: Load Saved Game".center(208, " ") + "\n")  # Not Implemented
    print("3: Settings       ".center(208, " "))  # Not Implemented
    Banner.ChangeFOREcolor(91, 190, 254)
    print("9: Exit           ".center(208, " "))
    print("\n")
    Banner.ChangeFOREcolor(255,255,0)
    try:
        GameSetupOptions(int(input("Select an option ( 1, 2, 3, or 9): ".rjust(110 + 9, " ")))) # GET USER SELECTED OPTION AND SEND TO COMMANDS
    except ValueError:
        GameSetupOptions(int(input("\nYou must Enter Number 1 or 9: ".rjust(104 + 9, " "))))

### COLLECTS USER OPTION SELECTED AND DISPLAYS NEEDED INFORMATION
def GameSetupOptions(selected_option):
    if selected_option == 1:
        Banner.EndColor()
        Banner.Clear_Line(15)
        Banner.ChangeFOREcolor(255,255,0)
        print("\n" * 2)
        for line in PlayerASCII:
            print(line.center(208," "))
        print("\n" * 4)
        PlayerName = input("What is your name? ".rjust(110, " "))

        Banner.ChangeFOREcolor(91, 190, 254)
        Player.SetupPlayer(PlayerName) # SETUP NEW PLAYER WITH PLAYER NAME
        print(("\n" * 2) + f"{PlayerName} your backpack will start with: ".center(208, " "))

        for item in Player.PlayerInfo.PlayerFood:
            print((item[1] + " - " + item[0]).center(208," "))
        for item in Player.PlayerInfo.PlayerWeapons:
            print((item[1] + " - " + item[0]).center(208," "))

        Banner.ChangeFOREcolor(255,255,0)
        print(("\n" * 3))
        input("Press Enter to Start Game...".rjust(120))
        Banner.EndColor()


        # Banner.Clear_Line(10)
        # print((Player.display_health_bar() + f"  # FOOD ITEMS: {len(Player.PlayerInfo.PlayerFood)}     WEAPONS: {len(Player.PlayerInfo.PlayerWeapons)}").center(208, " ")) # SHOWS INITIAL HEALTH BAR 
        Levels2.start() # SEND TO START OF GAME AT THE FIRST FLOOR
    elif selected_option == 9: # EXIT THE GAME AND TAKE OUT OF FULLSCREEN MODE
        Banner.EndColor()
        os.system('cls')
        # keyboard.press('f11')
        quit()
    else:
        GameSetupOptions(int(input("\nYou must Enter Number 1 or 9: ".rjust(104 + 9, " "))))


