from Board import Board
import numpy as np
restarts=[]
moves=[]
times=[]
for i in range(25):
    b = Board(8)
    b.newBoard()
    move,restart,time = b.hillClimbing()
    moves.append(move)
    restarts.append(restart)
    times.append(time)
    print("Restart :" ,restart)
    print("Move:" ,move)
    print("Time:",time)
for i in range(25):
    print("Board:{} Restart Count:{} Move Count:{} Time:{}".format(i,restarts[i],moves[i],times[i]))
print("Mean Values: Restart Count:{} Move Count:{} Time:{}".format(np.mean(restarts),np.mean(moves),np.mean(times)))