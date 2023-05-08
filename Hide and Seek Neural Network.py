# Initialising Pygame

import pygame
scale = 1
pygame.init()
fps = 1000
screen = pygame.display.set_mode((round(750*scale),round(450*scale)))
def rect(x1,y1,x2,y2,col):
    pygame.draw.rect(screen,col,[x1*scale,y1*scale,x2*scale,y2*scale])
def line(x1,y1,x2,y2,col):
    pygame.draw.line(screen,col,[x1*scale,y1*scale],[x2*scale,y2*scale])

# Preparing RNG

import random
randint = random.randint

# Preparing Time

import time
wait = time.sleep

# Defining Colours

White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Blue = (0,0,255)

# Creating Starting Networks

networklayout = [20,24,10,4]
networks = []
for i in range(20):
    networks.append({'lines':[],'nodes':[]})
    for j in range(len(networklayout)-1):
        networks[i]['lines'].append([])
        for p in range(networklayout[j]):
            networks[i]['lines'][j].append([])
            for q in range(networklayout[j+1]):
                networks[i]['lines'][j][p].append(randint(-100,100)/100)
    for j in range(len(networklayout)-1):
        networks[i]['nodes'].append([])
        for p in range(networklayout[j+1]):
            networks[i]['nodes'][j].append(0)

networkseeker = networks

networklayout = [20,24,10,5]
networks = []
for i in range(20):
    networks.append({'lines':[],'nodes':[]})
    for j in range(len(networklayout)-1):
        networks[i]['lines'].append([])
        for p in range(networklayout[j]):
            networks[i]['lines'][j].append([])
            for q in range(networklayout[j+1]):
                networks[i]['lines'][j][p].append(randint(-100,100)/100)
    for j in range(len(networklayout)-1):
        networks[i]['nodes'].append([])
        for p in range(networklayout[j+1]):
            networks[i]['nodes'][j].append(0)

networkhider = networks

# Starting the Simulation

spacemode = False
done = False
gen = 1
while not done:

    # Creating the Players

    seekers = []
    for i in range(20):
        seekers.append([0,0])
    
    hiders = []
    for i in range(20):
        hiders.append([14,8,1])
    

    # Creating the Map

    walls = [randint(1,7),randint(1,13)]
    walls.append(randint(walls[1],13))
    walls.append(randint(0,walls[1]-1))
    walls.append(randint(walls[2]+1,14))
    walls.append(randint(0,walls[0]-1))
    walls.append(randint(walls[0]+1,8))
    Map = []
    for i in range(15):
        Map.append([])
        for j in range(9):
            if j == walls[0] and i != walls[3] and i != walls[4]:
                Map[i].append(1)
            elif i == walls[1] and j > walls[0] and j != walls[6]:
                Map[i].append(1)
            elif i == walls[2] and j < walls[0] and j != walls[5]:
                Map[i].append(1)
            else:
                Map[i].append(0)
    screen.fill(White)
    for x in range(len(Map)):
        for y in range(len(Map[x])):
            if Map[x][y] == 1:
                rect(x*50,y*50,50,50,Black)

    moves = 0
    deaths = 0
    while deaths < len(hiders) and moves < 100:
        moves += 1

        # Detecting Inputs

        for inp in pygame.event.get():
            if inp.type == pygame.QUIT:
                done = True
                break
            if inp.type == pygame.KEYDOWN:
                if spacemode:
                    spacemode = False
                else:
                    spacemode = True
        if done:
            break
        
        # Calculating Inputs For Seekers

        Inputs = []
        for i in range(len(seekers)):
            Inputs.append([])
            for j in range(50):
                if seekers[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]][seekers[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + round((j/2)-0.1) > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+round((j/2)-0.1)][seekers[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+j][seekers[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - round((j/2)-0.1) < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+j][seekers[i][1]-round((j/2)-0.1)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+j][seekers[i][1]] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + round((j/2)-0.1) > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+j][seekers[i][1]+round((j/2)-0.1)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+j][seekers[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] + round((j/2)-0.1) > 14:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]+round((j/2)-0.1)][seekers[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]][seekers[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - round((j/2)-0.1) < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-round((j/2)-0.1)][seekers[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-j][seekers[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] + round(j/2) > 8:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-j][seekers[i][1]+round(j/2)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-j][seekers[i][1]] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - round(j/2) < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-j][seekers[i][1]-round(j/2)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-j][seekers[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if seekers[i][0] - round(j/2) < 0:
                    Inputs[i].append(j)
                    break
                if seekers[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[seekers[i][0]-round(j/2)][seekers[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            Inputs[i].append(seekers[i][0])
            Inputs[i].append(seekers[i][1])
            Inputs[i].append(hiders[i][0])
            Inputs[i].append(hiders[i][1])

        networks = networkseeker.copy()
        
        for i in range(len(networks)):
            for j in range(len(networks[i]['nodes'])):
                for q in range(len(networks[i]['nodes'][j])):
                    networks[i]['nodes'][j][q] = 0
                    for p in range(len(Inputs[i])):
                        networks[i]['nodes'][j][q] += Inputs[i][p] * networks[i]['lines'][j][p][q]
                Inputs[i] = networks[i]['nodes'][j]
        Outputs = []
        for i in range(len(networks)):
            Outputs.append([0,0])
            for j in range(len(networks[i]['nodes'][len(networks[i]['nodes'])-1])):
                if networks[i]['nodes'][len(networks[i]['nodes'])-1][j] > Outputs[i][0]:
                    Outputs[i] = [networks[i]['nodes'][len(networks[i]['nodes'])-1][j],j]

        seekeroutput = Outputs
        
        networks = []

        Inputs = []
        for i in range(len(hiders)):
            Inputs.append([])
            for j in range(50):
                if hiders[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]][hiders[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + round((j/2)-0.1) > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+round((j/2)-0.1)][hiders[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+j][hiders[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - round((j/2)-0.1) < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+j][hiders[i][1]-round((j/2)-0.1)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+j][hiders[i][1]] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + round((j/2)-0.1) > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+j][hiders[i][1]+round((j/2)-0.1)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + j > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+j][hiders[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] + round((j/2)-0.1) > 14:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]+round((j/2)-0.1)][hiders[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]][hiders[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - round((j/2)-0.1) < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-round((j/2)-0.1)][hiders[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + j > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-j][hiders[i][1]+j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] + round(j/2) > 8:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-j][hiders[i][1]+round(j/2)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-j][hiders[i][1]] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - round(j/2) < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-j][hiders[i][1]-round(j/2)] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - j < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-j][hiders[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            for j in range(50):
                if hiders[i][0] - round(j/2) < 0:
                    Inputs[i].append(j)
                    break
                if hiders[i][1] - j < 0:
                    Inputs[i].append(j)
                    break
                if Map[hiders[i][0]-round(j/2)][hiders[i][1]-j] == 1:
                    Inputs[i].append(j)
                    break
            Inputs[i].append(hiders[i][0])
            Inputs[i].append(hiders[i][1])
            Inputs[i].append(seekers[i][0])
            Inputs[i].append(seekers[i][1])

        networks = networkhider.copy()
        
        for i in range(len(networks)):
            for j in range(len(networks[i]['nodes'])):
                for q in range(len(networks[i]['nodes'][j])):
                    networks[i]['nodes'][j][q] = 0
                    for p in range(len(Inputs[i])):
                        networks[i]['nodes'][j][q] += Inputs[i][p] * networks[i]['lines'][j][p][q]
                Inputs[i] = networks[i]['nodes'][j]
        Outputs = []
        for i in range(len(networks)):
            Outputs.append([0,0])
            for j in range(len(networks[i]['nodes'][len(networks[i]['nodes'])-1])):
                if networks[i]['nodes'][len(networks[i]['nodes'])-1][j] > Outputs[i][0]:
                    Outputs[i] = [networks[i]['nodes'][len(networks[i]['nodes'])-1][j],j]

        hideroutput = Outputs

        networks = []

        for i in range(len(seekeroutput)):
            if hiders[i][2] == 1:
                if seekeroutput[i][1] == 0:
                    seekers[i][1] = max(seekers[i][1]-1,0)
                    if Map[seekers[i][0]][seekers[i][1]] == 1:
                        seekers[i][1] += 1
                if seekeroutput[i][1] == 1:
                    seekers[i][0] = min(seekers[i][0]+1,14)
                    if Map[seekers[i][0]][seekers[i][1]] == 1:
                        seekers[i][0] -= 1
                if seekeroutput[i][1] == 2:
                    seekers[i][1] = min(seekers[i][1]+1,8)
                    if Map[seekers[i][0]][seekers[i][1]] == 1:
                        seekers[i][1] -= 1
                if seekeroutput[i][1] == 3:
                    seekers[i][0] = max(seekers[i][0]-1,0)
                    if Map[seekers[i][0]][seekers[i][1]] == 1:
                        seekers[i][0] += 1
            if i == 0 or not spacemode:
                rect(seekers[i][0]*50+10,seekers[i][1]*50+10,30,30,Red)
        for i in range(len(hideroutput)):
            if hiders[i][2] == 1:
                if moves/2 == round(moves/2):
                    if hideroutput[i][1] == 0:
                        hiders[i][1] = max(hiders[i][1]-1,0)
                        if Map[hiders[i][0]][hiders[i][1]] == 1:
                            hiders[i][1] += 1
                    if hideroutput[i][1] == 1:
                        hiders[i][0] = min(hiders[i][0]+1,14)
                        if Map[hiders[i][0]][hiders[i][1]] == 1:
                            hiders[i][0] -= 1
                    if hideroutput[i][1] == 2:
                        hiders[i][1] = min(hiders[i][1]+1,8)
                        if Map[hiders[i][0]][hiders[i][1]] == 1:
                            hiders[i][1] -= 1
                    if hideroutput[i][1] == 3:
                        hiders[i][0] = max(hiders[i][0]-1,0)
                        if Map[hiders[i][0]][hiders[i][1]] == 1:
                            hiders[i][0] += 1
                    if hiders[i][0] == seekers[i][0] and hiders[i][1] == seekers[i][1]:
                        hiders[i][2] = 0
                if i == 0 or not spacemode:
                    rect(hiders[i][0]*50+10,hiders[i][1]*50+10,30,30,Blue)
        
        # Display

        pygame.display.flip()
        screen.fill(White)
        for x in range(len(Map)):
            for y in range(len(Map[x])):
                if Map[x][y] == 1:
                    rect(x*50,y*50,50,50,Black)
        if spacemode:
            wait(0.1)

    # Eliminating and Mutating

    seekerscores = {}
    hiderscores = {}
    for i in range(len(seekers)):
        hiderscores[i] = abs(hiders[i][0] - seekers[i][0]) + abs(hiders[i][1] - seekers[i][1])
        seekerscores[i] = 50 - hiderscores[i]

    networks = []
    scores = sorted(seekerscores.items(), key=lambda item: item[1])
    networks = networkseeker
    for i in range(round(len(scores)/2-0.1)):
        networks[scores[i][0]]['lines'] = []
        for j in networks[scores[len(scores)-i-1][0]]['lines']:
            networks[scores[i][0]]['lines'].append([])
            for q in j:
                networks[scores[i][0]]['lines'][networks[scores[len(scores)-i-1][0]]['lines'].index(j)].append([])
                for p in q:
                    networks[scores[i][0]]['lines'][networks[scores[len(scores)-i-1][0]]['lines'].index(j)][j.index(q)].append(p)
    for i in range(len(networks)):
        for j in range(len(networks[i]['lines'])):
            for q in range(len(networks[i]['lines'][j])):
                for p in range(len(networks[i]['lines'][j][q])):
                    networks[i]['lines'][j][q][p] += randint(-80,80) / 100
    networkseeker = networks

    networks = []
    scores = sorted(hiderscores.items(), key=lambda item: item[1])
    networks = networkhider
    for i in range(round(len(scores)/2-0.1)):
        networks[scores[i][0]]['lines'] = []
        for j in networks[scores[len(scores)-i-1][0]]['lines']:
            networks[scores[i][0]]['lines'].append([])
            for q in j:
                networks[scores[i][0]]['lines'][networks[scores[len(scores)-i-1][0]]['lines'].index(j)].append([])
                for p in q:
                    networks[scores[i][0]]['lines'][networks[scores[len(scores)-i-1][0]]['lines'].index(j)][j.index(q)].append(p)
    for i in range(len(networks)):
        for j in range(len(networks[i]['lines'])):
            for q in range(len(networks[i]['lines'][j])):
                for p in range(len(networks[i]['lines'][j][q])):
                    networks[i]['lines'][j][q][p] += randint(-80,80) / 100
    networkhider = networks
    print('Gen',gen,'complete')
    gen += 1
pygame.quit()
