
def print2dCube(cube):
    x = [["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""]]
    
    # manually map them
    x[0][2] = cube[0][0]
    x[0][3] = cube[0][1]
    x[1][2] = cube[0][2]
    x[1][3] = cube[0][3]

    x[2][0] = cube[4][0]
    x[2][1] = cube[4][1]
    x[3][0] = cube[4][2]
    x[3][1] = cube[4][3]

    x[2][2] = cube[2][0]
    x[2][3] = cube[2][1]
    x[3][2] = cube[2][2]
    x[3][3] = cube[2][3]

    x[2][4] = cube[1][0]
    x[2][5] = cube[1][1]
    x[3][4] = cube[1][2]
    x[3][5] = cube[1][3]

    x[2][6] = cube[5][0]
    x[2][7] = cube[5][1]
    x[3][6] = cube[5][2]
    x[3][7] = cube[5][3]

    x[4][2] = cube[3][0]
    x[4][3] = cube[3][1]
    x[5][2] = cube[3][2]
    x[5][3] = cube[3][3]

    for i in range(len(x)):
        print(x[i])

def printCube(c):
    print(c)

    print("      ", c[0], c[1])
    print("      ", c[2], c[3])

    c[4]
    c[5]
    c[6]
    c[7]
    # x[2][0] = c[1][0]
    # x[2][1] = c[1][1]
    # x[3][0] = c[1][2]
    # x[3][1] = c[1][3]

    # x[2][2] = cube[2][0]
    # x[2][3] = cube[2][1]
    # x[3][2] = cube[2][2]
    # x[3][3] = cube[2][3]

    # x[2][4] = cube[3][0]
    # x[2][5] = cube[3][1]
    # x[3][4] = cube[3][2]
    # x[3][5] = cube[3][3]

    # x[2][6] = cube[4][0]
    # x[2][7] = cube[4][1]
    # x[3][6] = cube[4][2]
    # x[3][7] = cube[4][3]

    # x[4][2] = cube[5][0]
    # x[4][3] = cube[5][1]
    # x[5][2] = cube[5][2]
    # x[5][3] = cube[5][3]

def make2dCube(x):
    a = [[],[],[],[],[],[]]
    # for i in range(len(a)):
    i = 0
    for j in range(0,len(x),4):
        # print(x[j:j+4])
        a[i] = x[j:j+4]
        i += 1
        
    # print(a)
    return a

def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    # x = [2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15, 8, 9, 18, 19, 16, 17, 22, 23]
    cube = make2dCube(x)
    printCube(x)

    print2dCube(cube)
    # printCube(x)
    

if __name__ == "__main__":
    main()