import random #These are modules that I import from the languages files
import math
import turtle
#import esc_stats (create a file called esc_stats.py then uncomment out the import to save & load your game) *You cannot save items but you can change classes with your saved file*
import ast

#This is where I've added the story into the game, this will appear at the start and other portions of the story will happen during certain encounters
print("""A mercenary, is what some call you. A hero to few, who purges evil whever it may take root.
Someone who does not bat an eye when starring into the face of danger. You are a Lionheart.
You are close to arriving to the village of Gemini, a small village near the outskirts of a dense and dark forest.
You are tasked with expelling the evil that has overcome the village of Gemini.
A Wizard some say, who has cast foul minions to dispose of any opposition.
Geminin's council leader, Mereen, has been taken hostage and the people have leaded to the Kingdom for aid, so they sent you.\n\n""")
p_c = input("What hero shall you choose? (Warrior/Sorceress/Monk/Paladin/Ranger/Shaman/Warlock): ").lower() #Here, the user inputs which class they'd like to play
while (p_c != 'warrior') and (p_c != 'sorceress') and (p_c != 'monk') and (p_c != 'shaman') and (p_c != 'ranger') and (p_c != 'paladin') and (p_c != 'warlock'):
    p_c = input("What hero shall you choose? (Warrior/Sorceress/Monk/Paladin/Ranger/Shaman/Warlock): ").lower() #This is the safety net incase they do not enter a class
print("Please wait while the map is being created")
save = open("esc_stats.py", "r") #saves the file esc_stats.py as a variable to turn into stats later on

def main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c): #The main function
    
    while True: #Creates a never ending loop
        fight = 0 #Sets the variable fight to 0, turning it off
        if p_c == 'warrior': #creates stats based on class seletion, which are different depending on the class
            baseh = 449 #Base stats for a warrior
            if items.ring == 'true': #if the ring is equipped, it will changed the base health
                baseh = 450 + 750
            if items.amulet == 'true': #if the amulet is equipped, it will change the base health also
                baseh = baseh + 1000
            if items.trinket == 'true':#the final health upgrade is when the trinket is equipped
                baseh = baseh + 5000
            basea = 25
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 10
        elif p_c == 'sorceress': #sorceress
            baseh = 334
            if items.ring == 'true':
                baseh = 335 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 9
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            basea = 9
            based = 30
        elif p_c == 'monk': #monk
            baseh = 424
            if items.ring == 'true':
                baseh = 425 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 15
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 20
        elif p_c == 'paladin': #paladin
            baseh = 439
            if items.ring == 'true':
                baseh = 440 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 20
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 15
        elif p_c == 'ranger': #ranger
            baseh = 324
            if items.ring == 'true':
                baseh = 440 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 6
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 45
        elif p_c == 'shaman': #shaman
            baseh = 424
            if items.ring == 'true':
                baseh = 425 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 12
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 25
        elif p_c == 'warlock': #warlock
            baseh = 499
            if items.ring == 'true':
                baseh = 500 + 750
            if items.amulet == 'true':
                baseh = baseh + 1000
            if items.trinket == 'true':
                baseh = baseh + 5000
            basea = 5
            basea1 = 0
            basea2 = 0
            if items.chestplate == 'true':
                basea1 = 35
            elif items.helm == 'true':
                basea2 = 75
            basea = basea + basea1 + basea2
            based = 10
        if p_c == 'sorceress':#This is where stat crunching and scalling is applied *based on level
            p_h = baseh + ((15 + level1) * level1)
            p_a = basea + (3 * level1)
            p_d = based + ((15 + level1) * level1)
        elif p_c == 'warrior':
            p_h = baseh + ((30 + level1) * level1)
            p_a = basea + (5 * level1)
            p_d = based + ((10 + level1) * level1)
        elif p_c == 'monk':
            p_h = baseh + ((30 + level1) * level1)
            p_a = basea + (4* level1)
            p_d = based + ((12 + level1) * level1)
        elif p_c == 'paladin':
            p_h = baseh + ((25 + level1) * level1)
            p_a = basea + (5 * level1)
            p_d = based + ((10 + level1) * level1)
        elif p_c == 'ranger':
            p_h = baseh + ((15 + level1) * level1)
            p_a = basea + (2 * level1)
            p_d = based + ((20 + level1) * level1)
        elif p_c == 'shaman':
            p_h = baseh + ((25 + level1) * level1)
            p_a = basea + (4 * level1)
            p_d = based + ((15 + level1) * level1)
        elif p_c == 'warlock':
            p_h = baseh + ((25 + level1) * level1)
            p_a = basea + (5 * level1)
            p_d = based + ((10 + level1) * level1)
        print("\n1. Adventure!")#The general options of the main function
        print("2. Return to Town")
        print("3. Abilities & Stats")
        print("4. Inventory")
        print("5. View turn count")
        print("6. Level up your skills")
        print("7. Quit & Save")

        selection = input("Choose your path: ") #Choice chosen from the menu
        print("\n")
        try:
            selection = int(selection)
        except ValueError:#This prevents the program from crashing if the input isn't valid
            print('Invalid selction')
            main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c)#runs main function
        else:
            while (selection < 0) or (selection > 7):
                print("Invalid selection")
                selection = input("Refer to the map and select the location of where you'd like to travel to [Numerical Value (1-30 or 'stats')]: ")
                try:
                    selection = int(selection)
                except ValueError:
                    print('Invalid selection')
                    main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c)#runs main function
        if selection == 1: #Challenge monsters
            if skill_up < 1: #Prevents player from challenging monsters w/ an unspent ability point -- which would crash the program
                Reward = Adventure(p_c, p_d, p_a, p_h, exp, gold, potion_count, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, turn, items, stats)
                potion_count = Reward[0]
                exp = Reward[1]
                gold = Reward[2]
                turn = Reward[3]
            else:
                print("\n\nYou must level an ability first")
                print("You have", skill_up, "ability points")
        elif selection == 2: #Takes you to the town function
            RTT = ReturntoTown(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, p_c, stats, p_h, p_a, p_d)
        elif selection == 3: #Shows your abilities & spent ability points
            Showp_ab(p_c, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, p_h, p_a, p_d)
        elif selection == 4: #Opens the inventory which has gold, items, and experience
            Inventory(gold, items, level1, level2, exp)
        elif selection == 5: #Displays the current turn number
            print(turn, 'turns')
        elif selection == 6: #skill leveling
           if skill_up > 0:
                m_ch, m_h, m_n = [0 for loop in range(3)] #necessary precautions to prevent crashing
                round1 = 'false'
                trait = 'false'
                trait2 = 'false'
                trait3 = 'false'
                trait4 = 'false'
                CD1 = 'false'
                CD2 = 'false'
                CD3 = 'false'
                skills = p_ab(p_c, p_d, p_a, m_ch, m_h, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, fight, m_n, items, round1, trait, trait2, trait3, trait4, CD1, CD2, CD3)
                ab1_skillup = skills[0]
                ab2_skillup = skills[1]
                ab3_skillup = skills[2]
                ab4_skillup = skills[3]
                skill_up = skills[4]
                print("You have", skill_up, "ability points left")
           else:
               print("You must level up to gain an ability point, you current have 0")
        elif selection == 7: #This option saves the current stats, but not items, may also fail to properly exit the game due to nested functions
            print("Goodbye!")
            save = open("esc_stats.py", "w")
            gold = str(gold)
            level1 = str(level1)
            level2 = str(level2)
            turn = str(turn)
            stats = str(stats)
            ab1_skillup = str(ab1_skillup)
            ab2_skillup = str(ab2_skillup)
            ab3_skillup = str(ab3_skillup)
            ab4_skillup = str(ab4_skillup)
            for loop in [gold, turn, stats, level1, level2, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup]: #loop that writes stats in esc_stats.py
                save.write(loop)
                save.write('\n')
            save.close()
            sys.exit()
        else:
            print("That path is not yours")
        while exp > level2: #This loop controls the leveling mechanics
            exp = exp - level2
            level1 = int(level1 + 1)
            print('You are level', level1)
            level2 = int(level2 * 1.0625) #The ratio at which experience increases by for the next level
            skill_up = skill_up + 1 #Gives you an ability point to spend
            print('You have', skill_up, 'ability points')
# -------------------------------------------------
def InTown(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, p_c, stats, p_h, p_a, p_d): #Town menu
    while True: #The town's menu
        print("\n1. Leave town")
        print("2. Shop")
        print("3. Gamble")
        print("4. Abilities")
        print("5. Inventory")
        print("6. View turn count")

        selection = input("What would you like to do?: ") #Players town input
        while (selection != '1') and (selection != '2') and (selection != '3') and (selection != '4') and (selection != '5') and (selection != '6') and (selection != 7):
            print("You cannot do that in town")
            selection = input("What would you like to do?: ")
        selection = int(selection)
        if selection == 1: #takes the player to main function
            main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c)
        elif selection == 2: #takes the player to the shop function
            shop = Shop(gold, potion_count, items)
            try:
                potion_count = shop[0]
            except TypeError:
                main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c) #returns to main
            gold = shop[1]
        elif selection == 3: #The Gamble selection, proceeds to run the Gambling function
            gamble = Gamble(gold, p_c, items)
            gold = gamble[0]
        elif selection == 4: #shows abilities
            Showp_ab(p_c, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, p_h, p_a, p_d)
        elif selection == 5: #shows items
            Inventory(gold, items, level1, level2, exp)
        elif selection == 6: #prints the current turn number
            print(turn, 'turns')
        else:
            print("You cannot do that in town")
# -------------------------------------------------
def Fight(p_c, p_h, p_a, p_d, exp, gold, potion_count, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, turn, items, monster): #the fighting function
    m = monster[0] #Turns the array Monster into the selected monster's stats
    m_n = monster[1]
    m_h = monster[2]
    m_d = monster[3]
    m_exp = monster[4]
    m_gold = monster[5]
    print("\nYou've encountered", m)    #Displays the monster's name you're encountering
    m_ch = m_h #sets dynamic variables from the static varibles to be used in the fighting algorithms
    sm_d = m_d
    p_ch = p_h
    sp_a = p_a
    sp_d = p_d
    x = 1
    y = 1
    fight_turn, turn2, turn3, turn4, turn5, trait, trait2, trait3, trait4, CD1, CD2, CD3, sw_d, sp_d1, sp_h1, sp_d2, sp_h2, sp_d3, sp_h3, bael_d, bael_h = [0 for loop in range(21)]
    round1 = 'true'
    while (p_ch >1) and (m_ch > 1):
        if m == 'Demon Spawn': #The Demon Spawn's mechanic
            if x == fight_turn: #adds another Demon Spawn w/ increasing intervals
                m_n = m_n + 1
                m_ch = m_ch + 75000
                m_d = m_d + 850
                m_exp = m_exp + 250
                m_gold = m_gold + 100
                x = x + y
                y = y + 1
        if m == 'Wandering Magi': #The Wandering Magi's fighting mechanic
            m_d = sm_d + (50 * fight_turn)
        m_ch = int(m_ch)
        if m == 'Minotaur': #The Mintoaur's fighting mechanic
            m_d = 35 + (200 * (m_ch / m_h))
        p_ch = int(p_ch)
        print("\n"+m+':', m_ch)
        print("Player:", p_ch, "\n")
        fight = 1 #Turns Fighting on & sets the stage for fighting, below calls the ability functions which the player chooses from
        ability = p_ab(p_c, p_d, p_a, m_ch, m_h, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, fight, m_n, items, round1, trait, trait2, trait3, trait4, CD1, CD2, CD3)
        attack = ability[0] #Sets variables from the ability array
        AoE = ability[1]
        Name = ability[2]
        trait = ability[3]
        trait2 = ability[4]
        trait3 = ability[5]
        trait4 = ability[6]
        CD1 = ability[7]
        CD2 = ability[8]
        CD3 = ability[9]
        round1 = 'false'
        fight_turn = fight_turn + 1 #Increases the turn interval by 1
        if p_c == 'sorceress': #This is all the mechanics involved with the Sorceress class
            if Name == 'Barrier': #mechanics involved w/ the ability Barrier
                bturn = fight_turn + (1 * ab1_skillup)
                armor = attack
                attack = 0
            if turn2 >= fight_turn:
                p_a = p_a + armor
            if turn2 < fight_turn:
                p_a = sp_a
            if (Name == 'Meteor') and (trait == 15): #Mechanics involved w/ the Meteor ability
                turn3 = fight_turn + 3
            if turn3 >= fight_turn:
                m_ch = int(m_ch - (m_h * 1/20))
        if p_c == 'warrior': #mechanics for the warrior
            if Name == 'Vampiric Strike': #mechanics involved w/ Vampiric Strike ability
                p_ch = p_ch + (attack * (trait * .01))
                if p_ch > p_h:
                    p_ch = p_h
            if Name == 'Execute': #mechanics involved w/ the Execute ability
                sm_ch = m_ch
                m_ch = m_ch - attack
                if m_ch > 0:
                    m_ch = sm_ch
                    attack = attack * .3
        if p_c == 'monk': #mechanics for the Monk
            if Name == 'Exploding Palm': #mechanics involved w/ Exploding Palm ability
                turn2 = fight_turn + 3
                DoT = attack
                attack = 0
            if turn2 > fight_turn:
                m_ch = m_ch - DoT
                if items.blindfold == 'true': #mechanics involved w/ the Monk item: blindfold
                    if trait < 5:
                        trait = trait + 1
            if Name == 'Endurance': #mechanics involved w/ the ability Endurance
                turn3 = fight_turn + 3
                armor = attack
                attack = 0
            if turn3 >= fight_turn:
                m_d = int(sm_d - (sm_d * (armor * .01)))
        if p_c == 'paladin': #mechanics for the Paladin
            if (turn2 >= fight_turn) and (turn4 >= fight_turn): #mechanic that controls the Damage Over Time effects
                DoT = DoT + (DoT * .2)
                DoT2 = DoT2 + (DoT2 * .2)
            if Name == 'Hammer Fury': #mechanics involved w/ the ability Hammer Fury
                turn2 = fight_turn + 4
                DoT = attack
                attack = 0
            if turn2 >= fight_turn:
                m_ch = m_ch - (DoT * m_n)
            if items.mace == 'false':
                if Name == 'Defensive/Offensive Aura': #mechanics of Paladin's aura ability
                    if trait % 2 != 0:
                        p_d = sp_d
                        p_a = p_a + attack + p_a
                    if trait % 2 == 0:
                        p_a = sp_a
                        p_d = p_d + attack + p_d
                    attack = 0
            elif items.mace == 'true': #mechanics involved w/ the Paladin item: Mace
                if Name == 'Defensive/Offensive Aura':
                    p_d = sp_d + trait3 + p_d
                    p_a = sp_a + trait2 + p_a
                    attack = 0
            if Name == 'Hammer of Justice':
                turn3 = fight_turn + 2
                turn5 = fight_turn + 1
                turn4 = fight_turn + 3
                DoT2 = attack * .5
            if turn4 >= fight_turn:
                m_ch = m_ch - (DoT2 * m_n)
            if turn5 > fight_turn:
                m_d = 0
            if turn3 == fight_turn:
                attack = attack + (attack * .25)
        if p_c == 'ranger':
            if items.bow == 'true':
                if trait % 3 == 0:
                    attack = attack + (3 * p_d)
            if Name == 'Stun Arrow':
                turn2 = fight_turn + 1
            if turn2 >= fight_turn:
                m_d = 0
            if Name == 'Clone':
                turn3 = fight_turn + 1
                turn4 = fight_turn + 1
                b_d = attack
                attack = 0
            if turn3 >= fight_turn:
                m_d = 0
            if items.quiver == 'true':
                turn4 = fight_turn + 3
            if turn4 >= fight_turn:
                p_d = p_d + b_d
            if Name == 'Counter Strike':
                attack = attack + m_d
        if p_c == 'shaman':
            if Name == 'Flame Totem':
                attack = 0
            if trait > 0:
                m_ch = m_ch - ((trait * trait2) * m_n)
            if Name == 'Spring Totem':
                attack = 0
            if trait3 > 0:
                p_ch = p_ch + (trait3 * trait4)
                if p_ch > p_h:
                    p_ch = p_h
            if Name == 'Earth Shock':
                turn3 = fight_turn + 2
            if turn3 > fight_turn:
                m_d = m_d - (m_d * (.5 * ab3_skillup))
            if Name == 'Windwalker':
                turn5 = fight_turn + 1
            if turn5 >= fight_turn:
                m_d = 0
        if p_c == 'warlock':
            if Name == 'Summon Shadowlings':
                static_swd = attack
                sw_d = int(attack * trait4)
            if Name == 'Summon Spirit':
                if (trait % 2 != 0) and (trait % 3 != 0):
                    sp_d1 = int(attack * (trait4 / 2))
                    sp_h1 = int(trait2 * (trait4 / 2))
                    print('Spirit1 has', sp_h1, 'health and', sp_d1, 'damage')
                elif (trait % 2 == 0) and (trait % 3 != 0):
                    sp_d2 = int(attack * (trait4 / 2))
                    sp_h2 = int(trait2 * (trait4 / 2))
                    print('Spirit2 has', sp_h2, 'health and', sp_d2, 'damage')
                elif (trait % 3 == 0):
                    sp_d3 = int(attack * (trait4 / 2))
                    sp_h3 = int(attack * (trait4 / 2))
                    print('Spirit3 has', sp_h3, 'health and', sp_d3, 'damage')
                trait3 = int((trait4 / 2) + trait3)
                trait4 = int(trait4 / 2)
            if Name == 'Summon Baelrog':
                static_trait3 = trait3
                bael_d = int((attack * trait3) + p_d)
                bael_h = int((15 + (15 * .3 * ab4_skillup) * trait3) + p_h)
                print('Your Baelrog has', bael_h, 'health and', bael_d, 'damage')
                trait3, trait4 = [0 for loop in range(2)]
            if bael_h > 0:
                bael_h = int(bael_h - m_d)
                m_d = 0
                if (items.brain == 'true') & (bael_h < 1):
                    if static_trait3 > 10:
                        trait4 = trait4 + 3
                        sw_d = int(static_swd * trait4) + sw_d
                    elif static_trait3 > 5:
                        trait4 = trait4 + 2
                        sw_d = int(static_swd * trait4) + sw_d
                    elif static_trait3 > 0:
                        trait4 = trait4 + 1
                        sw_d = int(static_swd * trait4) + sw_d
                if bael_h <= 0:
                    bael_d, bael_h = [0 for loop in range(2)]
            m_ch = m_ch - int(sw_d + sp_d1 + sp_d2 + sp_d3 + bael_d)
            hit_chance = random.randrange(1,11)
            if sp_h1 > 0:
                if hit_chance < 8:
                    sp_h1 = int(sp_h1 - m_d)
                    m_d = 0
                    if sp_h1 <= 0:
                        sp_d1, sp_h1 = [0 for loop in range(2)]
            if sp_h2 > 0:
                if hit_chance < 8:
                    sp_h2 = int(sp_h2 - m_d)
                    m_d = 0
                    if sp_h2 <= 0:
                        sp_d2, sp_h2 = [0 for loop in range(2)]
            if sp_h3 > 0:
                if hit_chance < 8:
                    sp_h3 = int(sp_h3 - m_d)
                    m_d = 0
                    if sp_h3 <= 0:
                        sp_d3, sp_h3 = [0 for loop in range(2)]
        if AoE == 'true':
            attack = attack * m_n
        m_ch = m_ch - attack #damaging monster
        if (m == 'Wandering Magi') and (m_ch <= 0):
            m = "Goliath's Henchmen (2)"
            m_n = 2
            m_ch = 125000
            m_d = 1200
            m_exp = m_exp + 350
            m_gold = m_gold + 100
            print("\n\tAs the mage falls, a swirling darkness appears above him, a flash of light appears from the center of the swirl")
            print('and three dark figures come forth and the center one speaks with evil in its voice')
            print('"Greetings Lionheart, I see you have done well killing my beasts this far, but Golaith has many more allies"')
            print('"You see, I am not fond of your presence here, so here are two of my henchmen, who will finish you off in the name of GOLIATH the Wizard!"')
        if (m == "Goliath's Summoned Beasts (5)") and (m_ch <= 0):
            m = "Goliath's Apprentice"
            m_n = 1
            m_ch = 350000
            m_d = 3000
            m_exp = m_exp + 750
            m_gold = m_gold + 250
            print("\n\tAs you scavenge around the dead bodies of the beasts, you feel a presence of something evil and you turn around")
            print('Standing before you, is a large man with dark robes with a long sturdy stick held up by both hands with swirling eyes')
            print('"Goliath has sent me here to finish you once and for all, Lionheart"')
        if (m == "Goliath the Unyielding") and (m_ch <= 0):
            m = "Goliath the Corrupt"
            m_n = 1
            m_h = 250000
            m_ch = m_h
            m_d = 4000
            m_exp = m_exp + 1000
            m_gold = m_gold + 500
            print("Goliath lays across the floor, dying.. He reaches into his pocket and pulls out a vial, full of a thick red liquid")
            print('Before you can react he sips it down, "Heh heh, now behold the power of Evil Lionheart! I am Goliath the Corrupt!"')
        if (m == "Goliath the Corrupt") and (m_ch <= 0):
            m = "Goliath the Undying"
            m_n = 1
            m_h = 5000000
            m_ch = m_h
            m_d = 3250
            m_exp = m_exp + 1000
            m_gold = m_gold + 500
            print("Goliath's skin begins to shrivel apart, and parts of his skeleton shows through, he is truly a monstrocity.")
            print('In a harsh and rasp voice Goliath speaks,')
            print('"Heeeh heh, my master has granted me powers beyond death, your end is here Lionheart"')
        if m_ch <= 0:
            print("Victory!")
            exp = exp + m_exp
            gold = gold + m_gold
            if m == 'Black Jack the Woodsmen':
                print("Listen sir, you have defeated me and broken the curse, I can tell you now where the man you seek dwells.")
                print("The man has a castle that way, *points deeper into the woods* but beware, he has a lot of deadly creatures")
            return (potion_count, exp, gold, turn, 'victory')
        if (m_n > 1):
            m_hpu = m_h / m_n
            n = 1
            h_l = m_h - (m_hpu * n)
            if m_ch <= h_l:
                d_l = m_d / m_n
                m_d = m_d - (d_l * n)
                n = n + 1
        if items.shield == 'true':
            m_d = m_d - (m_d * .2)
        if (p_c == 'shaman'):
            if m_d > 0:
                t_hit = random.randrange(1, 6)
                if (trait > 0) and (t_hit == 1):
                    trait = 0
                    m_d = m_d - (m_d * .8)
                    print(m,"has destroyed your Flame Totem(s)")
                if (trait3 > 0) and (t_hit == 5):
                    trait3 = 0
                    m_d = m_d - (m_d * .8)
                    print(m,"has destroyed your Spring Totem(s)")
        if p_c == 'warlock':
            print('\n\n')
            if trait4 > 0:
                print(trait4, 'Shadowling(s):', sw_d, 'damage')
            if sp_h1 > 0:
                print('Spirit1:', sp_h1, 'HP &', sp_d1, 'Damage')
            if sp_h2 > 0:
                print('Spirit2:', sp_h2, 'HP &', sp_d2, 'Damage')
            if sp_h3 > 0:
                print('Spirit3:', sp_h3, 'HP &', sp_d3, 'Damage')
            if bael_h > 0:
                print('Baelrog:', bael_h, 'HP &', bael_d, 'Damage')
        if (m_d <= 0) or (p_a >= m_d):
            p_ch = p_ch
        else:
            p_ch = int(p_ch - (m_d - p_a)) #monster damaing player
        m_d = sm_d
        p_ch = int(p_ch)
        m_ch = int(m_ch)
        turn = turn + 1
        if potion_count > 0:
            potion_use = input('Would you like to use a potion?: ')
            if potion_use == 'yes':
                p_ch = p_ch + 250
                potion_count = potion_count - 1
    if p_ch <= 0:
        print(m, m_ch, "health")
        print("You have been defeated, +5 turns")
        turn = turn + 5
        return (potion_count, exp, gold, turn, 'not victory')
# -------------------------------------------------
def Showp_ab(p_c, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, p_h, p_a, p_d): #Prints class-based abilities
    print('Health: {1}\nDamage: {2}\nArmor: {3}'.format(id,p_h,p_d,p_a))
    if p_c == 'warrior':
        print("Q - Vampiric Strike -", ab1_skillup, "- Strikes your foe with moderate damage and healing for a % of your damage")
        print("W - Slice N' Dice -", ab2_skillup, "- Attacks twice")
        print("E - Cleave -", ab3_skillup, "- Strikes all opponents")
        print("R - Execute -", ab4_skillup, "- Does more damage based on opponent's missing health (Only does 1/3rd of the damage if it does not kill)")
    elif p_c == 'sorceress':
        print("Q - Barrier -", ab1_skillup, "- Shield yourself reducing damage taken")
        print("W - Frost Strike -", ab2_skillup, "- Strike your foe with the power of the elements")
        print("E - Fire Nova -", ab3_skillup, "- Strike all opponents with elemental power")
        print("R - Meteor -", ab4_skillup, "- Summon a powerful meteor to deal devastating damage [CD: 3]")
    elif p_c == 'monk':
        print("Q - Sacred Fist -", ab1_skillup, "- Deal moderate damage, marking the target")
        print("W - Exploding Palm -", ab2_skillup, "- Creates a continual AoE damage for 3 turns")
        print("E - Endurance -", ab3_skillup, "- Marks a target and reduces damage taken by a percentage")
        print("R - Dragon Fist -", ab4_skillup, "- Consumes marks to deal increasing damage (Max 5)")
    elif p_c == 'shaman':
        print("Q - Fire Totem -", ab1_skillup, "- Periodically deals strong single and AoE target damage, may be targeted (max 3)")
        print("W - Healing Totem -", ab2_skillup, "- Creates a healing stream for you and your Golem, may be targeted (max 3) [CD: 3]")
        print("E - Earth Shock -", ab3_skillup, "- Shocks the enemy and reduces their damage by a percent [CD: 2]")
        print("R - Windwalker -", ab4_skillup, "- Creates fury of wind to deal damage and daze your oppoent for 1 turn and takes more damage while stunned")
    elif p_c == 'ranger':
        print("Q - Lightning Arrow -", ab1_skillup, "- Deals strong damage that channels through all opponents")
        print("W - Stun Arrow -", ab2_skillup, "- Deals minimal damage and stuns all targets for 1 turn (2 turns on multiples of 3) [CD: 5]")
        print("E - Shadow Clone -", ab3_skillup, "- Summons a clone that'll take damage for you [CD: 5]")
        print("R - Counter Strike -", ab4_skillup, "- Does high damage that increases based on the monster's last attack [CD: 5]")
    elif p_c == 'paladin':
        print("Q - Hurl Hammer -", ab1_skillup, "- Hurl your hammer dealing moderate damage")
        print("W - Hammer Fury -", ab2_skillup, "- Spinning hammers float around you for 3 turns dealing damage to all opponents")
        print("E - Defensive/Offensive Aura -", ab3_skillup, "- Decreases damage taken or increases your damage (multiples of 2 are Offensive Aura)")
        print("R - Hammer of Justice -", ab4_skillup, "- Powerful hammer falls from the sky\n dealing massive damage & consecrating the ground for 2 turns [CD: 5]\n Also stuns the enemy for 1 turn\n If both Consecration and Hammer of Justice are active both of their damage is increased")
    elif p_c == 'warlock':
        print("Q - Summon Shadow -", ab1_skillup, "- Summon's a weak shadowling (max 10)")
        print("W - Mind Sear -", ab2_skillup, "- Sears a monster's mind and causes it to deal damage to other nearby monsters")
        print("E - Summon Spirit -", ab3_skillup, "- Sacrifices half of Summoned Shadows with scaling health per each shadow (max 3) - Costs health also")
        print("R - Sacrifice -", ab4_skillup, "- Sacrifices all minions to summon a Baelrog, health & damage scale w/ minion and type sacrificed (max 1)")
# -------------------------------------------------
def p_ab(p_c, p_d, p_a, m_ch, m_h, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, fight, m_n, items, round1, trait, trait2, trait3, trait4, CD1, CD2, CD3):
    if skill_up > 0: #Levels up the abilities
         choice = input("Which ability would you like to level up? (Q, W, E, R): ")
         choice = choice.lower()
         while (choice != 'q') and (choice != 'w') and (choice != 'e') and (choice != 'r'):
             choice = input("Which ability would you like to level up? (Q, W, E, R): ")
             choice = choice.lower()
         skill_up = skill_up - 1
         if choice == 'q':
            ab1_skillup = ab1_skillup + 1
            return (ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, skill_up)
         elif choice == 'w':
            ab2_skillup = ab2_skillup + 1
            return (ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, skill_up)
         elif choice == 'e':
            ab3_skillup = ab3_skillup + 1
            return (ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, skill_up)
         elif choice == 'r':
            ab4_skillup = ab4_skillup + 1
            return (ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, skill_up)
    if fight == 1: #Inputs the abilities into the fighting function
        CD1 = CD1
        CD2 = CD2
        CD3 = CD3
        ab5 = 0
        if round1 == 'true':
            trait2, trait3, atk_no, mark, aura, d_totem, h_totem, shadowling = [0 for loop in range(8)]
            if items.enchanted_sticks == 'true':
                d_totem = 1
                h_totem = 1
            if items.bones == 'true':
                shadowling = 3
                trait4 = 3
        if p_c == 'warrior': #Warrior ability scaling
            trait = 15
            ab1 = 40 + (40 * .2 * ab1_skillup) + p_d
            ab2 = (12 + (12 * .33 * ab2_skillup) + 15) * 2
            if items.sword == 'true':
                ab2 = ab2 * 1.5
            ab3 = 45 + (45 * .25 * ab3_skillup) + p_d
            exe = 60 + (60 * .2 * ab4_skillup) + p_d
            ab4 = ((m_h/m_ch) * exe) + p_d
            print("Q - Vampiric Strike")
            print("W - Slice N' Dice")
            print("E - Cleave")
            print("R - Execute")
            move = input("Make your move: ")
            move = move.lower()
            if move == 'q':
                return (ab1, 'false', 'Vampiric Strike', trait, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'w':
                return (ab2, 'false', "Slice N' Dice", 'false', 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'e':
                return (ab3, 'true', 'Cleave', trait, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'r':
                return (ab4, 'false', 'Execute', trait, 'false', 'false', 'false', CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', trait, 'false', 'false', 'false', CD1, CD2, CD3)
        elif p_c == 'sorceress': #Sorceress ability scaling
            ab1 = 30 + (30 * .2 * ab1_skillup) + (p_a + p_d)
            ab2 = 45 + (45 * .28 * ab2_skillup) + p_d
            ab3 = 45 + (45 * .25 * ab3_skillup) + p_d
            ab4 = 34 + (35 * .33 * ab4_skillup) + p_d
            if items.staff == 'true':
                trait = 15
            else:
                trait == 'false'
            CD3 = CD3 - 1
            print("Q - Barrier")
            print("W - Fire Strike")
            print("E - Fire Nova")
            print("R - Meteor")
            move = input("Make your move: ")
            move = move.lower()
            while ((move == 'w' and (CD1 > 0)) or ((move == 'e') and (CD2 > 0)) or ((move == 'r') and (CD3 > 0))):
                print("That ability is on cooldown")
                move = input("Remake your move: ")
            if move == 'q':
                return (ab1, 'false', 'Barrier', trait, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'w':
                return (ab2, 'false', 'Frost Strike', trait, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'e':
                return (ab3, 'true', 'Fire Nova', 'false', trait, 'false', 'false', CD1,  CD2, CD3)
            elif move == 'r':
                CD3 = 3
                return (ab4, 'false', 'Meteor', 'false', trait, 'false', 'false', CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', 'false', trait, 'false', 'false', CD1, CD2, CD3)
        elif p_c == 'monk':
            mark = trait
            ab1 = 25 + (25 * .15 * ab1_skillup) + p_d
            ab2 = 40 + (40 * .28 * ab2_skillup) + p_d
            ab3 = 15 + (10  * .25 * ab3_skillup)
            ab4 = 70 + (55 * .25 * ab4_skillup) + p_d
            if (mark > 0) and (mark < 3):
                ab4 = ab4 + (mark * 48)
            elif (mark >= 3) and (mark < 5):
                ab4 = ab4 + (mark * (100 + (100 * .15 * ab4_skillup)))
            elif mark == 5:
                ab4 = ab4 + (mark * (125 + (125 * .3 * ab4_skillup))) 
            print("Q - Sacred Fist")
            print("W - Exploding Palm")
            print("E - Endurance")
            print("R - Dragon Fist")
            print("You have", mark, "marks")
            move = input("Remake your move: ")
            move = move.lower()
            if move == 'q':
                if mark != 5:
                    mark = mark + 1
                return (ab1, 'false', 'Sacred Fist', mark, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'w':
                if mark != 5:
                    mark = mark + 1
                return (ab2, 'true', 'Exploding Palm', mark, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'e':
                return (ab3, 'false', 'Endurance', mark, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'r':
                mark = 0
                return (ab4, 'false', 'Dragon Fist', mark, 'false', 'false', 'false', CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', mark, 'false', 'false', 'false', CD1, CD2, CD3)
        if p_c == 'paladin':
            aura = trait
            ab1 = 35 + (35 * .28 * ab1_skillup) + p_d
            ab2 = 25 + (25 * .28 * ab2_skillup) + p_d
            ab3 = 15 + (15 * .23 * ab3_skillup)
            if items.mace == 'true':
                trait2 = 15 + (15 * .23 * ab3_skillup)
                trait3 = (trait2 - p_a)
            if aura % 2 == 0:
                ab3 = (ab3 - p_a)
            ab4 = 65 + (65 * .25 * ab4_skillup) + p_d
            CD3 = CD3 - 1
            print("Q - Hurl Hammer")
            print("W - Hammer Fury")
            print("E - Defensive/Offensive Aura")
            print("R - Hammer of Justice")
            move = input("Remake your move: ")
            move = move.lower()
            while ((move == 'w' and (CD1 > 0)) or ((move == 'e') and (CD2 > 0)) or ((move == 'r') and (CD3 > 0))):
                print("That ability is on cooldown")
                move = input("Make your move: ")
            if move == 'q':
                return (ab1, 'false', 'Hurl Hammer', aura, trait2, trait3, 'false', CD1, CD2, CD3)
            elif move == 'w':
                return (ab2, 'true', "Hammer Fury", aura, trait2, trait3, 'false', CD1, CD2, CD3)
            elif move == 'e':
                aura = aura + 1
                return (ab3, 'false', 'Defensive/Offensive Aura', aura, trait2, trait3, 'false', CD1, CD2, CD3)
            elif move == 'r':
                CD3 = 5
                return (ab4, 'false', 'Hammer of Justice', aura, trait2, trait3, 'false', CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', aura, trait2, trait3, 'false', CD1, CD2, CD3)
        if p_c == 'ranger':
            atk_no = trait
            ab1 = 40 + (40 * .28 * ab1_skillup) + p_d
            ab2 = 20 + (20 * .25 * ab2_skillup) + p_d
            ab3 = 25 + (25 * .5 * ab3_skillup)
            ab4 = 50 + (50 * .28 * ab4_skillup) + p_d
            CD1 = CD1 - 1
            CD2 = CD2 - 1
            CD3 = CD3 - 1
            print("Q - Lightening Arrow")
            print("W - Stun Arrow")
            print("E - Clone")
            print("R - Counter Strike")
            move = input("Make your move: ")
            move = move.lower()
            while ((move == 'w' and (CD1 > 0)) or ((move == 'e') and (CD2 > 0)) or ((move == 'r') and (CD3 > 0))):
                print("That ability is on cooldown")
                move = input("Remake your move: ")
            if move == 'q':
                atk_no = atk_no + 1
                return (ab1, 'true', 'Lightening Arrow', atk_no, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'w':
                CD1 = 5
                return (ab2, 'false', "Stun Arrow", atk_no, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'e':
                CD2 = 5
                return (ab3, 'false', 'Clone', atk_no, 'false', 'false', 'false', CD1, CD2, CD3)
            elif move == 'r':
                atk_no = atk_no + 1
                CD3 = 5
                return (ab4, 'false', 'Counter Strike', atk_no, 'false', 'false', 'false', CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', atk_no, 'false', 'false', 'false', CD1, CD2, CD3)
        if p_c == 'shaman':
            d_totem = trait
            h_totem = trait3
            ab1 = 8 + (8 * .3 * ab1_skillup) + p_d
            ab2 = 10 + (10 * .25 * ab2_skillup) + p_a
            ab3 = 15 + (15 * .22 * ab3_skillup) + p_d
            ab4 = 60 + (60 * .30 * ab4_skillup) + p_d
            CD1 = CD1 - 1
            CD2 = CD2 - 1
            CD3 = CD3 - 1
            print("Q - Flame Totem")
            print("W - Spring Totem")
            print("E - Earth Shock")
            print("R - Windwalker")
            print("Flame Totem:", d_totem)
            print("Spring Totem:", h_totem)
            move = input("Make your move: ")
            move = move.lower()
            while ((move == 'w' and (CD1 > 0)) or ((move == 'e') and (CD2 > 0)) or ((move == 'r') and (CD3 > 0))):
                print("That ability is on cooldown")
                move = input("Remake your move: ")
            while (d_totem >= 3) and (move == 'q') or (h_totem >= 3) and (move == 'w'):
                print("You have a maximum of this totem, select another move")
                move = input("Remake your move: ")
            if move == 'q':
                d_totem = d_totem + 1
                luck = random.randint(1,8)
                if (luck == 5) and (items.enchanted_sticks == 'true'):
                    h_totem = h_totem + 1
                return (ab1, 'false', 'Flame Totem', d_totem, ab1, h_totem, ab2, CD1, CD2, CD3)
            elif move == 'w':
                CD1 = 4
                h_totem = h_totem + 1
                luck = random.randint(1,8)
                if (luck == 5) and (items.enchanted_sticks == 'true'):
                    d_totem = d_totem + 1
                return (ab2, 'false', "Spring Totem", d_totem, ab1, h_totem, ab2, CD1, CD2, CD3)
            elif move == 'e':
                CD2 = 2
                return (ab3, 'false', 'Earth Shock', d_totem, ab1, h_totem, ab2, CD1, CD2, CD3)
            elif move == 'r':
                CD3 = 4
                return (ab4, 'false', 'Windwalker', d_totem, ab1, h_totem, ab2, CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', d_totem, ab1, h_totem, ab2, CD1, CD2, CD3)
        elif p_c == 'warlock': #warlock ability scaling
            trait3 = trait4 + trait3
            ab1 = 8 + (8 * .35 * ab1_skillup)
            ab2 = 45 + (45 * .28 * ab2_skillup) + p_d
            ab3 = 20 + (20 * .25 * ab3_skillup)
            ab4 = 8 + (8 * .3 * ab4_skillup)
            trait2 = 180 + (180 * .25 * ab3_skillup)
            CD3 = CD3 - 1
            print("Q - Summon Shadowlings")
            print("W - Mind Sear")
            print("E - Summon Spirit")
            print("R - Summon Baelrog")
            move = input("Make your move: ")
            move = move.lower()
            while ((move == 'w' and (CD1 > 0)) or ((move == 'e') and (CD2 > 0)) or ((move == 'r') and (CD3 > 0))):
                print("That ability is on cooldown")
                move = input("Remake your move: ")
            if move == 'q':
                trait4 = trait4 + 1
                return (ab1, 'false', 'Summon Shadowlings', trait, trait2, trait3, trait4, CD1, CD2, CD3)
            elif move == 'w':
                return (ab2, 'true', 'Mind Sear', trait, trait2, trait3, trait4, CD1, CD2, CD3)
            elif move == 'e':
                trait = trait + 1
                return (ab3, 'true', 'Summon Spirit', trait, trait2, trait3, trait4, CD1,  CD2, CD3)
            elif move == 'r':
                CD3 = 4
                return (ab4, 'false', 'Summon Baelrog', trait, trait2, trait3, trait4, CD1, CD2, CD3)
            else:
                print("You failed to make a move")
                return (ab5 , 'false', 'F2M', trait, trait2, trait3, trait4, CD1, CD2, CD3)
    print("You do not have enough skill points to level up, you get 1 per level")
    return (ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup)
# -------------------------------------------------
def ReturntoTown(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, p_c, stats, p_h, p_a, p_d):
    turn = turn + 2
    InTown(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, p_c, stats, p_h, p_a, p_d)
# -------------------------------------------------
def Adventure(p_c, p_d, p_a, p_h, exp, gold, potion_count, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, turn, items, stats):
    print("Who shall we challenge?(1-30)") #Monster you are capable of fighting
    challenge = input("Refer to the map and select the location of where you'd like to travel to: ")
    try:
        challenge = int(challenge)
    except TypeError:
        print("USE A NUMBER DUDE!:")
    while (challenge < 0) or (challenge > 31):
        challenge = input("Invalid suggestion, possible numbers are 0-30 & 69: ")
        try:
            challenge = int(challenge)
        except TypeError:
            print("USE A NUMBER DUDE!:")
    if challenge == 0:
        if level1 <= 10:
            monster = ['Target Dummy', 1, 10000, 0, 0, 0]
        elif level1 <= 25:
            monster = ['Target Dummy', 1, 50000, 0, 0, 0]
        elif level1 >= 40:
            monster = ['Target Dummy', 1, 100000, 0, 0, 0]
            turn = turn - 5
    elif challenge == 1:
        monster = ['Wolf', 1, 500, 70, 45, 40]
    elif challenge == 2:
        monster = ['Golem', 1, 850, 135, 65, 50]
    elif challenge == 3:
        monster = ['Minotaur', 1, 1500, 250, 100, 80]
    elif challenge == 4:
        monster = ['Satyr', 1, 2250, 175, 150, 95]
    elif challenge == 5:
        monster = ['Griffyn', 1, 3800, 225, 200, 100]
    elif challenge == 6:
        monster = ['Harpy', 1, 4200, 250, 250, 120]
    elif challenge == 7:
        monster = ['Murlocks (2)', 2, 5000, 300, 325, 125]
    elif challenge == 8:
        monster = ['Chimera', 1, 5500, 325, 280, 130]
    elif challenge == 9:
        monster = ['The-Three-Stooges', 3, 21000, 600, 500, 300]
    elif challenge == 10:
        monster = ['Centaur', 1, 8500, 310, 300, 180]
    elif challenge == 11:
        monster = ['Orc', 1, 9000, 325, 400, 200]
    elif challenge == 12:
        monster = ['Horde of Zombies (10)', 10, 25000, 750, 600, 350]
    elif challenge == 13:
        monster = ['Dark Elf', 1, 10000, 425, 425, 220]
    elif challenge == 14:
        monster = ['Wyvern', 1, 12500, 450, 450, 280]
    elif challenge == 15:
        monster = ['Baby Dragon', 1, 15000, 500, 500, 250]
    elif challenge == 16:
        monster = ['Dragon Whelplings (30)', 30, 90000, 1200, 750, 400]
    elif challenge == 17:
        monster = ['Casper The Friendly Ghost', 1, 25000, 550, 550, 290]
    elif challenge == 18:
        monster = ['Troll', 1, 38000, 650, 600, 300]
    elif challenge == 19:
        monster = ['Onyxia', 1, 50000, 750, 700, 350]
    elif challenge == 20:
        monster = ['Hydra (3)', 3, 250000, 750, 750, 400]
    elif challenge == 21:
        monster = ['Skeleton', 1, 85000, 666, 800, 400]
    elif challenge == 22:
        monster = ['Wandering Magi', 1, 75000, 300, 1000, 425]
    elif challenge == 23:
        monster = ['Ent', 1, 250000, 1250, 1250, 450]
    elif challenge == 24:
        monster = ['Goblins (50)', 50, 750000, 8750, 3000, 500]
    elif challenge == 25:
        monster = ['Stormtrooper', 1, 20000, 10000, 1500, 500]
    elif challenge == 26:
        monster = ['Black Jack the Woodsmen', 1, 225000, 1500, 2000, 650]
    elif challenge == 27:
        if stats[21] > 0:
            monster = ["Goliath's Summoned Beasts (5)", 5, 500000, 2500, 2500, 700]
            print("After travelling into the heart of the forrest you come across a dark catle and you enter")
        else:
            print("You must defeat the Wandering Magi")
            return (potion_count, exp, gold, turn)
    elif challenge == 28:
        if stats[26] > 0:
            monster = ['Demon Spawn', 1, 75000, 850, 3000, 750]
        else:
            print("You must defeat Goliath's men to face a Demon Spawn")
            return (potion_count, exp, gold, turn)
    elif challenge == 29:
        if stats[22] > 0:
            monster = ['Black Knight of the Dark Forrest', 1500000, 1850, 4000, 1000]
            print("As you ascend to the top of the Black Castle, in an open room you see a man facing away.")
            print("You step forward, and the man instantly turns around revealing a large black sword and a man in full black armor")
            print('"I am the Black Knight of the Dark Forrest, and your quest ends here"')
        else:
            print("You must defeat the Demon Spawn to face the Black Knight")
            return (potion_count, exp, gold, turn)
    elif challenge == 30:
        if stats[24] > 0:
            monster = ['Goliath the Unyielding', 1, 2500000, 2500, 5000, 1500]
        else:
            print("You must defeat all of Goliath's close men to face him")
            return (potion_count, exp, gold, turn)
    elif challenge == 31:
        print('Times defeated each mob')
        print('Wolf:', stats[0])
        print('Golem:', stats[1])
        print('Minotaur:', stats[2])
        print('Satyr:', stats[3])
        print('Griffin:', stats[4])
        print('Harpy:', stats[5])
        print('Murlocks:', stats[6])
        print('Chimera:', stats[7])
        print('The Three Stooges:', stats[8])
        print('Centaur:', stats[9])
        print('Orc:', stats[10])
        print('Horde of Zombies:', stats[11])
        print('Dark Elf:', stats[12])
        print('Wyvern:', stats[13])
        print('Baby Dragon:', stats[14])
        print('Dragon Whelplings:', stats[15])
        print('Casper the Friendly Ghost:', stats[16])
        print('Troll:', stats[17])
        print('Onyxia:', stats[18])
        print('Hydra:', stats[19])
        print('Skeleton:', stats[20])
        print('Wandering Magi:', stats[21])
        print('Ent:', stats[22])
        print('Goblins:', stats[23])
        print('Stormtrooper:', stats[24])
        print('Black Jack the Woodsmen:', stats[25])
        print("Goliath's minions:", stats[26])
        print('Demon Spawn:', stats[27])
        print('Black Knight of the Dark Forrest:', stats[28])
        print('Goliath the Wizard:', stats[29])
    if challenge != 31:
        reward = Fight(p_c, p_h, p_a, p_d, exp, gold, potion_count, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, turn, items, monster)
        try:
            potion_count = reward[0]
        except TypeError:
            try:
                print(reward[0])
            except TypeError:
                print(potion_count)
        exp = reward[1]
        gold = reward[2]
        turn = reward[3]
        if reward[4] == 'victory':
            stats[challenge - 1] = stats[challenge - 1] + 1
    return (potion_count, exp, gold, turn)
# -------------------------------------------------
def Shop(gold, potion_count, items):
    print('You have', gold, 'gold')
    ingold = gold
    option = input("Would you like to buy gear or potions? (gear/potions): ").lower()
    while (option != 'gear') and (option != 'potions'):
        option = input("Invalid selection, enter in your choice again (gear/potions): ").lower()
    if option == 'potions':
        choice = int(input("How many potions would you like to buy? 75 gold each: "))
        ingold = ingold - (75 * choice)
        if ingold < 0:
            print("You do not have enough gold")
            print("You have", gold, "gold")
        else:
            gold = gold - (75 * choice)
            potion_count = potion_count + choice
            print('You have', gold, 'gold left')
        return(potion_count, gold, items)
    elif option == 'gear':
        choice = input("Would sort of gear would you like to buy? (chestplate - 2500/helm - 3800/ring - 5000/amulet - 7500/trinket - 50000): ").lower()
        while (choice != 'chestplate') and (choice != 'helm') and (choice != 'ring') and (choice != 'amulet') and (choice != 'trinket'):
            choice = input("Ain't got none of those! but we do have some (chestplate - 2500/helm - 3800/ring - 5000/amulet - 7500/trinket - 50000): ").lower()
        if choice == 'chestplate':
            ingold = ingold - 2500
            if ingold < 0:
                print("You do not have enough gold")
                print("You have", gold, "gold")
            else:
                gold = gold - 2500
                items.chestplate = 'true'
                print("You have", gold, "gold left")
            return (potion_count, gold, items)
        elif choice == 'helm':
            ingold = ingold - 3800
            if ingold < 0:
                print("You do not have enough gold")
                print("You have", gold, "gold")
            else:
                gold = gold - 3800
                items.helm = 'true'
                print("You have", gold, "gold left")
            return (potion_count, gold, items)
        elif choice == 'ring':
            ingold = ingold - 5000
            if ingold < 0:
                print("You do not have enough gold")
                print("You have", gold, "gold")
            else:
                gold = gold - 5000
                items.ring = 'true'
                print("You have", gold, "gold left")
            return (potion_count, gold, items)
        elif choice == 'amulet':
            ingold = ingold - 7500
            if ingold < 0:
                print("You do not have enough gold")
                print("You have", gold, "gold")
            else:
                gold = gold - 7500
                items.amulet = 'true'
                print("You have", gold, "gold left")
                return(potion_count, gold, items)
        elif choice == 'trinket':
            ingold = ingold - 50000
            if ingold < 0:
                print("You do not have enough gold")
                print("You have", gold, "gold")
            else:
                gold = gold - 50000
                items.trinket = 'true'
                print("You have", gold, "gold left")
                return(potion_count, gold, items)
# -------------------------------------------------
def Inventory(gold, items, level1, level2, exp):
    print('You are level', level1)
    print('You need', int(level2 - exp), 'experience to level up')
    print(gold,'gold')
    if p_c == 'sorceress':
        print('Staff:', items.staff, '- Allows Meteor to deal AoE damage and your barrier to absorb 10% more damage')
    if p_c == 'warrior':
        print('Sword:', items.sword,"- Allows Slice N' Dice to hit an extra time\nShield:", items.shield,'- Take 20% less damage')
    if p_c == 'monk':
        print('Blindfold:', items.blindfold, '- Your Exploding Palm places a mark for each damage tick')
    if p_c == 'shaman':
        print('Enchanted Sticks:', items.enchanted_sticks, '- Begin w/ 1 flame & spring totem & ocassionally place both')
    if p_c == 'ranger':
        print('Bow:', items.bow, '- Every 3rd attack that is not CC, will deal bonus damage scaling w/ your damage \nQuiver:', items.quiver, '- The damage increase from your clone lasts an extra 2 rounds')
    if p_c == 'paladin':
        print('Mace:', items.mace, '- Gain both auras (will require you to use the ability at least once)\nShield:', items.shield, '- Take 20% less damage')
    if p_c == 'warlock':
        print('Brain:', items.brain, '- When a Baelrog dies, gain 1-3 shadowlings (increases w/ # of shadowinglings sacrifice)\nBones:', items.bones, '- Start w/ 3 shadowlings')
# -------------------------------------------------
def Gamble(gold, p_c, items):
    luck = int(random.randrange(1,10))
    reward = 0
    print("I am Sneak the Gambler, I can tell from the look in your eyes you want to gamble if not you can turn around and not say a word. (type leave to exit)")
    while (reward == 0) and (gold >= 125):
        ingold = gold
        if p_c == 'sorceress':
            choice = input('Well hello there master of elements heh, would you like to gamble for? (staff): ').lower()
            while (choice != 'staff') and (choice != 'leave'):
                choice = input("Sorry I don't speak jibberish! Now make a choice: ").lower()
        if p_c == 'warrior':
            choice = input("Hello brute, ready to gamble? (sword/shield): ").lower()
            while (choice != 'sword') and (choice != 'shield') and (choice != 'leave'):
                choice = input("You're gonna make this difficult aren't you? Just pick! (sword/shield): ").lower()
        if p_c == 'monk':
            choice = input("You're a calm one, let's gamble? (blindfold): ").lower()
            while (choice != 'blindfold') and (choice != 'leave'):
                choice = input("Gamble or get out! (blindfold): ").lower()
        if p_c == 'ranger':
            choice = input("I've got a bow and quiver, with your name on it, of course, you'd have to win it first (bow/quiver): ").lower()
            while (choice != 'bow') and (choice != quiver) and (choice != 'leave'):
                choice = input("Stop stuttering and pick one! (bow/quiver): ").lower()
        if p_c == 'shaman':
            choice = input("I found these neat sticks if you wanna gamble for em? (sticks): ").lower()
            while (choice != 'sticks') and (choice != 'leave'):
                choice = input("I'm serious! I heard they are valuable for people like you, err shamans. (sticks): ").lower()
        if p_c == 'paladin':
            choice = input("A holy man, heh, does holy man like to gamble? (mace/shield): ").lower()
            while (choice != 'mace') and (choice != 'shield') and (choice != 'leave'):
                choice = input('Too holy to gamble? LIES! Gamble! (mace/shield): ').lower()
        if p_c == 'warlock':
            choice = input("You leave a trail of dread when you walk wanderer... I got just the things for you, care to gamble?! (brain/bones): ").lower()
            while (choice != 'brain') and (choice != 'bones') and (choice != 'leave'):
                choice = input("Who else would gamble for these things? I gotta get rid of em'! (brain/bones): ").lower()
        if choice == 'leave':
            return(gold, items)
        ingold = ingold - 125
        if ingold < 0:
            print("Why, you don't even got any money you little rat! Beat it!")
            return(gold, items)
        else:
            gold = gold - 125
            print("Alright, I'm thinkin' of a number between 1 and 10!")
            guess = int(input('Whatcha gonna guess chump?: '))
            while guess != luck:
                if (guess == 'leave') or (guess == 'quit'):
                    return(gold, items)
                ingold = ingold - 125
                if ingold < 0:
                    print('No gold! Haha sucker!')
                    return(gold, items)
                else:
                    gold = gold - 125
                    guess = int(input("Mmmm keep on guessin' bud: "))
                    while (guess <= 0)or (guess > 10):
                        guess = int(input('PICK A NUMBER BETWEEN 1 AND 10!?: '))
        if guess == luck:
            reward = 1
            print("ooh ooh ooh! What a lucky guess! Alright, here you go, now shoo!")
            if choice == 'staff':
                items.staff = 'true'
                return(gold, items)
            elif choice == 'sword':
                items.sword = 'true'
                return(gold, items)
            elif choice == 'shield':
                items.shield = 'true'
                return(gold, items)
            elif choice == 'blindfold':
                items.blindfold = 'true'
                return(gold, items)
            elif choice == 'bow':
                items.bow = 'true'
                return(gold, items)
            elif choice == 'quiver':
                items.quiver = 'true'
                return(gold, items)
            elif choice == 'brain':
                items.brain = 'true'
                return(gold, items)
            elif choice == 'bones':
                items.bones = 'true'
                return(gold, items)
            elif choice == 'mace':
                items.mace = 'true'
                return(gold, items)
            elif choice == 'sticks':
                items.enchanted_sticks = 'true'
                return(gold, items)
        else:
            print("Wrong! Hahahaha! Thanks for your donation pal\n")
# -------------------------------------------------
screen = turtle.Screen() #Turtle draws the map]
screen.delay(0)
def Dot(turtle, x, y):
    x = x + 8
    y = y
    TGo2(turtle, x, y)
    for loop in range(4):
        turtle.forward(2)
        turtle.left(90)
        
def TGo2(turtle, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def Inumeral(turtle, x, y, I):
    turtle.begin_fill()
    for loop in range(2):
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
    turtle.end_fill()
    if I > 1:
        for loop in range(I-1):
            x = x + 8
            TGo2(turtle, x, y)
            turtle.begin_fill()
            for loop in range(2):
                turtle.forward(5)
                turtle.left(90)
                turtle.forward(15)
                turtle.left(90)
            turtle.end_fill()

def Vnumeral(turtle, x, y, I):
    turtle.right(60)
    turtle.forward(12)
    turtle.left(120)
    turtle.forward(12)
    turtle.right(60)
    if I < 0:
        x = x - 8
        n = 1
        y = y - 11
        TGo2(turtle, x, y)
        Inumeral(turtle, x, y, I)
    elif I > 0:
        x = x + 16
        y = y - 12
        TGo2(turtle, x, y)
        Inumeral(turtle, x, y, I)
    else:
        x = x + 10
        y = y - 10
        Dot(turtle, x, y)

def Xnumeral(turtle, x, y, I):
    turtle.right(45)
    turtle.forward(15)
    turtle.left(90)
    y = y - 11
    TGo2(turtle, x, y)
    turtle.forward(15)
    turtle.right(45)
    if I < 0:
        x = x - 8
        n = 1
        TGo2(turtle, x, y)
        Inumeral(turtle, x, y, I)
    elif I > 0:
        x = x + 16
        TGo2(turtle, x, y)
        Inumeral(turtle, x, y, I)
    
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(2)
turtle.color('red')
turtle.fillcolor('red')
screen.screensize(300, 300)
screen.bgcolor('black')
turtle.hideturtle()

TGo2(turtle, 230, -270)

turtle.forward(10)
TGo2(turtle, 235, -270)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
TGo2(turtle, 245, -270)
for loop in range(4):
    turtle.forward(10)
    turtle.right(90)
TGo2(turtle, 260, -270)
turtle.right(90)
turtle.forward(10)
turtle.left(120)
turtle.forward(5)
turtle.right(60)
turtle.forward(5)
turtle.left(120)
turtle.forward(10)
TGo2(turtle, 275, -270)
turtle.right(180)
turtle.forward(10)
TGo2(turtle, 275, -270)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.left(90)

TGo2(turtle, 255, -250)
Inumeral(turtle, 255, -250, 1)
Dot(turtle, 255, -250)

TGo2(turtle, 255, -210)
Inumeral(turtle, 255, -210, 2)
Dot(turtle, 263, -210)

TGo2(turtle, 230, -170)
Inumeral(turtle, 230, -170, 3)
Dot(turtle, 246, -170)

TGo2(turtle, 210, -130)
Vnumeral(turtle, 210, -130, -1)
Dot(turtle, 215, -140)

TGo2(turtle, 190, -90)
Vnumeral(turtle, 185, -90, 0)

TGo2(turtle, 240, -50)
Vnumeral(turtle, 240, -50, 1)
Dot(turtle, 258, -60)

TGo2(turtle, 220, 0)
Vnumeral(turtle, 220, 0, 2)
Dot(turtle, 246, -10)

TGo2(turtle, 190, 40)
Vnumeral(turtle, 190, 40, 3)
Dot(turtle, 224, 30)

TGo2(turtle, 160, 80)
Xnumeral(turtle, 160, 80, -1)
Dot(turtle, 168, 70)

TGo2(turtle, 100, 75)
Xnumeral(turtle, 100, 75, 0)
Dot(turtle, 108, 65)

TGo2(turtle, 40, 40)
Xnumeral(turtle, 40, 40, 1)
Dot(turtle, 60, 30)

TGo2(turtle, -10, -10)
Xnumeral(turtle, -10, -10, 2)
Dot(turtle, 15, -20)

TGo2(turtle, -40, -40)
Xnumeral(turtle, -40, -40, 3)
Dot(turtle, -7, -50)

TGo2(turtle, -50, -70)
Xnumeral(turtle, -50, -70, 0)
TGo2(turtle, -27, -70)
Vnumeral(turtle, -27, -70, -1)
Dot(turtle, -19, -80)

TGo2(turtle, 0, -100)
Xnumeral(turtle, 0, -100, 0)
TGo2(turtle, 15, -100)
Vnumeral(turtle, 15, -100, 0)

class Items():
        chestplate = 'false'
        helm = 'false'
        ring = 'false'
        sword = 'false'
        shield = 'false'
        staff = 'false'
        blindfold = 'false'
        bow = 'false'
        quiver = 'false'
        enchanted_sticks = 'false'
        mace = 'false'
        shield = 'false'
        brain = 'false'
        bones = 'false'
        amulet = 'false'
        trinket = 'false'
items = Items()
gold, turn, potion_count, exp, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup = [0 for loop in range(9)]
level2 = 100
level1 = 1
stats = [(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0)]
load = input("Would you like to load a saved file?: ")
if load == 'yes please':
    gold = save.readline()
    turn = save.readline()
    stats = save.readline()
    stats = ast.literal_eval(stats)
    level1 = save.readline()
    level2 = save.readline()
    ab1_skillup = save.readline()
    ab2_skillup = save.readline()
    ab3_skillup = save.readline()
    ab4_skillup = save.readline()
    gold = int(gold)
    turn = int(turn)
    level1 = int(level1)
    level2 = int(level2)
    ab1_skillup = int(ab1_skillup)
    ab2_skillup = int(ab2_skillup)
    ab3_skillup = int(ab3_skillup)
    ab4_skillup = int(ab4_skillup)
save.close()
main(gold, turn, potion_count, exp, level1, level2, skill_up, ab1_skillup, ab2_skillup, ab3_skillup, ab4_skillup, items, stats, p_c)
