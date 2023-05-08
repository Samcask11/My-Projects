#-------------------------------------------------------------------------------------------------------------------------------
#                                                       STARTUP DEFINITIONS ETC
#-------------------------------------------------------------------------------------------------------------------------------

quits = False
begin = False
menu = False
gamediff = 1
doublecheck = ""

#Math

import math
sin = math.sin
cos = math.cos
rad = math.radians
deg = math.degrees
sqrt = math.sqrt

#Preparing Savefiles

import pickle
version = "Version"
file = "Savefile1"
def write():
    pickle.dump(filec,open(file,"wb"))
def read():
    return(pickle.load(open(file,'rb')))
def reset():
    controls = [("w",pygame.K_w),("s",pygame.K_s),("a",pygame.K_a),("d",pygame.K_d),("space",pygame.K_SPACE),("q",pygame.K_q),("r",pygame.K_r)]
    statistics = {"Kills": 0, "Base": 0, "Scout": 0, "Tiny": 0, "Tank": 0, "Stealth": 0, "Gunner": 0, "Damage": 0, "Invinc": 0, "Mothership": 0,
                  "Points": 0, "Highscore": 0}
    achievments = {"0score": 0, "1score": 0, "10score": 0, "100score": 0, "1000score": 0, "10000score": 0, "100000score": 0, "BaseKill": 0, "ScoutKill": 0,
                   "TinyKill": 0, "TankKill": 0, "StealthKill": 0, "GunnerKill": 0, "InvincDamage500": 0, "AllLasers": 0, "20Speed": 0, "FirstBuy": 0,
                   "BuyAllUp": 0, "500DmgHit": 0, "BossKill": 0}
    return([controls,statistics,achievments])
filec = read()

#Preparing Pygame

import pygame
pygame.init()
size = (1280,650)
screenw = pygame.display.Info().current_w
screenh = pygame.display.Info().current_h
screenscale = (screenw/size[0],screenh/size[1])
if screenscale[0] < screenscale[1]:
    mysize = (round(screenw),round((screenw/128)*65))
    scale = screenw / size[0]
else:
    mysize = (round((screenh/65)*128),round(screenh))
    scale = screensizeh / size[1]
screen = pygame.display.set_mode(mysize)
pygame.display.set_caption('Starship Revived')
fps = 25
pixel = pygame.draw.polygon
def text(xi,yi,sizei,colour,text):
    size = round(sizei*scale)
    x = xi*scale
    y = yi*scale
    font = pygame.font.SysFont("ocraextended",size,False,False)
    text1 = font.render(text,True,colour)
    screen.blit(text1,[x,y])
def rect(screen,colour,pos,outline = 0):
    x = pos[0]*scale
    y = pos[1]*scale
    xs = pos[2]*scale
    ys = pos[3]*scale
    pygame.draw.rect(screen,colour,[x,y,xs,ys],outline)

#Updating the Game

cv = pickle.load(open(version,'rb'))
if cv == 1:
    cv = 1.1
    pickle.dump(cv,open(version,"wb"))

#Controls

def setcont():
    global forward
    global forwardK
    global backward
    global backwardK
    global tuleft
    global tuleftK
    global turight
    global turightK
    global cshoot
    global cshootK
    global cbuy
    global cbuyK
    global creroll
    global crerollK
    forward = filec[0][0][0]
    forwardK = filec[0][0][1]
    backward = filec[0][1][0]
    backwardK = filec[0][1][1]
    tuleft = filec[0][2][0]
    tuleftK = filec[0][2][1]
    turight = filec[0][3][0]
    turightK = filec[0][3][1]
    cshoot = filec[0][4][0]
    cshootK = filec[0][4][1]
    cbuy = filec[0][5][0]
    cbuyK = filec[0][5][1]
    creroll = filec[0][6][0]
    crerollK = filec[0][6][1]
setcont()

#Random

import random
randscale = 2
randint = random.randint
def rand():
    return(randint(10-randscale,10+randscale)/10)

#Defining Colours

Black = (0,0,0)
Gray = (225,225,225)
DGray = (50,50,50)
DDGray = (100,100,100)
DDDGray = (20,20,20)
White = (255,255,255)
Red = (255,0,0)
DRed = (180,0,0)
DDRed = (100,0,0)
Blue = (0,150,255)
DBlue = (0,0,160)
Green = (0,255,0)
DGreen = (0,180,0)
DDGreen = (0,100,0)
BGreen = (0,255,255)
Orange = (255,150,0)
Gold = (200, 150, 0)
Purple = (255,0,255)
Yellow = (255,255,0)

#Buying and Rerolling

def reroll():
    global shop
    global coststack
    global storeflash
    coststack += rand()/5
    shop = randint(0,len(Items)-1)
    storeflash = 3
def buy():
    global points
    global power
    global rapid
    global fast
    global thrust
    global multi
    global enemysp
    global damageo
    global buletsp
    global shootspo
    global whitedmg
    global pixmak
    global goldeng
    global filec
    if round(points) >= round(Costs[shop] * coststack):
        filec[2]["FirstBuy"] = 1
        write()
        points -= round(Costs[shop] * coststack)
        Invent.append(Items[shop])
        if Items[shop] == "Powerful":
            power += 0.1
        if Items[shop] == "Rapid":
            rapid -= 0.1
        if Items[shop] == "Fast":
            fast += 0.2
        if Items[shop] == "Thrusters":
            thrust += 0.2
        if Items[shop] == "Scramblers":
            enemysp -= 1.5
        if Items[shop] == "Missile Bays":
            damageo *= 2
            buletsp /= 3
        if Items[shop] == "Multiplier":
            multi *= 3
        if Items[shop] == "Auto Turret":
            shootspo *= 3
        if Items[shop] == "Quad Guns":
            damageo *= 0.5
        whitelaser = ["Red Laser", "Gold Laser", "Purple Laser", "Yellow Laser", "Blue Laser", "White Laser"]
        if Items[shop] in whitelaser:
            whitedmg += 0.5
            if whitedmg == 4:
                filec[2]["AllLasers"] = 1
                write()
        if Items[shop] == "Pixel Maker":
            pixmak = 3
        if Items[shop] == "Golden Engines":
            goldeng = 1
        if shop > 3:
            Items.remove(Items[shop])
            Costs.remove(Costs[shop])
            Colours[shop] = "Remove"
            Colours.remove("Remove")
            Descriptions.remove(Descriptions[shop])
        reroll()
    if len(Items) == 4 and "Powerful" in Invent and "Fast" in Invent and "Thrusters" in Invent and "Rapid" in Invent:
        filec[2]["BuyAllUp"] = 1
        write()

#Collecting Pixels

def collect():
    if "Pixel Points" in Invent:
        global points
        global pointsflash
        diffpo = (diff/100) + 1
        points += 100 * multi * diffpo * rand()
        filec[1]["Points"] += 100 * multi * diffpo * rand()
        write()
        pointsflash = 3
    if "Pixel Tank" in Invent:
        global invinc
        invinc = 3 * fps
    if "Pixel Haste" in Invent:
        global haste
        haste = 2 * fps
    if "Pixel Strength" in Invent:
        global stren
        stren += 0.1
    if "Pixel Spread" in Invent:
        global enemies
        for i in range(len(enemies)):
            enemies[i][4] -= damage / 2
            enemies[i][5] = invuln

#Ship Pixel Art

ship = []
ship.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
ship.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
ship.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
ship.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
ship.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
ship.append([0,0,0,2,0,0,1,1,1,0,0,2,0,0,0])
ship.append([0,0,0,2,0,0,1,1,1,0,0,2,0,0,0])
ship.append([0,0,0,1,0,1,1,1,1,1,0,1,0,0,0])
ship.append([2,0,0,1,3,1,1,2,1,1,3,1,0,0,2])
ship.append([2,0,0,3,1,1,2,2,2,1,1,3,0,0,2])
ship.append([1,0,1,1,1,1,2,1,2,1,1,1,0,0,1])
ship.append([1,0,1,1,1,1,1,1,1,1,1,1,1,0,1])
ship.append([1,1,1,1,1,2,1,1,1,2,1,1,1,1,1])
ship.append([1,1,1,0,2,2,1,1,1,2,2,0,1,1,1])
ship.append([1,1,0,0,2,2,0,1,0,2,2,0,0,1,1])
ship.append([1,0,0,0,0,0,0,1,0,0,0,0,0,0,1])

#Enemy Pixel Art

E1 = []
E1.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
E1.append([0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
E1.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
E1.append([0,0,0,0,2,1,1,1,1,1,2,0,0,0,0])
E1.append([2,0,0,2,1,1,3,1,3,1,1,2,0,0,2])
E1.append([1,1,1,1,1,1,3,3,3,1,1,1,1,1,1])
E1.append([0,1,1,1,1,1,1,3,1,1,1,1,1,1,0])
E1.append([0,0,1,1,1,2,1,1,1,2,1,1,1,0,0])
E1.append([0,0,0,0,2,2,1,1,1,2,2,0,0,0,0])
E1.append([0,0,0,0,2,2,0,1,0,2,2,0,0,0,0])
E1.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])

#Title Screen Pixel Art

titlebuild = 0
titlebobco = 0
titleflash = 1000
showdiff = 0
diffflash = 0
Title = []
Title.append([0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1,0,0,0])
Title.append([0,0,0,1,2,1,1,1,0,1,1,2,2,1,1,1,2,2,1,2,2,1,2,2,1,2,2,1,2,1,1,1,1,2,2,1,2,2,1,1,1,2,2,1,1,1,2,2,1,2,2,1,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,0,1,2,2,1,0,1,2,2,1,2,2,1,2,2,1,2,1,1,2,2,2,2,1,2,2,2,2,2,1,0,1,2,2,1,0,1,2,2,1,2,2,1,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,0,1,2,2,1,0,1,2,2,2,2,2,1,2,2,2,2,1,1,2,2,2,2,1,2,2,2,2,2,1,0,1,2,2,1,0,1,2,2,2,2,2,1,0,0,0])
Title.append([0,0,0,0,1,1,1,2,1,0,1,2,2,1,0,1,2,2,1,2,2,1,2,2,1,2,2,1,1,1,1,2,1,2,2,1,2,2,1,1,1,2,2,1,1,1,2,2,1,1,1,0,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,0,1,2,2,1,0,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,1,0,0,0,0,0,0])
Title.append([0,0,0,1,2,2,2,2,1,0,1,2,2,1,0,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,1,0,0,0,0,0,0])
Title.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
Title.append([1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,1,0])
Title.append([1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,1,1])
Title.append([1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,1,1,0,0,1,3,3,1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,1])
Title.append([1,3,3,3,1,1,3,3,1,3,3,1,1,1,1,1,1,1,1,0,0,1,3,3,1,1,3,3,1,1,1,1,1,0,0,1,3,3,1,3,1,1,1,1,1,1,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,1,1,3,3,1,1,3,3,3,3,3,3,3,1,3,1,1,3,3,3,1,1,3,3,1,1,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,1,3,1,1,3,3,1,0,1,3,3,1,0,1,3,3,1,1,3,3,1,3,3,3,3,3,3,3,3,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,1,3,1,1,3,3,1,0,1,3,3,1,0,1,3,3,1,1,3,3,1,3,3,3,3,3,3,3,3,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,3,3,3,3,3,1,3,1,1,1,1,1,1,1,3,3,3,3,3,1,0,1,3,3,1,0,1,3,3,3,3,3,3,1,3,3,1,1,1,1,1,1,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,1,1,3,3,3,1,3,1,1,1,1,1,1,1,3,3,3,3,1,1,1,1,3,3,1,1,1,1,3,3,3,3,1,3,3,3,1,1,1,1,1,1,1,3,3,1,1,3,3,3,1])
Title.append([1,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,1,3,3,3,3,1,1,3,3,3,3,3,3,3,1,3,3,3,3,1,3,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,1])
Title.append([1,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,1,1,3,3,1,0,1,3,3,3,3,3,3,3,1,1,3,3,1,1,3,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,1,1])
Title.append([1,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,1,1,3,3,1,0,1,3,3,3,3,3,3,3,1,1,3,3,1,1,3,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,1,0])
Title.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])

#Drawing The Ship

def drawS(px,py,x,y,r,pixs):
    if cancer:
        p1 = (px-(pixs/2),py-(pixs/2))
        p1h = math.sqrt(p1[0]**2+p1[1]**2)*pixs
        p1a = math.acos(rad(abs(p1[1]*pixs)/p1h))
        if p1[0] < 0:
            p1a = 360 - p1a
        p2 = (px+(pixs/2),py-(pixs/2))
        p2h = math.sqrt(p2[0]**2+p2[1]**2)*pixs
        p2a = math.acos(rad(abs(p2[1]*pixs)/p2h))
        if p2[0] < 0:
            p2a = 360 - p2a
        p3 = (px+(pixs/2),py+(pixs/2))
        p3h = math.sqrt(p3[0]**2+p3[1]**2)*pixs
        p3a = math.acos(rad(abs(p3[1]*pixs)/p3h))
        if p3[0] < 0:
            p3a = 360 - p3a
        p4 = (px-(pixs/2),py+(pixs/2))
        p4h = math.sqrt(p4[0]**2+p4[1]**2)*pixs
        p4a = math.acos(rad(abs(p4[1]*pixs)/p4h))
        if p4[0] < 0:
            p4a = 360 - p4a
        p1c = ((sin(rad(r + p1a))*p1h)+(pixs*p1[0])+x+gamex,(cos(rad(r + p1a))*p1h)+(pixs*p1[1])+y+gamey)
        p2c = ((sin(rad(r + p2a))*p2h)+(pixs*p2[0])+x+gamex,(cos(rad(r + p2a))*p2h)+(pixs*p2[1])+y+gamey)
        p3c = ((sin(rad(r + p3a))*p3h)+(pixs*p3[0])+x+gamex,(cos(rad(r + p3a))*p3h)+(pixs*p3[1])+y+gamey)
        p4c = ((sin(rad(r + p4a))*p4h)+(pixs*p4[0])+x+gamex,(cos(rad(r + p4a))*p4h)+(pixs*p4[1])+y+gamey)
        return([p1c,p2c,p3c,p4c])
    else:
        p1 = (pixs*px-(pixs/2),pixs*py-(pixs/2))
        p1h = sqrt((p1[0])**2+(p1[1])**2)
        p1a = deg(math.acos(abs(p1[1])/p1h))
        if p1[0] <= 0 and p1[1] < 0:
            p1a = 360 - p1a
        elif p1[0] >= 0 and p1[1] > 0:
            p1a = 180 - p1a
        elif p1[0] <= 0 and p1[1] > 0:
            p1a += 180
        p1a += r
        p1 = ((sin(rad(p1a))*p1h+x+gamex)*scale,(cos(rad(p1a))*p1h+y+gamey)*scale)
        p2 = (pixs*px+(pixs/2),pixs*py-(pixs/2))
        p2h = sqrt((p2[0])**2+(p2[1])**2)
        p2a = deg(math.acos(abs(p2[1])/p2h))
        if p2[0] <= 0 and p2[1] < 0:
            p2a = 360 - p2a
        elif p2[0] >= 0 and p2[1] > 0:
            p2a = 180 - p2a
        elif p2[0] <= 0 and p2[1] > 0:
            p2a += 180
        p2a += r
        p2 = ((sin(rad(p2a))*p2h+x+gamex)*scale,(cos(rad(p2a))*p2h+y+gamey)*scale)
        p3 = (pixs*px+(pixs/2),pixs*py+(pixs/2))
        p3h = sqrt((p3[0])**2+(p3[1])**2)
        p3a = deg(math.acos(abs(p3[1])/p3h))
        if p3[0] <= 0 and p3[1] < 0:
            p3a = 360 - p3a
        elif p3[0] >= 0 and p3[1] > 0:
            p3a = 180 - p3a
        elif p3[0] <= 0 and p3[1] > 0:
            p3a += 180
        p3a += r
        p3 = ((sin(rad(p3a))*p3h+x+gamex)*scale,(cos(rad(p3a))*p3h+y+gamey)*scale)
        p4 = (pixs*px-(pixs/2),pixs*py+(pixs/2))
        p4h = sqrt((p4[0])**2+(p4[1])**2)
        p4a = deg(math.acos(abs(p4[1])/p4h))
        if p4[0] <= 0 and p4[1] < 0:
            p4a = 360 - p4a
        elif p4[0] >= 0 and p4[1] > 0:
            p4a = 180 - p4a
        elif p4[0] <= 0 and p4[1] > 0:
            p4a += 180
        p4a += r
        p4 = ((sin(rad(p4a))*p4h+x+gamex)*scale,(cos(rad(p4a))*p4h+y+gamey)*scale)
        return([p1,p2,p3,p4])

#Detecting Enemy Death

def overlap(e,ty):
    ew = range(-7,8)
    eh = range(-10,6)
    if ty == "Ranger":
        b = e
        s1h = [(-2,5),(2,4),(0,3),(-5,2),(-2,4),(-3,4),(-7,3),(-10,5),(-7,3),(-3,4),(-2,4),(-5,2),(0,3),(2,4),(-2,5)]
        if abs(x - rangerb[e][0]) < pixs * 14 or abs(y - rangerb[e][1]) < pixs * 14:
            for sx in ew:
                rr = rangerb[b][2]
                SP = []
                SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[0])
                SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[1])
                SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[2])
                SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[3])
                BP = []
                BP.append(drawS(0,-1,rangerb[b][0],rangerb[b][1],rangerb[b][2]-rr,pixs)[0])
                BP.append(drawS(0,-1,rangerb[b][0],rangerb[b][1],rangerb[b][2]-rr,pixs)[1])
                BP.append(drawS(0,1,rangerb[b][0],rangerb[b][1],rangerb[b][2]-rr,pixs)[2])
                BP.append(drawS(0,1,rangerb[b][0],rangerb[b][1],rangerb[b][2]-rr,pixs)[3])
                for i in range(4):
                    pc = SP[i]
                    ytop = BP[2][1]
                    ybot = BP[0][1]
                    xlef = BP[0][0]
                    xrig = BP[2][0]
                    if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                        return(True)
        return(False)
    if ty == "Pixel":
        b = e
        s1h = [(-2,5),(2,4),(0,3),(-5,2),(-2,4),(-3,4),(-7,3),(-10,5),(-7,3),(-3,4),(-2,4),(-5,2),(0,3),(2,4),(-2,5)]
        for sx in ew:
            SP = []
            SP.append(drawS(sx,s1h[sx+7][0],x,y,r,pixs)[0])
            SP.append(drawS(sx,s1h[sx+7][0],x,y,r,pixs)[1])
            SP.append(drawS(sx,s1h[sx+7][0],x,y,r,pixs)[2])
            SP.append(drawS(sx,s1h[sx+7][0],x,y,r,pixs)[3])
            BP = (drawS(0,0,pixels[b][0],pixels[b][1],0,pixs*4))
            ytop = BP[2][1]
            ybot = BP[0][1]
            xlef = BP[0][0]
            xrig = BP[2][0]
            for i in range(4):
                pc = SP[i]
                if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                    return(True)
        return(False)
    if enemies[e][3] == 0 or enemies[e][3] == 1 or enemies[e][3] == 4 or enemies[e][3] == 5:
        pixs2 = pixs
    if enemies[e][3] == 2:
        pixs2 = pixs/2
    if enemies[e][3] == 3 or enemies[e][3] == 6:
        pixs2 = pixs*1.2
    if enemies[e][3] == 7:
        pixs2 = pixs*2
    if ty == "Bullet" and not optimise:
        bx = 0
        for b in range(len(bullets)):
            for by in range(-1,2):
                for ex in ew:
                    for ey in eh:
                        if (E1[ey-eh[0]][ex-ew[0]] != 0 and (enemies[e][3] != 30)):
                            rr = enemies[e][2]
                            drawB = drawS(bx,by,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)
                            drawE = drawS(ex,ey,enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)
                            for i in range(4):
                                pc = drawB[i]
                                ytop = drawE[2][1]
                                ybot = drawE[0][1]
                                xlef = drawE[0][0]
                                xrig = drawE[2][0]
                                if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                                    bullets.remove(bullets[b])
                                    return(True)
                            rr = bullets[b][2]
                            drawB = drawS(bx,by,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)
                            drawE = drawS(ex,ey,enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)
                            for i in range(4):
                                pc = drawE[i]
                                ytop = drawB[2][1]
                                ybot = drawB[0][1]
                                xlef = drawB[0][0]
                                xrig = drawB[2][0]
                                if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                                    bullets.remove(bullets[b])
                                    return(True)
        return(False)
    elif ty == "Bullet" and optimise:
        if enemies[e][3] != 30:
            e1h = [(-1,0),(0,1),(0,2),(-1,2),(-2,4),(-3,4),(-7,3),(-10,5),(-7,3),(-3,4),(-2,4),(-1,2),(0,2),(0,1),(-1,0)]
        for b in range(len(bullets)):
            if abs(bullets[b][0] - enemies[e][0]) < pixs * 14 or abs(bullets[b][1] - enemies[e][1]) < pixs * 14:
                for ex in ew:
                    rr = enemies[e][2]
                    BP = []
                    BP.append(drawS(0,-1,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)[0])
                    BP.append(drawS(0,-1,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)[1])
                    BP.append(drawS(0,1,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)[2])
                    BP.append(drawS(0,1,bullets[b][0],bullets[b][1],bullets[b][2]-rr,pixs)[3])
                    EP = []
                    EP.append(drawS(ex,e1h[ex+7][0],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[0])
                    EP.append(drawS(ex,e1h[ex+7][0],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[1])
                    EP.append(drawS(ex,e1h[ex+7][1],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[2])
                    EP.append(drawS(ex,e1h[ex+7][1],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[3])
                    for i in range(4):
                        pc = BP[i]
                        ytop = EP[2][1]
                        ybot = EP[0][1]
                        xlef = EP[0][0]
                        xrig = EP[2][0]
                        if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                            if bullets[b][3] == 0:
                                bullets.remove(bullets[b])
                                return(True,damage)
                            if bullets[b][3] == 1:
                                bullets.remove(bullets[b])
                                return(True,damage*2)
                            if bullets[b][3] == 2:
                                bullets.remove(bullets[b])
                                return(True,damage*8)
                            if bullets[b][3] == 3:
                                bullets.remove(bullets[b])
                                return(True,0)
                            if bullets[b][3] == 4:
                                return(True,damage*0.5)
                            if bullets[b][3] == 5:
                                enemies[e][6] = 0.5
                                bullets.remove(bullets[b])
                                return(True,damage)
                            if bullets[b][3] == 6:
                                bullets.remove(bullets[b])
                                return(True,damage*whitedmg)
        return(False,damage)
    elif ty == "Ship" and not optimise:
        sx = 0
        for sx in range(-7,8):
            for sy in range(-10,6):
                if ship[sy][sx] != 0:
                    for ex in ew:
                        for ey in eh:
                            if (E1[ey][ex] != 0 and (enemies[e][3] != 30)):
                                rr = enemies[e][2]
                                drawP = drawS(sx,sy,x,y,r-rr,pixs)
                                drawE = drawS(ex,ey,enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs)
                                for i in range(4):
                                    pc = drawP[i]
                                    ytop = drawE[2][1]
                                    ybot = drawE[0][1]
                                    xlef = drawE[0][0]
                                    xrig = drawE[2][0]
                                    if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                                        return(True)
                                rr = r
                                drawP = drawS(sx,sy,x,y,r-rr,pixs)
                                drawE = drawS(ex,ey,enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs)
                                for i in range(4):
                                    pc = drawE[i]
                                    ytop = drawP[2][1]
                                    ybot = drawP[0][1]
                                    xlef = drawP[0][0]
                                    xrig = drawP[2][0]
                                    if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                                        return(True)
        return(False)
    elif ty == "Ship" and optimise:
        s1h = [(-2,5),(2,4),(0,3),(-5,2),(-2,4),(-3,4),(-7,3),(-10,5),(-7,3),(-3,4),(-2,4),(-5,2),(0,3),(2,4),(-2,5)]
        if enemies[e][3] != 30:
            e1h = [(-1,0),(0,1),(0,2),(-1,2),(-2,4),(-3,4),(-7,3),(-10,5),(-7,3),(-3,4),(-2,4),(-1,2),(0,2),(0,1),(-1,0)]
        if abs(x - enemies[e][0]) < pixs * 26 or abs(y - enemies[e][1]) < pixs * 26:
            for ex in ew:
                for sx in ew:
                    rr = enemies[e][2]
                    SP = []
                    SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[0])
                    SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[1])
                    SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[2])
                    SP.append(drawS(sx,s1h[sx+7][0],x,y,r-rr,pixs)[3])
                    EP = []
                    EP.append(drawS(ex,e1h[ex+7][0],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[0])
                    EP.append(drawS(ex,e1h[ex+7][0],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[1])
                    EP.append(drawS(ex,e1h[ex+7][1],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[2])
                    EP.append(drawS(ex,e1h[ex+7][1],enemies[e][0],enemies[e][1],enemies[e][2]-rr,pixs2)[3])
                    for i in range(4):
                        pc = SP[i]
                        ytop = EP[2][1]
                        ybot = EP[0][1]
                        xlef = EP[0][0]
                        xrig = EP[2][0]
                        if pc[1] >= ytop and pc[1] <= ybot and pc[0] >= xlef and pc[0] <= xrig:
                            return(True)
        return(False)

#How to Shot

def shoot():
    if len(bullets) < bulletcap or not optimise:
        global shootco
        if shootco >= shootsp*fps:
            shootco = 0
            bx = x
            by = y
            br = r
            bbr = r
            if "Auto Turret" in Invent and len(enemies) > 0:
                autotur = (10000,0)
                for i in range(len(enemies)):
                    if enemies[i][3] != 4:
                        autoturch = sqrt(abs(enemies[i][0] - x)**2 + abs(enemies[i][1] - y)**2)
                        if autotur[0] > autoturch:
                            autotur = (autoturch,i)
                if autotur[0] != 10000:
                    e = autotur[1]
                    xdiff = x - enemies[e][0]
                    ydiff = y - enemies[e][1]
                    if ydiff != 0:
                        nca = deg(math.atan(abs(xdiff)/abs(ydiff)))
                    else:
                        nca = 90
                    if xdiff >= 0 and ydiff <= 0:
                        br = 360 - nca
                    elif xdiff >= 0 and ydiff >= 0:
                        br = 180 + nca
                    elif xdiff <= 0 and ydiff >= 0:
                        br = 180 - nca
                    elif xdiff <= 0 and ydiff <= 0:
                        br = nca
                    bbr = br
            if "Quad Guns" in Invent and False:
                for i in range(4):
                    if i == 0 or i == 3:
                        hyp = sqrt((2)**2+(7)**2)
                        if i == 0:
                            br -= math.atan(2/7)
                        if i == 3:
                            br += math.atan(2/7)
                    if i == 1 or i == 2:
                        hyp = sqrt((5)**2+(4)**2)
                        if i == 0:
                            br -= deg(math.atan(5/4))
                        if i == 3:
                            br += deg(math.atan(5/4))
                    if br < 90:
                        quad = 3
                    elif br >= 90 and br < 180:
                        quad = 2
                        br = 180 - br
                    elif br >= 180 and br < 270:
                        quad = 1
                        br = 180 + br
                    elif br >= 270:
                        quad = 4
                        br = 360 - br
                    if quad == 1 or quad == 4:
                        bx -= sin(rad(br))*((pixs*hyp)-buletsp)
                    elif quad == 2 or quad == 3:
                        bx += sin(rad(br))*((pixs*hyp)-buletsp)
                    if quad == 1 or quad == 2:
                        by -= cos(rad(br))*((pixs*hyp)-buletsp)
                    elif quad == 3 or quad == 4:
                        by += cos(rad(br))*((pixs*hyp)-buletsp)
                    bullets.append([bx,by,bbr])
            else:
                if br < 90:
                    quad = 3
                elif br >= 90 and br < 180:
                    quad = 2
                    br = 180 - br
                elif br >= 180 and br < 270:
                    quad = 1
                    br = 180 + br
                elif br >= 270:
                    quad = 4
                    br = 360 - br
                if quad == 1 or quad == 4:
                    bx -= sin(rad(br))*(pixs*12-buletsp)
                elif quad == 2 or quad == 3:
                    bx += sin(rad(br))*(pixs*12-buletsp)
                if quad == 1 or quad == 2:
                    by -= cos(rad(br))*(pixs*12-buletsp)
                elif quad == 3 or quad == 4:
                    by += cos(rad(br))*(pixs*12-buletsp)
                LaserC = randint(0,5)
                if LaserC == 0:
                    if "Red Laser" in Invent:
                        bullets.append([bx,by,bbr,1])
                    else:
                        bullets.append([bx,by,bbr,0])
                elif LaserC == 1:
                    if "Gold Laser" in Invent:
                        bullets.append([bx,by,bbr,2])
                    else:
                        bullets.append([bx,by,bbr,0])
                elif LaserC == 2:
                    if "Purple Laser" in Invent:
                        bullets.append([bx,by,bbr,3])
                    else:
                        bullets.append([bx,by,bbr,0])
                elif LaserC == 3:
                    if "Yellow Laser" in Invent:
                        bullets.append([bx,by,bbr,4])
                    else:
                        bullets.append([bx,by,bbr,0])
                elif LaserC == 4:
                    if "Blue Laser" in Invent:
                        bullets.append([bx,by,bbr,5])
                    else:
                        bullets.append([bx,by,bbr,0])
                elif LaserC == 5:
                    if "White Laser" in Invent:
                        bullets.append([bx,by,bbr,6])
                    else:
                        bullets.append([bx,by,bbr,0])
                else:
                    bullets.append([bx,by,bbr,0])

#-------------------------------------------------------------------------------------------------------------------------------
#                                                       BEGINNING THE GAME
#-------------------------------------------------------------------------------------------------------------------------------

while not quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quits = True
            break
        if event.type == pygame.KEYDOWN:
            if forward == "":
                forwardK = event.key
                forward = pygame.key.name(event.key)
                filec[0][0] = (pygame.key.name(event.key),event.key)
                write()
            elif backward == "":
                backwardK = event.key
                backward = pygame.key.name(event.key)
                filec[0][1] = (pygame.key.name(event.key),event.key)
                write()
            elif tuleft == "":
                tuleftK = event.key
                tuleft = pygame.key.name(event.key)
                filec[0][2] = (pygame.key.name(event.key),event.key)
                write()
            elif turight == "":
                turightK = event.key
                turight = pygame.key.name(event.key)
                filec[0][3] = (pygame.key.name(event.key),event.key)
                write()
            elif cshoot == "":
                cshootK = event.key
                cshoot = pygame.key.name(event.key)
                filec[0][4] = (pygame.key.name(event.key),event.key)
                write()
            elif cbuy == "":
                cbuyK = event.key
                cbuy = pygame.key.name(event.key)
                filec[0][5] = (pygame.key.name(event.key),event.key)
                write()
            elif creroll == "":
                crerollK = event.key
                creroll = pygame.key.name(event.key)
                filec[0][6] = (pygame.key.name(event.key),event.key)
                write()
            else:
                if event.key == pygame.K_q:
                    done = True
                    quits = True
                    break
                if event.key == pygame.K_SPACE and menu == False:
                    begin = True
                if event.key == pygame.K_d and menu == False:
                    diffflash = 5
                    gamediff += 1
                    if gamediff > 3:
                        gamediff = 1
                if event.key == pygame.K_ESCAPE and menu == False:
                    doublecheck = ""
                    menu = "main"
                elif event.key == pygame.K_ESCAPE and menu != False:
                    doublecheck = ""
                    menu = False
                if event.key == pygame.K_c and menu == "main":
                    menu = "controls"
                if event.key == pygame.K_a and menu == "main":
                    menu = "audio"
                if event.key == pygame.K_s and menu == "main":
                    menu = "saves"
                if event.key == pygame.K_b and (menu == "audio" or menu == "controls" or menu == "saves"):
                    doublecheck = ""
                    menu = "main"
                if menu == "saves":
                    if event.key == pygame.K_1:
                        file = "Savefile1"
                        filec = read()
                        setcont()
                    if event.key == pygame.K_2:
                        file = "Savefile2"
                        filec = read()
                        setcont()
                    if event.key == pygame.K_3:
                        file = "Savefile3"
                        filec = read()
                        setcont()
                    if event.key == pygame.K_4:
                        doublecheck = "c"
                        filer = "Savefile1"
                    if event.key == pygame.K_5:
                        doublecheck = "c"
                        filer = "Savefile2"
                    if event.key == pygame.K_6:
                        doublecheck = "c"
                        filer = "Savefile3"
                    if event.key == pygame.K_y:
                        doublecheck = True
                    if event.key == pygame.K_n:
                        doublecheck = ""
                if menu == "controls":
                    if event.key == pygame.K_1:
                        forward = ""
                    if event.key == pygame.K_2:
                        backward = ""
                    if event.key == pygame.K_3:
                        tuleft = ""
                    if event.key == pygame.K_4:
                        turight = ""
                    if event.key == pygame.K_5:
                        cshoot = ""
                    if event.key == pygame.K_6:
                        cbuy = ""
                    if event.key == pygame.K_7:
                        creroll = ""
    if doublecheck == True:
        cfile = file
        file = filer
        filec = reset()
        write()
        file = cfile
        filec = read()
        doublecheck = ""
    if begin == True:
        #Defining Variables

        r = 180
        x = 0
        y = 0
        gamex = size[0]/2
        gamey = size[1]/2
        games = (800,600)
        pixs = 3
        cancer = False
        done = False
        UP = 0
        DOWN = 0
        LEFT = 0
        RIGHT = 0
        SPACE = 0
        accelo = 1
        deccel = 0.1
        rdeccel = 0.4
        maxspo = 10
        speed = 0
        rsped = 0
        bullets = []
        shootspo = 0.2
        shootco = 0
        buletsp = 15
        enemies = []
        enemysp = gamediff + 2
        spawnsp = 10
        spawnco = (fps*spawnsp)*0.5
        diff = 0
        diffco = 0
        diffsp = 5
        damageo = 20
        invuln = 5
        optimise = True
        ranger = 3
        rangerb = []
        rangers = 15
        points = 0
        starsize = 1
        pointsflash = 0
        storeflash = 0
        buyflash = 0
        rollflash = 0
        bulletcap = 6
        pixels = []
        pixmin = 10
        pixmax = 40
        pixco = 20*fps
        enemcap = 10
        spspboss = 3
        stateboss = 0

        #Shop Setup

        Invent = []
        #"Quad Guns", 240, ("Slightly decreased", "damage, but shoot 4", "lasers at once."),
        Items = ["Powerful", "Rapid", "Fast", "Thrusters", "Auto Turret", "Missile Bays", "Multiplier", "Scramblers", "Beserker", "Red Laser", "Momentum",
                 "Fuel Reserves", "Gold Laser", "Purple Laser", "Yellow Laser", "Blue Laser", "White Laser", "Pixel Maker", "Golden Engines", "Pixel Points",
                 "Pixel Tank", "Pixel Haste", "Pixel Strength", "Pixel Spread"]
        Costs = [100,        120,     120,    100,         350,           180,            300,          260,          250,        220,         190,
                 230,             170,          200,            150,            190,          250,           200,           300,              250,
                 350,          160,           270,              290]
        Colours = [Red, BGreen, Blue, Orange, Purple, BGreen, Yellow, Green, Orange, Red, Blue, Purple, Yellow, Purple, Yellow, Blue, White, Green, Orange, Green,
                   Blue, Green, Red, Red]
        Descriptions = [("Slightly increased", "damage."), ("Slightly increased attack", "speed."), ("Slightly increased max", "speed."),
                        ("Slightly increased", "acceleration."), ("All lasers automatically", "aim at the nearest enemy,", "but lowered attack speed."),
                        ("All lasers move slower,", "but deal more damage."), ("Extra points from all", "sources."), ("Enemies move slower.", ""),
                        ("Temporarily deal more", "damage after getting a", "kill."), ("Some lasers are red,", "dealing more damage."),
                        ("Deal more damage when", "moving faster."), ("Move faster if close", "enough to an enemy."),
                        ("Some lasers are gold,", "dealing no damage but", "giving extra points."),
                        ("Some lasers are purple,", "dealing huge damage, but", "giving no points."),
                        ("Some lasers are yellow,", "piercing multiple", "enemies."), ("Some lasers are blue,", "slowing down enemies on", "hit."),
                        ("Some lasers are white,", "dealing more damage for", "every laser colour", "upgrade."), ("Pixels spawn more", "frequently."),
                        ("Gain points while moving", "faster."), ("Collecting pixels grants", "points."), ("Collecting pixels grants", "temporary invincibility."),
                        ("Collecting pixels grants", "a temporary speed boost."),
                        ("Collecting pixels grants", "a permanent damage buff."),
                        ("Collecting pixels does", "minimal damage to all", "enemies. Grants no", "points.")]
        shop = randint(0,len(Items)-1)
        if False:
            shop = Items.index("Pixel Tank")
            points = Costs[shop] + 1000000
        beserk = 0
        power = 1
        rapid = 1
        fast = 1
        thrust = 1
        multi = 1
        fuel = 1
        whitedmg = 1
        coststack = 1
        pixmak = 1
        goldeng = 0
        invinc = 0
        haste = 0
        stren = 1

        #Creating Stars

        stars = []
        for i in range(400):
            stars.append((randint(gamex-games[0]/2,gamex+games[0]/2),randint(gamey-games[1]/2,gamey+games[1]/2)))

        #-------------------------------------------------------------------------------------------------------------------------------
        #                                                       PLAYING THE GAME
        #-------------------------------------------------------------------------------------------------------------------------------

        while not done:

            #Upgrades

            shootsp = shootspo * rapid
            damage = damageo * power * (1+(beserk/(3*fps))) * stren
            maxsp = maxspo * fast * fuel * ((haste/(fps*2))+1)
            accel = accelo * thrust * fuel
            if beserk > 0:
                beserk -= 1
            if "Momentum" in Invent:
                damage *= (abs(speed)*0.1) + 1
            fuel = 1
            roundscore = round(points)
            points += goldeng * (1/fps) * multi * abs(speed/2)
            filec[1]["Points"] += goldeng * (1/fps) * multi * abs(speed/2)
            write()
            if round(points) != roundscore and pointsflash < 2:
                pointsflash = 2
            if invinc > 0:
                invinc -= 1
                if invinc < 0:
                    invinc = 0
            if haste > 0:
                haste -= 1
                if haste < 0:
                    haste = 0
            
            #Controls
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quits = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == forwardK:
                        UP = 1
                    if event.key == backwardK:
                        DOWN = 1
                    if event.key == tuleftK:
                        LEFT = 1
                    if event.key == turightK:
                        RIGHT = 1
                    if event.key == cshootK:
                        SPACE = 1
                    if event.key == cbuyK:
                        buyflash = 2
                        buy()
                    if event.key == crerollK:
                        rollflash = 2
                        if points >= coststack * 20:
                            points -= coststack * 20
                            reroll()
                if event.type == pygame.KEYUP:
                    if event.key == forwardK:
                        UP = 0
                    if event.key == backwardK:
                        DOWN = 0
                    if event.key == tuleftK:
                        LEFT = 0
                    if event.key == turightK:
                        RIGHT = 0
                    if event.key == cshootK:
                        SPACE = 0

            #Control Computation
            
            if SPACE == 1:
                shoot()
            if shootco < shootsp * fps:
                shootco += 1
                if shootco > shootsp * fps:
                    shootco = shootsp * fps
            if UP == 1:
                speed += accel
                if speed > maxsp:
                    speed = maxsp
            elif DOWN == 1:
                speed -= accel/3
                if speed > 0:
                    speed -= accel/1.5
                if speed < maxsp/-3:
                    speed = maxsp/-3
            else:
                if speed > 0:
                    speed -= accel*deccel
                    if speed < 0:
                        speed = 0
                if speed < 0:
                    speed += accel*deccel
                    if speed > 0:
                        speed = 0
            if LEFT == RIGHT:
                if rsped > 0:
                    rsped -= accel*rdeccel
                    if rsped < 0:
                        rsped = 0
                if rsped < 0:
                    rsped += accel*rdeccel
                    if rsped > 0:
                        rsped =0
            elif RIGHT == 1:
                rsped -= accel
                if rsped < maxsp*-1:
                    rsped = maxsp*-1
            elif LEFT == 1:
                rsped += accel
                if rsped > maxsp:
                    rsped = maxsp
            
            #Movement

            if speed >= 20:
                filec[2]["20Speed"] = 1
                write()
            r += rsped
            if r >= 360:
                r -= 360
            elif r < 0:
                r += 360
            if r < 90:
                quad = 3
                cb = r
            elif r >= 90 and r < 180:
                quad = 2
                cb = 180 - r
            elif r >= 180 and r < 270:
                quad = 1
                cb = 180 + r
            elif r >= 270:
                quad = 4
                cb = 360 - r
            if quad == 1 or quad == 4:
                x -= sin(rad(cb))*speed
            elif quad == 2 or quad == 3:
                x += sin(rad(cb))*speed
            if quad == 1 or quad == 2:
                y -= cos(rad(cb))*speed
            elif quad == 3 or quad == 4:
                y += cos(rad(cb))*speed
            if x > games[0]/2:
                x = games[0]/2
            if x < games[0]/2 * - 1:
                x = games[0]/2 * -1
            if y > games[1]/2:
                y = games[1]/2
            if y < games[1]/2 * - 1:
                y = games[1]/2 * -1
            for i in range(len(bullets)):
                if i < len(bullets):
                    bx = bullets[i][0]
                    by = bullets[i][1]
                    br = bullets[i][2]
                    if br < 90:
                        quad = 3
                    elif br >= 90 and br < 180:
                        quad = 2
                        br = 180 - br
                    elif br >= 180 and br < 270:
                        quad = 1
                        br = 180 + br
                    elif br >= 270:
                        quad = 4
                        br = 360 - br
                    if quad == 1 or quad == 4:
                        bx -= sin(rad(br))*buletsp
                    elif quad == 2 or quad == 3:
                        bx += sin(rad(br))*buletsp
                    if quad == 1 or quad == 2:
                        by -= cos(rad(br))*buletsp
                    elif quad == 3 or quad == 4:
                        by += cos(rad(br))*buletsp
                    bullets[i][0] = bx
                    bullets[i][1] = by
                    if bx > games[0]/2:
                        bullets.remove(bullets[i])
                        break
                    if bx < games[0]/2 * - 1:
                        bullets.remove(bullets[i])
                        break
                    if by > games[1]/2:
                        bullets.remove(bullets[i])
                        break
                    if by < games[1]/2 * - 1:
                        bullets.remove(bullets[i])
                        break

            #Enemies

            if diff < 70:
                spawndiff = diff*0.01
            else:
                spawndiff = 0.7
            if spawnco >= (fps*spawnsp)*(1-(spawndiff*(1+((gamediff-1)*0.2)))) and stateboss != 1:
                spawnco = 0
                if len(enemies) >= enemcap:
                    enemies.remove(enemies[0])
                testnewunit = False
                if randint(0,3) == 0:
                    spawnx = randint(0-(games[0]/2)-(pixs*15),(games[0]/2)+(pixs*15))
                    spawny = 0 - (games[1]/2) - (pixs*15)
                elif randint(0,2) == 0:
                    spawnx = randint(0-(games[0]/2)-(pixs*15),(games[0]/2)+(pixs*15))
                    spawny = (games[1]/2) + (pixs*15)
                elif randint(0,1) == 0:
                    spawny = randint(0-(games[1]/2)-(pixs*15),(games[1]/2)+(pixs*15))
                    spawnx = (games[0]/2) + (pixs*15)
                else:
                    spawny = randint(0-(games[1]/2)-(pixs*15),(games[1]/2)+(pixs*15))
                    spawnx = 0 - (games[0]/2) - (pixs*15)
                if not testnewunit and not (diff >= 67 and stateboss == 0):
                    if diff > 160:
                        spawnra = randint(40,69)
                    elif diff > 70:
                        spawnra = randint(round(diff/4),69)
                    else:
                        spawnra = randint(round(diff/4),diff)
                    #Normal
                    if spawnra < 10:
                        #x,y,r,type,hp,inv,sped,special
                        enemies.append([spawnx,spawny,0,0,50,0,1])
                    #Scout
                    elif spawnra > 9 and spawnra < 20:
                        enemies.append([spawnx,spawny,0,1,25,0,1])
                    #Tiny
                    elif spawnra > 19 and spawnra < 30:
                        enemies.append([spawnx,spawny,0,2,1,0,1])
                    #Tank
                    elif spawnra > 29 and spawnra < 40:
                        enemies.append([spawnx,spawny,0,3,120,0,1])
                    #Stealth
                    elif spawnra > 39 and spawnra < 50:
                        enemies.append([spawnx,spawny,0,4,25,0,1])
                    #Ranger
                    elif spawnra > 49 and spawnra < 60:
                        enemies.append([spawnx,spawny,0,5,40,0,1,0])
                    #Invincible
                    elif spawnra > 59 and spawnra < 69:
                        enemies.append([spawnx,spawny,0,6,1000,0,1])
                    #Mothership
                    elif spawnra == 70:
                        enemies.append([spawnx,spawny,0,7,1000,0,1,0])
                elif stateboss == 0 and diff >= 67:
                    stateboss = 1
                    enemies.append([spawnx,spawny,0,7,1000,0,1,0])
                elif testnewunit:
                    enemies.append([spawnx,spawny,0,7,1000,0,1,0])
                
            else:
                spawnco += 1
            if diffco >= fps*diffsp:
                diff += 1
                diffco = 0
            else:
                diffco += 1
            
            pointsflash -= 1
            for i in range(len(enemies)):
                if i < len(enemies):
                    if enemies[i][4] <= 0:
                        enemies[i][5] -= 1
                        if enemies[i][5] <= 0:
                            enemies.remove(enemies[i])
                    else:
                        overlapcheck = overlap(i,"Bullet")
                        if overlapcheck[0]:
                            enemytype = enemies[i][3]
                            damado = overlapcheck[1]
                            enemies[i][5] = invuln
                            diffpo = (diff/100) + 1
                            if enemytype == 6:
                                points += damado * diffpo * rand() * multi
                                filec[1]["Points"] += damado * diffpo * rand() * multi
                                pointsflash = 3
                                filec[1]["Invinc"] += damado
                                filec[1]["Damage"] += damado
                                if damado >= 500:
                                    filec[2]["500DmgHit"] = 1
                            else:
                                points += damado/4 * diffpo * rand() * multi
                                filec[1]["Points"] += damado/4 * diffpo * rand() * multi
                                if damado == 0:
                                    enemies[i][4] -= damage * 4
                                    filec[1]["Damage"] += damage * 4
                                elif damado == damage * 8:
                                    pointsflash = 3
                                else:
                                    enemies[i][4] -= damado
                                    pointsflash = 3
                                    filec[1]["Damage"] += damado
                            if enemies[i][4] <= 0:
                                filec[1]["Kills"] += 1
                                if "Beserker" in Invent:
                                    beserk = 3 * fps
                                if damado != 0:
                                    if enemies[i][3] == 0:
                                        filec[1]["Base"] += 1
                                        points += 10 * diffpo * rand() * multi
                                        filec[1]["Points"] += 10 * diffpo * rand() * multi
                                    if enemies[i][3] == 1:
                                        filec[1]["Scout"] += 1
                                        points += 20 * diffpo * rand() * multi
                                        filec[1]["Points"] += 20 * diffpo * rand() * multi
                                    if enemies[i][3] == 2:
                                        filec[1]["Tiny"] += 1
                                        points += 40 * diffpo * rand() * multi
                                        filec[1]["Points"] += 40 * diffpo * rand() * multi
                                    if enemies[i][3] == 3:
                                        filec[1]["Tank"] += 1
                                        points += 60 * diffpo * rand() * multi
                                        filec[1]["Points"] += 60 * diffpo * rand() * multi
                                    if enemies[i][3] == 4:
                                        filec[1]["Stealth"] += 1
                                        points += 80 * diffpo * rand() * multi
                                        filec[1]["Points"] += 80 * diffpo * rand() * multi
                                    if enemies[i][3] == 5:
                                        filec[1]["Gunner"] += 1
                                        points += 100 * diffpo * rand() * multi
                                        filec[1]["Points"] += 100 * diffpo * rand() * multi
                                    if enemies[i][3] == 7:
                                        filec[1]["Mothership"] += 1
                                        points += 1000 * diffpo * rand() * multi
                                        filec[1]["Points"] += 100 * diffpo * rand() * multi
                                        filec[2]["BossKill"] = 1
                                        if stateboss == 1:
                                            stateboss = 2
                                i -= 1
                                if filec[1]["Kills"] >= 1:
                                    filec[2]["BaseKill"] = 1
                                if filec[1]["Scout"] >= 2:
                                    filec[2]["ScoutKill"] = 1
                                if filec[1]["Tiny"] >= 5:
                                    filec[2]["TinyKill"] = 1
                                if filec[1]["Tank"] >= 10:
                                    filec[2]["TankKill"] = 1
                                if filec[1]["Stealth"] >= 1:
                                    filec[2]["StealthKill"] = 1
                                if filec[1]["Gunner"] >= 2:
                                    filec[2]["GunnerKill"] = 1
                            if filec[1]["Invinc"] >= 500:
                                filec[1]["InvincDamage500"] = 1
                            write()
                        if enemies[i][5] > 0:
                            enemies[i][5] -= 1
                            if enemies[i][5] < 0:
                                enemies[i][5] = 0
                        if enemies[i][3] == 5:
                            if enemies[i][7] > ranger*fps:
                                enemies[i][7] = 0
                                rangerb.append([enemies[i][0],enemies[i][1],enemies[i][2]])
                                bx = enemies[i][0]
                                by = enemies[i][1]
                                br = enemies[i][2]
                                if br < 90:
                                    quad = 3
                                elif br >= 90 and br < 180:
                                    quad = 2
                                    br = 180 - br
                                elif br >= 180 and br < 270:
                                    quad = 1
                                    br = 180 + br
                                elif br >= 270:
                                    quad = 4
                                    br = 360 - br
                                if quad == 1 or quad == 4:
                                    bx -= sin(rad(br))*rangers
                                elif quad == 2 or quad == 3:
                                    bx += sin(rad(br))*rangers
                                if quad == 1 or quad == 2:
                                    by -= cos(rad(br))*rangers
                                elif quad == 3 or quad == 4:
                                    by += cos(rad(br))*rangers
                                rangerb[len(rangerb)-1][0] = bx
                                rangerb[len(rangerb)-1][1] = by
                            else:
                                enemies[i][7] += 1
                        xdiff = enemies[i][0] - x
                        ydiff = enemies[i][1] - y
                        if sqrt(xdiff**2 + ydiff**2) < 200 and "Fuel Reserves" in Invent:
                            fuel = ((200 - sqrt(xdiff**2 + ydiff**2)) / 100) + 1
                        if ydiff != 0:
                            nca = deg(math.atan(abs(xdiff)/abs(ydiff)))
                        else:
                            nca = 90
                        if xdiff >= 0 and ydiff <= 0:
                            enemies[i][2] = 360 - nca
                        elif xdiff >= 0 and ydiff >= 0:
                            enemies[i][2] = 180 + nca
                        elif xdiff <= 0 and ydiff >= 0:
                            enemies[i][2] = 180 - nca
                        elif xdiff <= 0 and ydiff <= 0:
                            enemies[i][2] = nca
                        bx = enemies[i][0]
                        by = enemies[i][1]
                        br = enemies[i][2]
                        if br < 90:
                            quad = 3
                        elif br >= 90 and br < 180:
                            quad = 2
                            br = 180 - br
                        elif br >= 180 and br < 270:
                            quad = 1
                            br = 180 + br
                        elif br >= 270:
                            quad = 4
                            br = 360 - br
                        if enemies[i][3] == 0:
                            if quad == 1 or quad == 4:
                                bx -= sin(rad(br))*enemysp * enemies[i][6]
                            elif quad == 2 or quad == 3:
                                bx += sin(rad(br))*enemysp * enemies[i][6]
                            if quad == 1 or quad == 2:
                                by -= cos(rad(br))*enemysp * enemies[i][6]
                            elif quad == 3 or quad == 4:
                                by += cos(rad(br))*enemysp * enemies[i][6]
                        if enemies[i][3] == 1:
                            if quad == 1 or quad == 4:
                                bx -= sin(rad(br))*enemysp*1.5 * enemies[i][6]
                            elif quad == 2 or quad == 3:
                                bx += sin(rad(br))*enemysp*1.5 * enemies[i][6]
                            if quad == 1 or quad == 2:
                                by -= cos(rad(br))*enemysp*1.5 * enemies[i][6]
                            elif quad == 3 or quad == 4:
                                by += cos(rad(br))*enemysp*1.5 * enemies[i][6]
                        if enemies[i][3] == 2:
                            if quad == 1 or quad == 4:
                                bx -= sin(rad(br))*enemysp*1.5 * enemies[i][6]
                            elif quad == 2 or quad == 3:
                                bx += sin(rad(br))*enemysp*1.5 * enemies[i][6]
                            if quad == 1 or quad == 2:
                                by -= cos(rad(br))*enemysp*1.5 * enemies[i][6]
                            elif quad == 3 or quad == 4:
                                by += cos(rad(br))*enemysp*1.5 * enemies[i][6]
                        if enemies[i][3] == 3 or enemies[i][3] == 4:
                            if quad == 1 or quad == 4:
                                bx -= sin(rad(br))*enemysp*0.6 * enemies[i][6]
                            elif quad == 2 or quad == 3:
                                bx += sin(rad(br))*enemysp*0.6 * enemies[i][6]
                            if quad == 1 or quad == 2:
                                by -= cos(rad(br))*enemysp*0.6 * enemies[i][6]
                            elif quad == 3 or quad == 4:
                                by += cos(rad(br))*enemysp*0.6 * enemies[i][6]
                        if enemies[i][3] == 5 or enemies[i][3] == 6 or enemies[i][3] == 7:
                            if quad == 1 or quad == 4:
                                bx -= sin(rad(br))*enemysp*0.4 * enemies[i][6]
                            elif quad == 2 or quad == 3:
                                bx += sin(rad(br))*enemysp*0.4 * enemies[i][6]
                            if quad == 1 or quad == 2:
                                by -= cos(rad(br))*enemysp*0.4 * enemies[i][6]
                            elif quad == 3 or quad == 4:
                                by += cos(rad(br))*enemysp*0.4 * enemies[i][6]
                        enemies[i][0] = bx
                        enemies[i][1] = by
                        if enemies[i][3] == 7:
                            if enemies[i][7] == spspboss * fps and len(enemies) < enemcap:
                                enemies[i][7] = 0
                                enemies.append([enemies[i][0],enemies[i][1],0,2,1,0,1])
                            else:
                                enemies[i][7] += 1
                        if overlap(i,"Ship"):
                            if invinc <= 0:
                                done = True
                                break
                            else:
                                invinc = 0
                                enemies[i][4] = 0
                                enemies[i][5] = invuln

            #Ranger Bullets

            for i in range(len(rangerb)):
                if i < len(rangerb):
                    bx = rangerb[i][0]
                    by = rangerb[i][1]
                    br = rangerb[i][2]
                    if br < 90:
                        quad = 3
                    elif br >= 90 and br < 180:
                        quad = 2
                        br = 180 - br
                    elif br >= 180 and br < 270:
                        quad = 1
                        br = 180 + br
                    elif br >= 270:
                        quad = 4
                        br = 360 - br
                    if quad == 1 or quad == 4:
                        bx -= sin(rad(br))*rangers
                    elif quad == 2 or quad == 3:
                        bx += sin(rad(br))*rangers
                    if quad == 1 or quad == 2:
                        by -= cos(rad(br))*rangers
                    elif quad == 3 or quad == 4:
                        by += cos(rad(br))*rangers
                    rangerb[i][0] = bx
                    rangerb[i][1] = by
                    if bx > games[0]/2:
                        rangerb.remove(rangerb[i])
                        break
                    if bx < games[0]/2 * - 1:
                        rangerb.remove(rangerb[i])
                        break
                    if by > games[1]/2:
                        rangerb.remove(rangerb[i])
                        break
                    if by < games[1]/2 * - 1:
                        rangerb.remove(rangerb[i])
                        break
                    if overlap(i,"Ranger"):
                        if invinc <= 0:
                            done = True
                        else:
                            invinc = 0
                            enemies.remove(enemies[i])
                        break

            #Pixels

            if pixco <= 0:
                pixco = randint(pixmin*fps,pixmax*fps)
                pixels.append([randint(0-(games[0]/2)+20,0+(games[0]/2)-20),randint(0-(games[1]/2)+20,0+(games[1]/2)-20),0,0])
            else:
                pixco -= pixmak
            for i in range(len(pixels)):
                if pixels[i][2] < 2:
                    if pixels[i][3] == 0:
                        pixels[i][2] += 0.2
                        if pixels[i][2] > 2:
                            pixels[i][2] = 2
                    else:
                        pixels[i][2] -= 0.5
                        if pixels[i][2] <= 0:
                            pixels.remove(pixels[i])
                            break
                if pixels[i][2] == 2:
                    if overlap(i,"Pixel"):
                        pixels[i][2] -= 0.5
                        pixels[i][3] = 1
                        collect()
            
            #Display
            
            screen.fill(Black)
            for i in range(len(stars)):
                rect(screen,White,[stars[i][0]-starsize/2,stars[i][1]-starsize/2,starsize,starsize])
            for i in range(len(pixels)):
                if pixels[i][2] >= 1:
                    pixfadcol = (255 - (55 * (pixels[i][2] - 1)), 255 - (105 * (pixels[i][2] - 1)), 0)
                else:
                    pixfadcol = White
                rect(screen,pixfadcol,[pixels[i][0]-(pixs*pixels[i][2])+gamex,pixels[i][1]-(pixs*pixels[i][2])+gamey,pixs*pixels[i][2]*2,pixs*pixels[i][2]*2])
            for i in range(len(bullets)):
                for j in range(3):
                    if bullets[i][3] == 0:
                        pixel(screen,Green,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 1:
                        pixel(screen,Red,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 2:
                        pixel(screen,Gold,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 3:
                        pixel(screen,Purple,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 4:
                        pixel(screen,Yellow,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 5:
                        pixel(screen,BGreen,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
                    if bullets[i][3] == 6:
                        pixel(screen,White,drawS(0,j-1,bullets[i][0],bullets[i][1],bullets[i][2],pixs))
            for i in range(len(rangerb)):
                for j in range(3):
                    pixel(screen,Red,drawS(0,j-1,rangerb[i][0],rangerb[i][1],rangerb[i][2],pixs))
            for i in range(len(ship[0])):
                for j in range(len(ship)):
                    if ship[j][i] == 1:
                        pixel(screen,Gray,drawS(i-7,j-10,x,y,r,pixs))
                    if ship[j][i] == 2:
                        pixel(screen,Red,drawS(i-7,j-10,x,y,r,pixs))
                    if ship[j][i] == 3:
                        pixel(screen,Blue,drawS(i-7,j-10,x,y,r,pixs))
            for e in range(len(enemies)):
                if len(enemies) > e:
                    for i in range(len(E1[0])):
                        for j in range(len(E1)):
                            pixmult = 1 + (0.05 * enemies[e][5])
                            if enemies[e][3] == 0:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,DGreen,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 2:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 3:
                                    pixel(screen,BGreen,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                            if enemies[e][3] == 1:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,Gray,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 2:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 3:
                                    pixel(screen,Blue,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                            if enemies[e][3] == 2:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs* 0.5 * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,BGreen,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs/2))
                                elif E1[j][i] == 2:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs/2))
                                elif E1[j][i] == 3:
                                    pixel(screen,Green,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs/2))
                            if enemies[e][3] == 3:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2 * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,DBlue,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                                elif E1[j][i] == 2:
                                    pixel(screen,Blue,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                                elif E1[j][i] == 3:
                                    pixel(screen,BGreen,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                            if enemies[e][3] == 4:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,Black,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 2:
                                    pixel(screen,Black,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 3:
                                    pixel(screen,Black,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                            if enemies[e][3] == 5:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,Orange,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 2:
                                    pixel(screen,BGreen,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                                elif E1[j][i] == 3:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs))
                            if enemies[e][3] == 6:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2 * pixmult))
                                elif E1[j][i] == 1:
                                    pixel(screen,DDGray,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                                elif E1[j][i] == 2:
                                    pixel(screen,Gold,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                                elif E1[j][i] == 3:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*1.2))
                            if enemies[e][3] == 7:
                                if enemies[e][5] > 0 and E1[j][i] != 0:
                                    pixel(screen,White,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*2 * (((pixmult-1)/2)+1)))
                                elif E1[j][i] == 1:
                                    pixel(screen,DRed,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*2))
                                elif E1[j][i] == 2:
                                    pixel(screen,Red,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*2))
                                elif E1[j][i] == 3:
                                    pixel(screen,DDRed,drawS(i-7,j-10,enemies[e][0],enemies[e][1],enemies[e][2],pixs*2))
            rect(screen,DGray, [0,0,size[0],gamey-(games[1]/2)])
            rect(screen,DGray, [0,gamey+(games[1]/2),size[0],gamey-(games[1]/2)])
            rect(screen,DGray, [0,0,gamex-(games[0]/2),size[1]])
            rect(screen,DGray, [gamex+(games[0]/2),0,gamex-(games[0]/2),size[1]])
            if pointsflash > 0:
                text(10,gamey,25+pointsflash,White,"Score: " + str(round(points)))
            else:
                text(10,gamey,25,White,"Score: " + str(round(points)))
            rect(screen,DDGray, [gamex+(games[0]/2)+5,gamey-65,((size[0]-games[0])/2)-10,90+(len(Descriptions[shop])*20)])
            rect(screen,Black, [gamex+(games[0]/2)+5,gamey-65,((size[0]-games[0])/2)-10,90+(len(Descriptions[shop])*20)],1)
            text(gamex+(games[0]/2)+10,gamey-60,25+storeflash,Colours[shop],Items[shop])
            text(gamex+(games[0]/2)+10,gamey-30,25+storeflash,Gold,str(round(Costs[shop]*coststack)))
            for i in range(len(Descriptions[shop])):
                text(gamex+(games[0]/2)+10,gamey+20+i*20,15+storeflash,Gray,Descriptions[shop][i])
            text(gamex+(games[0]/2)+10,gamey+60+i*20,20+buyflash,DDGray,cbuy + " to Buy")
            text(gamex+(games[0]/2)+10,gamey+220,20+rollflash,DDGray,creroll + " to Reroll")
            text(gamex+(games[0]/2)+10,gamey+250,20+rollflash,Gold,str(round(20*coststack)))
            if storeflash > 0:
                storeflash -= 1
            if buyflash > 0:
                buyflash -= 1
            if rollflash > 0:
                rollflash -= 1
            pygame.display.flip()
            pygame.time.Clock().tick(fps)
        begin = False
        titlebobco = 0
        titleflash = fps
        points = round(points)
        if points == 0:
            filec[2]["0score"] = 1
        elif len(str(points)) == 1:
            filec[2]["1score"] = 1
        elif len(str(points)) == 2:
            filec[2]["10score"] = 1
        elif len(str(points)) == 3:
            filec[2]["100score"] = 1
        elif len(str(points)) == 4:
            filec[2]["1000score"] = 1
        elif len(str(points)) == 5:
            filec[2]["10000score"] = 1
        elif len(str(points)) == 6:
            filec[2]["100000score"] = 1
        if round(points) > filec[1]["Highscore"]:
            filec[1]["Highscore"] = round(points)
        write()

    #-------------------------------------------------------------------------------------------------------------------------------
    #                                                       RENDERING THE MENU
    #-------------------------------------------------------------------------------------------------------------------------------
    
    if menu == False:
        titlesize = 10
        if titlebuild < len(Title):
            titlebuild += 1
        titlebobco += 1
        titlebobco /= fps
        if titlebobco >= 3:
            titlebobco = 0
        titlebob = sin(titlebobco) * titlesize
        titlebobco *= fps
        if titleflash == 1000 and titlebuild == len(Title):
            titleflash = fps * 1.9
        if titleflash != 1000:
            titleflash += 1
            if titleflash / fps >= 2:
                titleflash = 0

    if diffflash > 0:
        diffflash -= 1
        if diffflash < 0:
            diffflash = 0
    if menu != False:
        screen.fill(DDDGray)
    else:
        screen.fill(DGray)
    for i in range(titlebuild):
        for j in range(len(Title[i])):
            if Title[i][j] == 1:
                rect(screen,Black,[(j*titlesize)+((size[0]/2)-(len(Title[i])*titlesize*0.5)),(i+1)*titlesize+titlebob,titlesize,titlesize])
            if menu != False:
                if Title[i][j] == 2:
                    rect(screen,DDGray,[(j*titlesize)+((size[0]/2)-(len(Title[i])*titlesize*0.5)),(i+1)*titlesize+titlebob,titlesize,titlesize])
                if Title[i][j] == 3:
                    rect(screen,DDGreen,[(j*titlesize)+((size[0]/2)-(len(Title[i])*titlesize*0.5)),(i+1)*titlesize+titlebob,titlesize,titlesize])
            else:
                if Title[i][j] == 2:
                    rect(screen,White,[(j*titlesize)+((size[0]/2)-(len(Title[i])*titlesize*0.5)),(i+1)*titlesize+titlebob,titlesize,titlesize])
                if Title[i][j] == 3:
                    rect(screen,Green,[(j*titlesize)+((size[0]/2)-(len(Title[i])*titlesize*0.5)),(i+1)*titlesize+titlebob,titlesize,titlesize])
    if titlebuild == len(Title) and titleflash / fps < 1:
        showdiff = 1
        if menu != False:
            text((size[0]/2)-200,400,25,DDGray,"SPACE to Begin")
            text(20,40,25,DDGray,"ESC for Options")
            text((size[0]/2)-200,450,25,DDGray,"D to Change Difficulty")
        else:
            #rect(screen,Red,[(size[0]/2)-148,404,207,23])
            text((size[0]/2)-200,400,25,White,"SPACE to Begin")
            text(20,40,25,White,"ESC for Options")
            text((size[0]/2)-200,450,25,White,"D to Change Difficulty")
    if showdiff == 1:
        if menu != False:
            if gamediff == 1:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,DDGray,"Current Difficulty: EASY")
            elif gamediff == 2:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,DDGray,"Current Difficulty: MEDIUM")
            elif gamediff == 3:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,DDGray,"Current Difficulty: HARD")
        else:
            if gamediff == 1:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,White,"Current Difficulty: EASY")
            elif gamediff == 2:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,White,"Current Difficulty: MEDIUM")
            elif gamediff == 3:
                text((size[0]/2)-200-(diffflash*4),500-diffflash,25+diffflash,White,"Current Difficulty: HARD")
    if menu != False:
        rect(screen,DGray,[(size[0]/2)-91,94,182,40])
        #rect(screen,Red,[(size[0]/2)-81,104,162,19])
        text((size[0]/2)-83,100,25,White,"ESC to Exit")
    if menu != False and menu != "main":
        rect(screen,DGray,[(size[0]/2)-98,146,196,40])
        #rect(screen,Red,[(size[0]/2)-88,155,176,22])
        text((size[0]/2)-90,150,25,White,"B to go Back")
    if menu == "main":
        rect(screen,DGray,[(size[0]/2)-113,(size[1]/2)-50,226,40])
        text((size[0]/2)-105,(size[1]/2)-44,25,White,"C for Controls")
        rect(screen,DGray,[(size[0]/2)-91,(size[1]/2)+50,182,40])
        text((size[0]/2)-83,(size[1]/2)+56,25,White,"A for Audio")
        rect(screen,DGray,[(size[0]/2)-(len("S for Savefiles")*7.5+8.5),(size[1]/2)+150,len("S for Savefiles")*15+17,40])
        text((size[0]/2)-len("S for Savefiles")*7.5,(size[1]/2)+156,25,White,"S for Savefiles")
    if menu == "saves":
        rect(screen,DGray,[(size[0]/2)+170,244,len("Reset")*15+20,40])
        text((size[0]/2)+180,250,25,White,"Reset")
        rect(screen,DGray,[(size[0]/2)+12.5,244,len("Select")*15+20,40])
        text((size[0]/2)+22.5,250,25,White,"Select")
        if file == "Savefile1":
            rect(screen,DDGray,[(size[0]/2)-210,294,len("Save 1")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+50,294,len("1")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+200,294,len("4")*15+20,40])
        else:
            rect(screen,DGray,[(size[0]/2)-210,294,len("Save 1")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+50,294,len("1")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+200,294,len("4")*15+20,40])
        if file == "Savefile2":
            rect(screen,DDGray,[(size[0]/2)-210,394,len("Save 2")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+50,394,len("2")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+200,394,len("5")*15+20,40])
        else:
            rect(screen,DGray,[(size[0]/2)-210,394,len("Save 2")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+50,394,len("2")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+200,394,len("5")*15+20,40])
        if file == "Savefile3":
            rect(screen,DDGray,[(size[0]/2)-210,494,len("Save 3")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+50,494,len("3")*15+20,40])
            rect(screen,DDGray,[(size[0]/2)+200,494,len("6")*15+20,40])
        else:
            rect(screen,DGray,[(size[0]/2)-210,494,len("Save 3")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+50,494,len("3")*15+20,40])
            rect(screen,DGray,[(size[0]/2)+200,494,len("6")*15+20,40])
        text((size[0]/2)-200,300,25,White,"Save 1")
        text((size[0]/2)-200,400,25,White,"Save 2")
        text((size[0]/2)-200,500,25,White,"Save 3")
        text((size[0]/2)+60,300,25,White,"1")
        text((size[0]/2)+60,400,25,White,"2")
        text((size[0]/2)+60,500,25,White,"3")
        text((size[0]/2)+210,300,25,White,"4")
        text((size[0]/2)+210,400,25,White,"5")
        text((size[0]/2)+210,500,25,White,"6")
    if menu == "controls":
        rect(screen,DGray,[(size[0]/2)+140,194,len("Key to Change Control:")*15+17,40])
        text((size[0]/2)+150,200,25,White,"Key to Change Control:")
        rect(screen,DGray,[(size[0]/2)-208,244,len("Forward:")*15+17,40])
        text((size[0]/2)-200,250,25,White,"Forward:")
        rect(screen,DGray,[(size[0]/2)-10,244,len(forward)*15+17,40])
        text((size[0]/2)-2,250,25,White,forward)
        rect(screen,DGray,[(size[0]/2)+140,244,32,40])
        text((size[0]/2)+150,250,25,White,"1")
        rect(screen,DGray,[(size[0]/2)-208,294,len("Backward:")*15+17,40])
        text((size[0]/2)-200,300,25,White,"Backward:")
        rect(screen,DGray,[(size[0]/2)-10,294,len(backward)*15+17,40])
        text((size[0]/2)-2,300,25,White,backward)
        rect(screen,DGray,[(size[0]/2)+140,294,32,40])
        text((size[0]/2)+150,300,25,White,"2")
        rect(screen,DGray,[(size[0]/2)-208,344,len("Left:")*15+17,40])
        text((size[0]/2)-200,350,25,White,"Left:")
        rect(screen,DGray,[(size[0]/2)-10,344,len(tuleft)*15+17,40])
        text((size[0]/2)-2,350,25,White,tuleft)
        rect(screen,DGray,[(size[0]/2)+140,344,32,40])
        text((size[0]/2)+150,350,25,White,"3")
        rect(screen,DGray,[(size[0]/2)-208,394,len("Right:")*15+17,40])
        text((size[0]/2)-200,400,25,White,"Right:")
        rect(screen,DGray,[(size[0]/2)-10,394,len(turight)*15+17,40])
        text((size[0]/2)-2,400,25,White,turight)
        rect(screen,DGray,[(size[0]/2)+140,394,32,40])
        text((size[0]/2)+150,400,25,White,"4")
        rect(screen,DGray,[(size[0]/2)-208,444,len("Shoot:")*15+17,40])
        text((size[0]/2)-200,450,25,White,"Shoot:")
        rect(screen,DGray,[(size[0]/2)-10,444,len(cshoot)*15+17,40])
        text((size[0]/2)-2,450,25,White,cshoot)
        rect(screen,DGray,[(size[0]/2)+140,444,32,40])
        text((size[0]/2)+150,450,25,White,"5")
        rect(screen,DGray,[(size[0]/2)-208,494,len("Buy:")*15+17,40])
        text((size[0]/2)-200,500,25,White,"Buy:")
        rect(screen,DGray,[(size[0]/2)-10,494,len(cbuy)*15+17,40])
        text((size[0]/2)-2,500,25,White,cbuy)
        rect(screen,DGray,[(size[0]/2)+140,494,32,40])
        text((size[0]/2)+150,500,25,White,"6")
        rect(screen,DGray,[(size[0]/2)-208,544,len("Reroll:")*15+17,40])
        text((size[0]/2)-200,550,25,White,"Reroll:")
        rect(screen,DGray,[(size[0]/2)-10,544,(len(creroll)*15+17),40])
        text((size[0]/2)-2,550,25,White,creroll)
        rect(screen,DGray,[(size[0]/2)+140,544,32,40])
        text((size[0]/2)+150,550,25,White,"7")
    if menu == "audio":
        text(10,(size[1]/2),25,White,"This game does not have audio yet, what are you doing here, this section is useless.")
    if doublecheck == "c":
        rect(screen,Gray,[((size[0]/2)-len("Are you sure?")*15-17),((size[1]/2)-50),(len("Are you sure?")*30+34),100])
        text((size[0]/2)-len("Are you sure?")*15,(size[1]/2)-40,50,Red,"Are you sure?")
        text((size[0]/2)-len("Y / N")*7.5,(size[1]/2)+10,25,Red,"Y / N")
    pygame.display.flip()
    screen.set_at(position,(0,0,0))
    pygame.time.Clock().tick(fps)
pygame.quit()
