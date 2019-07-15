# Construction Strings
HeavyTalentsWeapons ="Weapon Training(Bolt) |OR| Weapon Training(Chain) |OR| Weapon Training(Flame) |OR| Weapon Training(Las) |OR| Weapon Training(Launcher) |OR| Weapon Training(Melta) |OR| Weapon Training(Plasma) |OR| Weapon Training(Power) |OR| Weapon Training(Shock) |OR| Weapon Training(Solid Projectile)"
HeavyWeaponsSelect = "Common Craftsmanship missile launcher with 5 Frag Missiles |OR| Common Craftsmanship heavy stubber |OR| Common Craftsmanship Regimental Favoured Heavy Weapon"
# The List Itself
showAll = False
Specialties = {
    "Heavy Gunner": {
        "CB": "Toughness",
        "Aptitudes": ["BallisticSkill", "Defence", "Fellowship", "Offence", "Perception", "Toughness"],
        "Skills": ["Athletics |OR| Survival", "Common Lore: Imperial Guard", "Common Lore: War", "Intimidate"],
        "Talents": ["Iron Jaw", "Weapon Training(Las) |OR| Weapon Training(Solid Projectile)", "Weapon Training(Heavy)", "Weapon Training(Low-Tech)", HeavyTalentsWeapons],
        "SpecialEquip": [HeavyWeaponsSelect],
        "Wounds": "10+1d5",
        "StartXP": 600,
        "Implants": [],
        "Traits": [],
    },
    "Medic": {},
    "Operator": {},
    "Sergeant": {},
    "Weapons Specialist": {
        "CB": ["Ballistic Skill |OR| Weapon Skill"],
        "Aptitudes": ["Agility", "BallisticSkill", "Fellowship", "Fieldcraft", "Finesse", "Weapon Skill"],
        "Skills": ["Athletics or Survival", "Navigate(Surface)", "Common Lore (Imperial Guard, War)"],
        "Talents": ["Iron Jaw", "Weapon Training(Las) |OR| Weapon Training(Solid Projectile)", "Weapon Training(Heavy)", "Weapon Training(Low-Tech)", HeavyTalentsWeapons],
        "SpecialEquip": [HeavyWeaponsSelect],
        "Wounds": "10+1d5",
        "StartXP": 600,
        "Implants": [],
        "Traits": [],
    },
    "Commisar": {},
    "Ministorum Priest": {},
    "Ogryn": {},
    "Ratling": {},
    "Sanctioned Psykers": {},
    "Storm Trooper": {},
    "Tech-Priest Enginseer": {},
}

Characteristic_Aptitudes = {
        "WeaponSkill": "Offence",
        "BallisticSkill": "Finesse",
        "Strength": "Offence",
        "Toughness": "Defence",
        "Agility": "Finesse",
        "Intelligence": "Knowledge",
        "Perception": "Fieldcraft",
        "Willpower": "Psyker",
        "Fellowship": "Social"
}
Characteristic_Prices = [100, 250, 500, 750, 1000, 2500]
CharacteristicLevel = {
    0: "",
    1: "Simple",
    2: "Intermediate",
    3: "Trained",
    4: "Expert"
}
SkillLevel = {
    0: "",
    1: "Known",
    2: "Trained",
    3: "Experienced",
    4: "Veteran"
}
Skill_price = [
    [300, 600, 900, 1200],
    [200, 400, 600, 800],
    [100, 200, 300, 400]
]
Skill_Aptitudes = {
    "Acrobatics":   ["Agility", "General"],
    "Athletics":    ["Strength", "General"],
    "Awareness":    ["Agility", "General"],
    "Charm":        ["Fellowship", "Social"],
    "Command":      ["Fellowship", "Leadership"],
    "Commerce":     ["Intelligence", "Knowledge"],
    "Deceive":      ["Fellowship", "Social"],
    "Dodge":        ["Agility", "Defence"],
    "Inquiry":      ["Fellowship", "Social"],
    "Interrogation":["Willpower", "Social"],
    "Intimidate":   ["Strength", "Social"],
    "Logic":        ["Intelligence", "Knowledge"],
    "Medicae":      ["Intelligence", "Fieldcraft"],
    "Parry":        ["WeaponSkill", "Defence"],
    "Psyniscience": ["Perception", "Psyker"],
    "Scrutiny":     ["Perception", "General"],
    "Security":     ["Intelligence", "Tech"],
    "SleightofHand":["Agility", "Knowledge"],
    "Stealth":      ["Agility", "Fieldcraft"],
    "Survival":     ["Perception", "Fieldcraft"],
    "Tech-Use":     ["Intelligence", "Tech"]
}
SSkill_Aptitudes = {
    "Common Lore":   ["Intelligence", "Knowledge"],
    "Forbidden Lore":["Intelligence", "Knowledge"],
    "Linguistics":  ["Intelligence", "General"],
    "Navigate":     ["Intelligence", "Fieldcraft"],
    "Operate":      ["Agility", "Fieldcraft"],
    "Scholastic Lore":["Intelligence", "Knowledge"],
    "Trade":        ["Intelligence", "General"]
}
Talent_price = [
    [600, 900, 1200],
    [300, 450, 600],
    [200, 300, 400]
]
Talent_Aptitudes_T1 = {
    "Air of Authority": [{"Characteristic":{"Fellowship":30}},["Fellowship","Leadership"]],
    "Ambidextrous":     [{"Characteristic":{"Agility":30}},["WeaponSkill","BallisticSkill"]],
    "Berserk Charge":    [{},["Strength","Offence"]],
    "Blind Fighting":    [{"Characteristic":{"Perception":30}},["Perception","Fieldcraft"]],
    "Catfall":          [{"Characteristic":{"Agility":30}},["Agility", "Fieldcraft"]],
    "Chem Geld":         [{},["Willpower","Defence"]],
    "Combat Formation":  [{"Characteristic":{"Intelligence":40}},["Leadership","Fieldcraft"]],
    "Combat Sense":      [{"Characteristic":{"Perception":30}},["Perception","Fieldcraft"]],
    "Deadeye Shot":      [{"Characteristic":{"BallisticSkill":30}},["BallisticSkill","Finesse"]],
    "Die Hard":          [{"Characteristic":{"Willpower":40}},["Willpower","Defence"]],
    "Disarm":           [{"Characteristic":{"Agility":30}},["WeaponSkill","Defence"]],
    "Disturbing Voice":  [{},["Fellowship","Social"]],
    "Double Team":       [ {},["General","Offence"]],
    "Enemy":            [{},["General","Social"]],
    "Ferric Summons":    [{"Implant":["Ferric Lure", "Mechanicus"]},["Willpower","Tech"]],
    "Frenzy":           [{},["Strength","Offence"]],
    "IronJaw":          [{"Characteristic":{"Toughness":40}},["Toughness","Defence"]],
    "Jaded":            [{"Characteristic":{"Willpower":40}},["Willpower","Defence"]],
    "LeapUp":           [{"Characteristic":{"Agility":30}},["Agility","General"]],
    "Light Sleeper":     [{"Characteristic":{"Perception":30}},["Perception","Fieldcraft"]],
    "Lightning Reflexes":[{},["Agility","Fieldcraft"]],
    "Meditation":       [{},["Willpower","Knowledge"]],
    "Mimic":            [{},["Fellowship","Social"]],
    "Orthoproxy":       [{},["Willpower","Tech"]],
    "Peer":             [{"Characteristic":{"Fellowship":30}},["Fellowship", "Social"]],
    "Polyglot":         [{"Characteristic":{"Intelligence":40,"Fellowship":30}},["Intelligence","Social"]],
    "QuickDraw":        [{},["Agility","Finesse"]],
    "Radiant Presence":  [{"Characteristic":{"Fellowship":40}},["Fellowship","Leadership"]],
    "Rapid Reload":      [{},["Agility","Fieldcraft"]],
    "Sound Constitution":[{},["Toughness","General"]],
    "Street Fighting":   [{"Characteristic":{"WeaponSkill":30}},["WeaponSkill","Offence"]],
    "Sure Strike":       [{"Characteristic":{"WeaponSkill":30}},["WeaponSkill","Finesse"]],
    "Takedown":         [{},["WeaponSkill","Offence"]],
    "Technical Knock":   [{"Characteristic":{"Intelligence":30}},["Intelligence", "Tech"]],
    "Total Recall":      [{"Characteristic":{"Intelligence":30}},["Intelligence", "Knowledge"]],
    "Unarmed Warrior":   [{"Characteristic":{"WeaponSkill":35,"Agility":35}},["Strength", "Offence"]],
    "Unremarkable":     [{},["General","Social"]],
    "Warp Sense":        [{"Trait":["PsyRating"],"Skill":"Psyniscience","Characteristic":{"Perception":30}},["Perception","Psyker"]],
    "Weapon-Tech":      [{"SkillRating":["TechUse", 2], "Characteristic":{"Intelligence":40}},["Intelligence", "Tech"]],
}

Talent_Aptitudes_T2 = {
    "Armour-Monger":	 		[{"Characteristic":{"Intelligence":35},"Talent":"Tech-Use","SSkill":"Trade (Armourer)"},    ["Intelligence","Tech"]],
    "Battle Rage":	 			[{"Talent":"Frenzy"},                                                                       ["Strength","Defence"]],
    "Bulging Biceps":	 		[{"Characteristic":{"Strength":45}},                                                        ["Strength","Offence"]],
    "Combat Master":	 		[{"Characteristic":{"WeaponSkill":30}},                                                     ["Weapon Skill", "Defence"]],
    "Counter Attack":	 		[{"Characteristic":{"WeaponSkill":40}},                                                     ["Weapon Skill", "Defence"]],
    "Crack Shot":	 			[{"Characteristic":{"BallisticSkill":50}},	                                                ["Ballistic Skill"," Finesse"]],
    "Crippling Strike":	 		[{"Characteristic":{"WeaponSkill":50}},	                                                    ["Weapon Skill"," Finesse"]],
    "Deflect Shot":	 			[{"Characteristic":{"Agility":50}},	                                                        ["Weapon Skill","Defence"]],
    "Exotic Weapon Training":	[{},                                                                                        ["Intelligence"," Finesse"]],
    "Foresight":	 			[{"Characteristic":{"Intelligence":30}},                                                    ["Intelligence"," Knowledge"]],
    "Furious Assault":			[{"Characteristic":{"WeaponSkill":35}},                                                     ["Weapon Skill","Offence"]],
    "Hard Target":	 			[{"Characteristic":{"Agility":40}},	                                                        ["Agility","Defence"]],
    "Hardy":	  				[{"Characteristic":{"Toughness":40}},	                                                    ["Toughness","Defence"]],
    "Hip Shooting":		 		[{"Characteristic":{"BallisticSkill":40,"Agility":40}},                                     ["Ballistic Skill"," Finesse"]],
    "Hotshot Pilot":	 		[{"Characteristic":{"Agility":40},"SSkill":"Operate"},                                      ["Agility", "Fieldcraft"]],
    "Independent Targeting":	[{"Characteristic":{"BallisticSkill":40}},	                                                ["Ballistic Skill"," Finesse"]],
    "Inspire Wrath":	 		[{"Talent":"Air of Authority"},	                                                            ["Fellowship","Leadership"]],
    "Iron Discipline":	  		[{"Characteristic":{"Fellowship":30}}, 	                                                    ["Fellowship","Leadership"]],
    "Killing Strike":	 		[{"Characteristic":{"WeaponSkill":50}},                                                     ["Weapon Skill","Offence"]],
    "Luminen Shock":	 		[{"Implant":["Luminen Capacitors", "Mechanicus"]}, 	                                        ["Weapon Skill","Tech"]],
    "Maglev Transcendence":	 	[{"Implant":["Maglev Coils","Mechanicus"]},	                                                ["Intelligence","Tech"]],
    "Marksman":	 				[{"Characteristic":{"BallisticSkill":35}},	                                                ["Ballistic Skill"," Finesse"]],
    "Munitorum Influence": 		[{}, 	                                                                                    ["Fellowship","Social"]],
    "Nerves of Steel": 			[{}, 	                                                                                    ["Willpower","Defence"]],
    "Paranoia": 				[{}, 	                                                                                    ["Perception","Fieldcraft"]],
    "Precise Blow": 			[{"Characteristic":{"WeaponSkill":40},"Talent":"Sure Strike"},                              ["Weapon Skill"," Finesse"]],
    "Prosanguine":	 			[{"Implant":["Autosanguine", "Mechanicus"]}, 						                        ["Toughness", "Tech"]],
    "Rapid Reaction": 			[{"Characteristic":{"Agility":40}},						                                    ["Agility", "Fieldcraft"]],
    "Sharpshooter": 			[{"Characteristic":{"BallisticSkill":40},"Talent":"Deadeye Shot"}, 				            ["Ballistic Skill", "Finesse"]],
    "Strong Minded":	 		[{"Characteristic":{"Willpower":30},"TalentR":"Resistance (Psychic Powers)"},               ["Willpower", "Defence"]],
    "Storm of Iron":	 		[{"Characteristic":{"BallisticSkill":45},"TalentR":"Weapon Training"},                      ["Ballistic Skill", "Offence"]],
    "Swift Attack":	 			[{"Characteristic":{"WeaponSkill":30}},                                                     ["Weapon Skill","Finesse"]],
    "Two-Weapon Wielder (Ballistic)":	 [{},	                                                                            ["Ballistic Skill"," Finesse"]],
    "Two-Weapon Wielder (Melee)":	 [{},	                                                                                ["Weapon Skill"," Finesse"]],
    "Unarmed Master":		 	[{"Characteristic":{"WeaponSkill":45,"Agility":40},"Talent":"Unarmed Warrior"},	            ["Strength","Offence"]],
    "Unshakable Faith": 	 	[{"Characteristic":{"Willpower":35}}, 	                                                    ["Willpower","Defence"]],
    "Warp Conduit": 			[{"Trait":["PsyRating"],"Talent":"Strong Minded","Characteristic":{"Willpower":50}},        ["Willpower","Psyker"]],
    "Whirlwind of Death":	 	[{"Characteristic":{"WeaponSkill":40}},                                                     ["Weapon Skill","Finesse"]]
}

