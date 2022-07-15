
## IMPORTS ##
import random
import time

## STATS ##

char_stats = {"Health": 100,
              "Stamina": 100,
              "Strength": 10,
              "Intelligence": 10,
              "Discipline": 10,
              "Storage": 0}

fw_dmg = 10
defo_dmg = 10
cc_dmg = 20

fire_dmg = 10

force_field = 100

random_int = 0
scottie = ''

## END MESSAGE ##
end_message = ("The creator sincerely hopes you have enjoyed playing Climate Change: 2090. Of course, everything stated in the game was purely fictitious, but the game was intended to teach all users about one important message: climate change. It is an unavoidable issue, and one that is slowly degrading the world we live in. There is no way to reverse the effects, but as long as we work together, united, hand-in-hand, we can slow down, or even halt the impending doom brought through climate change. We can't bring back extinct animals and plants, nor can we make the ice that has melted at the North And South Poles reform, but preventing even more of the irreversible damage from happening should be our collective effort. Thank you for playing the game and the creator hopes you had fun. Take care of the environment, one step at a time, one person at a time. \n \n=WS=")

# GAME #

print("Welcome to Climate Change: 2090!")
time.sleep(1)
print(input("To start the game, click enter"))

print(input("How to play: answer the questions and click enter to carry on with the game. That's all, enjoy ;)"))

name = input("For a start, enter your name: ")
while len(name) < 1:
    name = input("For a start, enter your name: ")
    
print(input("NARATOR: You wake up in an unknown land. Glancing around, all you see for miles around is baren land.\nSuddenly, a man stumbles out from a portal. He looks you up and down for a second before his eyes widens."))
print(input("???: There has been a rumour circulating around about you, {}, so tell me more about yourself.".format(name)))

gender = input("Enter your character's gender: ")
while len(gender) < 1:
    gender = input("Enter your character's gender: ")
home_town = input("Enter your character's home town: ")
while len(home_town) < 1:
    home_town = input("Enter your character's home town: ")

print(input("YOU: I am {}, as you already know, and I identify as a {}. I come from {}.".format(name, gender, home_town)))
print(input("RAYDEN: My name is Rayden, and I'm here to help you save our world."))
print(input("NARRATOR: Rayden pans his hands out to the barren lands behind him."))
print(input("RAYDEN: There has been monsters raging on Earth, and much of humanity has been wiped out. \nHumans has advanced so much in technology that we can teleport and control things with our minds but all these takes up a lot of fosil fuels, and that's our problem. \n Only you have the power to reverse the effects. Do us proud my fellow human."))
print(input("NARRATOR: Just as you are about to ask the millions of questions storming in your head, a hideous looking monster manifests, seemingly out of thin air."))
print(input("YOU: What is that! And the smell too!"))
print(input("NARRATOR: You cover your nose, backing away from the monster."))
print(input("RAYDEN: That is Food Waste, one of the overlooked mosters. It may seem small and insignificant, but actually 1.3 billion tons of edible food is wasted yearly, which is enough to feed 3 billion people!\nEverytime we waste food, it adds up to its power. It doesn't eat flora and fauna like its parent, Climate Change, but it helps Climate Change become stronger as well, making it dangerous in its own way."))
print(input("NARRATOR: Just as Rayden finishes explaining, as if on cue, Food Waste jumps at you. You cover your face with your hands as it collides with your body.\n Food scatters all around you, making you almost puke. You then notice the watch on your wrist start to vibrate."))
print(input("YOU: What is going on? Why is the watch vibrating?"))
print(input("RAYDEN: That is the Watch-O-Clock, and there's only 1 of them built in the world, and you are the one who has it."))
print(input("NARRATOR: You look at the Watch-O-Clock in awe as a notification pops up."))
print(input("WATCH-O-CLOCK: -YOU HAVE BEEN POISONED- \n -YOUR HEALTH IS DROPPING-"))
char_stats["Health"] = char_stats["Health"] - fw_dmg
print(input("WATCH-O-CLOCK: -Your health has been reduced by {}. Your health is now at {}.-".format(fw_dmg, char_stats['Health'])))
print(input("YOU: What! Rayden! What is all this?"))
print(input("RAYDEN: It says you're poisoned, here take this antidote, it'll stop the poison."))
choice1 = input("~CHOICE~: Drink antidote? (Type Y for yes and N for N to indicate your choice) ")

while choice1 != 'N' or choice1 != 'Y' or choice1 != 'n' or choice1 != 'y':
    if choice1 == 'N' or choice1 == 'Y' or choice1 != 'n' or choice1 != 'y':
        break
    choice1 = input("~CHOICE~: Drink antidote? (Type Y for yes and N for N to indicate your choice) ")

if choice1 == 'N' or 'n':
    char_stats["Health"] = char_stats["Health"] - fw_dmg
    print(input("WATCH-O-CLOCK: -Your health has been reduced by {}. Your health is now at {}.-".format(fw_dmg, char_stats['Health'])))
    print(input("NARRATOR: You decide not to drink the antitode."))
    char_stats["Health"] = char_stats["Health"] - fw_dmg
    print(input("WATCH-O-CLOCK: -Your health has been reduced by {}. Your health is now at {}.-".format(fw_dmg, char_stats['Health'])))
    print(input("NARRATOR: You lurch forward as a pounding headache assults you. You clutch your head in pain as Rayden chides you for your judgement. He catches you before you fall and lifts the antitode to your mouth. You have no choice but to drink it. Whatever your reason for not drinking the antitode, you mentally conclude that drinking the antitode could have saved you this lightheadedness and pain ricocheting through your chest."))
    print(input("Finally, the Watch-O-Clock stops vibrating. You still feel a little sick, but you you are regaining your strength."))
    print(input("RAYDEN: Hey, {}, you ok there?".format(name)))
    print(input("YOU: Yea, thanks for the antitode. Sorry I didn't drink it at first."))
    print(input("RAYDEN: Please be more careful next time. These kind of things can snowball."))
    print(input("NARRATOR: He smiles kindly at you and tucks his hands, that have been suporting you for the past minute, into his pockets. You think you saw a light shade of pink on his cheeks, but it could be just the remaining posion in your system clouding your eyes."))
elif choice1 == 'Y' or 'y':
    print(input("NARRATOR: You decide to drink the antidote, and the Watch-O-Clock stops vibrating."))
    print(input("WATCH-O-CLOCK: -YOUR CURRENT HEALTH IS {}.-".format(char_stats["Health"])))
    print(input("RAYDEN: Good choice. Did the posion get to you?"))
    print(input("YOU: No, thanks for offering the antitode. Without it, I think I might have been on the ground already."))
    print(input("NARRATOR: He smiles sheepishly and waves it off. You think you saw a light shade of pink on his cheeks, but it could've have just been the heat getting to him."))

print(input("YOU: How about all these food on the floor? What should we do with these?"))
print(input("RAYDEN: There are 3 things you can do. \nFirstly, you can eat them. It will increase your stamina, but your health may decrease because the food may have been out for long and it has been mixed with each other. \nSecondly, you can store them up for later, and it'll fill up your storage, but it might not be food you should be saving, and you don't have the adaquate food storage capability. \nThirdly, you can sweep it altogether. This will increase your strength, but will decrease your stamina. This will also rebuild the Food Waste monster, but you get to practice and hone your skills against the monsters."))
choice2 = input("~CHOICE~: What will you do with the scattered food? (Type 1 for eat, 2 for store or 3 for sweep) ")

while choice2 != '1' or choice2 != '2' or choice2 != '3':
    if choice2 == '1' or choice2 == '2' or choice2 == '3':
        break
    choice2 = input("~CHOICE~: What will you do with the scattered food? (Type 1 for eat, 2 for store or 3 for sweep) ")

if choice2 == '1':
    random_int = random.randint(1,3)
    char_stats["Health"] = char_stats["Health"] - random_int
    char_stats["Stamina"] = char_stats["Stamina"] + 2
    print(input("WATCH-O-CLOCK: -Your health has been reduced by {}. Your health is now at {}.-".format(random_int, char_stats['Health'])))
    print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("YOU: Hah, finally, all these food is gone, but I don't feel so good..."))
elif choice2 == '2':
    char_stats["Storage"] = char_stats["Storage"] + 2
    print(input("WATCH-O-CLOCK: -Your storage has been increased by 2. Your storage is now at {}.-".format(char_stats['Storage'])))
    print(input("YOU: Hah, finally all these food is gone. I'll save them for later."))
elif choice2 == '3':
    random_int = random.randint(2,5)
    char_stats["Strength"] = char_stats["Strength"] + random_int
    char_stats["Stamina"] = char_stats["Stamina"] - 2
    print(input("WATCH-O-CLOCK: -Your strenth has been increased by {}. Your strength is now at {}.-".format(random_int, char_stats['Strength'])))
    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("NARRATOR: The Food Waste monster manifests before your eyes as it towers over your frame."))
    print(input("RAYDEN: Quick! Double tap your Watch-O-Clock!"))
    print(input("NARRATOR: You hastily double tap the Watch-O-Clock and a force field hugs your figure."))
    print(input("RAYDEN: Now that you're well protected, you should start attacking it. There are 4 ways you can combat Food Waste."))
    print(input("1. Beat it with the broom I gave you earlier. It'll make a mess again so I don't know why you should do this. \n2. Use as a compost, the land may look baren now, but you can always plant stuff."))
    print(input("3. Use Waste-To-Energy(WTE) Incineration. It'll give you stamina, but it might burn you. \n4. You can use the larvae Black Soldier Flies to break down the monster and it shall be no more."))
    choice3 = input("~CHOICE~: How will you defeat Food Waste? (Type 1 for broom, 2 for compost, 3 for WTE Incineration or 4 for the larvae of Black Soldier Flies): ")

    while choice3 != '1' or choice3 != '2' or choice3 != '3' or choice4 != '4':
        if choice3 == '1' or choice3 == '2' or choice3 == '3' or choice3 == '4':
            break
        choice3 = input("~CHOICE~: How will you defeat Food Waste? (Type 1 for broom, 2 for compost, 3 for WTE Incineration or 4 for the larvae of Black Soldier Flies): ")

    if choice3 == '1':
        print(input("NARRATOR: You start wildly hitting Food Waste, making it fall to the ground in a heap, it's towering form lost."))
        random_int = random.randint(1,3)
        char_stats["Intellegence"] = char_stats["Intelligence"] - 2
        char_stats["Stamina"] = char_stats["Stamina"] - 3
        char_stats["Strength"] = char_stats["Strength"] + random_int
        print(input("WATCH-O-CLOCK: -Your intelligence has been decreased by 2. Your intellegence is now at {}.-".format(char_stats['Intelligence'])))
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("WATCH-O-CLOCK: -Your strenth has been increased by {}. Your strength is now at {}.-".format(random_int, char_stats['Strength'])))
        print(input("NARRATOR: Rayden looks at you, disappointed at what he has just witnessed. He is starting to wonder if you really are the one that is going to save the world."))
        print(input("RAYDEN: I'll clean up the food here..."))
        print(input("NARRATOR: Rayden points a ray gun at the food, and fires. The food may have all disappeared, but the sky seems to darken a shade and the ground seems to crack a little more. You shake your head, hoping it's just your imagination."))
    elif choice3 == '2':
        print(input("NARRATOR: You start hitting Food Waste at certain spots of it's body, prompting it to fall swiftly, separated enough to let you spread it easily around the barren land."))
        random_int = random.randint(1,3)
        char_stats["Intellegence"] = char_stats["Intelligence"] + 2
        char_stats["Stamina"] = char_stats["Stamina"] - 3
        char_stats["Strength"] = char_stats["Strength"] + random_int
        print(input("WATCH-O-CLOCK: -Your intelligence has been increased by 2. Your intellegence is now at {}.-".format(char_stats['Intelligence'])))
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("WATCH-O-CLOCK: -Your strenth has been increased by {}. Your strength is now at {}.-".format(random_int, char_stats['Strength'])))
        print(input("NARRATOR: As you are spreading out the waste, you ask Rayden if he has any water and seeds. He promptly surprises you yet again with sprinklers powered by solar energy and seeds of a plant you are unable to identify. You never said you were listening when the teacher was talking about plants."))
        print(input("Now you will have enough food to last when the seeds ripen and start to bear fruit, and they're safe to eat too."))
    elif choice3 == '3':
        print(input("NARRATOR: As per Rayden's guiding and instruction, you aim the Watch-O-Clock at Food Waste, turning the dail twice."))
        print(input("The heat stings, coming directly from the watch, but the force field seems to be strong enough to hold back the burns. For now. The energy seems to be absorbed into the Watch-O-Clock, but you're not really sure what is going on."))
        force_field = force_field - fire_dmg # FIRE FIRE FIRE FIRE
        force_field = force_field + random.randint(6, 12)
        char_stats["Intellegence"] = char_stats["Intelligence"] + 2
        print(input("WATCH-O-CLOCK: -Your intelligence has been increased by 2. Your intelligence is now at {}.-".format(char_stats['Intellegence'])))
    elif choice3 == '4':
        print(input("NARRATOR: Rayden releases a heap of larvae of Black Soldier Flies and they immediatly engulf Food Waste. These little bugs are not only able to clear food waste four times their size, but they are also a great source of food for you. \n That is if you are willing to eat them."))
        choice4 = input("~CHOICE~: Are you willing to eat the larvae of the Black Soldier Flies? (Type Y for yes and N for N to indicate your choice) ")

        while choice4 != 'N' or choice4 != 'Y' or choice4 != 'n' or choice4 != 'y':
            if choice4 == 'Y' or choice4 == 'N' or choice4 != 'n' or choice4 != 'y':
                break
            choice4 = input("~CHOICE~: Are you willing to eat the larvae of the Black Soldier Flies? (Type Y for yes and N for N to indicate your choice) ")

        if choice4 == 'N' or 'n':
            print(input("NARRATOR: You decide not to eat the larvae of the Black Soldier Flies."))
        elif choice4 == 'Y' or 'y':
            print(input("NARRATOR: You decide to eat the larvae of the Black Soldier Flies. After a quick roast and wash, you find them a good snack to munch on and you store some in your bag for later."))
            char_stats["Stamina"] = char_stats["Stamina"] + 3
            char_stats["Storage"] = char_stats["Storage"] + 4
            char_stats["Intelligence"] = char_stats["Intelligence"] + 2
            print(input("WATCH-O-CLOCK: -Your storage has been increased by 4. Your storage is now at {}.-".format(char_stats['Storage'])))
            print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
            print(input("WATCH-O-CLOCK: -Your intelligence has been increased by 2. Your intelligence is now at {}.-".format(char_stats['Intelligence'])))
            
print(input("RAYDEN: I should be going, it was nice meeting you though."))
print(input("NARRATOR: Rayden smiles modestly at you and you wonder if the twinkle you see in his eyes is real."))
print(input("NARRATOR: Rayden gives you a parting wave and disappears through a portal. You pinch yourself to make sure everything that happened to far is real, and you think it is, because a stinging pain in felt on your forearm."))

print(input("You start trudging forward, unsure where to go next. All you know is that there are more monsters awaiting, standing in between you and your mission. And that you'll be ready for whatever they throw at you."))        

print(input("=END OF DAY 1="))
char_stats["Stamina"] = char_stats["Stamina"] - 5
print(input("WATCH-O-CLOCK: -Your stamina has been reduced by 5. Your stamina is now at {}-".format(char_stats['Stamina'])))
print(input("=STATS AFTER DAY 1: {}=".format(char_stats)))

print(input("START OF DAY 2="))
char_stats["Stamina"] = char_stats["Stamina"] + 7
print(input("NARRATOR: You hear a blarring sound as you are roused from your sleep. It wasn't very comfortable sleeping on a makeshift bed in a cave, but at least it was dry. You contemplate whether to check what is making that sound to continue sleeping."))
choice5 = input("~CHOICE~: Do you wake up to investigate the sound or continue sleeping? (Type 1 for wake up and 2 for sleep to indicate your choice) ")

while choice5 != '1' or choice5 != '2':
    if choice5 == '2' or choice5 == '1':
        break
    choice5 = input("~CHOICE~: Do you wake up to investigate the sound or continue sleeping? (Type 1 for wake up and 2 for sleep to indicate your choice) ")

if choice5 == '1':
    print(input("NARRATOR: You begrudgingly awaken from your slumber to be faced with your Watch-O-Clock flapping around atop your bag. Then you remember you set an alarm to wake you up yesterday at 7am in the morning. You glance outside to see the sun barely peeking over the horizon. You strech and put on the Watch-O-Clock, getting ready to face a new day."))
    char_stats["Discipline"] = char_stats["Discipline"] + 5
    print(input("WATCH-O-CLOCK: -Your discipline has been increased by 5. Your discipline is now at {}.-".format(char_stats['Discipline'])))
    print(input("NARRATOR: You pick up the little amount of belongings you have, shoving them in your bag."))
    print(input("You exit the cave tentatively, eyeing out for anything that may jump out at you. You shiver, remembering the experience with Food Waste yesterday."))
    print(input("You scan the area in silence and your eyes land on a moving tree stump. Your eyebrows arch in confusion, and you approach it silently, holding your breath. Rayden isn't here to guide you, and you pray that you won't be caught off guard."))
    print(input("Just as you're nearing the tree stump, you accidently step on a branch, prompting the tree stump to turn around and face you."))
    print(input("TREE STUMP: Are you one of those pesky humans?"))
    choice6 = input("~CHOICE~: To lie or to tell the truth? (Type 1 to lie or type 2 to tell the truth) ")

    while choice6 != '1' or choice6 != '2':
        if choice6 == '1' or choice6 == '2':
            break
        choice6 = input("~CHOICE~: To lie or to tell the truth? (Type 1 to lie or type 2 to tell the truth) ")

    if choice6 == '1':
        print(input("YOU: N-no?"))
        char_stats["Discipline"] = char_stats["Discipline"] - 2
        print(input("WATCH-O-CLOCK: -Your discipline has been decreased by 2. Your discipline is now at {}.-".format(char_stats['Discipline'])))
        print(input("TREE STUMP: PESKY HUMAN! ALL OF YOU ARE THE SAME! ALL YOU DO IS LIE!"))
        print(input("NARRATOR: The roots of the tree stump jerks to life, expanding at a rapid pace. It wraps around your foot, lifting you up."))
        choice7 = input("~CHOICE~: What are you going to do now? (Type 1 to apologize or type 2 to attack the tree stump) ")
        
        while choice7 != '1' or choice7 != '2':
            if choice7 == '1' or choice7 == '2':
                break
            choice7 = input("~CHOICE~: What are you going to do now? (Type 1 to apologize or type 2 to attack the tree stump) ")
            
        if choice7 == '1':
            print(input("YOU: I'm sorry for lying! I didn't mean it! It was my instinctive reaction!"))
            char_stats["Discipline"] = char_stats["Discipline"] + 2
            print(input("WATCH-O-CLOCK: -Your discipline has been increased by 2. Your discipline is now at {}.-".format(char_stats['Discipline'])))
            print(input("NARRATOR: The tree stump looks at you, shocked, apparently not expecting you to apologize"))
            print(input("TREE STUMP: D-did pesky human mean your apology?"))
            print(input("NARRATOR: You nod your head quickly, not wanting to aggravate the tree stump any further."))
            print(input("TREE STUMP: I like this pesky human, what is pesky human's name?"))
            print(input("YOU: I am {}.".format(name)))
            print(input("NARRATOR: You choke out the words as the blood flowing to your head makes you very dizzy and uncomfortable. As if noticing your distress, the tree stump gently puts you down, recoiling it's roots."))
            print(input("TREE STUMP: {} is not a pesky human. Will {} help Scottie plant trees?".format(name, name)))
            choice8 = input("~CHOICE~: Will you help Scottie the tree stump plant trees? (Type Y for yes and N for N to indicate your choice) ")

            while choice8 != 'Y' or choice8 != 'N' or choice8 != 'n' or choice8 != 'y':
                if choice8 == 'Y' or choice8 == 'N' or choice8 != 'n' or choice8 != 'y':
                    break
                choice8 = input("~CHOICE~: Will you help Scottie the tree stump plant trees? (Type Y for yes and N for N to indicate your choice) ")
            
            if choice8 == 'Y' or 'y':
                print(input("SCOTTIE: Thank you {}! You are good human!".format(name)))
                char_stats["Intelligence"] = char_stats["Intelligence"] + 2
                print(input("WATCH-O-CLOCK: -Your intelligence has been increased by 2. Your intelligence is now at {}.-".format(char_stats['Intelligence'])))
                print(input("=11 HOURS LATER="))
                print(input("NARRATOR: You and Scottie spend practically the whole day planting trees."))
                char_stats["Strength"] = char_stats["Strength"] + 5
                print(input("WATCH-O-CLOCK: -Your strength has been increased by 5. Your strength is now at {}.-".format(char_stats['Strength'])))
                char_stats["Stamina"] = char_stats["Stamina"] - 6
                print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 6. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                print(input("YOU: Phew, it's tiring planting trees!"))
                print(input("NARRATOR: You wipe your brow, mouth agape, trying to get more oxygen into your system."))
                print(input("SCOTTIE: {} must be tired. Here, Scottie has fruits for {}!".format(name, name)))
                print(input("NARRATOR: You accept the fruits graciously, and munch down on them. They burst in your mouth, full of juicy sweetness. You don't think you have tasted any fruits sweeter or tastier than these."))
                char_stats["Stamina"] = char_stats["Stamina"] + 2
                print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                print(input("SCOTTIE: {} is a good human for helping Scottie all day, Scottie must tell Mama, goodbye {}!".format(name, name)))
                print(input("NARRATOR: Before you can even bid Scottie goodbye, it scampers away."))
                print(input("You lean against a tree a little longer before going back to the cave. As you set your bed, you think about the events of the day. You believe it has been a fruitful day. You wish Rayden was here to guide you, but you think you have done fairly well without him so far."))
                scottie = 'happy'
                random_int = 'End'
            elif choice8 == 'N' or 'n':
                print(input("NARRATOR: Scottie frowns but he doesn't question. It lets you bypass him and you trudge forward."))
                char_stats["Intelligence"] = char_stats["Intelligence"] - 2
                print(input("WATCH-O-CLOCK: -Your intelligence has been decreased by 2. Your intelligence is now at {}.-".format(char_stats['Intelligence'])))
                print(input("=5 HOURS LATER="))
                char_stats["Strength"] = char_stats["Strength"] + 3
                char_stats["Stamina"] = char_stats["Stamina"] - 5
                print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 5. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
                print(input("NARRATOR: The sun burns high in the sky, eliciting a sheen of sweat, and a grumble from you. There may be clouds overcast, hanging high in the sky, but it does nothing to help the sun's rays that are assulting your back. You have been trudging forward for hours now, and you feel famished, tired and groggy. Your rumbling stomach and aching legs remind you that you are not built for expedition. You have not seen a single other living being the past few hours, as baren land stretches far and wide. It is as if you are in the middle of the ocean, adrift on your boat, unsure which direction you came from, or when you will see land again, as you are at the sea's mercy."))
                print(input("Only this time, there is no food, water or shelter in sight."))
                scottie = 'eh'
                random_int = 'Early'
                if char_stats['Storage'] > 0:
                    print(input("Luckily for you, you have some larvae in your bag. They might not fill you up, but at least they are something. As you munch onto the snack, you lick your parched lips as your eyes squint from the heat. You pray that the heat will dissipate soon. You really are unable to keep this up for much longer."))
                    if char_stats['Discipline'] > 13:
                        print(input("You are disciplined enough not to eat all the larvae. As tempting as that is, you know you have to ration them and leave them for later, lest your luck still fais."))
                        char_stats["Discipline"] = char_stats["Discipline"] + 1
                        print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
                        char_stats['Storage'] = char_stats["Storage"] / 2
                        random_int = char_stats['Storage']
                        print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
                        char_stats["Stamina"] = char_stats["Stamina"] + char_stats["Storage"]
                        print(input("WATCH-O-CLOCK: -Your stamina has been increased by {}. Your stamina is now at {}.-".format(char_stats['Storage'], char_stats['Stamina'])))
                    else:
                        print(input("NARRATOR: You munch away at the larvae. They are not that filling, but it is what it is."))
                        char_stats['Storage'] = char_stats["Storage"] - char_stats["Storage"]
                        print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
                        char_stats["Stamina"] = char_stats["Stamina"] + 4
                        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                else:
                    print(input("NARRATOR: You rumage your little contents of your bag to see if you have anything edible. Unfortunately, there's nothing. Tough luck."))
            
        elif choice7 == '2':
            if char_stats["Strength"] > 14:
                if char_stats["Intelligence"] > 14:
                    print(input("NARRATOR: Your legs wrap around the tree stump's roots and you hoist your whole body weight to the side. The momentum breaks the branch and you drop into a roll, bracing for impact."))
                    char_stats["Stamina"] = char_stats["Stamina"] - 2
                    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    print(input("The tree stump lauches more roots at you, but you're well prepared this time. You swiftly turn the dail on the Watch-O-Clock and aim it at the roots."))  
                    force_field = force_field - fire_dmg # FIRE FIRE FIRE FIRE
                    force_field = force_field - fire_dmg # FIRE FIRE FIRE FIRE
                    force_field = force_field - fire_dmg # FIRE FIRE FIRE FIRE
                    print(input("The heat pricks at your skin, but there are still no burns. You see the force field flicker a little. This makes you wonder how many more times you should utilise the fire powers from your Watch-O-Clock."))
                    print(input("The roots keep coming, but so does your fire. Soon the regenerative abilities of the tree stump seem to slow, and a high pitched yelp is emitted from the tree. All the burnt roots flap around you while the charred ones retreat back to its master."))
                    print(input("TREE STUMP: Pesky human! How dare you hurt Scottie! Scottie must tell Mama about this pesky human!"))
                    print(input("NARRATOR: The tree stump dissipates, but you have a feeling this won't be the last time you hear from Scottie the tree stump."))
                    print(input("YOU: Phew, that was a close call. I should start exploring the place. It's why I woke up so early anyway."))
                    print(input("=5 HOURS LATER="))
                    char_stats["Strength"] = char_stats["Strength"] + 3
                    char_stats["Stamina"] = char_stats["Stamina"] - 5
                    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 5. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
                    print(input("NARRATOR: The sun burns high in the sky, eliciting a sheen of sweat, and a grumble from you. There may be clouds overcast, hanging high in the sky, but it does nothing to help the sun's rays that are assulting your back. You have been trudging forward for hours now, and you feel famished, tired and groggy. Your rumbling stomach and aching legs remind you that you are not built for expedition. You have not seen a single other living being the past few hours, as baren land stretches far and wide. It is as if you are in the middle of the ocean, adrift on your boat, unsure which direction you came from, or when you will see land again, as you are at the sea's mercy."))
                    print(input("Only this time, there is no food, water or shelter in sight."))
                    scottie = 'annoyed'
                    random_int = 'Early'
                    if char_stats['Storage'] > 0:
                        print(input("Luckily for you, you have some larvae in your bag. They might not fill you up, but at least they are something. As you munch onto the snack, you lick your parched lips as your eyes squint from the heat. You pray that the heat will dissipate soon. You really are unable to keep this up for much longer."))
                        if char_stats['Discipline'] > 13:
                            print(input("You are disciplined enough not to eat all the larvae. As tempting as that is, you know you have to ration them and leave them for later, lest your luck still fais."))
                            char_stats["Discipline"] = char_stats["Discipline"] + 1
                            print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
                            char_stats['Storage'] = char_stats["Storage"] / 2
                            random_int = char_stats['Storage']
                            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(random_int, char_stats['Storage'])))
                            char_stats["Stamina"] = char_stats["Stamina"] + 2
                            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                        else:
                            print(input("NARRATOR: You munch away at the larvae. They are not that filling, but it is what it is."))
                            char_stats['Storage'] = char_stats["Storage"] - char_stats["Storage"]
                            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
                            char_stats["Stamina"] = char_stats["Stamina"] + 4
                            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    else:
                        print(input("NARRATOR: You rumage your little contents of your bag to see if you have anything edible. Unfortunately, there's nothing. Tough luck."))
                
                else:
                    print(input("YOU: That all you got?"))
                    print(input("NARRATOR: Your hands wrap around the tree stump's roots and twist in opposite directions. You hear a satisfying crunch below your fingers."))
                    char_stats["Stamina"] = char_stats["Stamina"] - 1
                    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 1. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    print(input("A low growl escapes from your throat as you steady yourself for the next wave of roots."))
                    print(input("TREE STUMP: Gra! How is pesky human so strong! Scottie has not seen anything like this!"))
                    print(input("NARRATOR: The roots approaching you wrap around one another, morphing into one stronger root. The tree stump grunts in effort as the roots starts to move once more."))
                    print(input("It may be big and strong, but it's very imbalanced and you instinctively duck under it. Your hands work on their own, scratching, pulling, pushing and doing everything it possibly can everytime the root swings by. It takes some time, but you finally manage to break through the roots, eliciting a scream from Scottie."))
                    char_stats["Stamina"] = char_stats["Stamina"] - 4
                    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    print(input("SCOTTIE: No! My roots! Gra! Scottie must tell Mama about this pesky human!"))
                    print(input("NARRATOR: Scottie dissipates, but you have a feeling this won't be the last time you hear from it."))
                    print(input("YOU: Phew, that was a close call. I should start exploring the place. It's why I woke up so early anyway."))
                    print(input("=5 HOURS LATER="))
                    char_stats["Strength"] = char_stats["Strength"] + 3
                    char_stats["Stamina"] = char_stats["Stamina"] - 5
                    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 5. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
                    print(input("NARRATOR: The sun burns high in the sky, eliciting a sheen of sweat, and a grumble from you. There may be clouds overcast, hanging high in the sky, but it does nothing to help the sun's rays that are assulting your back. You have been trudging forward for hours now, and you feel famished, tired and groggy. Your rumbling stomach and aching legs remind you that you are not built for expedition. You have not seen a single other living being the past few hours, as baren land stretches far and wide. It is as if you are in the middle of the ocean, adrift on your boat, unsure which direction you came from, or when you will see land again, as you are at the sea's mercy."))
                    print(input("Only this time, there is no food, water or shelter in sight."))
                    scottie = 'fear'
                    random_int = 'Early'
                    if char_stats['Storage'] > 0:
                        print(input("Luckily for you, you have some larvae in your bag. They might not fill you up, but at least they are something. As you munch onto the snack, you lick your parched lips as your eyes squint from the heat. You pray that the heat will dissipate soon. You really are unable to keep this up for much longer."))
                        if char_stats['Discipline'] > 13:
                            print(input("You are disciplined enough not to eat all the larvae. As tempting as that is, you know you have to ration them and leave them for later, lest your luck still fais."))
                            char_stats["Discipline"] = char_stats["Discipline"] + 1
                            print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
                            char_stats['Storage'] = char_stats["Storage"] / 2
                            random_int = char_stats['Storage']
                            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(random_int, char_stats['Storage'])))
                            char_stats["Stamina"] = char_stats["Stamina"] + 2
                            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                        else:
                            print(input("NARRATOR: You munch away at the larvae. They are not that filling, but it is what it is."))
                            char_stats['Storage'] = char_stats["Storage"] - char_stats["Storage"]
                            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
                            char_stats["Stamina"] = char_stats["Stamina"] + 4
                            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    else:
                        print(input("NARRATOR: You rumage your little contents of your bag to see if you have anything edible. Unfortunately, there's nothing. Tough luck."))
                
            else:
                print(input("NARRATOR: You trash around wildly, unable to land any hits on the tree stump's roots."))
                print(input("TREE STUMP: Heh heh! Pesky human, pesky human, Mama will be happy when she sees no more pesky humans!"))
                print(input("NARRATOR: You bite your tongue, stopping an insult from tumbling out. You might be unhappy to back down, but you are unwilling to ruffle anymore feathers."))
                print(input("TREE STUMP: Heh heh! Why is pesky human not saying anything? What did other persky human say? Ca... Ca... Cat got your mouth? Eh. Cat got your lips? Eh. Cat... Ah, nevermind. Why is this pesky human not talking anymore? Is this pesky human dead? Eek!"))
                print(input("NARRATOR: Seemingly taking your silence as your demise, the tree stump plops you to the ground. You want to cry out from the pain of being dropped several metres, but you bite the inside of your cheek. The tree stump thinks you're dead, and you intent to play along, if that is what it takes to make the tree stump depart."))
                print(input("TREE STUMP: Waaa, please don't come haunt Scottie. Scottie is sorry!"))
                print(input("NARRATOR: You peek through your eyelids, watching Scottie the tree stump dissipate, but you have a feeling this won't be the last time you hear from it."))
                print(input("YOU: Phew, that was a close call. I should start exploring the place. It's why I woke up so early anyway."))
                print(input("=5 HOURS LATER="))
                char_stats["Strength"] = char_stats["Strength"] + 3
                char_stats["Stamina"] = char_stats["Stamina"] - 5
                print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 5. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
                print(input("NARRATOR: The sun burns high in the sky, eliciting a sheen of sweat, and a grumble from you. There may be clouds overcast, hanging high in the sky, but it does nothing to help the sun's rays that are assulting your back. You have been trudging forward for hours now, and you feel famished, tired and groggy. Your rumbling stomach and aching legs remind you that you are not built for expedition. You have not seen a single other living being the past few hours, as baren land stretches far and wide. It is as if you are in the middle of the ocean, adrift on your boat, unsure which direction you came from, or when you will see land again, as you are at the sea's mercy."))
                print(input("Only this time, there is no food, water or shelter in sight."))
                scottie = 'dead'
                random_int = 'Early'
                if char_stats['Storage'] > 0:
                    print(input("Luckily for you, you have some larvae in your bag. They might not fill you up, but at least they are something. As you munch onto the snack, you lick your parched lips as your eyes squint from the heat. You pray that the heat will dissipate soon. You really are unable to keep this up for much longer."))
                    if char_stats['Discipline'] > 13:
                        print(input("You are disciplined enough not to eat all the larvae. As tempting as that is, you know you have to ration them and leave them for later, lest your luck still fais."))
                        char_stats["Discipline"] = char_stats["Discipline"] + 1
                        print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
                        char_stats['Storage'] = char_stats["Storage"] / 2
                        random_int = char_stats['Storage']
                        print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(random_int, char_stats['Storage'])))
                        char_stats["Stamina"] = char_stats["Stamina"] + 2
                        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                    else:
                        print(input("NARRATOR: You munch away at the larvae. They are not that filling, but it is what it is."))
                        char_stats['Storage'] = char_stats["Storage"] - char_stats["Storage"]
                        print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
                        char_stats["Stamina"] = char_stats["Stamina"] + 4
                        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                else:
                    print(input("NARRATOR: You rumage your little contents of your bag to see if you have anything edible. Unfortunately, there's nothing. Tough luck."))

    elif choice6 == '2':
        print(input("YOU: I am what you call a pesky human."))
        char_stats["Discipline"] = char_stats["Discipline"] + 3
        print(input("WATCH-O-CLOCK: -Your discipline has been increased by 3. Your discipline is now at {}.-".format(char_stats['Discipline'])))
        print(input("NARRATOR: The tree stump looks at you, shocked, apparently not expecting you to be honest."))
        print(input("TREE STUMP: This pesky human is honest human? Wow! It's my first time seeing honest human."))
        print(input("NARRATOR: The tree stump pokes at your face and seems very intrigued."))
        print(input("TREE STUMP: Hello honest human, I am Scottie, what is honest human's name?"))
        print(input("YOU: I am {}.".format(name)))
        print(input("SCOTTIE: Wow, {} has a nice name! Come, help Scottie plant some trees. {} will help right?"))
        print(input("NARRATOR: You are not immune to the tone in Scottie's voice and his pleading eyes and you nod your head.")) 
        print(input("SCOTTIE: Thank you {}! You are good human!".format(name)))
        print(input("=11 HOURS LATER="))
        print(input("NARRATOR: You and Scottie spend practically the whole day planting trees."))
        char_stats["Strength"] = char_stats["Strength"] + 5
        print(input("WATCH-O-CLOCK: -Your strength has been increased by 5. Your strength is now at {}.-".format(char_stats['Strength'])))
        char_stats["Stamina"] = char_stats["Stamina"] - 6
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 6. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("YOU: Phew, it's tiring planting trees!"))
        print(input("NARRATOR: You wipe your brow, mouth agape, trying to get more oxygen into your system."))
        print(input("SCOTTIE: {} must be tired. Here, Scottie has fruits for {}!".format(name, name)))
        print(input("NARRATOR: You accept the fruits graciously, and munch down on them. They burst in your mouth, full of juicy sweetness. You don't think you have tasted any fruits sweeter or tastier than these."))
        char_stats["Stamina"] = char_stats["Stamina"] + 2
        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("SCOTTIE: {} is a good human for helping Scottie all day, Scottie must tell Mama, goodbye {}!".format(name, name)))
        print(input("NARRATOR: Before you can even bid Scottie goodbye, it scampers away."))
        print(input("You lean against a tree a little longer before going back to the cave. As you set your bed, you think about the events of the day. You believe it has been a fruitful day. You wish Rayden was here to guide you, but you think you have done fairly well without him so far."))
        scottie = 'happy'
        random_int = 'End'
        
if choice5 == '2':
    print(input("NARRATOR: You grumble in your head, hoping internally that whatever is making that atrocious noise will stop. As if hearing your wishes, the sound dies down and you continue sleeping comfortably."))
    char_stats["Stamina"] = char_stats["Stamina"] + 2
    char_stats["Discipline"] = char_stats["Discipline"] - 3
    print(input("=4 HOURS LATER="))
    print(input("NARRATOR: You stretch, feeling refreshed. The light shines into the cave and blinds you momentarily. You wonder how long you have been asleep for, and scamble to the Watch-O-Clock to check the time. Your eyes widden in shock as you notice the time."))
    print(input("You pick up the little amount of belongings you have, shoving them in your bag. You might has missed 4 hours of monster hunting, but at least you got more sleep. Right?"))
    print(input("You sling the bag over your shoulder and wear the Watch-O-Clock. You notice the few notifications on the screen and you click them open, not wanting to miss anything more after your 4 hours of sleep."))
    print(input("WATCH-O-CLOCK: -Your discipline has been decreased by 3. Your discipline is now at {}.-".format(char_stats['Discipline'])))
    print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("NARRATOR: You clench your teeth in annoyance but you sling the watch on your wrist. Hopefully this is the last time you slip up with time management."))
    print(input("=2 HOURS LATER="))
    char_stats["Strength"] = char_stats["Strength"] + 1
    char_stats["Stamina"] = char_stats["Stamina"] - 2
    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("WATCH-O-CLOCK: -Your strength has been increased by 1. Your strength is now at {}.-".format(char_stats['Strength'])))
    print(input("NARRATOR: The sun burns high in the sky, eliciting a sheen of sweat, and a grumble from you. There may be clouds overcast, hanging high in the sky, but it does nothing to help the sun's rays that are assulting your back. You have been trudging forward for hours now, and you feel famished, tired and groggy. Your rumbling stomach and aching legs remind you that you are not built for expedition. You have not seen a single other living being the past few hours, as baren land stretches far and wide. It is as if you are in the middle of the ocean, adrift on your boat, unsure which direction you came from, or when you will see land again, as you are at the sea's mercy."))
    print(input("Only this time, there is no food, water or shelter in sight."))
    scottie = 'unknown'
    random_int = 'Late'
    if char_stats['Storage'] > 0:
        print(input("Luckily for you, you have some larvae in your bag. They might not fill you up, but at least they are something. As you munch onto the snack, you lick your parched lips as your eyes squint from the heat. You pray that the heat will dissipate soon. You really are unable to keep this up for much longer."))
        if char_stats['Discipline'] > 13:
            print(input("You are disciplined enough not to eat all the larvae. As tempting as that is, you know you have to ration them and leave them for later, lest your luck still fais."))
            char_stats["Discipline"] = char_stats["Discipline"] + 1
            print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
            char_stats['Storage'] = char_stats["Storage"] / 2
            random_int = char_stats['Storage']
            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(random_int, char_stats['Storage'])))
            char_stats["Stamina"] = char_stats["Stamina"] + 2
            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        else:
            print(input("NARRATOR: You munch away at the larvae. They are not that filling, but it is what it is."))
            char_stats['Storage'] = char_stats["Storage"] - char_stats["Storage"]
            print(input("WATCH-O-CLOCK: -Your storage has been decreased by {}. Your storage is now at {}.-".format(char_stats['Storage'], char_stats['Storage'])))
            char_stats["Stamina"] = char_stats["Stamina"] + 4
            print(input("WATCH-O-CLOCK: -Your stamina has been increased by 4. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    else:
        print(input("NARRATOR: You rumage your little contents of your bag to see if you have anything edible. Unfortunately, there's nothing. Tough luck."))


if random_int == 'End':
    print(input("=END OF DAY 2="))
    print(input("=STATS AFTER DAY 2: {}=".format(char_stats)))
elif random_int == 'Early':
    if char_stats['Discipline'] > 15:
        print(input("NARRATOR: You may be worn out from all that walking, but you know the more time you seize to explore, the higher the chances of you finding something valuable. You decide to rest for a little before you continue your journey."))
        char_stats["Discipline"] = char_stats["Discipline"] + 1
        print(input("WATCH-O-CLOCK: -Your discipline has been increased by 1. Your discipline is now at {}.-".format(char_stats['Discipline'])))
        print(input("=6 HOURS LATER="))
        char_stats["Strength"] = char_stats["Strength"] + 3
        char_stats["Stamina"] = char_stats["Stamina"] - 6
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 6. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
        print(input("NARRATOR: Lady luck has not smilled upon you earlier, but she is now. A forest lies ahead, with fruits hanging from the trees. You silivate looking at the fruits. The sun is just starting to set, and there's just enough time for you to find a dry spot in the forest to set up camp. You're not sure why this part has not been affected by the effects of climate change, but you'll work it out tomorrow."))
        print(input("=END OF DAY 2="))
        print(input("=STATS AFTER DAY 2: {}=".format(char_stats)))
        random_int = 'Dry'
    else:
        print(input("NARRATOR: You are worn out from all that walking and you decide to have a little rest."))
        print(input("=1 HOUR LATER"))
        char_stats["Stamina"] = char_stats["Stamina"] + 1
        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 1. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("NARRATOR: After an hour rest, your legs feel more attached to your body. You continue your exploration."))
        print(input("=6 HOURS LATER="))
        char_stats["Strength"] = char_stats["Strength"] + 3
        char_stats["Stamina"] = char_stats["Stamina"] - 6
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 6. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
        print(input("NARRATOR: The sun is just starting to set, and your eyes land on a forest. You hope you're not hallucinating, because you don't want to be walking around in the darkness."))
        print(input("You manage to reach the forest when the moon is hanging in the sky. You can barely see past your own hands when you enter the forest, and you decide to rest at the corner of the forest. It's cold, but you don't think you can find a dry spot without tripping. You're not sure why this part has not been affected by the effects of climate change, but you'll work it out tomorrow."))
        print(input("=END OF DAY 2="))
        print(input("=STATS AFTER DAY 2: {}=".format(char_stats)))
        random_int = 'Corner'        
elif random_int == 'Late':
    print(input("=7 HOURS LATER="))
    char_stats["Strength"] = char_stats["Strength"] + 4
    char_stats["Stamina"] = char_stats["Stamina"] - 7
    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 7. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("WATCH-O-CLOCK: -Your strength has been increased by 4. Your strength is now at {}.-".format(char_stats['Strength'])))
    print(input("NARRATOR: Even though the sun has almost set, you continue trudging on in hopes of finding something valuable. You already wasted enough time, and you already rested enough earlier."))
    print(input("=2 HOURS LATER="))
    char_stats["Strength"] = char_stats["Strength"] + 1
    char_stats["Stamina"] = char_stats["Stamina"] - 3
    print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("WATCH-O-CLOCK: -Your strength has been increased by 1. Your strength is now at {}.-".format(char_stats['Strength'])))
    print(input("NARRATOR: As much as you want to continue searching, you need to have enough rest for tomorrow. You set up camp on the surprisingly cool cracked ground. You remember it burning earlier, but it could be just the build-up of heat."))
    print(input("=END OF DAY 2="))
    print(input("=STATS AFTER DAY 2: {}=".format(char_stats)))
    random_int = 'Close'
else:
    print(input("ERROR"))
    quit()

print(input("START OF DAY 3="))
if random_int == 'End':
    print(input("NARRATOR: You feel something poking into your cheek and you swat your hands to shoo it away, but to no avail. Soon you shoot awake."))
    char_stats["Stamina"] = char_stats["Stamina"] + 6
    print(input("WATCH-O-CLOCK: -Your stamina has been increased by 6. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("YOU: Wha-"))
    print(input("SCOTTIE: Oh hello {}! You are finally awake!".format(name)))
    print(input("YOU: Huh? Scottie? What is going on?"))
    print(input("SCOTTIE: I bought Mama here to see you!"))
    print(input("NARRATOR: You shoot up immediately."))
    print(input("YOU: Climate Change is here to see me?"))
    print(input("SCOTTIE: Who is Climate Change? I only know Mama."))
    print(input("NARRATOR: Before you can protest, Scottie pulls you out of the cave. And in all her glory, stands Climate Change. Whatever you have imagined her to look like, it definitely wasn't like that. With no doubt though, she is breathtaking. Metaphorically and literally. Your cheeks heat up and you are pretty sure it's rude to stare, but you really couldn't help it, she was magnificent."))
    print(input("CLIMATE CHANGE: Human, I'd say you have ogled enough."))
    print(input("YOU: Uh I um, sorry."))
    print(input("NARRATOR: A clear blush forms on your cheeks. You have been caught by Climate Change herself. She chuckles at your slip-up and you sink deeper into embarrassment."))
    print(input("SCOTTIE: Heh? Why is {} so red, Mama?".format(name)))
    print(input("CLIMATE CHANGE: It's a natural reaction my dear. Now say {}, I have heard you helped my dear boy, Scottie, plant some trees?".format(name)))
    print(input("NARRATOR: You nod your head shyly, unable to meet Climate Change's eyes. You don't think you'll ever recover from earlier."))
    print(input("CLIMATE CHANGE: Well it seems there is some hope for humanity after all. Will you be a dear and explain to your friend the procedure?"))
    print(input("NARRATOR: Scottie starts chattering away and you listen intently. At the end, you are thrilled to know that Earth can be restored to its former glory. As long as you help them, step by step, the world will heal, little by little. Of course you help, this is what you planned to do since your first day here."))
    print(input("RAYDEN: {}? What's going on here?"))
    print(input("NARRATOR: You see Rayden step out of a portal, watching the Scottie and Climate Change tentatively."))
    print(input("YOU: Rayden! Hi! Uh this is Scottie, and ths is Climate Change."))
    print(input("NARRATOR: He glances at them, back at you, and then back at them again."))
    print(input("RAYDEN: I. I can't believe I'm face-to-face with Climate Change."))
    print(input("NARRATOR: He looks at Climate Change like how a fanboy looking at their bias. You touch his shoulder and smirk."))
    print(input("YOU: You're staring."))
    print(input("NARRATOR: Rayden snaps out of his haze at your words and Climate Change giggles."))
    print(input("CLIMATE CHANGE: Say Rayden, would you like to help restore the Earth?"))
    print(input("NARRATOR: You explain the contents of the plan to save Earth and his eyes light up at the prospect."))
    print(input("RAYDEN: I can't believe this. Since day 1, I have always strived to reserve Earth for as long as I could, and I never once thought about reversing the effects. No one thought it was possible."))
    print(input("CLIMATE CHANGE: Oh it is very possible, but it's slow, and takes up a lot of energy. I needed to find the right humans who will use the right energy to reverse these effects and not use it for their own personal gains. To see such a promising saviour {} have a positive reception to you, I knew both of you would be a good pair of heroes."))
    print(input("NARRATOR: You and Rayden beam from the praise. \nYou don't know how long it will take or how you got here, but this is your life now. Now your goal is to make Earth better, and with Rayden by your side, you know nothing is impossible."))
    time.sleep(1)
    print("=GAME END=")
    print("You ended the game with these statistics: {}".format(char_stats))
    print(input(end_message))
    quit()
    
elif random_int == 'Dry':
    char_stats["Stamina"] = char_stats["Stamina"] + 8
    print(input("WATCH-O-CLOCK: -Your stamina has been increased by 8. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("NARRATOR: Your eyes flutter open upon hearing the birds chirping. You quite miss the sound. You don't remember if you heard these sounds before you poped up in this world, but it's still wonderfully pleasant."))
    print(input("For breakfast, you indulge in some fresh fruits. You don't think you have tasted any fruits sweeter."))
    char_stats["Stamina"] = char_stats["Stamina"] + 2
    print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
    print(input("NARRATOR: Just then, you see a hare pop out from the trees. Your stomach rumbles in delight. Meat will not only restore stamina but also provide you with strength, it just may be time consuming and difficult for first timers. And you might not actually catch it."))
    choice15 = input("~CHOICE~: Catch the hare? (Type Y for yes and N for N to indicate your choice) ")

    while choice15 != 'N' or choice15 != 'Y' or choice15 != 'n' or choice15 != 'y':
        if choice15 == 'N' or choice15 == 'Y' or choice15 != 'n' or choice15 != 'y':
            break
        choice15 = input("~CHOICE~: Catch the hare? (Type Y for yes and N for N to indicate your choice) ")
    if choice15 == 'N' or 'n':
        print(input("YOU: Nah, fruits are good enough."))
        print(input("NARRATOR: You watch the hare bolt away after you stand up."))
        print(input("RAYDEN: {}?".format(name)))
        print(input("NARRATOR: You turn around to see Rayden stepping out of a portal. You shoot him a kind smile and he returns it."))
        print(input("RAYDEN: I see you found the hav-"))
    elif choice15 == 'Y' or 'y':
        if char_stats["Intelligence"] > 15 and char_stats["Stamina"] > 75 and char_stats["Strength"] > 15:
            print(input("NARRATOR: You lure the hare towards you by slowing your movements and an apple you plucked earlier. It bounces towards you happily. As it launches its teeth into the apple, you stroke it. It's years flick in appreciation as you hit a sensitive spot. You don't find it in your heart to kill it for food anymore, maybe companionship would suffice?"))
            choice20 = input("~CHOICE~: Do you really want to kill the hare? (Type Y for yes and N for N to indicate your choice) ")

            while choice20 != 'N' or choice20 != 'Y' or choice20 != 'n' or choice20 != 'y':
                if choice20 == 'N' or choice20 == 'Y' or choice20 != 'n' or choice20 != 'y':
                    break
                choice20 = input("~CHOICE~: Do you really want to kill the hare? (Type Y for yes and N for N to indicate your choice) ")
            if choice20 == 'Y' or 'y':
                print(input("NARRATOR: Your hands shift from petting the hare to carrasing it. Slowly, it leans into your touch, basking in the attention. \n \nSnap. \nThe hare's blood seeps through your fingers. It's dead. You got some meat for later."))
                char_stats["Strength"] = char_stats["Strength"] + 2
                char_stats["Storage"] = char_stats["Storage"] + 8
                char_stats["Stamina"] = char_stats["Stamina"] - 2
                print(input("WATCH-O-CLOCK: -Your storage has been increased by 8. Your storage is now at {}.-".format(char_stats['Storage'])))
                print(input("WATCH-O-CLOCK: -Your strenth has been increased by 2. Your strength is now at {}.-".format(char_stats['Strength'])))
                print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
                print(input("RAYDEN: {}! Why is your hands covered in blood?".format(name)))
                print(input("NARRATOR: You turn around to see Rayden stepping out of a portal, eyes widdening in horror at the sight of your bloody hands."))
                print(input("YOU: I killed a hare, for food."))
                print(input("NARRATOR: You lift up the hare by the ears, almost making Rayden lurch forward and puke."))
                print(input("RAYDEN: Don't you already know? Killing an animal will practically make it extinct. This place here, it was presserved by some miracle, and everything here, is practically what the world has to offer. Killing that hare may but their species in even more danger. And please, at least you could've done it more humanly."))
                print(input("NARRATOR: You look at your stained hands. It could've been responsible for stripping the world of a whole species, how are you going to be the protecter of Earth?"))
                time.sleep(1)
                print("=YOU HAVE FAILED AS A PROTECTOR OF EARTH=")
                time.sleep(0.35)
                print("G")
                time.sleep(0.2)
                print("A")
                time.sleep(0.2)
                print("M")
                time.sleep(0.2)
                print("E")
                time.sleep(0.2)
                print(" ")
                time.sleep(0.2)
                print("O")
                time.sleep(0.2)
                print("V")
                time.sleep(0.2)
                print("E")
                time.sleep(0.2)
                print("R \n")
                print("You ended the game with these statistics: {} \n \n".format(char_stats))
                print(end_message)
                quit()
            elif choice20 == 'N' or 'n':
                print(input("NARRATOR: Your hands shift from petting the hare to carrasing it. Slowly, it leans into your touch, basking in the attention. You scratch behind its ear and its nose starts twitching, showing approval. Maybe comapanionship is enough."))
                print(input("RAYDEN: {}?".format(name)))
                print(input("NARRATOR: You turn around to see Rayden stepping out of a portal. You shoot him a kind smile and he returns it."))
                print(input("RAYDEN: Cute friend you got th-")) 
        else:
            print(input("NARRATOR: You lunge for the hare and it bolts away. You curse inwardly. Maybe you should have tried a different method to catch it."))
            print(input("RAYDEN: {}?".format(name)))
            print(input("NARRATOR: You turn around and see Rayden staring at you amusedly."))
            print(input("RAYDEN: I know the soil is rich in nutrients bu-"))

    elif random_int == 'Corner':
        char_stats["Stamina"] = char_stats["Stamina"] + 5
        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 5. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("NARRATOR: The sun blares into your eyes and you groan. You sit up groggily as the sun continues its torment. You want to sleep more, but it is obviously not possible with the heat. At least there are fruits on the trees for you to eat. At the very least, you are greatful for that.")) 
        print(input("You pluck a mango hanging on the tree give it a quick once-over before bitting into it, it seems clean. As soon as your teeth sinks into the mango, your taste buds are assulted with sweetness."))
        print(input("You don't realize how hungry you are until only the pit of the mango is left in your hands."))
        char_stats["Stamina"] = char_stats["Stamina"] + 2
        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 2. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("RAYDEN: You should plant that pit."))
        print(input("YOU: Rayden! How long have you been standing there?"))
        print(input("RAYDEN: Long eno-"))

    elif random_int == 'Close':
        char_stats["Stamina"] = char_stats["Stamina"] + 3
        print(input("WATCH-O-CLOCK: -Your stamina has been increased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("NARRATOR: The sun is barely peeking above the horizon and you already feel clammy. At least you can continue searching for something beneficial to you."))
        print(input("=2 HOURS LATER="))
        char_stats["Strength"] = char_stats["Strength"] + 1
        char_stats["Stamina"] = char_stats["Stamina"] - 3
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 3. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("WATCH-O-CLOCK: -Your strength has been increased by 1. Your strength is now at {}.-".format(char_stats['Strength'])))
        print(input("NARRATOR: You feel as if you have not rested from sleep, but the outline of some trees makes you perk up. You force yourself to walk faster even though you are clearly tired."))
        char_stats["Stamina"] = char_stats["Stamina"] - 1
        print(input("WATCH-O-CLOCK: -Your stamina has been decreased by 1. Your stamina is now at {}.-".format(char_stats['Stamina'])))
        print(input("NARRATOR: Just as you are about to reach the forest, Rayden pops out of a portal."))
        print(input("YOU: Rayden!"))
        print(input("RAYDEN: {}! Are you ok? You look worn and weary.".format(name)))
        print(input("YOU: Now that you're here I'm feeling much better."))
        print(input("RAYDEN: {}! Please, this is not a time to be foo-".format(name)))
        
print(input("NARRATOR: Rayden's words are interupted abruptly, as the floor shakes and the animals scatter."))
print(input("YOU: What is going on?"))
print(input("NARRATOR: Before Rayden can answer you, a tree stump emerges from the trees."))
if scottie == 'eh':
    char_stats["Intelligence"] -= 3
    print(input("WATCH-O-CLOCK: -Your intelligence has been decreased by 3. Your intelligence is now at {}.-".format(char_stats['Intelligence'])))
    print(input("NARRATOR: You are not sure if it's a glitch, but your intelligence has just been decreased for no particular reason. You don't see how that might affect you, but it still feels disappointing to see your stats drop for no particular reason."))
elif scottie == 'fear':
    char_stats["Strength"] += 3
    print(input("WATCH-O-CLOCK: -Your strength has been increased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
    print(input("NARRATOR: You are not sure if it's a glitch, but your strength has just been increased for no particular reason. You don't see how that might affect you, but it feels pleasent to see the stats increase for no particular reason."))
elif scottie == 'dead':
    char_stats["Health"] += 3
    print(input("WATCH-O-CLOCK: -Your health has been increased by 3. Your health is now at {}.-".format(char_stats['Health'])))
    print(input("NARRATOR: You are not sure if it's a glitch, but your health has just been increased for no particular reason. You don't see how that might affect you, but it feels pleasent to see the stats increase for no particular reason."))
elif scottie == 'annoyed':
    char_stats["Strength"] -= 3
    print(input("WATCH-O-CLOCK: -Your strength has been decreased by 3. Your strength is now at {}.-".format(char_stats['Strength'])))
    print(input("NARRATOR: You are not sure if it's a glitch, but your strength has just been decreased for no particular reason. You don't see how that might affect you, but it still feels disappointing to see your stats drop for no particular reason."))
if scottie == 'unknown':
    print(input("YOU: First a monster made out of food waste and now a walking tree stump?"))
    print(input("RAYDEN: That should be Deforestation. At least it's the tree stump, you don't want to be neaer the charred one."))
    print(input("???: Pesky humans... Mama said a pesky human was coming, I didn't think there would be two."))
    print(input("???: The more the merrier."))
    print(input("NARRATOR: A charred tree steps out after the tree stump. Rayden's warning is fresh in your mind, and you clench you jaw. This is not going to be fun, though you could try to talk your way out of this."))
    choice11 = input("~CHOICE~: Do you want to try talking or do you want to fight? (Type 1 to talk or 2 to fight) ")
if scottie == 'eh':
    print(input("YOU: Scottie."))
    print(input("SCOTTIE: Brother, this is the human I was talking about. They didn't want to plan trees with me."))
    print(input("NARRATOR: Scottie's brother is a tree, chared beyond recognition. He looks a lot more intimidating than Scottie, due to his height and girth"))
    print(input("???: How unfortunate. You don't want to save the Earth? Then I guess you are not worth saving."))
    print(input("NARRATOR: The charred tree spurts fire from his body, prompting everything in his path to scatter or burn, including you and Rayden. You barely dodge it as the force field splutters to life on its own accord."))
    force_field = force_field - fire_dmg / 2 # FIRE FIRE FIRE FIRE     
    print(input("It's a little ironic for the charred tree to try to burn you and Rayden, but that's not very important right now. You try to go closer to the trees to launch a counterattack on them but to no avail. The fire keeps coming at you. You glance over to see how Rayden is holding up with the tree stump, afterall, the fire has a limited area span, thank god. Rayden is grunting in effort, slicing his way through the tree stump's roots, trying to curl around him. You seeth with anger at the sight. Maybe you should find a way to fight back, or you can have a peace talk instead?"))          
else:
    print(input("YOU: Scottie."))
    print(input("NARRATOR: The name rumbles low in your throat, and you clench your fist till your knuckles turn white. You're not surprised to see him here, but the thing that emerges next makes your face drop. A charred tree. As if Scottie alone wasn't hard enough to deal with, but now it's a fair 2v2 fight. With Rayden's multitude of experience, you are sure that winning the fight would not be a problem."))

while choice11 != '1' or choice11 != '2':
    if choice11 == '1' or choice11 == '2':
        break
    choice11 = input("~CHOICE~: Do you want to try talking or do you want to fight? (Type 1 to talk or 2 to fight) ")

if choice11 == '1':
    print(input("NARRATOR: You choose to talk. Why ask for war? Many innocents will be hurt, directly or indirectly."))
    print(input("YOU: We don't have to fight, the more we fight, the more we hurt this place. The flora and fauna, they'll be burned alive, would you want that?"))
    print(input("SCOTTIE: Brother, they're right. If we continue fighting like this, everything here, they'll die..."))
    print(input("???: Then we just have to make sure to eliminate them without hurting anything else. Scottie, grab them!"))
    print(input("NARRATOR: Both you and Rayden launch in different dirrections, making it harder for Scottie to grab both of you."))
if choice11 == '2':
    print(input("NARRATOR: You choose to fight. Afterall, peace was never an option."))

print(input("=YOUR STATS RIGHT NOW IS {}. CHOOSE YOUR NEXT OPTIONS WISELY=".format(char_stats)))
fight = True
rayden_health = 100
name_upper = name.upper
scobro_health = 200
scobro_choice = range(3)

while fight == True:
    if scobro_health <= 70:
        fight = False
        print(input("SCOTTIE: Brother, we are too weak to continue this fight, we have to retreat."))
        print(input("NARRATOR: Scottie and his brother retreats. You have won the fight, but at what cost?"))
        time.sleep(1)
        print("=GAME END=")
        print("You ended the game with these statistics: {}".format(char_stats))
        print(input(end_message))
        quit()
        
    if char_stats["Stamina"] <= 0:
        fight = False
        print(input("You plop to the ground. You do not have enough stamina for this."))
        time.sleep(0.35)
        print("G")
        time.sleep(0.2)
        print("A")
        time.sleep(0.2)
        print("M")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print(" ")
        time.sleep(0.2)
        print("O")
        time.sleep(0.2)
        print("V")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print("R \n \n")
        print("You ended the game with these statistics: {}".format(char_stats))
        print(input(end_message))
        quit()

    if char_stats["Health"] <= 0:
        fight = False
        print("=YOU HAVE DIED=")
        time.sleep(0.35)
        print("G")
        time.sleep(0.2)
        print("A")
        time.sleep(0.2)
        print("M")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print(" ")
        time.sleep(0.2)
        print("O")
        time.sleep(0.2)
        print("V")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print("R \n \n")
        print("You ended the game with these statistics: {}".format(char_stats))
        print(input(end_message))
        quit()

    if rayden_health <= 0:
        fight = False
        print("=RAYDEN HAS DIED=")
        print(input("NARRATOR: You are heartbroken as you watch Rayden lie on the ground. Motionless."))
        time.sleep(0.35)
        print("G")
        time.sleep(0.2)
        print("A")
        time.sleep(0.2)
        print("M")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print(" ")
        time.sleep(0.2)
        print("O")
        time.sleep(0.2)
        print("V")
        time.sleep(0.2)
        print("E")
        time.sleep(0.2)
        print("R \n \n")
        print("You ended the game with these statistics: {}".format(char_stats))
        print(input(end_message))
        quit()
    
    for i in range(1):
        print(input("=THERE ARE 5 DIFFERENT ACTIONS FOR YOU TO PICK FROM. THEY ARE HIGHLY DEPENDABLE ON YOUR PREVIOUS CHOICES AND YOUR STATS. EVERY ACTION CONTRIBUTES TOWARDS THE OUTCOME OF THE FIGHT AND THE GAME. GOOD LUCK {}.".format(name_upper)))
    fight_choice = input("1 for Basic Attack. 2 for Special Attack. 3 for Heal. You can press 4 to learn more about the actions.")
    while fight_choice != '1' or fight_choice != '2' or fight_choice != '3' or fight_choice != '4':
        if fight_choice == '1' or fight_choice == '2' or fight_choice == '3' or fight_choice == '4':
            break
        fight_choice = input("1 for Basic Attack. 2 for Special Attack. 3 for Heal. You can press 4 to learn more about the actions.")
    if fight_choice == '4':
        print(input('''
Basic Attack: Needs stamina. If landed, will reduce opponents health. The strength of the attack depends on your stats.
Special Attack: Needs stamina, strength and intelligence. If landed, will drastically reduce opponents health. The strength of the attack depends on your stats.
Heal: Needs storage. Will restore health and stamina.'''))
    
    if fight_choice == '1':
        char_stats["Stamina"] -= 5
        if soboro_choice == '1':
            scobro_choice = range(3)
            print(input("=BOTH TEAMS ATTACK AT THE SAME TIME, CAUSING THEM TO CLASH. NO ONE GETS HURT="))
        if scobro_choice == '2':
            scobro_choice = range(3)
            print(input('=THE ATTACK IS SUCCESSFUL. SCOTTIE AND HIS BROTHER HEALS IMMEDIATELY AFTER='))
            if char_stats["Strength"] > 25:
                scobro_health -= 20
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 25. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if char_stats["Strength"] > 15:
                scobro_health -= 15
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 20. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            else:
                scobro_health -= 10
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 15. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
        if scobro_choice == '3':
            scobro_choice = range(3)
            print(input('=THE ATTACK IS UNSUCCESSFUL. SCOTTIE AND HIS BROTHER LAUNCH A STRONGER ATTACK THAT OVERPOWERS YOURS='))
            if char_stats["Strength"] > 25:
                rayden_health -= 10
                char_stats["Health"] -= 10
                print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 20, 10 EACH PERSON="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if char_stats["Strength"] > 15:
                rayden_health -= 15
                char_stats["Health"] -= 15
                print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 30, 15 EACH PERSON="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            else:
                rayden_health -= 20
                char_stats["Health"] -= 20
                print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 40, 20 EACH PERSON="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))

    if fight_choice == '2':
        char_stats["Stamina"] -= 10
        if soboro_choice == '1':
            scobro_choice = range(3)
            print(input('=THE ATTACK IS SUCCESSFUL='))
            if char_stats["Strength"] > 25:
                scobro_health -= 35
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 35="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if char_stats["Strength"] > 15:
                scobro_health -= 30
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 30="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            else:
                scobro_health -= 25
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 25="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
        if scobro_choice == '2':
            scobro_choice = range(3)
            print(input('=THE ATTACK IS SUCCESSFUL. SCOTTIE AND HIS BROTHER HEALS IMMEDIATELY AFTER='))
            if char_stats["Strength"] > 25:
                scobro_health -= 30
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 35. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if char_stats["Strength"] > 15:
                scobro_health -= 25
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 30. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            else:
                scobro_health -= 20
                print(input("=OPPONENTS HEALTH HAS BEEN REDUCED BY 25. SCOTTIE AND HIS BROTHER HEALS AND INCREASES HEALTH BY 5="))
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
        if scobro_choice == '3':
            scobro_choice = range(3)
            print(input("=BOTH TEAMS ATTACK AT THE SAME TIME, CAUSING THEM TO CLASH. NO ONE GETS HURT="))
            
    if fight_choice == '3':
        if char_stats["Storage"] <= 0:
            print(input("=THERE IS NO FOOD TO HEAL YOU. CHOOSE ANOTHER ACTION="))
        else:
            char_stats["Storage"] -= 2
            char_stats["Health"] += 5
            char_stats["Stamina"] += 5
            print(input("=YOUR HEALTH HAS BEEN INCREASED BY 5=\n=YOUR STAMINA HAS BEEN INCREASED BY 5="))
            if scobro_choice == '3':
                scobro_choice = range(3)
                if char_stats["Strength"] > 25:
                    rayden_health -= 10
                    char_stats["Health"] -= 10
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 20, 10 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
                if char_stats["Strength"] > 15:
                    rayden_health -= 15
                    char_stats["Health"] -= 15
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 30, 15 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
                else:
                    rayden_health -= 20
                    char_stats["Health"] -= 20
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 40, 20 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if scobro_choice == '1':
                scobro_choice = range(3)
                if char_stats["Strength"] > 25:
                    rayden_health -= 5
                    char_stats["Health"] -= 5
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 10, 5 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
                if char_stats["Strength"] > 15:
                    rayden_health -= 10
                    char_stats["Health"] -= 10
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 20, 10 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
                else:
                    rayden_health -= 15
                    char_stats["Health"] -= 15
                    print(input("=YOUR TEAMS HEALTH HAS BEEN REDUCED BY 30, 15 EACH PERSON="))
                    print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))
            if scobro_choice == '2':
                scobro_choice = range(3)
                print(input("=THE OPPOSING TEAM HAS HEALED="))
                scobro_health += 5
                print(input('=OPPONENTS HEALTH: {} \nYOUR STATS: {} \nRAYDEN HEALTH: {}='.format(scobro_health, char_stats, rayden_health)))


 
                
