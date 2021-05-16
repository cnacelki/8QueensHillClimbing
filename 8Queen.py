from Board import Board
for i in range(25):
    b = Board(8)
    b.newBoard()
    move,restart,time = b.hillClimbing()
    print("Restart :" ,restart)
    print("Move:" ,move)
    print("Time:",time)