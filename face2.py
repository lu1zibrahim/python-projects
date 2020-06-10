board = [
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1],
    [1,0,2,1,3,4,5,6,1]
   
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------")

        else:
            for j in range(len(bo)):
                if j % 3 == 0 and j !=0:
                    print(" | ", end="")


                elif j == 8:
                    print(bo[i][j])

                else:
                    print(f'{bo[i][j]}' + "", end="")

print_board(board)