def even(i):
    return i/2

def odd(i):
    return (3*i) + 1

MyGoalList= []

goal = 0
goal2 = 0

for j in range (2, 1000000):
    goal  = 0
    #if goal > goal2:
        #goal2 = goal
    while j != 1:
        if j %2 == 0:
            j = even(j)
            goal +=1
            if goal > goal2:
                goal2 = goal
            
        else:
            j = odd(j)
            goal +=1
            if goal > goal2:
                goal2 = goal
    MyGoalList.append(goal)


print(max(MyGoalList))
print(MyGoalList.index(max(MyGoalList))+2)

# Highest_sequence = 0
# for i in range (0,len(MyGoalList)-1):
#     if MyGoalList[i] > Highest_sequence:
#         Highest_sequence = MyGoalList[i]
#         print(i+2)




#can also use built in funcitons max(list) to find biggest number in list and list.index(max(list)) to find the corresponding index