board = [
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5],
    [1,0,2,1,3,4,5,6,1,2,3,5]
]

def print_board(bo):
    for i in range(0,len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------")

    for j in range(0,len(bo[0])):
        if j % 3 == 0 and j !=0:
            print(" | ", end="")


        elif j == 8:
            print(bo[i][j])

        else:
            print(f'{bo[i][j]} + ""', end="")

print_board(board)