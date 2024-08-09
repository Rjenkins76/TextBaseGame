''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import Banner,GhostASCII
from sty import fg, bg, ef, rs

printWin = (
            " __      __  ______  __    __      __       __ ______ __    __ ",
            "|  \\    /  \\/      \\|  \\  |  \\    |  \\  _  |  \\      \\  \\  |  \\",
            " \\▓▓\\  /  ▓▓  ▓▓▓▓▓▓\\ ▓▓  | ▓▓    | ▓▓ / \\ | ▓▓\▓▓▓▓▓▓ ▓▓\\ | ▓▓",
            "  \\▓▓\\/  ▓▓| ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓/  ▓\\| ▓▓ | ▓▓ | ▓▓▓\\| ▓▓",
            "   \\▓▓  ▓▓ | ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓  ▓▓▓\\ ▓▓ | ▓▓ | ▓▓▓▓\\ ▓▓",
            "    \\▓▓▓▓  | ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓ ▓▓\\▓▓\\▓▓ | ▓▓ | ▓▓\\▓▓ ▓▓",
            "    | ▓▓   | ▓▓__/ ▓▓ ▓▓__/ ▓▓    | ▓▓▓▓  \\▓▓▓▓_| ▓▓_| ▓▓ \\▓▓▓▓",
            "    | ▓▓    \\▓▓    ▓▓\\▓▓    ▓▓    | ▓▓▓    \\▓▓▓   ▓▓ \\ ▓▓  \\▓▓▓",
            "     \\▓▓     \\▓▓▓▓▓▓  \\▓▓▓▓▓▓      \\▓▓      \\▓▓\\▓▓▓▓▓▓\\▓▓   \\▓▓")

def DisplayLOSEGame():
    Banner.ClearScreen()
    print(fg(250, 100, 100))
    print("\n" * 5)
    print("  ▄· ▄▌      ▄• ▄▌  ·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄    ".rjust(130))
    print(" ▐█▪██▌ ▄█▀▄ █▪██▌  ██▪ ██ ██ ▀▄.▀·██▪ ██   ".rjust(130))
    print(" ▐█▌▐█▪▐█▌.▐▌█▌▐█▌  ▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌  ".rjust(130))
    print("  ▐█▀·.▐█▌.▐▌▐█▄█▌  ██. ██ ▐█▌▐█▄▄▌██. ██   ".rjust(130))
    print("   ▀ •  ▀█▄▀▪ ▀▀▀   ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀•   ".rjust(130))
    print("\n" * 5)
    print(fg.rs)
    for i in GhostASCII.printReaper:
        print(i.rjust(130))
    print("\n" * 6)

def DisplayWINGame():
    Banner.ClearScreen()
    print(fg(100,255,100))
    print("\n" * 5)
    for i in printWin:
        print(i.center(208," "))
    print("\n" * 5)
    print(fg.rs)
    for i in GhostASCII.printBoss1Face:
        print(i.center(208," "))
    print("\n" * 6)

                                                          
                                                   
 