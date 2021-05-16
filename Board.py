import numpy
import random
import time

class Board:
    def __init__(self, n):
        self.n = n
        self.board = numpy.zeros((self.n,self.n))
        self.queens=[]
        self.currenth=0
        self.minh=0

    def newBoard(self):
        self.board = numpy.zeros((self.n, self.n))
        self.queens=[]
        for i in range(self.n):
            while True:
                x = random.randrange(0, self.n)
                y = random.randrange(0, self.n)
                if self.board[x][y] == 0:
                    self.board[x][y] = 1
                    self.queens+=[[x,y]]
                    break
        self.currenth=self.calculateH()

    def calculateH(self):
        h=0
        for i in range(self.n):
            queen = self.queens[i]
            for j in range(i+1,self.n):
                otherqueen=self.queens[j]
                #Vertical
                if queen[0] == otherqueen[0]:
                    h+=1
                #Horizontal
                elif queen[1] == otherqueen[1]:
                    h+=1
                #Diagonal
                elif abs(queen[0] - otherqueen[0]) == abs(queen[1] - otherqueen[1]):
                    h+=1
        return h

    def move(self,oldCoor,newCoor):
        if oldCoor in self.queens:
            if newCoor not in self.queens:
                index = self.queens.index(oldCoor)
                self.board[self.queens[index][0]][self.queens[index][1]] = 0
                self.board[newCoor[0]][[newCoor[1]]] = 1
                self.queens[index]=newCoor

    def hillClimbing(self):
        restart=0
        move=0
        start= time.process_time()
        while True:
            bestMove = None
            newh =self.currenth
            for i in range(self.n):
                oldPos = self.queens[i]
                for x in range(self.n):
                    for y in range(self.n):
                        self.move(oldPos,[x,y])
                        h= self.calculateH()
                        if (h<newh):
                            bestMove = (oldPos,x,y)
                            newh = h
                        self.move([x,y],oldPos)
            if bestMove == None:
                self.newBoard()
                restart+=1
            else:
                end = time.process_time()
                self.currenth = newh
                self.move(bestMove[0],[bestMove[1],bestMove[2]])
                move+=1
                if self.currenth ==self.minh:
                    self.printBoard()
                    return move,restart,end-start

    def printBoard(self):
        print("x\y(0)(1)(2)(3)(4)(5)(6)(7)")
        for i in range(self.n):
            print("({})".format(i), end="")
            for j in range(self.n):
                if self.board[i, j] == 0:
                    print("( )", end="")
                elif self.board[i, j] == 1:
                    print("(Q)", end="")
            print("")
        print("")