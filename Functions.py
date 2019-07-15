from Data import *
import Character


def levelCharacteristic(char):
    prices = {}
    print("")
    print("Please Choose Characteristic, or press 0 to return")
    counter = 1
    for characteristic in char.Characteristic:
        matches = 2
        for apt in char.Aptitudes:
            if apt == characteristic:
                matches = matches - 1
            if apt == Characteristic_Aptitudes[characteristic]:
                matches = matches - 1
        prices[characteristic] = Characteristic_Prices[matches]
        charlevel = CharacteristicLevel[char.CharacteristicLevel[characteristic]]
        price = Characteristic_Prices[matches]
        if(price>char.XpAvailable):
            if showAll:
                print("    " + str(counter) + " " + characteristic.ljust(15) + "(" + charlevel + ") " + str(
                    Characteristic_Prices[matches]))
                counter = counter + 1
        else:
            print("    " + str(counter) + " " + characteristic.ljust(15) + "(" + charlevel + ") " + str(
                Characteristic_Prices[matches]))
            counter = counter + 1
    counter = 1
    playerinput = input()
    for characteristic in char.Characteristic:
        if int(counter) == int(playerinput):
            char.XpAvailable = char.XpAvailable - prices[characteristic]
            char.Characteristic[characteristic] = char.Characteristic[characteristic] + 5
            char.CharacteristicLevel[characteristic] = char.CharacteristicLevel[characteristic] + 1
            break
        if int(counter) != int(playerinput):
            if showAll:
                counter = counter + 1
            else:
                if characteristic in prices:
                    counter = counter + 1

def levelSkills(char):
    prices = {}
    print("")
    print("Please Choose Skill, or press 0 to return")
    counter = 1
    #for skill in char.Skills:
    for skill in Skill_Aptitudes:
        matches = 0
        skill_level_amount = 0
        if skill in char.Skills:
            skill_level_amount = char.Skills[skill]
        skill_level = SkillLevel[skill_level_amount]
        for aptitude in char.Aptitudes:
            if aptitude == Skill_Aptitudes[skill][0]:
                matches = matches + 1
            if aptitude == Skill_Aptitudes[skill][1]:
                matches = matches + 1
        price = Skill_price[matches][skill_level_amount]
        if (price > char.XpAvailable):
            if showAll:
                print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(
                    Skill_price[matches][skill_level_amount]))
                prices[skill] = Skill_price[matches][skill_level_amount]
                counter = counter + 1
        else:
            print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(
                Skill_price[matches][skill_level_amount]))
            prices[skill] = Skill_price[matches][skill_level_amount]
            counter = counter + 1
    counter = 1
    playerinput = input()
    for skill in Skill_Aptitudes:
        if int(counter) == int(playerinput):
            char.XpAvailable = char.XpAvailable - prices[skill]
            if skill not in char.Skills:
                char.Skills[skill] = 1
            else:
                char.Skills[skill] = char.Skills[skill] + 1
            break
        if int(counter) != int(playerinput):
            if showAll:
                counter = counter + 1
            else:
                if skill in prices:
                    counter = counter + 1


def levelSSkills(char):
    prices = {}
    print("")
    print("Please Choose Special Skill, or press 0 to return")
    counter = 1
    for skill in char.SSkills:
        matches = 0
        skill_level_amount = char.SSkills[skill]
        skill_level = SkillLevel[skill_level_amount]
        for aptitude in char.Aptitudes:
            if aptitude == SSkill_Aptitudes[skill.split(":")[0]][0]:
                matches = matches + 1
            if aptitude == SSkill_Aptitudes[skill.split(":")[0]][1]:
                matches = matches + 1
        price = Skill_price[matches][skill_level_amount]
        if (price > char.XpAvailable):
            if showAll:
                print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(Skill_price[matches][skill_level_amount]))
                prices[skill] = Skill_price[matches][skill_level_amount]
                counter = counter + 1
        else:
            print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(Skill_price[matches][skill_level_amount]))
            prices[skill] = Skill_price[matches][skill_level_amount]
            counter = counter + 1
    for skill in SSkill_Aptitudes:
        matches = 0
        skill_level_amount = 0
        skill_level = SkillLevel[skill_level_amount]
        for aptitude in char.Aptitudes:
            if aptitude == SSkill_Aptitudes[skill][0]:
                matches = matches + 1
            if aptitude == SSkill_Aptitudes[skill][1]:
                matches = matches + 1
        price = Skill_price[matches][skill_level_amount]
        if (price > char.XpAvailable):
            if showAll:
                print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(Skill_price[matches][skill_level_amount]))
                prices[skill] = Skill_price[matches][skill_level_amount]
                counter = counter + 1
        else:
            print("    " + str(counter).ljust(2) + " " + skill.ljust(15) + "(" + skill_level + ") " + str(
                Skill_price[matches][skill_level_amount]))
            prices[skill] = Skill_price[matches][skill_level_amount]
            counter = counter + 1
    counter = 1
    playerinput = input()
    for skill in char.SSkills:
        if int(counter) == int(playerinput):
            char.XpAvailable = char.XpAvailable - prices[skill]
            if skill not in char.SSkills:
                char.SSkills[skill] = 1
            else:
                char.SSkills[skill] = char.SSkills[skill] + 1
            return
        if int(counter) != int(playerinput):
            if showAll:
                counter = counter + 1
            else:
                if skill in prices:
                    counter = counter + 1
    for skill in SSkill_Aptitudes:
        if int(counter) == int(playerinput):
            char.XpAvailable = char.XpAvailable - prices[skill]
            skillname = input("Please Enter the Skills Name: ")
            skill = skill + ": " + skillname
            char.SSkills[skill] = 1
            return
        if int(counter) != int(playerinput):
            if showAll:
                counter = counter + 1
            else:
                if skill in prices:
                    counter = counter + 1


def levelTalents(char):
    print("")
    print("Which Tier would you like to Look at?")
    print("    1: Tier 1")
    print("    2: Tier 2")
    print("    3: Tier 3")
    print("    4: Repeatables")
    playerChoose = input()
    print("")
    if int(playerChoose) == 1:
        talentTier(char, Talent_Aptitudes_T1, 1)
    if int(playerChoose) == 1:
        talentTier(char, Talent_Aptitudes_T2, 2)
    if int(playerChoose) == 1:
        talentTier(char, Talent_Aptitudes_T3, 3)

def talentTier(char, talents, tier):
    prereqs = {}
    prices = {}
    counter = 1
    print("please choose Talent or enter 0 to return")
    for talent in talents:#look at pre-requisits
        meet_prereqs = True
        if "Characteristic" in talents[talent][0]:
            for cha in talents[talent][0]["Characteristic"]:
                talentValue = talents[talent][0]["Characteristic"][cha]
                if talentValue > char.Characteristic[cha]:
                    meet_prereqs = False
        if "Trait" in talents[talent][0]:
            for tra in talents[talent][0]["Trait"]:
                if tra in char.Traits:
                    meet_prereqs = False
        if "Implant" in talents[talent][0]:
            for tra in talents[talent][0]["Implant"]:
                if tra in char.Implants:
                    meet_prereqs = False
        prereqs[talent] = meet_prereqs
        matches = 0
        for apt in talents[talent][1]:
            if apt in char.Aptitudes:
                matches = matches + 1
        pricelevel = tier
        price = Talent_price[matches][pricelevel]
        if price < char.XpAvailable:
            if meet_prereqs:
                print("    "+str(counter).rjust(2)+" "+talent.rjust(20)+" "+str(price))
                counter = counter + 1
                prices[talent] = price
    counter = 1
    playerinput = input()
    for talent in talents:
        if int(counter) == int(playerinput):
            char.XpAvailable = char.XpAvailable - prices[talent]
            char.Talents.append(talent)
            return
        if int(counter) != int(playerinput):
            if talent in prices:
                counter = counter + 1


    # Options are characterisitc, Trait, Implant