# Constantine Macris
# Prof Ilias Hotzoglou
# March 26, 2021
# Programming Assignment #2 in Python
import random  # module imported for choosing random monster names, health, and damage
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

def story():  # optional story for hero
    input(f"\n{hero_name} awakens and groggily opens his eyes, "
          f"unsure of where he is...")
    clearConsole()
    input(f"\nCRACK——the muffled sound of a twig SNAPS behind him...")
    input(f"\nHeart racing, {hero_name} realizes he is in the heart of an unfamiliar forest,"
          f"\nand an unsettling feeling starts creeping into his mind...")
    input(f"\nThere is at least one pair of eyes tracking {hero_name}'s every move...")
    input(f"\n{hero_name} scrambles desperately toward what appears to be a sword jutting out of a rock...")
    input(f"\nHe only just manages to free the sword from the stone when——WHOOSH——")
    input(f"\nA terrifying figure BURSTS through the bushes and readies itself to attack...")


def attack(a, d):  # attack function takes as input health as well as damage taken and returns resulting health
    a = a - d
    return a


def lvl_up(lv, mh, d):  # function takes input of level, max health, and damage
    mx = (50*2**lv)  # calculates new max XP
    mh += 20  # adds 20 health
    h = mh  # restores max health
    d += 5  # increases damage by 5
    return mx, mh, h, d  # returns leveled-up max xp, max hp, hp, and dp


def main_game():  # main game program function
    xp = 0  # initial variables are all defined outside of the games main loop
    lvl = 1
    dp = 10
    hp = 100
    diff = 20
    max_xp = 100
    max_hp = 100
    while True:  # indefinitely repeating loop containing the core game
        print(f"\n~{hero_name}'s Current Stats~\n" 
              f"       LEVEL {lvl}\n       "
              f"DP | {dp}\n       "
              f"HP | {int(hp)}/{int(max_hp)}\n       "
              f"XP | {int(xp)}/{int(max_xp)}"  
              f"\n----------------------")  # displays stats before each fight
        choice = input(menu)  # displays menu and takes input of users choice
        try:
            choice = choice[0].upper()  # validates input by taking the first letter inputted and capitalizing it
        except ValueError:
            print("Invalid Input. Try again.\n")
            continue
        except IndexError:
            print("Invalid Input. Try again.\n")
            continue  # resets while loop in case of index or value error
        if choice != 'F' and choice != 'S' and choice != 'L' and choice != 'E':
            print("\nThat wasn't one of the options. Try again...\n")  # validates input
            continue
        mon_name = random.choice(["Big Poe", "Flaming Keese", "Red Lynel", "Evil Chipmunk",
                                  "Villainous Rabbit", "Wizzrobe", "Wallmaster"])
        # produces random choice of monsters name (this just makes each fight unique and interesting)
        mhp = random.choice(range(diff, 2 * diff))  # monster DP and HP calculated at start of fight
        mdp = random.choice(range(diff // 4, diff // 2))
        win_xp = mhp + mdp  # calculates xp to be gained from each fight
        print(f"\nA terrifying {mon_name} emerges with {mhp} health and {mdp} damage power!")  # displays monster stats
        if choice == 'F':
            while True:  # loop for fight
                print(f"""
                               \\
                /\\          \\   \\\\  \\
                )(               \\\\\\  \\       |\\ /|
        (_)_____(*)//////////////////////> ┌∩┐(◣_◢)┌∩┐
                )(                         | |/   \\| |
                \\/                            \\   /
        ______________________/FIGHT\\_______________________
                [{hero_name}]                   [{mon_name}]
            """)  # I defined this art within the main game loop only so that the monster name and hero name are defined
                mhp = attack(mhp, dp)  # invokes attack function to calculate damage on monster
                if mhp <= 0:  # breaks out to main loop if monster dies
                    break
                hp = attack(hp, mdp)  # invokes attack function to calculate damage on hero
                if hp <= 0:  # breaks out to main loop if hero dies
                    break
                if mhp > 0 and hp > 0:  # displays fight info and awaits input to continue
                    input(f"\nThe {mon_name} has {int(mhp)} HP left...\n{hero_name} has {int(hp)} HP left..."
                          f"\n\nHit ENTER to keep fighting-->")
        elif choice == 'S':
            if xp >= (0.1*(max_xp-xp)):  # if hero has sufficient xp, the short rest takes some xp and gives some hp
                xp -= 0.1*(max_xp-xp)
                hp += 0.1 * max_hp
            else:
                input(f"\n...but {hero_name} is not tired enough to rest before this fight...")
                continue  # loops back to menu in case of invalid attempt to rest
            print(f"\n(ー。ー) zzz... {hero_name} spends {int(0.1*(max_xp-xp))} XP "
                  f"and restores {int(0.1*max_hp)} HP with a short rest...")
            if hp > max_hp:  # ensures hp stays at or below max hp
                hp = max_hp
                print("\n~RESTED TO FULL HEALTH~\n")  # notifies if max hp reached
            input(f"\n(press enter to wake up and fight again)")  # continues to fight with 'enter'
            while True:
                print(f"""
                               \\
                /\\          \\   \\\\  \\
                )(               \\\\\\  \\       |\\ /|
        (_)_____(*)//////////////////////> ┌∩┐(◣_◢)┌∩┐
                )(                         | |/   \\| |
                \\/                            \\   /
        ______________________/FIGHT\\_______________________
                [{hero_name}]                   [{mon_name}]
            """)
                mhp = attack(mhp, dp)
                if mhp <= 0:
                    break
                hp = attack(hp, mdp)
                if hp <= 0:
                    break
                if mhp > 0 and hp > 0:
                    input(f"\nThe {mon_name} has {int(mhp)} HP left...\n{hero_name} has {int(hp)} HP left..."
                          f"\n\nHit ENTER to keep fighting-->")
        elif choice == 'L':
            if xp >= (0.2*(max_xp-xp)):
                hp += 0.2*max_hp
                xp -= 0.2*(max_xp-xp)
                print(f"\n(ー。ー) zzz... {hero_name} spends {int(0.2*(max_xp-xp))} XP "
                      f"and restores {int(0.2*max_hp)} HP with a short rest...")
                if hp > max_hp:
                    hp = max_hp
                    print("\n~RESTED TO FULL HEALTH~\n")
                input(f"\n(press enter to wake up and fight again)")
            else:
                input(f"\n...but {hero_name} is not tired enough to rest before this fight...")
                continue
            while True:
                print(f"""
                               \\
                /\\          \\   \\\\  \\
                )(               \\\\\\  \\       |\\ /|
        (_)_____(*)//////////////////////> ┌∩┐(◣_◢)┌∩┐
                )(                         | |/   \\| |
                \\/                            \\   /
        ______________________/FIGHT\\_______________________
                [{hero_name}]                   [{mon_name}]
            """)
                mhp = attack(mhp, dp)
                if mhp <= 0:
                    break
                hp = attack(hp, mdp)
                if hp <= 0:
                    break
                if mhp > 0 and hp > 0:
                    input(f"\nThe {mon_name} has {int(mhp)} HP left...\n{hero_name} has {int(hp)} HP left..."
                          f"\n\nHit ENTER to keep fighting-->")
        elif choice == 'E':  # escape option calculates and displays score and exits main game
            print(f"\n...but {hero_name} manages to escape to safety...\n\n"
                  f"FINAL SCORE = {int(lvl + (xp / (max_xp - xp)))}")
            break
        if mhp <= 0:  # increases difficulty and adds win_xp for victory over monster
            diff += 4
            xp += win_xp
            input(f"\n{hero_name} defeated the {mon_name} and gained +{int(win_xp)} XP!")
        if hp <= 0:  # exits game in case of hero death
            print(f"\n{hero_name} HAS BEEN SLAIN.\n\n\n\nGAME OVER\n\nFINAL SCORE = {int(lvl+(xp/(max_xp-xp)))}\n")
            break
        if xp >= max_xp:  # level up 'if' statement
            lvl += 1  # increases level
            xp -= max_xp  # sets xp to remaining xp after level up
            new_lvl = lvl_up(lvl, max_hp, dp)  # invokes level up function and sets the value to a variable
            max_xp, max_hp, hp, dp = new_lvl[0], new_lvl[1], new_lvl[2], new_lvl[3]
            # redefines the original variables with the values returned by the function
            input(f"\n{hero_name} LEVELED UP!\n(+20 Max Health)\n(+5 Damage Power)\n")  # notifies user of level up


menu = ("[F] FIGHT now!\n[S] SHORT REST then FIGHT...\n[L] LONG REST then FIGHT...\n[E] ESCAPE with your life!\n"
        "--------CHOOSE------->")  # initializing the menu variable
g_icon = f"""\n\n
                                       ((•))
                                        |||
                                        |||
                                   //==[OVO]==\\\\
                                 ///    | |    \\\\\\
                                        (Y)         --------------------
                                        |||,     < QUEST OF THE LOST HERO >
                                   ,c88888888b      --------------------
                                  ,420888888888b
                                  8888888886988P'
                            |.,;;\\"Y8888888888Y,|,/,;;.,; 
                            \\\\\\(press ENTER to begin)///"""
input(g_icon)  # title screen art awaits 'enter' input to proceed to game
while True:  # loop to take input of hero name
    hero_name = input("\nWhat is your hero's name? ")  # sets inputted name to hero_name variable
    try:  # try clause to validate input
        hero_name[0].isalpha()
        hero_name = hero_name.capitalize()
    except IndexError:
        continue
    except ValueError:
        continue
    break
while True:  # meta loop to contain the whole game program
    try:  # optional narrative with input validation
        ans = input("\nWould you like to hear the story (Y/N)? ")
        ans = ans.capitalize()
        if ans[0] == 'N':
            main_game()
            play = input("\nWould you like to play again (Y/N)? ")
            play = play.capitalize()
            if play[0] == 'N':
                break
            else:
                continue
        else:  # continues to main game unless 'n' is inputted
            story()  # calls story function
            main_game()  # calls main game function
            play = input("\nWould you like to play again (Y/N)? ")  # allows for new game without having to restart
            play = play.capitalize()
            if play[0] == 'N':  # validation
                break  # allows for exit path
            else:
                continue
    except ValueError:
        print("Invalid Input, try again.\n")
        continue
    except IndexError:
        print("Invalid Input, try again.\n")
        continue
print("\n\n\n\nThanks for playing!\n")  # exit message outside of all loops
