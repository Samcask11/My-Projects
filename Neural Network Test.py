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

Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
White = (255,255,255)
Black = (0,0,0)

# Creating Starting Networks

networks = []
for i in range(40):
    networks.append([[[],[]],[[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0]],7,4,1,0,[]])
    for x in range(30):
        networks[i][0][0].append(randint(-100,100)/100)
    for x in range(30):
        networks[i][0][1].append(randint(-100,100)/100)

# Starting The Simulations

pause = False
spacemode = False
averages = []
done = False
for generation in range(10000):

    # Creating A Map

    Map = []
    for i in range(15):
        Map.append([])
        for x in range(9):
            if randint(0,10) == 0:
                Map[i].append(-1)
            elif randint(0,9) == 0:
                Map[i].append(2)
            else:
                Map[i].append(1)
    Map[7][4] = 0
    for i in range(len(networks)):
        networks[i][6] = []
        for j in range(len(Map)):
            networks[i][6].append(Map[j].copy())

    # Running A Simulation

    deaths = 0
    moves = 0
    while deaths < len(networks) and moves < 100:
        for inp in pygame.event.get():
            if inp.type == pygame.QUIT:
                done = True
            if inp.type == pygame.KEYDOWN:
                if inp.key == pygame.K_SPACE:
                    if spacemode:
                        spacemode = False
                    else:
                        spacemode = True
                if inp.key == pygame.K_p:
                    pause = True
        if done:
            break
        moves += 1
        if spacemode:
            for x in range(15):
                for y in range(9):
                    if networks[0][6][x][y] == -1:
                        rect(x*50,y*50,50,50,Red)
                    if networks[0][6][x][y] == 1:
                        rect(x*50,y*50,50,50,Green)
                    if networks[0][6][x][y] == 2:
                        rect(x*50,y*50,50,50,Blue)
        else:
            for x in range(15):
                for y in range(9):
                    if Map[x][y] == -1:
                        rect(x*50,y*50,50,50,Red)
                    if Map[x][y] == 1:
                        rect(x*50,y*50,50,50,Green)
                    if Map[x][y] == 2:
                        rect(x*50,y*50,50,50,Blue)
        for i in range(len(networks)):
            if networks[i][4] == 1:
                if networks[i][3] > 0:
                    networks[i][1][0][0] = networks[i][6][networks[i][2]][networks[i][3]-1]
                else:
                    networks[i][1][0][0] = -2
                if networks[i][2] < 14:
                    networks[i][1][0][1] = networks[i][6][networks[i][2]+1][networks[i][3]]
                else:
                    networks[i][1][0][1] = -2
                if networks[i][3] < 8:
                    networks[i][1][0][2] = networks[i][6][networks[i][2]][networks[i][3]+1]
                else:
                    networks[i][1][0][2] = -2
                if networks[i][2] > 0:
                    networks[i][1][0][3] = networks[i][6][networks[i][2]-1][networks[i][3]]
                else:
                    networks[i][1][0][3] = -2
                networks[i][1][0][4] = randint(-2,2)
                
                networks[i][1][1][0] = ((networks[i][1][0][0]*networks[i][0][0][0]) + (networks[i][1][0][1]*networks[i][0][0][6])
                                        + (networks[i][1][0][2]*networks[i][0][0][12]) + (networks[i][1][0][3]*networks[i][0][0][18])
                                        + (networks[i][1][0][4]*networks[i][0][0][24]))
                networks[i][1][1][1] = ((networks[i][1][0][0]*networks[i][0][0][1]) + (networks[i][1][0][1]*networks[i][0][0][7])
                                        + (networks[i][1][0][2]*networks[i][0][0][13]) + (networks[i][1][0][3]*networks[i][0][0][19])
                                        + (networks[i][1][0][4]*networks[i][0][0][25]))
                networks[i][1][1][2] = ((networks[i][1][0][0]*networks[i][0][0][2]) + (networks[i][1][0][1]*networks[i][0][0][8])
                                        + (networks[i][1][0][2]*networks[i][0][0][14]) + (networks[i][1][0][3]*networks[i][0][0][20])
                                        + (networks[i][1][0][4]*networks[i][0][0][26]))
                networks[i][1][1][3] = ((networks[i][1][0][0]*networks[i][0][0][3]) + (networks[i][1][0][1]*networks[i][0][0][9])
                                        + (networks[i][1][0][2]*networks[i][0][0][15]) + (networks[i][1][0][3]*networks[i][0][0][21])
                                        + (networks[i][1][0][4]*networks[i][0][0][27]))
                networks[i][1][1][4] = ((networks[i][1][0][0]*networks[i][0][0][4]) + (networks[i][1][0][1]*networks[i][0][0][10])
                                        + (networks[i][1][0][2]*networks[i][0][0][16]) + (networks[i][1][0][3]*networks[i][0][0][22])
                                        + (networks[i][1][0][4]*networks[i][0][0][28]))
                networks[i][1][1][5] = ((networks[i][1][0][0]*networks[i][0][0][5]) + (networks[i][1][0][1]*networks[i][0][0][11])
                                        + (networks[i][1][0][2]*networks[i][0][0][17]) + (networks[i][1][0][3]*networks[i][0][0][23])
                                        + (networks[i][1][0][4]*networks[i][0][0][29]))

                networks[i][1][2][0] = ((networks[i][1][1][0]*networks[i][0][1][0]) + (networks[i][1][1][1]*networks[i][0][1][5])
                                        + (networks[i][1][1][2]*networks[i][0][1][10]) + (networks[i][1][1][3]*networks[i][0][1][15])
                                        + (networks[i][1][1][4]*networks[i][0][1][20]) + (networks[i][1][1][5]*networks[i][0][1][25]))
                networks[i][1][2][1] = ((networks[i][1][1][0]*networks[i][0][1][1]) + (networks[i][1][1][1]*networks[i][0][1][6])
                                        + (networks[i][1][1][2]*networks[i][0][1][11]) + (networks[i][1][1][3]*networks[i][0][1][16])
                                        + (networks[i][1][1][4]*networks[i][0][1][21]) + (networks[i][1][1][5]*networks[i][0][1][26]))
                networks[i][1][2][2] = ((networks[i][1][1][0]*networks[i][0][1][2]) + (networks[i][1][1][1]*networks[i][0][1][7])
                                        + (networks[i][1][1][2]*networks[i][0][1][12]) + (networks[i][1][1][3]*networks[i][0][1][17])
                                        + (networks[i][1][1][4]*networks[i][0][1][22]) + (networks[i][1][1][5]*networks[i][0][1][27]))
                networks[i][1][2][3] = ((networks[i][1][1][0]*networks[i][0][1][3]) + (networks[i][1][1][1]*networks[i][0][1][8])
                                        + (networks[i][1][1][2]*networks[i][0][1][13]) + (networks[i][1][1][3]*networks[i][0][1][18])
                                        + (networks[i][1][1][4]*networks[i][0][1][23]) + (networks[i][1][1][5]*networks[i][0][1][28]))
                networks[i][1][2][4] = ((networks[i][1][1][0]*networks[i][0][1][4]) + (networks[i][1][1][1]*networks[i][0][1][9])
                                        + (networks[i][1][1][2]*networks[i][0][1][14]) + (networks[i][1][1][3]*networks[i][0][1][19])
                                        + (networks[i][1][1][4]*networks[i][0][1][24]) + (networks[i][1][1][5]*networks[i][0][1][29]))

                if (networks[i][1][2][0] >= networks[i][1][2][1] and networks[i][1][2][0] >= networks[i][1][2][2]
                    and networks[i][1][2][0] >= networks[i][1][2][3] and networks[i][1][2][0] >= networks[i][1][2][4]):
                    networks[i][3] -= 1
                elif (networks[i][1][2][1] >= networks[i][1][2][0] and networks[i][1][2][1] >= networks[i][1][2][2]
                    and networks[i][1][2][1] >= networks[i][1][2][3] and networks[i][1][2][1] >= networks[i][1][2][4]):
                    networks[i][2] += 1
                elif (networks[i][1][2][2] >= networks[i][1][2][1] and networks[i][1][2][2] >= networks[i][1][2][0]
                    and networks[i][1][2][2] >= networks[i][1][2][3] and networks[i][1][2][2] >= networks[i][1][2][4]):
                    networks[i][3] += 1
                elif (networks[i][1][2][3] >= networks[i][1][2][1] and networks[i][1][2][3] >= networks[i][1][2][2]
                    and networks[i][1][2][3] >= networks[i][1][2][0] and networks[i][1][2][3] >= networks[i][1][2][4]):
                    networks[i][2] -= 1
                if networks[i][2] < 0 or networks[i][2] > 14 or networks[i][3] < 0 or networks[i][3] > 8:
                    networks[i][4] = 0
                    deaths += 1
                elif networks[i][6][networks[i][2]][networks[i][3]] == -1:
                    networks[i][4] = 0
                    deaths += 1
                elif networks[i][6][networks[i][2]][networks[i][3]] == 1:
                    networks[i][5] += 10
                elif networks[i][6][networks[i][2]][networks[i][3]] == 2:
                    networks[i][5] += 100
                if i == 0 or not spacemode:
                    rect(networks[i][2]*50+10,networks[i][3]*50+10,30,30,Black)
                for x in range(15):
                    for y in range(9):
                        if networks[i][2] == x and networks[i][3] == y and networks[i][6][x][y] > 0:
                            networks[i][6][x][y] = 0
        def colourline(j):
            return(networks[0][0][0][j]*127.5+127.5,networks[0][0][0][j]*127.5+127.5,networks[0][0][0][j]*127.5+127.5)
        linecolour = 0
        for x in range(5):
            for y in range(6):
                line(640,20*x+20,690,20*y+10,colourline(linecolour))
                linecolour += 1
        linecolour = 0
        for x in range(6):
            for y in range(5):
                line(690,20*x+10,740,20*y+20,colourline(linecolour))
                linecolour += 1
        pygame.display.flip()
        screen.fill(White)
        if spacemode and networks[0][4] == 1:
            wait(0.1)
        while pause:
            for inp in pygame.event.get():
                if inp.type == pygame.QUIT:
                    done = True
                    break
                if inp.type == pygame.KEYDOWN:
                    if inp.key == pygame.K_p:
                        pause = False
        if done:
            break
        pygame.time.Clock().tick(fps)
    if done:
        break
    scores = []
    for i in range(len(networks)):
        for j in range(len(scores)):
            if networks[i][5] < scores[j][1]:
                scores.insert(j,[i,networks[i][5]])
                break
        if len(scores) - 1 < i:
            scores.append([i,networks[i][5]])
    for i in range(round(len(networks)/2)):
        for j in range(30):
            networks[scores[i][0]][0][0][j] = networks[scores[(len(networks)-1)-i][0]][0][0][j]
        for j in range(30):
            networks[scores[i][0]][0][1][j] = networks[scores[(len(networks)-1)-i][0]][0][1][j]
    for i in range(len(networks)):
        for j in range(30):
            networks[i][0][0][j] += randint(-30,30) / 100
            networks[i][0][0][j] = max(min(networks[i][0][0][j],1),-1)
        for j in range(30):
            networks[i][0][1][j] += randint(-30,30) / 100
            networks[i][0][1][j] = max(min(networks[i][0][1][j],1),-1)
        networks[i][2] = 7
        networks[i][3] = 4
        networks[i][4] = 1
        networks[i][5] = 0
    average = 0
    highest = 0
    for i in range(len(networks)):
        highest = max(highest,scores[i][1])
        average += scores[i][1]
    average /= len(networks)
    print('Gen:',generation,'Mean:',average,'Max:',highest)
    averages.append(average)
pygame.quit()
