import ringel_script_1_stat as script_1
import ringel_script_2_ev as script_2

"""
Pokemon: Meowth
Level = 50
Nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)
Based Stats:
    Hp: 40 (iv = 27, ev = 105)
	Attack: 45 (iv = 17, ev = 69)
	Defense: 35 (iv = 6, ev = 55)
	Sp. Atk: 40 (iv = 21, ev = 43)
	Sp.Def: 40 (iv = 25 , ev = 50)
	Speed: 50 (iv = 8, ev = 120)
"""

iv = [0,0,0,0,0,0]
ev = [0,0,0,0,0,0]
nature = [1,1,1,0.9,1,1.1]
base = [0,0,0,0,0,0]
ivcal = [0,0,0,0,0,0]
evcal = [0,0,0,0,0,0]

check_ev = 0

add_stat = [0,0,0,0,0,0]

def start():
    print("""
    Choose Calculation:

    1. Stats calculation
    2. Ev calculation
    3. Exit
    """)
    opt = int(input("Choose an option: "))

    if opt == 1:
        statsCalculation()
    elif opt == 2:
        while True:
            print("""
            1. Perform EV calculation for single stats
            2. Perform EV calculation for all stats
            3. Back
            """)
            opt = int(input("Choose an option: "))
            if opt == 1:
                singleStats()
            if opt == 2:
                allStats()
            if opt == 3:
                start()
            print("Invalid Choice, Try Again")
    elif opt == 3:
        exit()
    else:
        print("Invalid Choice, Try Again")
        start()

# stats calculation function
def statsCalculation():
    print("\nPls note that IV values only range from 0 - 31 and EV values to 0 - 255 with a maximum of 510 values in all stats! \n")
    #input values
    print("\nEnter pokemon stat/s: \n")
    lvl = int(input("Enter level: "))
    hp = int(input("\nEnter based hp: "))
    iv[0] = int(input("Enter IV: "))
    ev[0] = int(input("Enter EV: "))
    #input other stats values
    print("\nFor Other Stats\n")
    atk = int(input("Enter attack: "))
    iv[1] = int(input("Enter IV: "))
    ev[1] = int(input("Enter EV: "))
    defense = int(input("Enter defense: "))
    iv[2] = int(input("Enter IV: "))
    ev[2] = int(input("Enter EV: "))
    spAtk = int(input("Enter Sp. attack: "))
    iv[3] = int(input("Enter IV: "))
    ev[3] = int(input("Enter EV: "))
    spDef = int(input("Enter Sp. defense: "))
    iv[4] = int(input("Enter IV: "))
    ev[4] = int(input("Enter EV: "))
    spd = int(input("Enter Speed: "))
    iv[5] = int(input("Enter IV: "))
    ev[5] = int(input("Enter EV: "))

    check_ev = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if check_ev > 510:
        print("\nEffort value should not exceed 510 when totaled! Try again.")
        statsCalculation()
 
    print("\nPokemon Stats\n")
    print("Nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
    totalHp = script_1.pokemonStats.hp_statsfunction(lvl,hp,iv,ev)
    print("\nHp: ", round(totalHp, 2), end='\n\n')
    print("Other Stats: \n")
    str = script_1.pokemonStats.other_statsfunction(atk,defense,spAtk,spDef,spd,iv,ev,lvl,nature)
    stats_name = ['Attack: ','Defense: ','Special Attack: ','Special Defense: ','Speed:']
    for x in range(len(str)):
        print(stats_name[x],round(str[x], 2))
        x = x + 1
    anotherCalculation()

def singleStats():
    basestat = [0,0,0,0,0,0]
    while True:
        print("""
        1. Hp
        2. Attack
        3. Defense
        4. Sp. Attack
        5. Sp. Defense
        6. Speed
        """)
        opt = int(input("Choose an option: "))
        if opt == 1:
            stat_type = 'hp'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[0] = int(input("Enter base hp: "))
            iv[0] = int(input("Enter IV: "))
            if iv[0] > 31:
                print("\nIv should range from 0 to 31.Try again!")
                singleStats()
            ev[0] = int(input("Enter EV: "))
            if ev[0] > 255:
                print("\nEv should range from 0 to 255.Try again!")
                singleStats()
            stat = int(input("Desired increased in hp: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 2:
            stat_type = 'attack'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[1] = int(input("Enter base attack: "))
            iv[1] = int(input("Enter IV: "))
            ev[1] = int(input("Enter EV: "))
            stat = int(input("Desired increased in attack: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)
            
            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 3:
            stat_type = 'defense'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[2] = int(input("Enter base defense: "))
            iv[2] = int(input("Enter IV: "))
            ev[2] = int(input("Enter EV: "))
            stat = int(input("Desired increased in defense: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)
            
            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 4:
            stat_type = 'special attack'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[3] = int(input("Enter base sp. attack: "))
            iv[3] = int(input("Enter IV: "))
            ev[3] = int(input("Enter EV: "))
            stat = int(input("Desired increased in sp. attack: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)
            
            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 5:
            stat_type = 'special defense'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[4] = int(input("Enter base sp. defense: "))
            iv[4] = int(input("Enter IV: "))
            ev[4] = int(input("Enter EV: "))
            stat = int(input("Desired increased in sp. defense: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)
            
            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        if opt == 6:
            stat_type = 'speed'
            print("\nEnter pokemon stat/s: \n")
            lvl = int(input("Enter level: "))
            basestat[5] = int(input("Enter base speed: "))
            iv[5] = int(input("Enter IV: "))
            ev[5] = int(input("Enter EV: "))
            stat = int(input("Desired increased in speed: "))

            ev_needed = script_2.pokemonEv.singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature)
            
            print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nThe EVs needed to increase the",stat_type,": ", round(ev_needed, 2))
            
            while True:
                print("""
                1. Perform another EVs calculation
                2. Back
                """)
                opt = int(input("Choose an option: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anotherCalculation()
                print("Invalid Choice, Try Again")
        print("Invalid Choice, Try Again")

def allStats():
    stat_type = ['hp','attack','defense','special attack','special defense','speed',]
    print("\nEnter pokemon stat/s: \n")
    lvl = int(input("Enter level: "))
    for x in range(len(stat_type)):
        base[x] = int(input("\nEnter base " + stat_type[x] + ": "))
        ivcal[x] = int(input("Enter IV : "))
        if ivcal[x] > 31:
            print("\nIv should range from 0 to 31.Try again!")
            allStats()
        evcal[x] = int(input("Enter EV : "))
        if evcal[x] > 255:
            print("\nEv should range from 0 to 255.Try again!")
            allStats()
        add_stat[x] = int(input("Desired increased in " + stat_type[x] + ": "))
        x = x + 1
    
    check_ev = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if check_ev > 510:
        print("\nEffort value should not exceed 510 when totaled! Try again.")
        allStats()

    ev_needed = script_2.pokemonEv.allStatsFunction(lvl,base,ivcal,evcal,add_stat,nature)

    print("Pokemon's nature: Jolly(inc. Stat in Speed, while dec. stat in Sp.Atk)")
    print("\nThe EVs needed to increase in: \n")
    
    for i in range(len(stat_type)):
        print(stat_type[i], ": ", round(ev_needed[i], 2))
        i = i + 1

    anotherCalculation()



def anotherCalculation():
    while True:
        print("""
        1. Perform another Calculation
        2. End
        """)
        opt = int(input("Choose an option: "))
        if opt == 1:
            start()
        if opt == 2:
            exit()
        print("Invalid Choice, Try Again")

start()