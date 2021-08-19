import sys
import random

global fullcount
dict = {}
flag = 0
newchessboard = []
notcount = 0
allcount = 0
fullcount = 0

def collisionscount(chessboard):
    count = 0
    length = len(chessboard)

    for i in range(0, length-1):
        for j in range(i+1, length):

            if (chessboard[i] == chessboard[j]):
                count = count+1
    # print count
    # print chessboard
    for i in range(0, length):
        temp = chessboard[i]
        tempi = i
        for j in range(1, len(chessboard)):
            dummy = temp-j
            downdummy = temp+j

            if(tempi > length-2):
                break
            if(downdummy == chessboard[tempi+1]):
                count = count+1
            if(dummy < 1):
                break

            if(dummy == chessboard[tempi+1]):
                count = count+1

            tempi = tempi+1
            
    return count

def nextfunction(chessboard):
    global allcount
    global notcount
    global fullcount
    length = len(chessboard)
    heuristicvalue = collisionscount(chessboard)
    for i in range(0, length):
        already = chessboard[i]
        for j in range(1, length+1):
            chessboard[i] = j
            newheuristic = collisionscount(chessboard)
            if(newheuristic == 0):
                allcount = allcount+1
                if(fullcount < 100):
                    print "This is a solution"
                    print chessboard
                    fullcount = fullcount+1
                return chessboard
            dict[i,j] = newheuristic
            # print dict
            # print chessboard
            # print newheuristic
            chessboard[i] = already

    k,l = min(dict, key = dict.get)
    result = dict [k,l]
    if(result >= heuristicvalue):
        if(fullcount < 100):
            print "Not a solution"
            print chessboard
            fullcount = fullcount+1
        notcount = notcount+1
        return chessboard
    # print k
    # print l
    # print chessboard
    chessboard[k] = l
    # print chessboard
    # print collisionscount(chessboard)
    nextfunction(chessboard)

# Main Function
print "Enter the 'N' number of Queens: "
input = int(raw_input())
print "Output for the 1st 100 times"
for i in range (0, 100):
    chessboard = []
    for i in range(1, input+1):
        randvalue = random.randint(1, input)
        # print randvalue
        # print i
        chessboard.append(randvalue)
    # print chessboard

    if(fullcount < 100):
        print "Run Number: %s" %fullcount
        print chessboard

        nextfunction(chessboard)

print "You get the solution for %s times" %allcount

