import random
import time

mode = ""
playerCount = 0
p1Name = ""
p2Name = ""

def tutorial():
    costumeList = ["skeleton", "ghost", "vampire", "witch", "royal", "pirate", "scarecrow", "clown", "superhero", "doll", "dinosaur", "cowboy", "bear", "mermaid", "zombie"]
    tutorialActive = 1
    print("Welcome to the Haunted Halloween Hunt tutorial!")
    print("Here, we'll go over the basics of the game, how to play, and how to get that sweet, sweet candy!")
    time.sleep(10)
    print("")
    while tutorialActive >= 1:
        if mode == "singlePlayer":
            print("In this game, you will go through five rounds of different houses in attempt to get as much candy as possible.")
            print("Once approaching each house, you'll be given a description of the house, which may have a hint as to what costume to wear for")
            print("it.")
            time.sleep(10)
            print("")
            print("After a few seconds, you will be prompted to pick a costume to go to that house with.")
            print("Going to the house in any costume will give you some candy, however you will gain even more if you cater to the house's")
            print("interests!")
            time.sleep(10)
            print("")
            print("Here are the possible costume types that you will find!")
            time.sleep(3)
            print("")
            tutorialCostumeCount = 1
            for tutorialCostumeCount in range(1,15):
                print(f"- {costumeList[tutorialCostumeCount]}")
                time.sleep(1)
            print("")
            print("After five rounds, your final candy total will be revealed, try to go for the highest score!!")
            time.sleep(5)
        else:
            print("In this game, you two will take turns through five rounds of different houses in attempt to get as much candy as possible.")
            print("Once approaching each house, you'll be given a description of the house, which may have a hint as to what costume to wear for")
            print("it.")
            time.sleep(10)
            print("")
            print("After a few seconds, you will be prompted to pick a costume to go to that house with.")
            print("Going to the house in any costume will give you some candy, however you will gain even more if you cater to the house's")
            print("interests!")
            time.sleep(10)
            print("")
            print("Here are the possible costume types that you will find!")
            time.sleep(3)
            print("")
            tutorialCostumeCount = 1
            for tutorialCostumeCount in range(1,15):
                print(f"- {costumeList[tutorialCostumeCount]}")
                time.sleep(1)
            print("")
            print("After five rounds, the two of your final candy counts will be compared, and whoever has the most wins!!")
            time.sleep(7.5)
        print("")
        print("Keep an eye out for the elusive Golden Mansion! Though rare, if found, you can gain twice as much candy from it!")
        print("How wonderfully conveniet!!")
        time.sleep(10)
        print("")
        print("On the contrary, however, beware of the Abandoned House. If you find it, and don't put on the correct costume, you'll LOSE")
        print("candy!")
        print("Although, the ghost in there is genorous enough to still give you candy if you wear the proper costume, but not as much...")
        time.sleep(10)
        print("")
        print("One more thing, do not input any responses until you are prompted to do so! Doing so can potentially cause game to bug out!")
        time.sleep(9)
        print("")
        print("And that's it for the game's tutorial! Do you want me to go over it again?")
        print("")
        print("Please input the response 'Yes' or 'No'.")
        print("")
        if input().lower() == "no":
            tutorialActive = 0
            print("")
            print("Very well then, good luck on your candy hunting expidition!")
            time.sleep(5)
        else:
            print("")
            print("Don't worry, I am more than willing to explain it all again!")
            time.sleep(5)
        print("")     

def soloPlay():
    p1Candy = 0
    houseLuck = 0
    houseType = "normal"
    roundCount = 1
    costumeList = ["skeleton", "ghost", "vampire", "witch", "royal", "pirate", "scarecrow", "clown", "superhero", "doll", "dinosaur", "cowboy", "bear", "mermaid", "zombie"]
    prefferedCostume = ""
    selectedCostume = ""

    for roundCount in range(1,6):
        print(f"ROUND {roundCount}")
        time.sleep(2)
        print("")
        print("You approach the house...")
        time.sleep(3)
        print("")
        houseLuck = random.randint(1,20)
        if houseLuck == 1:
            houseType = "abandoned"
            print("Bad luck...you found the Abandoned House!")
        elif houseLuck == 20:
            houseType = "golden"
            print("Lucky you! You found the Golden Mansion!!")
        else:
            houseType = "normal"
            print("Looks like a normal house.")
        time.sleep(4)
        print("")
        prefferedCostume = costumeList[random.randint(0,14)]
        if prefferedCostume == "skeleton":
            print("The house looks like a graveyard is placed outside of it. Remains of lifeforms can be seen in the dirt.")
        elif prefferedCostume == "ghost":
            print("You don't know why, but this place just gives you the feeling of being watched by an otherworldly entity...")
        elif prefferedCostume == "vampire":
            print("Bats swarm around this house as if their owner lives in this castle-esque structure.")
        elif prefferedCostume == "witch":
            print("This castle-esque house looks perfect for a bit of a magic show!")
        elif prefferedCostume == "royal":
            print("This elegance of this house is palpable. It seems as if it would need guarding by a knight in shining armor!")
        elif prefferedCostume == "pirate":
            print("A sense of adventure can be felt in this house, almost as if there's a greater treasure to be found than candy!")
        elif prefferedCostume == "scarecrow":
            print("Cornstalks surround this home, in a maze-like structure. Not an animal in sight can be seen around this place...")
        elif prefferedCostume == "clown":
            print("It seems like getting candy from this house looks like a lot of fun! Maybe you'll even get a laugh out of it!!")
        elif prefferedCostume == "superhero":
            print("This house isn't as creepy as the others, but even so, it feels as though there's trouble afoot...")
        elif prefferedCostume == "doll":
            print("A lot of toys can be seen around this house. It's almost as if you're in one big playset!")
        elif prefferedCostume == "dinosaur":
            print("Dirty landscape? Boney creatures? Tall trees? This house is prehistoric!")
        elif prefferedCostume == "cowboy":
            print("It's quiet...almost too quiet. Like at any moment, a rival of yours could draw their gun...")
        elif prefferedCostume == "bear":
            print("This forestal house seems better of a place to find fish! Not candy!!")
        elif prefferedCostume == "mermaid":
            print("I hope you like the sea, because you'll need one HUGE fish fin to get to this house!")
        elif prefferedCostume == "zombie":
            print("This house seems...desolate. It's as if it came right out of a time of apocalypse!")
        else:
            print("Huh...I'm not actually sure about this house...oh well. Good luck!")
        time.sleep(8)
        print("")
        print("Which costume will you wear?")
        print("Please input your choice (Be gender neutral in your specified costume):")
        selectedCostume = input().lower()
        print("")
        print("You put on your costume and open the door...")
        time.sleep(3)
        if prefferedCostume == selectedCostume:
            if houseType == "abandoned":
                print("")
                print("The ghost inside liked your costume, and gave you 3 candy!")
                p1Candy += 3
            elif houseType == "golden":
                print("")
                print("The person inside really liked your costume, and gave you 10 candy!")
                p1Candy += 10
            else:
                print("")
                print("The person inside really liked your costume, and gave you 5 candy!")
                p1Candy += 5
        else:
            if houseType == "abandoned":
                print("")
                print("The ghost inside didn't like your costume...he stole 5 candy!")
                p1Candy -= 5
            elif houseType == "golden":
                print("")
                print("The person inside enjoyed your costume, and gave you 5 candy!")
                p1Candy += 5
            else:
                print("")
                print("The person inside enjoyed your costume, and gave you 3 candy!")
                p1Candy += 3
        if p1Candy < 0:
            p1Candy = 0
        time.sleep(5)
        if roundCount < 5:
            print("")
            print(f"{p1Name}'s Candy: {p1Candy}")
            time.sleep(3)
        print("")
    return p1Candy

def multiPlay():
    p1Candy = 0
    p2Candy = 0
    houseLuck = 0
    houseType = "normal"
    roundCount = 1
    costumeList = ["skeleton", "ghost", "vampire", "witch", "royal", "pirate", "scarecrow", "clown", "superhero", "doll", "dinosaur", "cowboy", "bear", "mermaid", "zombie"]
    prefferedCostume = ""
    selectedCostume = ""

    for roundCount in range(1,6):
        print(f"ROUND {roundCount}")
        time.sleep(2)
        print("")
        print(f"{p1Name}'s Turn!")
        time.sleep(2)
        print("")
        print("You approach the house...")
        time.sleep(3)
        print("")
        houseLuck = random.randint(1,20)
        if houseLuck == 1:
            houseType = "abandoned"
            print("Bad luck...you found the Abandoned House!")
        elif houseLuck == 20:
            houseType = "golden"
            print("Lucky you! You found the Golden Mansion!!")
        else:
            houseType = "normal"
            print("Looks like a normal house.")
        time.sleep(4)
        print("")
        prefferedCostume = costumeList[random.randint(0,14)]
        if prefferedCostume == "skeleton":
            print("The house looks like a graveyard is placed outside of it. Remains of lifeforms can be seen in the dirt.")
        elif prefferedCostume == "ghost":
            print("You don't know why, but this place just gives you the feeling of being watched by an otherworldly entity...")
        elif prefferedCostume == "vampire":
            print("Bats swarm around this house as if their owner lives in this castle-esque structure.")
        elif prefferedCostume == "witch":
            print("This castle-esque house looks perfect for a bit of a magic show!")
        elif prefferedCostume == "royal":
            print("This elegance of this house is palpable. It seems as if it would need guarding by a knight in shining armor!")
        elif prefferedCostume == "pirate":
            print("A sense of adventure can be felt in this house, almost as if there's a greater treasure to be found than candy!")
        elif prefferedCostume == "scarecrow":
            print("Cornstalks surround this home, in a maze-like structure. Not an animal in sight can be seen around this place...")
        elif prefferedCostume == "clown":
            print("It seems like getting candy from this house looks like a lot of fun! Maybe you'll even get a laugh out of it!!")
        elif prefferedCostume == "superhero":
            print("This house isn't as creepy as the others, but even so, it feels as though there's trouble afoot...")
        elif prefferedCostume == "doll":
            print("A lot of toys can be seen around this house. It's almost as if you're in one big playset!")
        elif prefferedCostume == "dinosaur":
            print("Dirty landscape? Boney creatures? Tall trees? This house is prehistoric!")
        elif prefferedCostume == "cowboy":
            print("It's quiet...almost too quiet. Like at any moment, a rival of yours could draw their gun...")
        elif prefferedCostume == "bear":
            print("This forestal house seems better of a place to find fish! Not candy!!")
        elif prefferedCostume == "mermaid":
            print("I hope you like the sea, because you'll need one HUGE fish fin to get to this house!")
        elif prefferedCostume == "zombie":
            print("This house seems...desolate. It's as if it came right out of a time of apocalypse!")
        else:
            print("Huh...I'm not actually sure about this house...oh well. Good luck!")
        time.sleep(8)
        print("")
        print("Which costume will you wear?")
        print("Please input your choice (Be gender neutral in your specified costume):")
        selectedCostume = input().lower()
        print("")
        print("You put on your costume and open the door...")
        time.sleep(3)
        if prefferedCostume == selectedCostume:
            if houseType == "abandoned":
                print("")
                print("The ghost inside liked your costume, and gave you 3 candy!")
                p1Candy += 3
            elif houseType == "golden":
                print("")
                print("The person inside really liked your costume, and gave you 10 candy!")
                p1Candy += 10
            else:
                print("")
                print("The person inside really liked your costume, and gave you 5 candy!")
                p1Candy += 5
        else:
            if houseType == "abandoned":
                print("")
                print("The ghost inside didn't like your costume...he stole 5 candy!")
                p1Candy -= 5
            elif houseType == "golden":
                print("")
                print("The person inside enjoyed your costume, and gave you 5 candy!")
                p1Candy += 5
            else:
                print("")
                print("The person inside enjoyed your costume, and gave you 3 candy!")
                p1Candy += 3
        if p1Candy < 0:
            p1Candy = 0
        time.sleep(5)
        print("")
        print(f"{p2Name}'s Turn!")
        time.sleep(2)
        print("")
        print("You approach the house...")
        time.sleep(3)
        print("")
        houseLuck = random.randint(1,20)
        if houseLuck == 1:
            houseType = "abandoned"
            print("Bad luck...you found the Abandoned House!")
        elif houseLuck == 20:
            houseType = "golden"
            print("Lucky you! You found the Golden Mansion!!")
        else:
            houseType = "normal"
            print("Looks like a normal house.")
        time.sleep(4)
        print("")
        prefferedCostume = costumeList[random.randint(0,14)]
        if prefferedCostume == "skeleton":
            print("The house looks like a graveyard is placed outside of it. Remains of lifeforms can be seen in the dirt.")
        elif prefferedCostume == "ghost":
            print("You don't know why, but this place just gives you the feeling of being watched by an otherworldly entity...")
        elif prefferedCostume == "vampire":
            print("Bats swarm around this house as if their owner lives in this castle-esque structure.")
        elif prefferedCostume == "witch":
            print("This castle-esque house looks perfect for a bit of a magic show!")
        elif prefferedCostume == "royal":
            print("This elegance of this house is palpable. It seems as if it would need guarding by a knight in shining armor!")
        elif prefferedCostume == "pirate":
            print("A sense of adventure can be felt in this house, almost as if there's a greater treasure to be found than candy!")
        elif prefferedCostume == "scarecrow":
            print("Cornstalks surround this home, in a maze-like structure. Not an animal in sight can be seen around this place...")
        elif prefferedCostume == "clown":
            print("It seems like getting candy from this house looks like a lot of fun! Maybe you'll even get a laugh out of it!!")
        elif prefferedCostume == "superhero":
            print("This house isn't as creepy as the others, but even so, it feels as though there's trouble afoot...")
        elif prefferedCostume == "doll":
            print("A lot of toys can be seen around this house. It's almost as if you're in one big playset!")
        elif prefferedCostume == "dinosaur":
            print("Dirty landscape? Boney creatures? Tall trees? This house is prehistoric!")
        elif prefferedCostume == "cowboy":
            print("It's quiet...almost too quiet. Like at any moment, a rival of yours could draw their gun...")
        elif prefferedCostume == "bear":
            print("This forestal house seems better of a place to find fish! Not candy!!")
        elif prefferedCostume == "mermaid":
            print("I hope you like the sea, because you'll need one HUGE fish fin to get to this house!")
        elif prefferedCostume == "zombie":
            print("This house seems...desolate. It's as if it came right out of a time of apocalypse!")
        else:
            print("Huh...I'm not actually sure about this house...oh well. Good luck!")
        time.sleep(8)
        print("")
        print("Which costume will you wear?")
        print("Please input your choice (Be gender neutral in your specified costume):")
        selectedCostume = input().lower()
        print("")
        print("You put on your costume and open the door...")
        time.sleep(3)
        if prefferedCostume == selectedCostume:
            if houseType == "abandoned":
                print("")
                print("The ghost inside liked your costume, and gave you 3 candy!")
                p2Candy += 3
            elif houseType == "golden":
                print("")
                print("The person inside really liked your costume, and gave you 10 candy!")
                p2Candy += 10
            else:
                print("")
                print("The person inside really liked your costume, and gave you 5 candy!")
                p2Candy += 5
        else:
            if houseType == "abandoned":
                print("")
                print("The ghost inside didn't like your costume...he stole 5 candy!")
                p2Candy -= 5
            elif houseType == "golden":
                print("")
                print("The person inside enjoyed your costume, and gave you 5 candy!")
                p2Candy += 5
            else:
                print("")
                print("The person inside enjoyed your costume, and gave you 3 candy!")
                p2Candy += 3
        if p2Candy < 0:
            p2Candy = 0
        time.sleep(5)
        if roundCount < 5:
            print("")
            print(f"{p1Name}'s Candy: {p1Candy}")
            print(f"{p2Name}'s Candy: {p2Candy}")
            time.sleep(3)
        print("")
    return p1Candy, p2Candy

def soloResults(p1TotalCollected):
    print("GAME OVER")
    time.sleep(3)
    print("")
    print(f"Welcome back, {p1Name}! Looks like all five rounds have concluded!")
    time.sleep(6)
    print("")
    print("Well, in that case, let's see how you did! Let's see how much candy you got!")
    time.sleep(6)
    print("")
    print(f"{p1Name}, your final score is...")
    time.sleep(7)
    if p1TotalCollected == 0:
        print("Nothing?! You didn't get anything?!")
        time.sleep(3)
        print("I feel bad for you! How many times did you have to find the abandoned house to get NOTHING?!")
    elif p1TotalCollected > 0 and p1TotalCollected < 16:
        print(f"A lackluster {p1TotalCollected} candy...")
        time.sleep(3)
        print("Don't get discouraged! It's never too late to try again! I'm sure that you got it next time!")
    elif p1TotalCollected > 15 and p1TotalCollected < 26:
        print(f"A modest {p1TotalCollected} candy!")
        time.sleep(3)
        print("Not too shaby! If I were you, I'd say this hunt was a success! But what do I know? I'm just a program! :D")
    elif p1TotalCollected > 25 and p1TotalCollected < 50:
        print(f"A massive {p1TotalCollected} candy!!")
        time.sleep(3)
        print("You must have been lucky enough to get the golden house this time around! Lucky you!!")
    elif p1TotalCollected == 50:
        print("I can't believe it!! A perfect 50 candy!!!")
        time.sleep(3)
        print("Never in my days have I seen ANYONE get the Golden Mansion FIVE TIMES IN THE SAME GAME! Simply incredible!!")
    time.sleep(8)
    print("")
    print("Well, either way, I hope you had fun! I hope to see you playing again soon! Thanks for playing Haunted Halloween Hunt! Buhbye!!")
    time.sleep(10)
    print("")
    endCard(p1TotalCollected, p1TotalCollected)

def multiResults(p1TotalCollected, p2TotalCollected):
    if p1TotalCollected > p2TotalCollected:
        gameWinner = p1Name
        scoreDifference = p1TotalCollected - p2TotalCollected
    elif p2TotalCollected > p1TotalCollected:
        gameWinner = p2Name
        scoreDifference = p2TotalCollected - p1TotalCollected
    else:
        gameWinner = "N/A"

    print("GAME OVER")
    time.sleep(3)
    print("")
    print(f"Welcome back, you two! Looks like all five rounds have concluded!")
    time.sleep(6)
    print("")
    print("Hope you've been trying hard, because we're about to reveal the winner!")
    time.sleep(6)
    print("")
    if gameWinner == "N/A":
        print(f"{p1Name}, {p2Name}, the winner is...")
    else:
        print(f"{p1Name}, {p2Name}, the winner, with a difference of {scoreDifference} candy, is...")
    time.sleep(12)
    if gameWinner == p1Name:
        print(f"{p1Name}! With a total of {p1TotalCollected} candy!!")
        time.sleep(6)
        print(f"Well done on the candy, {p1Name}! Oh, and {p2Name}, don't get discouraged it's never too late for round 2!")
    elif gameWinner == p2Name:
        print(f"{p2Name}! With a total of {p2TotalCollected} candy!!")
        time.sleep(6)
        print(f"Well done on the candy, {p2Name}! Oh, and {p1Name}, don't get discouraged it's never too late for round 2!")
    else:
        print("What?! A tie?!")
        time.sleep(6)
        print("Well well well, what to do in this situation...I guess you guys are obligated to go for another game!")
    time.sleep(8)
    print("")
    print("Well, either way, I hope you two had fun! I hope to see you playing again soon! Thanks for playing Haunted Halloween Hunt!")
    print("Buhbye!")
    time.sleep(10)
    print("")
    endCard(p1TotalCollected, p2TotalCollected)

def endCard(p1EndCard, p2EndCard):
    if mode == "singlePlayer":
        print(f"{p1Name}'s Candy: {p1EndCard}")
    else:
        print(f"{p1Name}'s Candy: {p1EndCard}")
        print(f"{p2Name}'s Candy: {p2EndCard}")
    print("")
    print("If you want to play again, close and reopen this script. Thanks for playing!")
    print("")
    print("Script made by Manuel Otero Jr. in DAE")

print("Welcome to Haunted Halloween Hunt! A Halloween candy obtaining extravaganza that you can play entirely within your computer's terminal!")
print("")
print("To start, will you be playing single player, or will you be playing 2 player battle mode?")
print("")
print("Please input the player count. (0-1 = Single Player Mode, 2+ = 2 Player Battle Mode)")
print("")
if int(input()) <= 1:
    mode = "singlePlayer"
else:
    mode = "multiPlayer"
print("")
if mode == "singlePlayer":
    playerCount = 1
    print("Solo it is then! Even alone you can still enjoy the spooky fun of Haunted Halloween Hunt!")
    print("")
    print("Next up on the agenda: Let's get your name so we can keep track of your candy!")
else:
    playerCount = 2
    print("Two's always better than one! Let's see which of you two can get the most candy!")
    print("")
    print("Next up on the agenda: Let's get your names so we can keep track of who's candy is who's!")
print("")
if playerCount == 1:
    print("Please input your name. This cannot be changed later!")
    print("")
    p1Name = input()
    print("")
    print(f"{p1Name} is a nice name! Let's see how you fair in the world of candy collecting!")
else:
    print("Please input player 1's name. This cannot be changed later!")
    print("")
    p1Name = input()
    print("")
    print("Please input player 2's name. This also cannot be changed later!")
    print("")
    p2Name = input()
    print("")
    print(f"So, it's a candy collecting duel between {p1Name} & {p2Name}...so be it, then!")
print("")
print("Would you like to go through a quick tutorial before we start?")
print("")
print("Please input the response 'Yes' or 'No'.")
print("")
if input().lower() == "yes":
    print("")
    print("Alright then! Let's go through the tutorial together!")
    print("")
    time.sleep(5)
    tutorial()
else:
    print("")
    print("Going in without? Very well then, good luck on your candy hunting expidition!")
    print("")
    time.sleep(5)

if mode == "multiPlayer":
    finalScores = multiPlay()
    p1FinalScore = finalScores[0]
    p2FinalScore = finalScores[1]
    multiResults(p1FinalScore, p2FinalScore)
else:
    p1FinalScore = soloPlay()
    soloResults(p1FinalScore)