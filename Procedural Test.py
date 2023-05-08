# Setting up Pygame

import pygame
pygame.init()
fps = 100
ups = fps
screen = pygame.display.set_mode((1000,600))

# Importing RNG

from random import randint

# Importing Math

import math
sqrt = math.sqrt
floor = math.floor
ceil = math.ceil
def sin(ang):
    return(math.sin(math.radians(ang)))
def asin(opp,hyp):
    if hyp != 0:
        return(math.degrees(math.asin(opp/hyp)))
    else:
        return(0)
def cos(ang):
    return(math.cos(math.radians(ang)))
def acos(adj,hyp):
    if hyp != 0:
        return(math.degrees(math.acos(adj/hyp)))
    else:
        return(0)
def tan(ang):
    return(math.tan(math.radians(ang)))
def atan(opp,adj):
    if adj != 0:
        return(math.degrees(math.atan(opp/adj)))
    else:
        return(90)
def pythag(pos1,pos2):
    return(math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2))
def calculatedamage(damage,piercing,defence,hardness):
    return(damage*max(0.01,1-(max(0,defence-piercing)*(0.01+hardness/1000))))

# Checking IRL Time

from datetime import datetime
def checktime():
    return(float(datetime.now().strftime('%S')+'.'+datetime.now().strftime('%f')))

# Gamescale and Drawing

scale = 1.5
def rect(col,x1,y1,xs,ys,outline=0):
    pygame.draw.rect(screen,col,[x1,y1,xs,ys],outline)
def screenrect(col,x1,y1,xs,ys,outline=0):
    pygame.draw.rect(screen,col,[((x1-500)-max(min(screenx,1980-(500/scale)),500/scale+20)+500)*scale+500-transition[0][0],
                                 ((y1-300)-max(min(screeny,1180-(300/scale)),300/scale+20)+300)*scale+300-transition[0][1],
                                 xs*scale,ys*scale],outline)
def line(col,x1,y1,x2,y2,outline=1):
    pygame.draw.line(screen,col,(x1,y1),(x2,y2),outline)
def screenline(col,x1,y1,x2,y2,outline=1):
    pygame.draw.line(screen,col,(((x1-500)-max(min(screenx,1980-(500/scale)),500/scale+20)+500)*scale+500-transition[0][0],
                                 ((y1-300)-max(min(screeny,1180-(300/scale)),300/scale+20)+300)*scale+300-transition[0][1]),
                     (((x2-500)-max(min(screenx,1980-(500/scale)),500/scale+20)+500)*scale+500-transition[0][0],
                      ((y2-300)-max(min(screeny,1180-(300/scale)),300/scale+20)+300)*scale+300-transition[0][1]),outline)

# Colours

White = (255,255,255)
Gray = (100,100,100)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)

# Reversing a List

def fliplist(flip):
    flip = list(flip)
    flip.reverse()
    return(flip)

# Viewing the World

def viewworld():
    for i in range(len(world[0])):
        view = ''
        for j in range(len(world)):
            if i == 7 and j == 7:
                view += '2 '
            elif world[j][i] == 1:
                view += '  '
            elif world[j][i] == 2:
                view += '3 '
            else:
                view += '1 '
        print(view)
def viewlevel(levx,levy):
    for i in range(len(world[levx][levy][0])):
        view = ''
        for j in range(len(world[levx][levy])):
            if world[levx][levy][j][i] == 1:
                view += '  '
            else:
                view += '1 '
        print(view)

# Major Functions

def makelevel(): # Forming a Level
    level = []
    enemies = []
    for i in range(50):
        level.append([])
        for j in range(30):
            level[i].append(1)
    diggers = [[24,14],[25,14],[24,15],[25,15]]
    for i in range(500):
        j = 0
        while j < len(diggers):
            level[diggers[j][0]][diggers[j][1]] = 0
            if randint(0,60) == 0:
                enemyspawn = randint(0,1)
                if enemyspawn == 0:
                    enemies.append({'entity':{'cat':'enemy','subcat':'grunt'},
                                    'pos':{'x':diggers[j][0]*40+20,'y':diggers[j][1]*40+20},
                                    'tags':{'stats':{'health':100,'defence':10,'hardness':0,'speed':8},
                                            'weapons':[{'type':'contact','damage':20,'haste':1,'piercing':0,'cooldown':0}],
                                            'attention':0,'attentionspan':10,'path':()}})
            if randint(0,3) == 0:
                diggers[j][0] -= 1
                if diggers[j][0] == 0:
                    diggers.remove(diggers[j])
                    j -= 1
            elif randint(0,2) == 0:
                diggers[j][0] += 1
                if diggers[j][0] == 49:
                    diggers.remove(diggers[j])
                    j -= 1
            elif randint(0,1) == 0:
                diggers[j][1] -= 1
                if diggers[j][1] == 0:
                    diggers.remove(diggers[j])
                    j -= 1
            else:
                diggers[j][1] += 1
                if diggers[j][1] == 29:
                    diggers.remove(diggers[j])
                    j -= 1
            j += 1
    return(level,enemies)

def makeworld(): # Making a World
    world = []
    entities = []
    for i in range(15):
        world.append([])
        entities.append([])
        for j in range(15):
            world[i].append(1)
            entities[i].append(1)
    diggers = [[7,7],[7,7],[7,7]]
    for i in range(500):
        j = 0
        while j < len(diggers):
            world[diggers[j][0]][diggers[j][1]] = 0
            entities[diggers[j][0]][diggers[j][1]] = []
            if randint(0,3) == 0:
                diggers[j][0] -= 1
                if diggers[j][0] == -1:
                    diggers.remove(diggers[j])
                    j -= 1
            elif randint(0,2) == 0:
                diggers[j][0] += 1
                if diggers[j][0] == 15:
                    diggers.remove(diggers[j])
                    j -= 1
            elif randint(0,1) == 0:
                diggers[j][1] -= 1
                if diggers[j][1] == -1:
                    diggers.remove(diggers[j])
                    j -= 1
            else:
                diggers[j][1] += 1
                if diggers[j][1] == 15:
                    diggers.remove(diggers[j])
                    j -= 1
            j += 1
    for xt in range(len(world)):
        for yt in range(len(world[xt])):
            if world[xt][yt] == 0:
                getlevel = makelevel()
                world[xt][yt] = getlevel[0]
                if not (xt == 7 and yt == 7): 
                    entities[xt][yt] = getlevel[1]
                if xt > 0:
                    if world[xt-1][yt] != 1:
                        for i in range(len(world[xt][yt])):
                            if 0 in world[xt][yt][i]:
                                randtest = randint(1,len(world[xt][yt][i])-2)
                                while world[xt][yt][i][randtest] != 0:
                                    randtest = randint(1,len(world[xt][yt][i])-2)
                                for j in range(i):
                                    world[xt][yt][j][randtest] = 0
                                break
                if xt < 14:
                    if world[xt+1][yt] != 1:
                        for i in fliplist(range(len(world[xt][yt]))):
                            if 0 in world[xt][yt][i]:
                                gamermode = 10
                                randtest = randint(1,len(world[xt][yt][i])-2)
                                while world[xt][yt][i][randtest] != 0:
                                    randtest = randint(1,len(world[xt][yt][i])-2)
                                for j in fliplist(range(i,50)):
                                    world[xt][yt][j][randtest] = 0
                                break
                if yt > 0:
                    if world[xt][yt-1] != 1:
                        done = False
                        for i in range(len(world[xt][yt][0])):
                            for j in range(len(world[xt][yt])):
                                if world[xt][yt][j][i] == 0:
                                    randtest = randint(1,len(world[xt][yt])-2)
                                    while world[xt][yt][randtest][i] != 0:
                                        randtest = randint(1,len(world[xt][yt])-2)
                                    for j in range(i):
                                        world[xt][yt][randtest][j] = 0
                                    done = True
                                    break
                            if done:
                                break
                if yt < 14:
                    if world[xt][yt+1] != 1:
                        done = False
                        for i in fliplist(range(len(world[xt][yt][0]))):
                            for j in range(len(world[xt][yt])):
                                if world[xt][yt][j][i] == 0:
                                    randtest = randint(1,len(world[xt][yt])-2)
                                    while world[xt][yt][randtest][i] != 0:
                                        randtest = randint(1,len(world[xt][yt])-2)
                                    for j in fliplist(range(i,30)):
                                        world[xt][yt][randtest][j] = 0
                                    done = True
                                    break
                            if done:
                                break
    return(world,entities)

def gameinputs(): #Movement and General Controls
    global done
    global scale
    global x
    global y
    global xvel
    global yvel
    global movingup
    global movingdown
    global movingleft
    global movingright
    global level
    global screenx
    global screeny
    global screeninp
    global transition
    global offset
    inputs = pygame.event.get()
    for inp in inputs:
        if inp.type == pygame.QUIT:
            done = True
            break
        if inp.type == pygame.MOUSEWHEEL and False:
            if inp.y == -1 and scale > 1.5:
                scale -= 0.2
            if inp.y == 1 and scale < 3.5:
                scale += 0.2
            scale = round(scale*10)/10
        if inp.type == pygame.KEYDOWN:
            if inp.key == pygame.K_w:
                movingup = True
            if inp.key == pygame.K_s:
                movingdown = True
            if inp.key == pygame.K_a:
                movingleft = True
            if inp.key == pygame.K_d:
                movingright = True
        if inp.type == pygame.KEYUP:
            if inp.key == pygame.K_w:
                movingup = False
            if inp.key == pygame.K_s:
                movingdown = False
            if inp.key == pygame.K_a:
                movingleft = False
            if inp.key == pygame.K_d:
                movingright = False
                
    if (movingright or movingleft) and (movingup or movingdown):
        speedcap = sqrt((speed**2)/2)
    else:
        speedcap = speed
        
    # Processing Vertical Inputs
        
    if movingup and not movingdown:
        yvel -= speed * 20 / ups
        if yvel < -speedcap:
            yvel = -speedcap
    if ((not movingup and not movingdown) or (movingup and movingdown)) and yvel < 0:
        yvel += speed * 10 / ups
        if yvel > 0:
            yvel = 0
    if movingdown and not movingup:
        yvel += speed * 20 / ups
        if yvel > speedcap:
            yvel = speedcap
    if ((not movingup and not movingdown) or (movingup and movingdown)) and yvel > 0:
        yvel -= speed * 10 / ups
        if yvel < 0:
            yvel = 0
    y += yvel / ups * 20

    # Vertical Level Transition
            
    if y < 20:
        level[1] -= 1
        for i in range(len(world[level[0]][level[1]])):
            if world[level[0]][level[1]][i][len(world[level[0]][level[1]][i])-1] == 0:
                break
        offset = (i - floor(x/40)) * 40
        x += offset
        y += 1160
        for i in range(len(screeninp)):
            screeninp[i][0] += offset
            screeninp[i][1] += 1160
        for i in range(len(transition)):
            transition[i][1] = 560 - (560*i/len(transition))
    if y > 1180:
        level[1] += 1
        for i in range(len(world[level[0]][level[1]])):
            if world[level[0]][level[1]][i][0] == 0:
                break
        offset = (i - floor(x/40)) * 40
        x += offset
        y -= 1160
        for i in range(len(screeninp)):
            screeninp[i][0] += offset
            screeninp[i][1] -= 1160
        for i in range(len(transition)):
            transition[i][1] = (560*i/len(transition)) - 560
            
    # Vertical Wall Collision
    
    if yvel > 0 and y < 1160:
        if world[level[0]][level[1]][floor(x/40)][floor(y/40)+1] == 1 and y % 40 > 30:
            y = (floor(y/40))*40+30
        if x >= 40:
            if world[level[0]][level[1]][floor(x/40)-1][floor(y/40)+1] == 1 and y % 40 > 30 and x % 40 < 10:
                y = (floor(y/40))*40+30
                x += 100 / ups
                if x % 40 > 10:
                    x = (floor(x/40))*40+10
        if x < 1960:
            if world[level[0]][level[1]][floor(x/40)+1][floor(y/40)+1] == 1 and y % 40 > 30 and x % 40 > 30:
                y = (floor(y/40))*40+30
                x -= 100 / ups
                if x % 40 < 30:
                    x = (floor(x/40))*40+30
    if yvel < 0 and y >= 40:
        if world[level[0]][level[1]][floor(x/40)][floor(y/40)-1] == 1 and y % 40 < 10:
            y = (floor(y/40))*40+10
        if x >= 40:
            if world[level[0]][level[1]][floor(x/40)-1][floor(y/40)-1] == 1 and y % 40 < 10 and x % 40 < 10:
                y = (floor(y/40))*40+10
                x += 100 / ups
                if x % 40 > 10:
                    x = (floor(x/40))*40+10
        if x < 1960:
            if world[level[0]][level[1]][floor(x/40)+1][floor(y/40)-1] == 1 and y % 40 < 10 and x % 40 > 30:
                y = (floor(y/40))*40+10
                x -= 100 / ups
                if x % 40 < 30:
                    x = (floor(x/40))*40+30

    # Processing Horizontal Movements
                    
    if movingleft and not movingright:
        xvel -= speed * 20 / ups
        if xvel < -speedcap:
            xvel = -speedcap
    if ((not movingleft and not movingright) or (movingleft and movingright)) and xvel < 0:
        xvel += speed * 10 / ups
        if xvel > 0:
            xvel = 0
    if movingright and not movingleft:
        xvel += speed * 20 / ups
        if xvel > speedcap:
            xvel = speedcap
    if ((not movingleft and not movingright) or (movingleft and movingright)) and xvel > 0:
        xvel -= speed * 10 / ups
        if xvel < 0:
            xvel = 0
    x += xvel / ups * 20

    # Horizontal Level Transition
            
    if x < 20:
        level[0] -= 1
        for i in range(len(world[level[0]][level[1]][len(world[level[0]][level[1]])-1])):
            if world[level[0]][level[1]][len(world[level[0]][level[1]])-1][i] == 0:
                break
        offset = (i - floor(y/40)) * 40
        x += 1960
        y += offset
        for i in range(len(screeninp)):
            screeninp[i][0] += 1960
            screeninp[i][1] += offset
        for i in range(len(transition)):
            transition[i][0] = 960 - (960*i/len(transition))
    if x > 1980:
        level[0] += 1
        for i in range(len(world[level[0]][level[1]][0])):
            if world[level[0]][level[1]][0][i] == 0:
                break
        offset = (i - floor(y/40)) * 40
        x -= 1960
        y += offset
        for i in range(len(screeninp)):
            screeninp[i][0] -= 1960
            screeninp[i][1] += offset
        for i in range(len(transition)):
            transition[i][0] = (960*i/len(transition)) - 960
            
    # Horizontal Wall Collision
    
    if xvel > 0 and x < 1960:
        if world[level[0]][level[1]][floor(x/40)+1][floor(y/40)] == 1 and x % 40 > 30:
            x = (floor(x/40))*40+30
        if y >= 40:
            if world[level[0]][level[1]][floor(x/40)+1][floor(y/40)-1] == 1 and x % 40 > 30 and y % 40 < 10:
                x = (floor(x/40))*40+30
                y += 100 / ups
                if y % 40 > 10:
                    y = (floor(y/40))*40+10
        if y < 1160:
            if world[level[0]][level[1]][floor(x/40)+1][floor(y/40)+1] == 1 and x % 40 > 30 and y % 40 > 30:
                x = (floor(x/40))*40+30
                y -= 100 / ups
                if y % 40 < 30:
                    y = (floor(y/40))*40+30
    if xvel < 0 and x >= 40:
        if world[level[0]][level[1]][floor(x/40)-1][floor(y/40)] == 1 and x % 40 < 10:
            x = (floor(x/40))*40+10
        if y >= 40:
            if world[level[0]][level[1]][floor(x/40)-1][floor(y/40)-1] == 1 and x % 40 < 10 and y % 40 < 10:
                x = (floor(x/40))*40+10
                y += 100 / ups
                if y % 40 > 10:
                    y = (floor(y/40))*40+10
        if y < 1160:
            if world[level[0]][level[1]][floor(x/40)-1][floor(y/40)+1] == 1 and x % 40 < 10 and y % 40 > 30:
                x = (floor(x/40))*40+10
                y -= 100 / ups
                if y % 40 < 30:
                    y = (floor(y/40))*40+30

    # Camera Movement
    
    screeninp.append([x,y])
    screeninp.remove(screeninp[0])
    transition.append([0,0])
    transition.remove(transition[0])
    screenx = screeninp[0][0]
    screeny = screeninp[0][1]

def LoS(pos1,pos2): # Detecting Line of Sight
    LoSx = pos1[0]
    LoSy = pos1[1]
    clear = True
    if pos1[0] < pos2[0]:
        while LoSx < pos2[0]:
            LoSx += sin(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if pos1[1] < pos2[1]:
                LoSy += cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            else:
                LoSy -= cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if LoSx > pos2[0]:
                LoSx = pos2[0]
                LoSy = pos2[1]
            if LoSx % 40 != 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 == 0:
                if (world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1 and
                   world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)-1] == 1):
                    clear = False
                    break
            elif LoSx % 40 != 0 and LoSy % 40 == 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1:
                    clear = False
                    break
    elif pos1[0] > pos2[0]:
        while LoSx > pos2[0]:
            LoSx -= sin(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if pos1[1] < pos2[1]:
                LoSy += cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            else:
                LoSy -= cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if LoSx < pos2[0]:
                LoSx = pos2[0]
                LoSy = pos2[1]
            if LoSx % 40 != 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 == 0:
                if (world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1 and
                   world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)-1] == 1):
                    clear = False
                    break
            elif LoSx % 40 != 0 and LoSy % 40 == 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1:
                    clear = False
                    break
    elif pos1[1] < pos2[1]:
        while LoSy < pos2[1]:
            LoSy += cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if LoSy > pos2[0]:
                LoSy = pos2[1]
            if LoSx % 40 != 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 == 0:
                if (world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1 and
                   world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)-1] == 1):
                    clear = False
                    break
            elif LoSx % 40 != 0 and LoSy % 40 == 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1:
                    clear = False
                    break
    else:
        while LoSy > pos2[1]:
            LoSy -= cos(atan(abs(pos1[0]-pos2[0]),abs(pos1[1]-pos2[1])))*5
            if LoSy < pos2[0]:
                LoSy = pos2[1]
            if LoSx % 40 != 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 != 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1:
                    clear = False
                    break
            elif LoSx % 40 == 0 and LoSy % 40 == 0:
                if (world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)] == 1 and
                   world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1 and world[level[0]][level[1]][floor(LoSx/40)-1][floor(LoSy/40)-1] == 1):
                    clear = False
                    break
            elif LoSx % 40 != 0 and LoSy % 40 == 0:
                if world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)] == 1 and world[level[0]][level[1]][floor(LoSx/40)][floor(LoSy/40)-1] == 1:
                    clear = False
                    break
    return(clear)

def enemyai(): # Controlling all Enemies
    global entities
    global hp
    for i in range(len(entities[level[0]][level[1]])):
        if entities[level[0]][level[1]][i]['entity']['cat'] == 'enemy':
            enemy = entities[level[0]][level[1]][i]
            enemyx = enemy['pos']['x']
            enemyy = enemy['pos']['y']

            # Enemy Attacks
            
            for j in range(len(enemy['tags']['weapons'])):
                if enemy['tags']['weapons'][j]['type'] == 'contact':
                    if (((enemyx-10 >= x-10 and enemyx-10 <= x+10) or (enemyx+10 >= x-10 and enemyx+10 <= x+10)) and
                        ((enemyy-10 >= y-10 and enemyy-10 <= y+10) or (enemyy+10 >= y-10 and enemyy+10 <= y+10)) and
                        enemy['tags']['weapons'][j]['cooldown'] <= 0):
                        enemy['tags']['weapons'][j]['cooldown'] = enemy['tags']['weapons'][j]['haste']/1
                        hp -= calculatedamage(enemy['tags']['weapons'][j]['damage'],enemy['tags']['weapons'][j]['piercing'],defence,hardness)
                    elif enemy['tags']['weapons'][j]['cooldown'] > 0:
                        enemy['tags']['weapons'][j]['cooldown'] -= 1 / ups

            # Enemy Pathfinding
                        
            if enemy['entity']['subcat'] == 'grunt':
                if (LoS((x-10,y-10),(enemyx-10,enemyy-10)) and LoS((x+10,y-10),(enemyx+10,enemyy-10)) and
                    LoS((x+10,y+10),(enemyx+10,enemyy+10)) and LoS((x-10,y+10),(enemyx-10,enemyy+10))):
                    enemy['tags']['attention'] = enemy['tags']['attentionspan']
                elif enemy['tags']['attention'] > 0:
                    enemy['tags']['attention'] -= 1/ups
                    if enemy['tags']['attention'] <= 0:
                        enemy['tags']['attention'] = 0
                        enemy['tags']['path'] = ()
                if enemy['tags']['attention'] == enemy['tags']['attentionspan']:
                    enemy['tags']['path'] = (x,y)
                if enemy['tags']['path'] == () and randint(1,round(5*ups)) == 1:
                    enemy['tags']['path'] = (randint(round(enemyx-80),round(enemyx+80)),randint(round(enemyy-80),round(enemyy+80)))
                    j = 0
                    while j < 4 and not (LoS((enemyx-10,enemyy-10),(enemy['tags']['path'][0]-10,enemy['tags']['path'][1]-10)) and
                                         LoS((enemyx+10,enemyy-10),(enemy['tags']['path'][0]+10,enemy['tags']['path'][1]-10)) and
                                         LoS((enemyx+10,enemyy+10),(enemy['tags']['path'][0]+10,enemy['tags']['path'][1]+10)) and
                                         LoS((enemyx-10,enemyy+10),(enemy['tags']['path'][0]-10,enemy['tags']['path'][1]+10))):
                        j += 1
                        enemy['tags']['path'] = (randint(round(enemyx-80),round(enemyx+80)),randint(round(enemyy-80),round(enemyy+80)))
                    if not (LoS((enemyx-10,enemyy-10),(enemy['tags']['path'][0]-10,enemy['tags']['path'][1]-10)) and
                            LoS((enemyx+10,enemyy-10),(enemy['tags']['path'][0]+10,enemy['tags']['path'][1]-10)) and
                            LoS((enemyx+10,enemyy+10),(enemy['tags']['path'][0]+10,enemy['tags']['path'][1]+10)) and
                            LoS((enemyx-10,enemyy+10),(enemy['tags']['path'][0]-10,enemy['tags']['path'][1]+10))):
                        enemy['tags']['path'] = ()

            # Enemy Movement
                        
            if enemy['tags']['path'] != ():
                if pythag((enemy['tags']['path'][0],enemy['tags']['path'][1]),(enemyx,enemyy)) < enemy['tags']['stats']['speed']/ups*20:
                    enemyx = enemy['tags']['path'][0]
                    enemyy = enemy['tags']['path'][1]
                    enemy['tags']['path'] = ()
                    attention = 0
                else:
                    if enemy['tags']['path'][0] > enemyx:
                        enemyx += sin(atan(abs(enemyx-enemy['tags']['path'][0]),
                                           abs(enemyy-enemy['tags']['path'][1])))*enemy['tags']['stats']['speed']/ups*20
                    else:
                        enemyx -= sin(atan(abs(enemyx-enemy['tags']['path'][0]),
                                           abs(enemyy-enemy['tags']['path'][1])))*enemy['tags']['stats']['speed']/ups*20
                    if enemy['tags']['path'][1] > enemyy:
                        enemyy += cos(atan(abs(enemyx-enemy['tags']['path'][0]),
                                           abs(enemyy-enemy['tags']['path'][1])))*enemy['tags']['stats']['speed']/ups*20
                    else:
                        enemyy -= cos(atan(abs(enemyx-enemy['tags']['path'][0]),
                                           abs(enemyy-enemy['tags']['path'][1])))*enemy['tags']['stats']['speed']/ups*20
                enemy['pos']['x'] = enemyx
                enemy['pos']['y'] = enemyy
                                                        
                            
def displaygame(): # Displaying the Game
    screen.fill(Gray)
    for i in range(len(world[level[0]][level[1]])):
        for j in range(len(world[level[0]][level[1]][i])):
            if world[level[0]][level[1]][i][j] == 0:
                screenrect(White,i*40,j*40,40,40)
    if transition[0][0] > 0:
        for i in range(len(world[level[0]+1][level[1]])):
            for j in range(len(world[level[0]+1][level[1]][i])):
                if world[level[0]+1][level[1]][i][j] == 0:
                    screenrect(White,i*40+1960,j*40+offset,40,40)
    if transition[0][0] < 0:
        for i in range(len(world[level[0]-1][level[1]])):
            for j in range(len(world[level[0]-1][level[1]][i])):
                if world[level[0]-1][level[1]][i][j] == 0:
                    screenrect(White,i*40-1960,j*40+offset,40,40)
    if transition[0][1] > 0:
        for i in range(len(world[level[0]][level[1]+1])):
            for j in range(len(world[level[0]][level[1]+1][i])):
                if world[level[0]][level[1]+1][i][j] == 0:
                    screenrect(White,i*40+offset,j*40+1160,40,40)
    if transition[0][1] < 0:
        for i in range(len(world[level[0]][level[1]-1])):
            for j in range(len(world[level[0]][level[1]-1][i])):
                if world[level[0]][level[1]-1][i][j] == 0:
                    screenrect(White,i*40+offset,j*40-1160,40,40)

    screenrect(Black,x-10,y-10,20,20)
    for entity in entities[level[0]][level[1]]:
        if entity['entity']['cat'] == 'enemy':
            if entity['entity']['subcat'] == 'grunt':
                screenrect(Red,entity['pos']['x']-10,entity['pos']['y']-10,20,20)
                
    pygame.display.flip()

def timekeep():
    global time
    global ups
    global upss
    global timerecord
    time.remove(time[0])
    time.append(checktime())
    if time[1] < time[0]:
        time[0] -= 60
    ups = 1/(time[1]-time[0])
    upss.append(ups)
    while timerecord[0] < time[1] - 5:
        timerecord.remove(timerecord[0])
    timerecord.append(time[1])
    if ups < 1:
        print(timerecord)

def playgame(): # Playing the Game
    done = False
    while not done:
        gameinputs()

        enemyai()

        displaygame()

        timekeep()
        
        pygame.time.Clock().tick(fps)
    pygame.quit()

def chooseweapon():
    done = False

# Gameplay Variables

maxhp = 100
hp = 100
speed = 10
defence = 0
hardness = 0
weapons = []

# Movement Variables

x = 1000
y = 600
xvel = 0
yvel = 0
movingup = False
movingdown = False
movingleft = False
movingright = False
screenx = 1000
screeny = 600
screeninp = []
transition = []
for i in range(round(fps/10)):
    screeninp.append([x,y])
for i in range(round(fps/3)):
    transition.append([0,0])

# Time Variables

timerecord = [checktime()]
time = [checktime(),checktime()]
upss = []

# World Creation

getlevel = makeworld()
world = getlevel[0]
entities = getlevel[1]
level = [7,7]
viewworld()

# Running the Game

chooseweapon()

playgame()
