import pygame
import random
import math
sqrt = math.sqrt
randint = random.randint

#Defining Colours
Red = (255,0,0)
Red1 = (200,0,0)
Orange = (255,100,0)
Orange1 = (200,70,0)
Yellow = (255,255,0)
Yellow1 = (200,200,0)
Green = (0,255,0)
Green1 = (0,200,0)
Cyan = (0,255,255)
Cyan1 = (0,200,200)
Blue = (100,0,255)
Blue1 = (70,0,200)
Pink = (255,0,255)
Pink1 = (200,0,200)
White = (255,255,255)
Black = (0,0,0)
Gray = (200,200,200)
Gray1 = (195,195,195)
Gray2 = (225,225,225)
Background = (175,200,225)
Background1 = (125,150,175)

#Defining Shapes
Line = [[4, 5, 6, 7], [1, 5, 9, 13]]
Z = [[4, 5, 9, 10], [2, 6, 5, 9]]
S = [[5, 6, 8, 9], [1, 5, 6, 10]]
LBack = [[4, 5, 6, 10], [1, 5, 8, 9], [0, 4, 5, 6], [1, 2, 5, 9]]
L = [[4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6], [1, 5, 9, 10]]
T = [[4, 5, 6, 9], [1, 4, 5, 9], [1, 4, 5, 6], [1, 5, 6, 9]]
Square = [[5, 6, 9, 10]]
Shapes = [Line, Z, S, L, LBack, T, Square]

#Beggining Pygame
pygame.init()
size = (540, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

#Variable Stuffs
speed = 1
fps = 25
counter = 0
pressing_down = False
shape = False
shapeno = 0
rotation = 0
colour = Red
x = 0
y = 0
done = False
state = "Start"
score = 0
LEFT = 0
RIGHT = 0
Lcount = 0
Rcount = 0
Highscore = 0
cancer = False
paused = 0

#Creating the Field
def reset():
    field = []
    for i in range(20):
        newline = []
        for j in range(10):
            newline.append(0)
        field.append(newline)
    return(field)
field = reset()
if cancer is True:
    screen.fill(White)

#Detecting Collisions
def intersect():
    global x
    global y
    for i in range(4):
        for j in range(4):
            if i * 4 + j in Shapes[shapeno][rotation]:
                if i + y > 19 or j + x > 9 or j + x < 0 or i + y < 0 or field[i+y][j+x] > 0:
                    return(True)
    return(False)

#Randomiser... For Some Added Spice
def randomint(num):
    low = (num - (num/4))*100
    high = (num + (num/4))*100
    return(randint(low,high)/100)

#Stopping a Shape
def stop():
    global x
    global y
    for i in range(4):
            for j in range(4):
                if i * 4 + j in Shapes[shapeno][rotation]:
                    field[i+y][j+x] = shapeno + 1
    lines = 0
    for i in range(20):
        if 0 not in field[i]:
            lines += 1
            field.remove(field[i])
            field.insert(0,[0,0,0,0,0,0,0,0,0,0])
    global score
    global Highscore
    if lines == 1:
        score += randomint(40)
    if lines == 2:
        score += randomint(100)
    if lines == 3:
        score += randomint(300)
    if lines == 4:
        score += randomint(1200)
    if score > Highscore:
        Highscore = score
    global shape
    shape = False

#Moving Down
def down():
    global y
    y += 1
    if intersect():
        y -= 1
        stop()

#Moving Sideways
def side(dx):
    global x
    x += dx
    if intersect():
        x -= dx

#Defining the First Shape
NewShape = Shapes[randint(0,6)]
if NewShape == Line:
    NewColour = Orange
    NewShapeno = 0
    NewColour1 = Orange1
elif NewShape == Z:
    NewColour = Cyan
    NewShapeno = 1
    NewColour1 = Cyan1
elif NewShape == S:
    NewColour = Green
    NewShapeno = 2
    NewColour1 = Green1
elif NewShape == LBack:
    NewColour = Pink
    NewShapeno = 4
    NewColour1 = Pink1
elif NewShape == L:
    NewColour = Blue
    NewShapeno = 3
    NewColour1 = Blue1
elif NewShape == Square:
    NewColour = Red
    NewShapeno = 6
    NewColour1 = Red1
elif NewShape == T:
    NewColour = Yellow
    NewShapeno = 5
    NewColour1 = Yellow1

#The Game
while done is False:

    if score > Highscore:
        Highscore = score
    
    #Making a New Shape
    if shape == False and state == "Start":
        x = 3
        y = -1
        rotation = 0
        shape = NewShape
        shapeno = NewShapeno
        colour = NewColour
        colour1 = NewColour1
        NewShape = Shapes[randint(0,6)]
        if NewShape == Line:
            NewColour = Orange
            NewShapeno = 0
            NewColour1 = Orange1
        elif NewShape == Z:
            NewColour = Cyan
            NewShapeno = 1
            NewColour1 = Cyan1
        elif NewShape == S:
            NewColour = Green
            NewShapeno = 2
            NewColour1 = Green1
        elif NewShape == LBack:
            NewColour = Pink
            NewShapeno = 4
            NewColour1 = Pink1
        elif NewShape == L:
            NewColour = Blue
            NewShapeno = 3
            NewColour1 = Blue1
        elif NewShape == Square:
            NewColour = Red
            NewShapeno = 6
            NewColour1 = Red1
        elif NewShape == T:
            NewColour = Yellow
            NewShapeno = 5
            NewColour1 = Yellow1
        if intersect():
            state = "End"
        
    #Timer for Moving Down
    if paused == 0:
        counter += (1 + ((len(str(round(score)))-1)**2)/10) * speed
    if counter > 10:
        counter = 0
        down()
    if pressing_down:
        down()
        
    #Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and state == "Start":
                paused += 1
                if paused == 2:
                    paused = 0
        if event.type == pygame.KEYDOWN and paused == 0:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                currentR = rotation
                rotation = (rotation + 1) % len(Shapes[shapeno])
                if intersect() is True:
                    rotation = currentR
                currentR = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pressing_down = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                LEFT = 1
                RIGHT = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                RIGHT = 1
                LEFT = 0
            if event.key == pygame.K_SPACE and state == "Start":
                while not intersect():
                    y += 1
                    score += randomint(1)
                    if score > Highscore:
                        Highscore = score
                y -= 1
                stop()
                counter = 0
            if event.key == pygame.K_ESCAPE:
                field = reset()
                shape = False
                state = "Start"
                score = 0
                counter = -10
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pressing_down = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                LEFT = 0
                Lcount = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                RIGHT = 0
                Rcount = 0
    if LEFT == 1:
        if Lcount == 0 or Lcount == 2 or Lcount > 3:
            side(-1)
        Lcount += 1
    if RIGHT == 1:
        if Rcount == 0 or Rcount == 2 or Rcount > 3:
            side(1)
        Rcount += 1

    #Display
    if cancer is False:
        screen.fill(Background)
        for i in range(20):
            pygame.draw.rect(screen, Background1, [i * 40 + 20, 0, 20, 600])
        pygame.draw.rect(screen, Gray, [40, 50, 200, 400])
        for i in range(5):
            pygame.draw.rect(screen, Gray1, [60 + i * 40, 50, 20, 400])
        pygame.draw.rect(screen, Black, [40, 50, 200, 400], 1)
    for i in range(20):
        for j in range(10):
            if field[i][j] > 0:
                pygame.draw.rect(screen, Black, [40 + 20 * j, 50 + 20 * i, 20, 20], 1)
            if field[i][j] == 1:
                pygame.draw.rect(screen, Orange1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Orange, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 2:
                pygame.draw.rect(screen, Cyan1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Cyan, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 3:
                pygame.draw.rect(screen, Green1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Green, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 4:
                pygame.draw.rect(screen, Blue1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Blue, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 5:
                pygame.draw.rect(screen, Pink1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Pink, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 6:
                pygame.draw.rect(screen, Yellow1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Yellow, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
            elif field[i][j] == 7:
                pygame.draw.rect(screen, Red1, [40 + 20 * j + 1, 50 + 20 * i + 1, 18, 18])
                pygame.draw.rect(screen, Red, [42 + 20 * j + 1, 52 + 20 * i + 1, 13, 13])
    if cancer is False:
        pygame.draw.rect(screen, Gray, [300, 70, 160, 80])
        for i in range(4):
            pygame.draw.rect(screen, Gray1, [300 + i * 40, 70, 20, 80])
        pygame.draw.rect(screen, Black, [300, 70, 160, 80], 1)
        pygame.draw.rect(screen, Gray, [300, 210, 200, 85])
        for i in range(5):
            pygame.draw.rect(screen, Gray1, [300 + i * 40, 210, 20, 85])
        pygame.draw.rect(screen, Black, [300, 210, 200, 85], 1)
    if NewShapeno == 0:
        yq = 10
    else:
        yq = 0
    if NewShapeno == 1 or NewShapeno == 2 or NewShapeno == 3 or NewShapeno == 4 or NewShapeno == 5:
        xq = 10
    else:
        xq = 0
    for i in range(2):
        for j in range(4):
            if (i + 1) * 4 + j in Shapes[NewShapeno][0]:
                pygame.draw.rect(screen, NewColour1, [340 + 20 * j + 1 + xq, 90 + 20 * i + 1 + yq, 18, 18])
                pygame.draw.rect(screen, NewColour, [342 + 20 * j + 1 + xq, 92 + 20 * i + 1 + yq, 13, 13])
                pygame.draw.rect(screen, Black, [340 + 20 * j + xq, 90 + 20 * i + yq, 20, 20], 1)
            
    if shape is not None:
        for i in range(4):
            for j in range(4):
                slot = i * 4 + j
                if slot in Shapes[shapeno][rotation]:
                    pygame.draw.rect(screen, Black, [40 + 20 * (j+x), 50 + 20 * (i+y), 20, 20], 1)
                    pygame.draw.rect(screen, colour1, [40 + 20 * (j+x) + 1, 50 + 20 * (i+y) + 1, 18, 18])
                    pygame.draw.rect(screen, colour, [42 + 20 * (j+x) + 1, 52 + 20 * (i+y) + 1, 13, 13])

    #Text
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 35, True, False)
    text = font.render("Score: " + str(round(score)), True, Black)
    text1 = font.render("Highscore: " + str(round(Highscore)), True, Black)
    text_game_over = font1.render("Game Over", True, Red)
    text_game_over1 = font1.render("Press ESC", True, Red)
    text_paused = font1.render("Paused", True, Background1)

    if paused == 1:
        pressing_down = False
        LEFT = 0
        RIGHT = 0
        pygame.draw.rect(screen, Gray2, [41, 200, 198, 100])
        #pygame.draw.rect(screen, Gray, [88, 237.5, 104, 25])
        screen.blit(text_paused, [87.5, 234.5])
    screen.blit(text, [310, 220])
    screen.blit(text1, [310, 260])
    if state == "End":
        pygame.draw.rect(screen, Gray2, [41, 200, 198, 100])
        #pygame.draw.rect(screen, Gray, [57.5, 217, 165, 24])
        #pygame.draw.rect(screen, Gray, [72, 259, 136, 24])
        screen.blit(text_game_over, [57.5, 213])
        screen.blit(text_game_over1, [71, 255])
    
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
