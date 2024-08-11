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
                  "{NAME} bravely fought in the retreat from Corunna, but a stray bullet brought an abrupt and unexpected end to his life. This time, he did not find peace in death. His spirit remained tethered to the earth, unable to move on because of the unresolved grief and the unfulfilled yearning for peace.",
                  "Fighting in a critical battle near Fort Niagara, {NAME} receives a mortal wound from a musket ball that lodges itself in his abdomen. Despite being offered a chance to retreat, he refuses, encouraging his soldiers to push forward. {NAME} dies a hero's death on the battlefield with thoughts of Ellen and his family still filling his mind.",
                  "One fateful day, during a critical mission, {NAME}'s unit came under heavy fire. As his fellow soldiers fell around him, {NAME} fought with a fierce determination to protect them. In a moment of heroic sacrifice, he threw himself in front of a grenade, saving the lives of his comrades but losing his own in the process.",
                  "One fateful day, during a desperate battle, {NAME} made the ultimate sacrifice, giving his life to save his fellow soldiers. As he lay dying on the battlefield, his eyes filled with a mixture of regret and acceptance, he made a solemn vow to continue his fight, even in death.",
                  "Tragically, {NAME}'s life was cut short during a particularly brutal battle, his body left to the elements on the battlefield. Yet, even in death, his spirit refused to rest, forever bound to the horrors he had experienced.Now, as a restless ghost, {NAME} wanders the earth, his soul consumed by the unresolved anguish of his past. He is driven by a deep desire to find meaning in the senseless violence he witnessed, to somehow make sense of the sacrifices he and his fellow soldiers made.",
                  "Tragically, {NAME}'s service came to a tragic end when, during a fierce skirmish, he was struck down by enemy fire. Though his body succumbed to the wounds, his spirit refused to depart, leaving him forever trapped in a ghostly limbo, condemned to walk the earth as a restless specter.",
                  "{NAME}'s dedication to his work became an unhealthy obsession, as he sought to find a way to cheat death and Driven to the brink of madness, {NAME} conducted a series of unethical experiments, crossing moral and ethical boundaries in his desperate attempt to unlock the secrets of the afterlife. Tragically, his reckless actions resulted in a devastating fire that claimed his own life, leaving him trapped in a limbo between the world of the living and the dead."]

GhostStoryFemale = ["{NAME}'s most impactful experience came in 1863 when her village was caught in the crossfire of a battle. A cannonball exploded near her, and a shard of debris pierced her heart. {NAME} died on the scene, too young to understand the progression of the war or the cruel realities it brought.",
                    "{NAME}'s life was marked by the harsh realities of poverty and the dangers of the coal mining industry. The most significant event was the day of the skirmish where a stray bullet found its way to her home, taking her life. This event left her family and the whole community in a state of shock and mourning.",
                    "In 1900, a devastating diphtheria outbreak hit the lower east side. Despite the dangerous conditions, {NAME} threw herself into her work, caring for the sick and dying. Unfortunately, she contracted the disease herself and succumbed to it within a week.",
                    "{NAME}'s life took a tragic turn when a deadly outbreak of influenza swept through the city. Despite her best efforts, Nancy watched helplessly as many of her patients succumbed to the illness. Overcome with grief and a sense of failure, Nancy fell ill herself, and within a matter of days, she passed away, her own life claimed by the devastating pandemic.",
                    "{NAME} volunteered to serve as a nurse in the trenches, where she tirelessly attended to the wounded soldiers, providing comfort and critical care amidst the chaos of battle. {NAME}'s life was cut short when she contracted a deadly illness while caring for a patient. Despite the heroic efforts of her fellow nurses, {NAME} succumbed to the illness and passed away, leaving behind a legacy of selflessness and a profound impact on those whose lives she had touched.",
                    "One fateful night, while attempting to assist a group of homeless children, {NAME} was caught in the crossfire of a violent altercation. Tragically, she succumbed to her injuries, her life snuffed out before she could realize her dreams of a better future.",
                    "One fateful night, a devastating fire swept through the weapons factory where {NAME} worked, trapping countless workers inside. In a desperate attempt to save her colleagues, {NAME} rushed back into the burning building, her selfless act of heroism ultimately costing her her own life.",
                    "{NAME}s service was cut short when a mortar strike claimed her life in the final days of the war. In her final moments, she was haunted by the horrors she had witnessed and the lives she had been unable to save. Her spirit, unable to find peace, remained tethered to the battlefield, becoming a ghostly presence that would linger for decades to come.",
                    "One fateful day, as {NAME} tended to the wounded on the front lines, a devastating explosion ripped through the makeshift hospital, claiming the lives of countless soldiers and civilians, including {NAME} herself. In the aftermath of the tragedy, her spirit refused to be extinguished, and {NAME} found herself trapped between the realms of the living and the dead, a ghost haunted by the memories of the war and the loved ones she had lost.",
                    "Tragically, {NAME}'s life was cut short when a mortar strike hit the medical tent she was working in. She died instantly, never having the chance to return home and live out the life she had dreamed of. But in the moments before her death, {NAME} found solace in the knowledge that she had given everything she had to help her fellow soldiers.",]

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
            # namesMale.remove(self.name)
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
            # nameFemale.remove(self.name)
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