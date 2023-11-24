# Permutations for each move
from os import defpath
from random import choice, randint
from sys import argv
from time import time

MOVES_LIST = {
    "U":  [2,   0,   3,   1,  20,  21,   6,   7,   4,   5,  10,  11,  12,  13,  14,  15,   8,   9,  18,  19,  16,  17,  22,  23],
    "U'": [1,   3,   0,   2,   8,   9,   6,   7,  16,  17,  10,  11,  12,  13,  14,  15,  20,  21,  18,  19,   4,   5,  22,  23],
    "R":  [0,   9,   2,  11,   6,   4,   7,   5,   8,  13,  10,  15,  12,  22,  14,  20,  16,  17,  18,  19,   3,  21,   1,  23],
    "R'": [0,  22,   2,  20,   5,   7,   4,   6,   8,   1,  10,   3,  12,   9,  14,  11,  16,  17,  18,  19,  15,  21,  13,  23],
    "F":  [0,   1,  19,  17,   2,   5,   3,   7,  10,   8,  11,   9,   6,   4,  14,  15,  16,  12,  18,  13,  20,  21,  22,  23],
    "F'": [0,   1,   4,   6,  13,   5,  12,   7,   9,  11,   8,  10,  17,  19,  14,  15,  16,   3,  18,   2,  20,  21,  22,  23],
    "D":  [0,   1,   2,   3,   4,   5,  10,  11,   8,   9,  18,  19,  14,  12,  15,  13,  16,  17,  22,  23,  20,  21,   6,   7],
    "D'": [0,   1,   2,   3,   4,   5,  22,  23,   8,   9,   6,   7,  13,  15,  12,  14,  16,  17,  10,  11,  20,  21,  18,  19],
    "L":  [23,  1,  21,   3,   4,   5,   6,   7,   0,   9,   2,  11,   8,  13,  10,  15,  18,  16,  19,  17,  20,  14,  22,  12],
    "L'": [8,   1,  10,   3,   4,   5,   6,   7,  12,   9,  14,  11,  23,  13,  21,  15,  17,  19,  16,  18,  20,   2,  22,   0],
    "B":  [5,   7,   2,   3,   4 , 15,   6,  14,   8,   9,  10,  11,  12,  13,  16,  18,   1,  17,   0,  19,  22,  20,  23,  21],
    "B'": [18, 16,   2,   3,   4,   0,   6,   1,   8,   9,  10,  11,  12,  13,   7,   5,  14,  17,  15,  19,  21,  23,  20,  22],
}

# Potential Values for distance in Heuristics Function and PDDL
# Sticker Indices for each corner pieces
CORNER_LIST = [(10, 12, 19), ( 6, 11, 13),
               ( 2,  8, 17), ( 3,  4,  9),
               (14, 18, 23), ( 7, 15, 22),
               ( 0, 16, 21), ( 1,  5, 20)]

# 3D Coordinates for each corner
COORDINATES_LIST = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0),
                    (0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)]

# Compl
complementsList = {"U" : "D'", "U'": "D" ,
                   "L'": "R" , "L" : "R'",
                   "F" : "B'", "F'": "B" ,
                   "D'": "U" , "D" : "U'",
                   "R" : "L'", "R'": "L" ,
                   "B'": "F" , "B" : "F'"}

class Cube2x2:
    
    # Function: Initialize Cube
    def __init__(self, cube = "WWWW RRRR GGGG YYYY OOOO BBBB", movesList=[], parentState=None, depth=0, f=0):
        self.movesList = movesList
        self.depth = depth
        self.state = self.checkCube(cube)
        self.parent = parentState
        self.f = f

    # Function: Check Cube String
    def checkCube(self, state):
        state = state.replace(" ", "")
        state = state.upper()
        if len(state) != 24:
            raise ValueError("State must have only 24 Stickers.")
        colors = ["W", "R", "G", "Y", "O", "B"]
        for color in colors:
            if state.count(color) != 4:
                raise ValueError("State must exactly have 4 Stickers of each Color.")
        return state

    # Function: Print Cube
    def __str__(self):
        state = self.state
        printCube = "   {}{}      \n".format(state[0], state[1])
        printCube += "   {}{}      \n".format(state[2], state[3])
        printCube += "{}{} {}{} {}{} {}{}\n".format(state[16], state[17], state[8], state[9], state[4], state[5], state[20], state[21])
        printCube += "{}{} {}{} {}{} {}{}\n".format(state[18], state[19], state[10], state[11], state[6], state[7], state[22], state[23])
        printCube += "   {}{}      \n".format(state[12], state[13])
        printCube += "   {}{}      \n".format(state[14], state[15])
        return printCube
    
    def print(self):
        return(str(self))

    def printMultipleMoves(self, moves):
        state1 = str(self)
        n = 0
        for move in moves:
            n += 1
            if n == 4:
                n = 0
                print(state1)
                self.state = self.executeMove(self.state, move)
                state1 = str(self)
                continue
            self.state = self.executeMove(self.state, move)
            state2 = str(self)
            state1 = "\n".join(["  ".join(state3) for state3 in zip(state1.split("\n"), state2.split("\n"))])
        print(state1)

    # Function: Return Current State
    def returnCurrentState(self):
        return self.state

    # Function: Check if Goal State Reached
    def checkIfGoalState(self):
        for i in range(0, len(self.state), 4):
            side = self.state[i:i+4]
            if side.count(side[0]) != 4:
                return False
        return True

    # Function: Execute a single given Move to the State
    def executeMove(self, state, move):
        # For Invalid Move
        if move not in MOVES_LIST.keys():
            raise ValueError("Invalid Move.")

        # Sticker Rotation for a Given Move
        permutations = MOVES_LIST[move]
        state = "".join([state[i] for i in permutations])
        return state

    # Function: Execute a set of given Moves to the State
    def executeMoves(self, moves):
        state = self.returnCurrentState()
        for move in moves.split():
            state = self.executeMove(state, move)
        return state

    # Function: Shuffle Cube with N Moves
    def shuffleCube(self, N):
       # Choose n random moves from the list of moves and creates an algorithm to apply
        moves = list(MOVES_LIST.keys())
        shuffle = " ".join([choice(moves) for i in range(N)])
        shuffledState = self.executeMoves(shuffle)
        return Cube2x2(shuffledState)

    # Function: To check for a Valid Move (not inverse/complement of last move and not doing same move 3 times)
    def checkIfValidMove(self, move):
        if self.movesList:
            lastMove = self.movesList[-1]
            if move == self.checkIfInverseMove(lastMove) or move == self.checkIfComplementMove(lastMove):
                return False
            elif len(self.movesList) >= 2 and move == lastMove and move == self.movesList[-2]:
                return False
        return True

    # Function: Inverse of move
    def checkIfInverseMove(self, move):
        if len(move) == 1:
            return move + "'"
        else:
            return move[0]

    # Returns the complement of the given move
    def checkIfComplementMove(self, move):
        return complementsList[move]

    # Function: Generate Normalised form of state
    def generateNormalForm(self, state):
        state = self.checkCube(state)
        oppositeColor = {"O": "R", "G": "B", "Y": "W", "R": "O", "B": "G", "W": "Y"}

        # Opposite colors
        state0, state1, state2 = state[10], state[12], state[19]
        opp0, opp1, opp2 = oppositeColor[state0], oppositeColor[state1], oppositeColor[state2]
        mapping = {state0: "G", state1: "Y", state2: "O", opp0: "B", opp1: "W", opp2: "R"}

        # Normal Form
        normalState = ""
        for s in state:
            normalState += mapping[s]
        return normalState

    # Function: Applied Move added in movesList
    def addMove(self, move):
        self.movesList.append(move)

    # Function: A* Implementation
    def aStar(self):
        if self.checkIfGoalState():
            return self.movesList, 0, 0.0
        start = time()
        cubes = [self]
        opened = [self.state]
        closed = set()
        nodeCount = 0
        while opened:
            # Open the first state in the list
            state0 = opened.pop(0)
            cube0 = cubes.pop(0)
            # Close the state
            closed.add(state0)
            depth = cube0.depth + 1
            for move in MOVES_LIST.keys():
                # Skips moves that lead to inverse and complement states
                if not cube0.checkIfValidMove(move):
                    continue
                # Applies move and normalizes result so we don't store duplicate states
                state = self.generateNormalForm(self.executeMove(cube0.state, move))
                if state not in closed and state not in opened:
                    nodeCount += 1
                    # Compute heuristic function
                    f = depth + self.calculateHeuristics(state)
                    # Creates a cube for this state and tracks the moves
                    cube = Cube2x2(state, cube0.movesList[:], cube0, depth, f)
                    cube.addMove(move)
                    if cube.checkIfGoalState():
                        return cube.movesList, nodeCount, time() - start
                    # Inserts the state depending on its heuristic
                    for i in range(len(cubes) + 1):
                        if i == len(cubes):
                            opened.append(state)
                            cubes.append(cube)
                        elif cube.f < cubes[i].f:
                            opened.insert(i, state)
                            cubes.insert(i, cube)
                            break
    
    # Function: Calculate Heuristics:
    # Computes the sum of number of moves to put each corner in its correct position divided by 4
    def calculateHeuristics(self, state):
        myCorners = []
        solvedCorners = []
        cornerSum = 0
        s = self.generateNormalForm(state)
        solved = Cube2x2().state

        # Corner of current state and goal state
        for x, y, z in CORNER_LIST:
            corner = "".join(sorted(s[x] + s[y] + s[z]))
            myCorners.append(corner)
            corner = "".join(sorted(solved[x] + solved[y] + solved[z]))
            solvedCorners.append(corner)

        # 3D plot
        for i in range(len(COORDINATES_LIST)):
            # Current corner coordinates
            myCorner = myCorners[i]
            myCoords = COORDINATES_LIST[i]
            # Corner coordinates if solved
            idx = solvedCorners.index(myCorner)
            solvedCoords = COORDINATES_LIST[idx]
            # 3D Manhattan distance if corner not solved
            if myCoords != solvedCoords:
                x = abs(solvedCoords[0] - myCoords[0])
                y = abs(solvedCoords[1] - myCoords[1])
                z = abs(solvedCoords[2] - myCoords[2])
                cornerSum += x + y + z

        return cornerSum / 4
    
def main():
    print("A Star")
    cubeAStar = Cube2x2()
    shuffledMovesCount = 6
    nodeCountAvg = 0
    timeAvg = 0
    for shuffleCount in range(1,shuffledMovesCount+1):
        for i in range(100):
            shuffledCube = cubeAStar.shuffleCube(shuffleCount)
            moves, nodeCount, time = shuffledCube.aStar()
            # print(" ".join(moves))
            # shuffledCube.printMultipleMoves(moves)
            # print("NodeCount: ", nodeCount)
            # print("Time: ", round(time, 2), "msecs")
            nodeCountAvg += nodeCount
            timeAvg += time
        print("Average Time and NodeCount for ", shuffledMovesCount, ": ", round(timeAvg/100, 5), ", ", nodeCountAvg/100)
    
if __name__ == "__main__":
    main()