# Name: Aditya Maleeswaran
# Assignment Name: Homework 1
# File Name: WordLadderProblemBFS.py

class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    __slots__ = ('name', 'neighbors')

    def __str__(self):
        result = self.name + ' : '
        for n in self.neighbors:
            result += n.name + ', '
        return result[:-1]


def buildWordGraph(file):
    w = {}
    f = open(file)
    words = f.read().split('\n')

    for word in words:
        for i in range(len(word)):
            wcard = word[:i] + '*' + word[i + 1:]
            if wcard in w:
                w[wcard].append(word)
            else:
                w[wcard] = [word]

    for key in w:
        wordlist = w[key]
        for w1 in wordlist:
            for w2 in wordlist:
                if w1 != w2:
                    inputGraph(w1, w2)


def inputGraph(word1, word2):

    if word1 not in Graph:
        node = Node(word1)
        node.neighbors.append(Node(word2))
        Graph[word1] = node
    else:

        neighbors = Graph[word1].neighbors

        if word2 not in [x.name for x in neighbors]:
            neighbors.append(Node(word2))

    if word2 not in Graph:
        node = Node(word2)
        node.neighbors.append(Node(word1))
        Graph[word2] = node
    else:

        neighbors = Graph[word2].neighbors

        if word1 not in [x.name for x in neighbors]:
            neighbors.append(Node(word1))


class Queue():
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue==[]

def bfs(start,finish,Graph):
    parents={}
    q=Queue()
    q.enqueue(start)
    parents[start.name]=None

    while(not q.empty()):
        node=q.dequeue()
        for neighbor in node.neighbors:
            n=neighbor.name

            if n not in parents:
                parents[n]=node.name
                if n==finish.name:
                    return parents
                q.enqueue(Graph[neighbor.name])

    return parents

def getPath(start,finish,parents):
    finish=finish.name
    path=[finish]
    if finish in parents:
        node=parents[finish]
        while(node!=start.name):
            path.append(node)
            node=parents[node]
    else:
        "No Path "

    path.append(start.name)

    return path[::-1]


if __name__ == '__main__':

    Graph = {}
    
    file="Words.txt"

    buildWordGraph(file) 

    word1 = 'fool'
    word2 = 'sage'

    if word1 in Graph:

        start = Graph[word1]
        
        if word2 in Graph:
            finish = Graph[word2]
            traverse = bfs(start, finish, Graph)
            path = getPath(start, finish, traverse) 
            str = ''

            for p in path:
                str += p + ' -> '

            print (str[:-3])
	        	
        else:
             print("Word2 not in Graph") 
	
    else:
        print("Word1 not in Graph")

