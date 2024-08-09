''' ROGER JENKINS
    IT-140-15969-M01 Introduction to Scripting
    PYTHON 3.12.3
    PROFESSOR: Ben Payeur, M.S, P.E   '''

import random, textwrap

namesMale = ['Liam Miller','Gary Monroe', 'Mike Bailey', 'John Anderson','David Roman', 'Wade Gross', 'Eli Hunter', 'Kenneth Gray', 'Ronnie Dunn', 'Alan Wood']
nameFemale = ['Fiona Smith', 'Shauna Watson', 'Taylor Rollins','Mandy Hobbs', 'Sonya Parks', 'Ann Craven', 'Mary Franks', 'Gail Bennet','Susan Day', 'Linda Hill']

GhostStoryMale = ["In the midst of a fierce battle, a young soldier named {NAME} valiantly fought alongside his comrades against a formidable enemy army. Despite his bravery and skills on the battlefield, fate had a cruel twist for {NAME}, as he fell victim to a surprise attack that ultimately claimed his life.",
                  "{NAME} fought valiantly in the Mexican-American War (1846-1848), commended for his bravery and exceptional skill on the battlefield.  However, the war took a heavy toll on his body; he was injured during a battle that left him with a debilitating limp.  In 1850, as {NAME}'s health worsened, he found himself at the mercy of a violent fever, eventually succumbing to his injuries.  He died at the age of 20, never to witness the fruits of his labor.",
                  "Captain {NAME} was given command of a battalion, tasked to aid in quelling a rebellion During this time, their forces faced significant losses,but Captain {NAME} remained a pillar of strength, leading his men fearlessly into each battle. It was during one such battle in which Captain {NAME}  met his end. In an attempt to save his men during a surprise attack, he was fatally wounded and took his final breath on the battlefield.",
                  ]

GhostStoryFemale = ["{NAME}'s most impactful experience came in 1863 when her village was caught in the crossfire of a battle. A cannonball exploded near her, and a shard of debris pierced her heart. {NAME} died on the scene, too young to understand the progression of the war or the cruel realities it brought.",
                    "{NAME}'s life was marked by the harsh realities of poverty and the dangers of the coal mining industry. The most significant event was the day of the skirmish where a stray bullet found its way to her home, taking her life. This event left her family and the whole community in a state of shock and mourning.",
                    "{NAME}'s life was marked by the harsh realities of poverty and the dangers of the coal mining industry. The most significant event was the day of the skirmish where a stray bullet found its way to her home, taking her life. This event left her family and the whole community in a state of shock and mourning."]

####### Ghost Information ########
# Ghost_Name
# Ghost_Story
# Ghost_Story_SPLIT
# Ghost_location_on_Grid
# Ghost_HP
# Ghost_DropItem
# Ghost_KillItems
# Ghost_ASCII_Art
###################################
Ghost_List = []

class Ghost1:
    def __init__(self,sex):
        if sex == "male":
            self.name = random.choice(namesMale)
            namesMale.remove(self.name)
            story_info = self.Create_Ghost_Story(sex)
            self.story = story_info[0]
            self.story_lines = story_info[1]
            self.location = 0
            self.drop_item = []
            self.kill_items = []
            self.Ghost_HP = 75
            self.ASCII_art = ""

        if sex == "female":
            self.name = random.choice(nameFemale)
            nameFemale.remove(self.name)
            story_info = self.Create_Ghost_Story(sex=sex)
            self.story = story_info[0]
            self.story_lines = story_info[1]
            self.location = 0
            self.drop_item = []
            self.kill_items = []
            self.Ghost_HP = 75
            self.ASCII_art = ""

    def Create_Ghost_Story(self,sex):
        if sex == "male":
            story = random.choice(GhostStoryMale)
            Ghost_Story = story.replace("{NAME}", self.name)
            Ghost_Story_SPLIT = self.SplitLines(Ghost_Story)

        if sex == "female":
            story = random.choice(GhostStoryMale)
            Ghost_Story = story.replace("{NAME}", self.name)
            Ghost_Story_SPLIT = self.SplitLines(Ghost_Story)
        
        return [Ghost_Story,Ghost_Story_SPLIT]
    
    def SplitLines(self,Ghost_Story):
        sentence = []
        IntroScripts = Ghost_Story
        wrapper = textwrap.TextWrapper(width=125)
        word_list = wrapper.wrap(text=IntroScripts)
        for element in word_list:
            sentence.append(element)
        return sentence

def SetupGhost(number_needed):
    for i in range(number_needed):
        sex = ["male","female"]
        ghost = Ghost1(random.choice(sex))
        Ghost_List.append(ghost)

# SetupGhost(1)
# for i in Ghost_List:
#     print(i.name, i.story)