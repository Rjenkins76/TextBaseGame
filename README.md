IT-140-15969-M01 Introduction to Scripting

PYTHON 3.12.3

Final project for class

#### (INTRO SCREEN) ####
![Screenshot 2024-08-09 165833](https://github.com/user-attachments/assets/14dbef4a-d393-4230-bf14-d8dfa4175d02)
![Screenshot 2024-08-13 135450](https://github.com/user-attachments/assets/60b9b6ad-193a-4b32-ab7e-ac9473759049)

#### (FLOOR MAP EXAMPLE) ####
![Screenshot 2024-08-09 165941](https://github.com/user-attachments/assets/5bc249a9-4097-47cd-90dc-0660cb1675a7)

#### (ENCOUNTER GHOST) ####
![Screenshot 2024-08-13 135535](https://github.com/user-attachments/assets/716e76bb-8220-4c00-86d3-1cfaf8b46c47)

#### (FOUND FOOD ITEM) ####
![Screenshot 2024-08-13 135717](https://github.com/user-attachments/assets/8d27ac21-93df-4c24-9dc5-042c50ab32be)

#### (GHOST AND PLAYER EATING FOOD) ####
![Screenshot 2024-08-13 135615](https://github.com/user-attachments/assets/0ca2a650-b1dd-475b-93d9-7b1713d63bab)

#### (GHOST FIGHT) ####
![Screenshot 2024-08-13 135822](https://github.com/user-attachments/assets/fb90bc7c-debe-4b4d-8686-fece81f2f88f)

#### (FOUND WEAPON) ####
![Screenshot 2024-08-13 135912](https://github.com/user-attachments/assets/cfeea32d-8746-4758-b01b-5e95bd9459b1)

#### (WALK INTO A TRAP) ####
![Screenshot 2024-08-13 140006](https://github.com/user-attachments/assets/eaca1eaf-fd17-4546-a8a8-f29a9f2d180d)


#### (WIN SCREEN) ####
![Screenshot 2024-08-13 135332](https://github.com/user-attachments/assets/ddbf6a7f-4c7f-421f-9086-e3f496099e01)

#### ASCII art was sourced from the internet and not created by myself. ####
#### Professor gave permission to create a more adv version of the game ####

#### KNOWN BUGS ####
1. #### When coming back to map screen, player cell doesn't always show ####
2. 

#### MINIMUM REQUIREMENTS FOR ASSIGNMENT ####
#### Directions
#### In Project One, you designed pseudocode or flowcharts for the two main actions in the game: moving between rooms and gathering items. In this project, you will write the code for the full game based on your designs. You will also need to include some additional components beyond your original designs to help your game work as intended. You will develop all of your code in one Python (PY) file, titled “TextBasedGame.py.”

#### IMPORTANT: The directions include sample code from the dragon-themed game. Be sure to modify any sample code so that it fits the theme of your game.

#### First, create a new file in the PyCharm integrated development environment (IDE), title it “TextBasedGame.py,” and include a comment at the top with your full name. As you develop your code, remember that you must use industry standard best practices including in-line comments and appropriate naming conventions to enhance the readability and maintainability of the code.
#### In order for a player to navigate your game, you will need to develop a function or functions using Python script. Your function or functions should do the following:
#### Show the player the different commands they can enter (such as “go North”, “go West”, and “get [item Name]”).
#### Show the player’s status by identifying the room they are currently in, showing a list of their inventory of items, and displaying the item in their current room.
#### You could make these separate functions or part of a single function, depending on how you prefer to organize your code. 
#### #Sample function showing the goal of the game and move commands
#### def show_instructions():  
####    #print a main menu and the commands
####    print("Dragon Text Adventure Game")
####    print("Collect 6 items to win the game, or be eaten by the dragon.")
####    print("Move commands: go South, go North, go East, go West")
####    print("Add to Inventory: get 'item name'")

#### #In this solution, the player’s status would be shown in a separate function.
#### #You may organize your functions differently.
#### Next, begin developing a main function in your code. The main function will contain the overall gameplay functionality. Review the Project Two Sample Text Game Flowchart, located in the Supporting Materials section, to help you visualize how main() will work.
#### For this step, simply add in a line of code to define your main function, and a line at the end of your code that will run main(). You will develop each of the pieces for main() in Steps #4–7.

#### In main(), create a dictionary linking rooms to one another and linking items to their corresponding rooms. The game needs to store all of the possible moves per room and the item in each room in order to properly validate player commands (input). This will allow the player only to move between rooms that are linked or retrieve the correct item from a room. Use your storyboard and map from Project One to help you create your dictionary.
#### Here is an example of a dictionary for a few of the rooms from the sample dragon text game.
#### #A dictionary linking a room to other rooms
#### #and linking one item for each room except the Start room (Great Hall) and the room containing the villain
#### rooms = {
####    'Great Hall' : { 'South' : 'Bedroom', 'North': 'Dungeon', 'East' : 'Kitchen', 'West' : 'Library' },
####    'Bedroom' : { 'North' : 'Great Hall', 'East' : 'Cellar', 'item' : 'Armor' },
####    'Cellar' : { 'West' : 'Bedroom', 'item' : 'Helmet' },
####    'Dining Room' : { 'South' : 'Kitchen', 'item' : 'Dragon' } #villain
#### }
#### #The same pattern would be used for the remaining rooms on the map.
#### The bulk of the main function should include a loop for the gameplay. In your gameplay loop, develop calls to the function(s) that show the player’s status and possible commands. You developed these in Step #2. When called, the function(s) should display the player’s current room and prompt the player for input (their next command). The player should enter a command to either move between rooms or to get an item, if one exists, from a room.
#### Here is a sample status from the dragon text game:
####    You are in the Dungeon
####    Inventory: []
####    You see a Sword
####    ----------------------
####    Enter your move:
#### As the player collects items and moves between rooms, the status function should update accordingly. Here is another example after a player has collected items from two different rooms:
####    You are in the Gallery
####    Inventory: [‘Sword’, ‘Shield’]
####    --------------
####    Enter your move:
#### Note: If you completed the Module Six milestone, you have already developed the basic structure of the gameplay loop, though you may not have included functions. Review any feedback from your instructor, copy your code into your “TextBasedGame.py” file, make any necessary adjustments, and finish developing the code for the gameplay loop.
#### Within the gameplay loop, you should include decision branching to handle different commands and control the program flow. This should tell the game what to do for each of the possible commands (inputs) from the player. Use your pseudocode or flowcharts from Project One to help you write this code.
#### What should happen if the player enters a command to move between rooms?
#### What should happen if the player enters a valid command to get an item from the room?
#### Be sure to also include input validation by developing code that tells the program what to do if the player enters an invalid command.

#### Note: If you completed the Module Six milestone, you have already developed a portion of this code by handling “move” commands. Review any feedback from your instructor, copy your code into your “TextBasedGame.py” file, make any necessary adjustments, and finish developing the code.
#### The gameplay loop should continue looping, allowing the player to move to different rooms and acquire items until the player has either won or lost the game. Remember that the player wins the game by retrieving all of the items before encountering the room with the villain. The player loses the game by moving to the room with the villain before collecting all of the items. Be sure to include output to the player for both possible scenarios: winning and losing the game.

#### Hint: What is the number of items the player needs to collect? How could you use this number to signal to the game that the player has won? 
#### Here is a sample from the dragon text game of the output that will result if the player wins the game:
####    Congratulations! You have collected all items and defeated the dragon!
####    Thanks for playing the game. Hope you enjoyed it. 
#### If the player loses the game, they will see the following output:
####    NOM NOM...GAME OVER!
####    Thanks for playing the game. Hope you enjoyed it.
#### Note: If you completed the Module Six milestone, the gameplay loop ended through the use of an “exit” room. You will need to remove the “exit” room condition and adjust the code so that the game ends when the player either wins or loses, as described above.
#### As you develop, you should be sure to debug your code to minimize errors and enhance functionality. After you have developed all of your code, be sure to run the code and use the map you designed to navigate through the rooms, testing to make sure that the game is working correctly. Be sure to test different scenarios such as the following:
#### What happens if the player enters a valid direction? Does the game move them to the correct room?
#### When the player gets an item from a room, is the item added to their inventory?
#### What happens if the player enters an invalid direction or item command? Does the game provide the correct output?
#### What happens if the player wins the game? What happens if the player loses the game? 

####
