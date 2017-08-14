import sys
import msvcrt
from random import randint

boardsize = 7
tower_x = randint(0, boardsize - 1)
tower_y = randint(0, boardsize - 1)

yeti_x = randint(0, boardsize - 1)
yeti_y = randint(0, boardsize - 1)

health = 11

sword = False

towerlist = ['leave', 'up', 'sit', 'armoir']
towertoplist = ['down', 'open']

def gameover(x, y, a, b, h):
    print "\n You died. Game Over :(\n"
    yn = raw_input("Play again? (y/n): ")
    if yn.lower() == 'y':
        showboard(2, 2, yeti_x, yeti_y, health)
    else:
        sys.exit()

def yetimove(x):
    if x in range(2, boardsize - 1):
        x += randint(-1, 1)
        return x
    elif x < 2:
        x += randint(0, 1)
        return x
    elif x > boardsize - 2:
        x += randint(-1, 0)
        return x

def showboard(x, y, a, b, h):
    h -= 1
    print "COLD DAMAGE:"
    print "Health = " + str(h)
    board = []
    for row in range(boardsize):
        board.append(['O'] * boardsize)
    a = yetimove(a)
    b = yetimove(b)
    board[a][b] = 'Y'
    board[tower_y][tower_x] = '#'
    board[y][x] = 'X'
    print "\n"
    for row in board:
        print " ".join(row)
    print "\n" * 20
    if h < 0:
        gameover(x, y, a, b, h)
    if x == b and y == a:
        yetifight(x, y, a, b, h)
    move(x, y, a, b, h)

def yetifight(x, y, a, b, h):
    print "\nA giant yeti appears!\n"
    print "He slashes at you with his big yeti claws!\n"
    h -= 5
    print "YETI SLASH:"
    print "Health = " + str(h)
    if h < 0:
        gameover(x, y, a, b, h)
    else:
        showboard(x, y, a, b, h)

def towerdoor(x, y, a, b, h):
    print "\nYou arrive at an old tower.\n"
    print "The heavy door looms before you.\n"
    print "Type 'push' to try pushing the door open.\n"
    print "Type 'knock' to knock on the door.\n"
    print "Type 'leave' to leave.\n"

    actionlist = ['push', 'knock', 'leave']
    action = getaction(actionlist)

    if action == 'leave':
        print "\nYou turn away."
        showboard(x, y, a, b, h)
    elif action == 'push':
        print "\nThe door creaks open.\n"
        tower(x, y, a, b, h)
    elif action == 'knock':
        print "\nYou graze your knuckles on the rough wood. :(\n"
        h -= 1
        print "SPLINTER ATTACK:"
        print "Health = " + str(h)
        if h < 0:
            gameover(x, y, a, b, h)
        else:
            towerdoor(x, y, a, b, h)

def tower_text():
    if 'sit' in towerlist:
        print "\nAs your eyes adjust to the gloom you can make out"
        print "a chair resting by a glowing fireplace,"
        print "an armoir in the corner"
        print "and a spiral staircase leading upwards.\n"
        print "Type 'sit' to sit in the chair.\n"
        print "Type 'armoir' to check out the armoir.\n"
        print "Type 'up' to go up the stairs.\n"
        print "Type 'leave' to leave the tower.\n"
    else:
        print "\nAs your eyes adjust to the gloom you can make out"
        print "a chair by a cold fireplace,"
        print "an armoir in the corner"
        print "and a spiral staircase leading upwards.\n"
        print "Type 'armoir' to check out the armoir.\n"
        print "Type 'up' to go up the stairs.\n"
        print "Type 'leave' to leave the tower.\n"


def tower(x, y, a, b, h):
    tower_text()

    actionlist = towerlist
    action = getaction(actionlist)

    if action == 'leave':
        print "\nYou leave the tower.\n"
        showboard(x, y, a, b, h)
    if action == 'up':
        print "\nYou climb the narrow stairs to the top of the tower.\n"
        towertop(x, y, a, b, h)
    if action == 'sit':
        print "\nYou sit by the fireplace for a while."
        print "You feel warmer and healthier!\n"
        h += 5
        print "Health = " + str(h)
        towerlist.remove('sit')
        tower(x, y, a, b, h)
    if action == 'armoir':
        print "\nYou are attacked by a grue!\n"
        if sword == False:
            h -= 5
            print "GRUE ATTACK:"
            print "Health = " + str(h)
            if h < 0:
                gameover(x, y, a, b, h)
        elif sword == True:
            tower(x, y, a, b, h)

def towertop_text():
    if 'open' in towertoplist:
        print "\nYou are at the top of the tower."
        print "There is a big golden chest labled 'Yeti Killing Apparatus'\n"
        print "Type 'open' to open the chest."
        print "Type 'down' to descend."
    else:
        print "\nYou are at the top of the tower."
        print "There is an empty chest labled 'Yeti Killing Apparatus'\n"
        print "Type 'down' to descend."


def towertop(x, y, a, b, h):
    towertop_text()

    actionlist = towertoplist
    action = getaction(actionlist)

    if action == 'down':
        print "You carefully descend the staircase."
        tower(x, y, a, b, h)
    elif action == 'open':
        print "\nYou open the chest and pull out a giant sword!\n"
        print "\n You get the GIANT SWORD!"
        sword = True

        towertoplist.remove('open')
        towertop(x, y, a, b, h)




def move(x, y, a, b, h):

    cmdlist = ['w', 'a', 's', 'd', 'f', 'h']
    cmd = getcmd(cmdlist)

    if cmd == 'w':
        if y == 0:
            showboard(x, y, a, b, h)
            print "\nThat's the edge of the map."
        else:
            y -= 1
            showboard(x, y, a, b, h)
    elif cmd == 'a':
        if x == 0:
            showboard(x, y, a, b, h)
            print "\nThat's the edge of the map."
        else:
            x -= 1
            showboard(x, y, a, b, h)
    elif cmd == 's':
        if y == boardsize - 1:
            showboard(x, y, a, b, h)
            print "\nThat's the edge of the map."
        else:
            y += 1
            showboard(x, y, a, b, h)
    elif cmd == 'd':
        if x == boardsize - 1:
            showboard(x, y, a, b, h)
            print "\nThat's the edge of the map."
        else:
            x += 1
            showboard(x, y, a, b, h)
    elif cmd == 'f':
        if x == tower_x and y == tower_y:
            towerdoor(x, y, a, b, h)
        else:
            # add a chance to pick up something nourishing
            print "You find nothing but snow."
            showboard(x, y, a, b, h)
    elif cmd == 'h':
        h += 1
        print "'wasd' to move.\n"
        print "Hit 'f' to investigate a tile.\n"
        print "Hit 'l' to quit.\n"
        print "Hit 'h' for help.\n"
        showboard(x, y, a, b, h)

def getaction(actionlist):
    print "\n"
    action = raw_input("What do you do? >>> ")
    if action in actionlist:
        print "\n" * 25
        return action.lower()
    else:
        print "\n" * 25
        print "\nThat's not a thing you can do :(\n"
        return getaction(actionlist)

def getcmd(cmdlist):
    cmd = msvcrt.getch()
    if cmd in cmdlist:
        return cmd
    elif cmd == 'l':
        sys.exit()
    else:
        print "\n That's not a valid command. :( \n"
        return getcmd(cmdlist)

print "\nTOPDOWN ADVENTURES 1:\n"
print "The Curse Of The RNG.\n"
print "\nYou ('X' on the map) find yourself in a snowy wasteland."
print "If you don't find shelter you will freeze to death!\n"
print "'wasd' to move.\n"
print "Hit 'f' to investigate a tile.\n"
print "Hit 'l' to quit.\n"
print "Hit 'h' for help.\n"

print "Hit 'a' for anal.\n"

showboard(2, 2, yeti_x, yeti_y, health)
