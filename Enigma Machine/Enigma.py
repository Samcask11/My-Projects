import random
x = 1
space = ['~','-','@','=','$','^']
dot = ['!',',','?',')','|','*']
while x == 1:
    rot1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    rot2 = [17,9,23,18,14,26,20,12,15,3,25,22,16,1,8,6,11,10,5,24,21,2,19,4,7,13]
    rot3 = [15,25,18,6,1,22,13,12,10,8,21,5,20,14,4,11,9,24,17,7,16,19,23,26,2,3]
    rot4 = [1,21,8,19,18,3,5,2,20,25,7,26,13,10,11,12,9,22,15,17,24,6,23,14,16,4]
    rot5 = [21,7,6,13,22,4,20,11,14,16,5,2,15,25,8,12,26,9,23,18,19,24,3,10,17,1]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rotor1 = int(input('1st rotor: '))
    rotor2 = int(input('2nd rotor: '))
    rotor3 = int(input('3rd rotor: '))
    rotat1 = int(input('1st rotation: '))
    rotat2 = int(input('2nd rotation: '))
    rotat3 = int(input('3rd rotation: '))
    #wire11 = input('Wire 1 start: ')
    #wire12 = input('Wire 1 end: ')
    #wire21 = input('Wire 2 start: ')
    #wire22 = input('Wire 2 end: ')
    #rotor1 = random.randint(1,5)
    #rotor2 = random.randint(1,5)
    #rotor3 = random.randint(1,5)
    #rotat1 = random.randint(0,25)
    #rotat2 = random.randint(0,25)
    #rotat3 = random.randint(0,25)
    if rotor1 == 1:
        rotor1 = rot1
    if rotor1 == 2:
        rotor1 = rot2
    if rotor1 == 3:
        rotor1 = rot3
    if rotor1 == 4:
        rotor1 = rot4
    if rotor1 == 5:
        rotor1 = rot5
    if rotor2 == 1:
        rotor2 = rot1
    if rotor2 == 2:
        rotor2 = rot2
    if rotor2 == 3:
        rotor2 = rot3
    if rotor2 == 4:
        rotor2 = rot4
    if rotor2 == 5:
        rotor2 = rot5
    if rotor3 == 1:
        rotor3 = rot1
    if rotor3 == 2:
        rotor3 = rot2
    if rotor3 == 3:
        rotor3 = rot3
    if rotor3 == 4:
        rotor3 = rot4
    if rotor3 == 5:
        rotor3 = rot5
    OrMe = input('Message: ')
    #OrMe = OrMe.replace(wire11,wire12)
    #OrMe = OrMe.replace(wire21,wire22)
    LeMe = len(OrMe)
    EnMe = ''
    i = 0
    while i < LeMe:
        if OrMe[i] == ' ':
            EnMe = EnMe + space[random.randint(0,5)]
            i += 1
        elif OrMe[i] == '.':
            EnMe = EnMe + dot[random.randint(0,5)]
            i += 1
        else:
            NeDi = alphabet.index(OrMe[i])
            NeDi += rotor1[rotat1]
            NeDi += rotor2[rotat2]
            NeDi += rotor3[rotat3]
            NeDi += rotor3[rotat3]
            NeDi += rotor2[rotat2]
            NeDi += rotor1[rotat1]
            while NeDi > 25:
                NeDi -= 25
            rotat1 += 1
            if rotat1 == 26:
                rotat1 = 0
                rotat2 += 1
            if rotat2 == 26:
                rotat2 = 0
                rotat3 += 1
            if rotat3 == 26:
                rotat3 = 0
            EnMe = EnMe + alphabet[NeDi]
            i += 1
    #EnMe = EnMe.replace(wire12,wire11)
    #EnMe = EnMe.replace(wire22,wire21)
    print(EnMe)
    input('')
