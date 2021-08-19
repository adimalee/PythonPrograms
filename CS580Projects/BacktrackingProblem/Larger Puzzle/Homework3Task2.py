import copy
import sys
import time

file = open('Words.txt','r')

start_time = time.clock()

# Lastly, I was planing to set up the MRV constraint for this puzzle
worddict = {}
dependencies = {}
wholedependencies = {}

copyworddict = copy.deepcopy(worddict)
domaindict = copy.deepcopy(copyworddict)
answerdict = {}
value = 1

def backtrack(copyworddict):
    global domaindict
    if (domaindict == {}):
        print answerdict
        print time.clock() - start_time, "seconds"
        exit()

    global value

    for m in domaindict:
        min = len(domaindict[m])
        value = m
        break
    # print domaindict
    
    for i in domaindict:
        
        if (len(domaindict[i]) < min):
            min = len(domaindict[i])
            value = i
	# print value,"Value: "

    for k in copyworddict[value]:
        flag = 1
        for j in dependencies[value]:
            if(flag == 1):
                # print j,"j Value: "
                wholedepvalue = wholedependencies[value][j]
                othersidevalue = wholedependencies[j][value]
                # print wholedepvalue,"Wholedepvalue: "
                # print othersidevalue,"Othersidevalue: "
                for h in copyworddict[j]:
                    # print k,h
                    if (k[wholedepvalue] == h[othersidevalue]):
                        flag = 1
                        break
                    else:
                        flag = 0

        if flag == 1:
            break

    answerdict[value] = k
    # print answerdict,"Answers: "
    forwardchecking(k,value,copyworddict)
    domaindict = copy.deepcopy(copyworddict)
    for t in answerdict:
        domaindict.pop(t)
    # print domaindict

    global worddict
    worddict = copy.deepcopy(copyworddict)
    backtrack(copyworddict)


def forwardchecking(k,value,copyworddict):
    for j in dependencies[value]:
        wholedepvalue = wholedependencies[value][j]
        othersidevalue = wholedependencies[j][value]
        # print wholedepvalue,"Wholedepvalue: "
        # print othersidevalue,"Othersidevalue: "
        
        for h in worddict[j]:
            if (k[wholedepvalue] == h[othersidevalue]):
                continue
            else:
                copyworddict[j].remove(h)
                # print copyworddict

    return copyworddict


# Calling the backtrack function from the main function
# Main Function
backtrack(copyworddict)

# I was planning on opening the Words.txt file and read in the words from the main function

