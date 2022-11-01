import random

print("This is the famous Montly Hall Problem! \n3 doors and one of them could be chosen. \nSelect the prize door  = Win  ")
print("Select not prize door = a door different from selected door and \nnot prize door is opened")
print("Chance is given to change the door")

numOfRounds = int(input("Please select how many times this game is to be played "))

doorA = 'A'
doorB = 'B'
doorC = 'C'
doorList = [doorA,doorB,doorC]
win_noswitch = 0
win_switch = 0
print("\n\n\n")
for a in range (0,numOfRounds):
    prizedoor  = random.choice(doorList)
    agent_chosen_door = random.choice(doorList)
    print("The door chosen by the player is ",agent_chosen_door)
    print("The Prize door is ",prizedoor)
    #showing the agent a door one of the other two doors
    defacto_doorlist = doorList.copy()
    defacto_doorlist.remove(prizedoor)
    if (agent_chosen_door != prizedoor):
        defacto_doorlist.remove(agent_chosen_door)
    #print(defacto_doorlist)
    doorshowed = defacto_doorlist[0]
    print("Showing the door : ",doorshowed)



    print("Not switching doors")
    if (agent_chosen_door == prizedoor):
        win_noswitch += 1
        print("Won without switch")


    print("Switching doors")
    defacto_doorlist = doorList.copy()
    defacto_doorlist.remove(doorshowed)
    defacto_doorlist.remove(agent_chosen_door)
    agent_chosen_door = random.choice(defacto_doorlist)

    if (agent_chosen_door == prizedoor):

        win_switch += 1
        print("Won with switching")


print("Total count of winning without switch",win_noswitch)
print("Total count of winning with switch", win_switch)
print("Probability of winning without switching is {0:.4f}".format(win_noswitch/numOfRounds))
print("Probability of winning with switching is {0:.4f}".format(win_switch/numOfRounds))

       # if (choice_switch_door == 0):
       #     agent_chosen_door = agent_chosen_door

