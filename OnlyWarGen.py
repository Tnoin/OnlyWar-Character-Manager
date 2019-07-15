# imports
from dice import roll_die
from Data import Specialties, Characteristic_Aptitudes, Characteristic_Prices, CharacteristicLevel, SSkill_Aptitudes
from Functions import *

import Character
import math

# skillVars
heretic = False  # IT BETTER BE
char = Character.PlayerChar()

# generating characteristics:
counter = 0
for skill in char.Characteristic:
    fd = roll_die(10)
    sd = roll_die(10)
    dr = fd+sd
    sv = char.Characteristic[skill]+dr
    char.Characteristic[skill] = sv
    print(str(counter)+": "+str(skill) + " " + str(sv)+"(" + str(fd) + "|" + str(sd) + ") " + " CB: "+str(int(sv/10)))
    counter = counter + 1
print("")

print("Please enter the number of the line you would like to re-roll")
print("if you are happy with what the emperor has given you, enter 9")
reRoll = input()
print("")

if str(reRoll) == "praise Khorne":
    heretic = True
    char.Characteristic["WeaponSkill"] = 100
    char.Characteristic["BallisticSkill"] = 100
    char.Characteristic["Strength"] = 100
    char.Characteristic["Toughness"] = 30
    char.Characteristic["Willpower"] = 20
    char.Characteristic["Intelligence"] = 20
if str(reRoll) == "im Big E":
    for cha in char.Characteristic:
        char.Characteristic[cha] = 100
if reRoll.isdigit():
    if reRoll != 9:
        heretic = True
        if int(reRoll) < 9:
            counter = 0
            for skill in char.Characteristic:
                if int(counter) == int(reRoll):
                    fd = roll_die(10)
                    sd = roll_die(10)
                    dr = fd + sd
                    sv = char.Characteristic[skill] + dr
                    char.Characteristic[skill] = sv
                    print("re-roll complete" + ": "+str(skill) + " " + str(sv)+"(" + str(fd) + "|" + str(sd) + ") " + " CB: " + str(int(sv/10)))
                    break
                if int(counter) != int(reRoll):
                    counter = counter + 1

else:
    print("A NUMBER YOU HERETIC")
print("")

counter = 0
for speciality in Specialties:
    print(str(counter) + ": " + speciality)
    counter += 1
print("Choose a speciality:")
playerInput = input()
print("")

counter = 0
while 1:
    if playerInput.isdigit():
        for speciality in Specialties:
            if int(counter) != int(playerInput):
                counter += 1
            if int(counter) == int(playerInput):
                char.Class = speciality
                spec = Specialties[speciality]
                #char.Characteristic[spec["CB"]] = char.Characteristic[spec["CB"]]+5
                #print("new "+spec["CB"] + " is " + str(char.Characteristic[spec["CB"]]))
                char.Aptitudes = spec["Aptitudes"]
                print("As a " + str(speciality) + " your aptitudes are: ")
                # Aptitudes
                for apt in char.Aptitudes:
                    print("    "+apt)
                # Skills
                for skill in spec["Skills"]:
                    if "|OR|" in skill:
                        print("please choose between:")
                        choose = skill.split(" |OR| ")
                        choiceCount = 0
                        for choice in choose:
                            print("    " + str(choiceCount) + " " + choice)
                            choiceCount += 1
                        skillChose = input()
                        choiceCount = 0
                        for choice in choose:
                            if int(skillChose) == int(choiceCount):
                                found = False
                                for key in SSkill_Aptitudes:
                                    if key in skill:
                                        found = True
                                if (found):
                                    char.SSkills[choice] = 1
                                else:
                                    char.Skills[choice] = 1
                                break
                            if int(skillChose) != int(choiceCount):
                                choiceCount += 1

                    else:
                        found = False
                        for key in SSkill_Aptitudes:
                            if key in skill:
                                found = True


                        if(found):
                            char.SSkills[skill] = 1
                        else:
                            char.Skills[skill] = 1
                # Talents
                for talent in spec["Talents"]:
                    if "|OR|" in talent:
                        print("please choose between:")
                        choose = talent.split(" |OR| ")
                        choiceCount = 0
                        for choice in choose:
                            print("    " + str(choiceCount) + " " + choice)
                            choiceCount += 1
                        skillChose = input()
                        choiceCount = 0
                        for choice in choose:
                            if int(skillChose) == int(choiceCount):
                                char.Talents.append(choice)
                                break
                            if int(skillChose) != int(choiceCount):
                                choiceCount += 1

                    else:
                        char.Talents.append(talent)
                # Equip
                for Equip in spec["SpecialEquip"]:
                    if "|OR|" in Equip:
                        print("please choose between:")
                        choose = Equip.split(" |OR| ")
                        choiceCount = 0
                        for choice in choose:
                            print("    " + str(choiceCount) + " " + choice)
                            choiceCount += 1
                        skillChose = input()
                        choiceCount = 0
                        for choice in choose:
                            if int(skillChose) == int(choiceCount):
                                char.Equip.append(choice)
                                break
                            if int(skillChose) != int(choiceCount):
                                choiceCount += 1

                    else:
                        char.Equip.append(Equip)
                # Wounds
                wounds = spec["Wounds"]
                wounds_split = wounds.split("+")
                wound = int(wounds_split[0])
                wounddice = wounds_split[1].split("d")
                for i in range(int(wounddice[0])):
                    wound = wound + roll_die(int(wounddice[1]))
                char.Wounds = wound
                print("You have " + str(wound) + " Wounds")
                # XP
                char.XpAvailable = spec["StartXP"]
                char.XpEarned = spec["StartXP"]
                # Fate
                fateRoll = roll_die(10)
                if fateRoll < 8:
                    char.Fate = 1
                if fateRoll < 10:
                    char.Fate = 2
                if fateRoll == 10:
                    char.Fate = 3
                char.Implants = spec["Implants"]
                char.Traits = spec["Traits"]
                break
        break
    else:
        print("so you decided to be difficult huh...")
        playerInput = input("how about you try again?")



for i in range(10):
    print("")
print("Character Summary")
print("")
char.print()


while 1:
    print("")
    print("Current Options:")
    print("1: Print Character")
    print("2: Advance Characteristics")
    print("3: Advance Skills")
    print("4: Advance Special Skills")
    print("5: Advance Talents")

    playerChoose = input()
    if int(playerChoose) == 1:
        char.print()
    if int(playerChoose) == 2:
        levelCharacteristic(char)
    if int(playerChoose) == 3:
        levelSkills(char)
    if int(playerChoose) == 4:
        levelSSkills(char)
    if int(playerChoose) == 5:
        levelTalents(char)


