from Data import CharacteristicLevel, SkillLevel

class PlayerChar:
    Characteristic = {
        "WeaponSkill": 20,
        "BallisticSkill": 20,
        "Strength": 20,
        "Toughness": 20,
        "Agility": 20,
        "Intelligence": 20,
        "Perception": 20,
        "Willpower": 20,
        "Fellowship": 20
    }
    CharacteristicLevel = {
        "WeaponSkill": 0,
        "BallisticSkill": 0,
        "Strength": 0,
        "Toughness": 0,
        "Agility": 0,
        "Intelligence": 0,
        "Perception": 0,
        "Willpower": 0,
        "Fellowship": 0
    }
    Aptitudes = []
    Skills = {}
    SSkills = {}
    Talents = []
    Equip = []
    Wounds = 0
    Corruption = 0
    Class = ""
    XpAvailable = 0
    XpEarned = 0
    Fate = 0
    Implants = []
    Traits = []
    Talents = []
    Talents_repeatable = {}

# TODO Traits (mechanicus/psy-rating)
# TODO Implants (mechanicus/cripples)

    def print(self):
        print("Class:")
        print(self.Class)
        print("")
        print("Characteristics: ")
        for cha in self.Characteristic:
            char_level = CharacteristicLevel[self.CharacteristicLevel[cha]]
            print("    " + cha.ljust(15) + "(" + char_level + ") "+str(self.Characteristic[cha]))
            #print("    "+str(cha)+" "+str(self.Characteristic[cha]))
        print("")
        print("Skills: ")
        for skill in self.Skills:
            skill_level = SkillLevel[self.Skills[skill]]
            print("    " + skill.ljust(15) + "(" + skill_level + ") ")
            #print("    " + str(skill))
        print("")
        print("Specialist Skills: ")
        for skill in self.SSkills:
            skill_level = SkillLevel[self.SSkills[skill]]
            print("    " + skill.ljust(30) + "(" + skill_level + ") ")
            # print("    " + str(skill))
        print("")
        print("Talents: ")
        for talent in self.Talents:
            print("    " + str(talent))
        print("")
        print("Equipment: ")
        for equip in self.Equip:
            print("    " + str(equip))
        print("")
        print("Characteristics: ")
        print("Wounds: "+str(self.Wounds))
        print("")
        print("XP left:" + str(self.XpAvailable))



