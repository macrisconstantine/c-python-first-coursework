// Constantine Macris
// Prof Ilias Hotzoglou
// March 26, 2021
// ITC 2088
// Programming Assignment #1 in C

/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
*/
int attack(a, d) {
    a = a - d;
    return a;
}


int up_level(int lv){
    int mx = (int)(50 * pow(2, lv));
    return mx;
}

int mon_hp(dif){
    srand((unsigned int)time(NULL));
    int ran_num = rand() % (2*dif-dif+1);
    return ran_num;
}

int mon_dp(dif){
    srand((unsigned int)time(NULL));
    int ran_num = rand() % (dif/2-dif/4+1);
    return ran_num;
}

int main() {
    int diff = 20;
    int lvl = 1;
    int dp = 10;
    int hp = 100;
    int max_hp = 100;
    int xp = 0;
    int max_xp = 100;
    int choice;
    do {
        while (1) {
            printf("\n~Hero's Current Stats~\n       LEVEL %d\n       "
                   "DP | %d\n       HP | %d/%d\n       "
                   "XP | %d/%d\n----------------------", lvl, dp, hp, max_hp, xp, max_xp);
            printf("\n[1] FIGHT now!\n[2] SHORT REST then FIGHT...\n[3] LONG REST then FIGHT...\n[4] ESCAPE with your life!\n"
                   "--------CHOOSE------->");
            scanf("%d", &choice);
            if (choice != 1 && choice != 2 && choice != 3 && choice != 4) {
                printf("\nThat wasn't one of the options. Try again...\n");
            } else {
                break;
            }
        }
        int mhp = mon_hp(diff)+diff;
        int mdp = mon_dp(diff)+diff/4;
        printf("%d %d", mhp, mdp);
        int win_xp = mhp + mdp;
        if (choice == 1) {
            while (1) {
                mhp = attack(mhp, dp);
                if (mhp <= 0) {
                    diff += 4;
                    xp = xp + win_xp;
                    printf("The Hero defeated the monster and gained XP!\n");
                    break;
                }
                hp = attack(hp, mdp);
                if (hp <= 0) {
                    break;
                }
            }
        } else if (choice == 2) {
            if (xp >= ((max_xp - xp) / 10)) {
                hp += max_hp / 10;
                xp -= (max_xp - xp) / 10;
            } else {
                printf("\nSorry. You don't have enough XP to take even a SHORT REST yet...");
                continue;
            }
            printf("\n(ー。ー) zzz... The Hero spends a little XP and restores a little HP with a short rest...");
            if (hp > max_hp) {
                hp = max_hp;
                printf("\n~RESTED TO FULL HEALTH~\n");
            }
            while (1) {
                mhp = attack(mhp, dp);
                if (mhp <= 0) {
                    diff += 4;
                    xp += win_xp;
                    printf("\nThe Hero defeated the monster and gained XP!\n");
                    break;
                }
                hp = attack(hp, mdp);
                if (hp <= 0) {
                    break;
                }
            }
        } else if (choice == 3) {
            if (xp >= (max_xp - xp) / 5) {
                hp += max_hp / 5;
                xp -= (max_xp - xp) / 5;
                printf("\n(ー。ー) zzz... The Hero spends a lot of XP and restores a lot of HP with a long rest...\n");
            } else {
                printf("\nSorry. You don't have enough XP to take a LONG REST yet...\n");
                continue;
            }
            if (hp > max_hp) {
                hp = max_hp;
                printf("\n~RESTED TO FULL HEALTH~\n");
            }
            while (1) {
                mhp = attack(mhp, dp);
                if (mhp <= 0) {
                    diff += 4;
                    xp += win_xp;
                    printf("\nThe Hero defeated the monster and gained XP!\n");
                    break;
                }
                hp = attack(hp, mdp);
                if (hp <= 0) {
                    break;
                }
            }
        }
        if (xp >= max_xp) {
            lvl += 1;
            xp -= max_xp;
            max_xp = up_level(lvl);
            max_hp += 20;
            dp += 5;
            hp = max_hp;
            printf("\nThe Hero LEVELED UP!\n(+20 Max Health)\n(+5 Damage Power)\n");
            continue;
        }
        if (choice == 4 || hp <= 0) {
            printf("\nThe Hero has been slain!\n");
            printf("\n\n\nGAME OVER\n\nFINAL SCORE = %d \n", (lvl + (xp / (max_xp - xp))));
            break;
        }
    } while (1);
    return 0;
}