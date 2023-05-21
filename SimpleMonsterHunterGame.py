import random
import time


health = 100
MHhealth = 100
potion = 3

Monterlist = ["DevilJho","Rathalos",
              "Velkhana","Rathian","Rajang",
              "Nergigante","Almudron"]
print("Game Start")
time.sleep(2)
print("Welcome Hunter")
time.sleep(2)
print(random.choice(Monterlist) + " Has Appear!")
time.sleep(1)
print("Enter the battle")
time.sleep(1)

menu_option = ("1" , "2" , "3")


while(True):
    
    print()
    print("Player Health : " + str(health))
    print("Monster Health : " + str(MHhealth))
    print("Potion Left : " + str(potion))
    print()
    print("xxxx Menu xxxx")
    print("1. Attack")
    print("2. Heal")
    print("3. Leave")
    
    print()
    pilih = str(input("Choice : "))

    if pilih in menu_option:
        if pilih  == '1' :

            damagedealt = random.randint(10,30)
            damagetaken = random.randint(50,100)

            health -= damagetaken
            MHhealth -= damagedealt


            print("Attacking...")
            time.sleep(2)
            print()
            print("You have succefuly damage : " + str(damagedealt) + "Damage")
            print("You have been taken damage : " + str(damagetaken) + "Damage")
        
            print()
        
            if health <= 0 :
                print("You have been died")
                time.sleep(1)
                print("GAME OVER")
                time.sleep(1)
                break
            if MHhealth <= 0 :
                print("You Have been slain the Monster")
                item = random.randint(1,3)
                if item >= 1 :
                    print("You have been found a potion " + str(item) + " Potion")
                    potion += item
                MHhealth += 150
            
        if pilih == '2' :
            if potion >= 1 :
                health += 20
                potion -= 1
                print("Drinking Potion.....")
                time.sleep(2)
                print("You have been use a potion. Your health now is : " + str(health))
            else :
                print("You don't have any potion left!!!!")
        


        
    
        if pilih == '3' :
            print()
            print("You have been leave the battle")
            time.sleep(2)
            print("Thanks for playing")
            break


    else:
        print()
        print("There was no option!!!")


    



