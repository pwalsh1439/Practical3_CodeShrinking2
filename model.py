# -*- coding: utf-8 -*-
"""
Created on 06/11/2017

@author: Paul
"""

#importing standard libaries
import random, operator
#external libary
import  matplotlib.pyplot

# Set Up Varibles
num_of_agents = 10
num_of_iterations = 100
agents = [] 

'''
#Loop through all agents using variable then
#Randomises the y,x starting location
for i in range (num_of_agents):   
    agents.append([random.randint(0,99),random.randint(0,99)])

    print ("Start postion for agent " + str(agents[i]) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))

   
#Move each Agent 2 teps in a random direction
#Loop through each agent
for i in range(num_of_agents):
    #y Step 1
    if random.random() < 0.5:
        agents[i][0] += 1 
    else:
        agents[i][0] -= 1
    #x Step 1
    if random.random() < 0.5:
        agents[i][1] += 1 
    else:
        agents[i][1] -= 1  
    
    #y Step 2
    if random.random() < 0.5:
        agents[i][0] += 1 
    else:
        agents[i][0] -= 1
    
    #x Step 2
    if random.random() < 0.5:
        agents[i][1] += 1 
    else:
        agents[i][1] -= 1  


    print ("Start postion for agent " + str(agents[i]) + " is - y " + str(agents[0][0]) + " x " + str(agents[0][1]))

#Not needed in practicsl Code shrinking 2
#Calculate the distance between the two agents
#uses Y difference squared added to X difference squared then square rooted
#euclidiean_distance = (((agents[0][0]-agents[1][0])**2)+((agents[0][1]-agents[1][1])**2))**0.5
#
#print ("The euclidiean distance between the two agents is " + str(euclidiean_distance))
    
    
#pulls out the higest y
#print ("The Furthest north Agent- " + str(max(agents)))

#pulls out the higest x. Varible used to allow string function
#furthest_east = max(agents, key=operator.itemgetter(1))
#print ("The Furthest East Agent- " + str(furthest_east))


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#matplotlib.pyplot.scatter(furthest_east[1],furthest_east[0], color='red')
matplotlib.pyplot.show()
'''


'''
#Step 3 Control flow ---------------------------------------------------

#Loop through all agents using variable then
#Randomises the y,x starting location
for i in range (num_of_agents):   
    agents.append([random.randint(0,99),random.randint(0,99)])

    print ("Start postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))

   
#For each step in the iteration move each agent  in a random direction.
#Loop through each step iteration 
for j in range(num_of_iterations):
    #Loop through each agent
    for i in range(num_of_agents):
        #random y Step 
        if random.random() < 0.5:
            agents[i][0] += 1 
        else:
            agents[i][0] -= 1
        #random x Step
        if random.random() < 0.5:
            agents[i][1] += 1 
        else:
            agents[i][1] -= 1  

# Plot final postion
for i in range(num_of_agents):
    print ("End postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
 
matplotlib.pyplot.show()
'''


#Step 5 Control flow ---------------------------------------------------

#Loop through all agents using variable then
#Randomises the y,x starting location
for i in range (num_of_agents):   
    agents.append([random.randint(0,99),random.randint(0,99)])

    print ("Start postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))

   
#For each step in the iteration move each agent  in a random direction.
#Loop through each step iteration 
for j in range(num_of_iterations):
    #Loop through each agent
    for i in range(num_of_agents):
        #random y Step 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] + 1) % 100
        #random x Step
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100 
        else:
            agents[i][1] = (agents[i][1] + 1) % 100

# Plot final postion
for i in range(num_of_agents):
    print ("End postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
 
matplotlib.pyplot.show()