# CS5446 Project [Group P34] 
Classing Planning to solve a 2x2x2 Rubiks Cube [A-Star Algorithm]
```
├── CubeLabels.py [Added labelling for cube sides and rotations]
└── README.md
```

function make2dCube()
takes in a list of 24 elements and returns a two-dimensional list:
input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
output: [[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11],
         [12, 13, 14, 15],
         [16, 17, 18, 19],
         [20, 21, 22, 23]]

function print2dCube()
takes in a list of 24 elements and outputs it in the following form for easier checking:
input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

prints:
['', '', 0, 1, '', '', '', '']
['', '', 2, 3, '', '', '', '']
[4, 5, 8, 9, 12, 13, 16, 17]
[6, 7, 10, 11, 14, 15, 18, 19]
['', '', 20, 21, '', '', '', '']
['', '', 22, 23, '', '', '', '']
