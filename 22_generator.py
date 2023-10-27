import os
import sys
import random
import getopt

# 2x2 cube init
def cubeInit():
    red='red'
    orange='orange'
    white='white'
    green='green'
    yellow='yellow'
    blue='blue'
    cr = [[[red, red], [red, red]],
          [[orange, orange], [orange, orange]],
          [[white, white], [white, white]],
          [[green, green], [green, green]],
          [[blue, blue], [blue, blue]],
          [[yellow, yellow], [yellow, yellow]]]
    
    return cr

# F (Front): Rotate the front face 90 degrees clockwise.
# F' (Front Inverted): Rotate the front face 90 degrees counterclockwise.
# B (Back): Rotate the back face 90 degrees clockwise.
# B' (Back Inverted): Rotate the back face 90 degrees counterclockwise.
# U (Up): Rotate the upper face 90 degrees clockwise.
# U' (Up Inverted): Rotate the upper face 90 degrees counterclockwise.
# D (Down): Rotate the bottom face 90 degrees clockwise.
# D' (Down Inverted): Rotate the bottom face 90 degrees counterclockwise.
# L (Left): Rotate the left face 90 degrees clockwise.
# L' (Left Inverted): Rotate the left face 90 degrees counterclockwise.
# R (Right): Rotate the right face 90 degrees clockwise.
# R' (Right Inverted): Rotate the right face 90 degrees counterclockwise.

def F(CC):
    cm1 = [[[CC[4][0][0], CC[4][0][1]], [CC[0][1][0], CC[0][1][1]]],  # red
           [[CC[1][0][0], CC[3][0][0]], [CC[1][1][0], CC[3][0][1]]],  # orange
           [[CC[2][0][1], CC[2][1][1]], [CC[2][0][0], CC[2][1][0]]],  # white
           [[CC[0][0][0], CC[0][0][1]], [CC[3][1][0], CC[3][1][1]]],  # green
           [[CC[1][0][1], CC[1][1][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
           [[CC[5][0][0], CC[5][0][1]], [CC[5][1][0], CC[5][1][1]]]]  # yellow
    return cm1

def Frev(CC):
    cm2 = [[[CC[3][0][0], CC[3][0][1]], [CC[0][1][0], CC[0][1][1]]],  # red
           [[CC[1][0][0], CC[4][0][0]], [CC[1][1][0], CC[4][0][1]]],  # orange
           [[CC[2][1][0], CC[2][0][0]], [CC[2][1][1], CC[2][0][1]]],  # white
           [[CC[1][0][1], CC[1][1][1]], [CC[3][1][0], CC[3][1][1]]],  # green
           [[CC[0][0][0], CC[0][0][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
           [[CC[5][0][0], CC[5][0][1]], [CC[5][1][0], CC[5][1][1]]]]  # yellow
    return cm2

def B(CC):
    cm5 = [[[CC[0][0][0], CC[0][0][1]], [CC[3][1][0], CC[3][1][1]]],  # red
           [[CC[4][1][0], CC[1][0][1]], [CC[4][1][1], CC[1][1][1]]],  # orange
           [[CC[2][0][0], CC[2][0][1]], [CC[2][1][0], CC[2][1][1]]],  # white
           [[CC[3][0][0], CC[3][0][1]], [CC[1][0][0], CC[1][1][0]]],  # green
           [[CC[4][0][0], CC[4][0][1]], [CC[0][1][0], CC[0][1][1]]],  # blue
           [[CC[5][0][1], CC[5][1][1]], [CC[5][0][0], CC[5][1][0]]]]  # yellow
    return cm5

def Brev(CC):
    cm6 = [[[CC[0][0][0], CC[0][0][1]], [CC[4][1][0], CC[4][1][1]]],  # red
           [[CC[3][1][0], CC[1][0][1]], [CC[3][1][1], CC[1][1][1]]],  # orange
           [[CC[2][0][0], CC[2][0][1]], [CC[2][1][0], CC[2][1][1]]],  # white
           [[CC[3][0][0], CC[3][0][1]], [CC[0][1][0], CC[0][1][1]]],  # green
           [[CC[4][0][0], CC[4][0][1]], [CC[1][0][0], CC[1][1][0]]],  # blue
           [[CC[5][1][0], CC[5][0][0]], [CC[5][1][1], CC[5][0][1]]]]  # yellow
    return cm6

def L(CC):
    cm7 = [[[CC[5][0][1], CC[0][0][1]], [CC[5][0][0], CC[0][1][1]]],  # red
           [[CC[1][0][0], CC[1][0][1]], [CC[2][1][1], CC[2][1][0]]],  # orange
           [[CC[0][1][0], CC[0][0][0]], [CC[2][1][1], CC[2][0][1]]],  # white
           [[CC[3][0][0], CC[3][0][1]], [CC[3][1][0], CC[3][1][1]]],  # green
           [[CC[4][0][1], CC[4][1][1]], [CC[4][0][0], CC[4][1][0]]],  # blue
           [[CC[1][1][1], CC[1][0][1]], [CC[5][1][0], CC[5][1][1]]]]  # yellow
    return cm7

def Lrev(CC):
    cm8 = [[[CC[2][1][1], CC[0][0][1]], [CC[2][0][1], CC[0][1][1]]],  # red
           [[CC[1][0][0], CC[1][0][1]], [CC[5][0][1], CC[5][1][1]]],  # orange
           [[CC[1][0][1], CC[1][1][1]], [CC[2][0][1], CC[2][1][1]]],  # white
           [[CC[3][0][0], CC[3][0][1]], [CC[3][1][0], CC[3][1][1]]],  # green
           [[CC[4][1][0], CC[4][0][0]], [CC[4][1][1], CC[4][0][1]]],  # blue
           [[CC[0][0][0], CC[0][1][0]], [CC[5][1][0], CC[5][1][1]]]]  # yellow
    return cm8

def R(CC):
    cm12 = [[[CC[0][0][0], CC[2][1][1]], [CC[0][1][0], CC[2][1][0]]],  # red
            [[CC[5][1][1], CC[5][1][0]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[2][0][0], CC[2][0][1]], [CC[1][0][1], CC[1][0][0]]],  # white
            [[CC[3][0][1], CC[3][1][1]], [CC[3][0][0], CC[3][1][0]]],  # green
            [[CC[4][0][0], CC[4][0][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
            [[CC[5][0][0], CC[5][0][1]], [CC[0][1][1], CC[0][0][1]]]]  # yellow
    return cm12

def Rrev(CC):
    cm11 = [[[CC[0][0][0], CC[5][1][1]], [CC[0][1][0], CC[5][1][0]]],  # red
            [[CC[2][1][1], CC[2][1][0]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[2][0][0], CC[2][0][1]], [CC[0][1][1], CC[0][0][1]]],  # white
            [[CC[3][1][0], CC[3][0][0]], [CC[3][1][1], CC[3][0][1]]],  # green
            [[CC[4][0][0], CC[4][0][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
            [[CC[5][0][0], CC[5][0][1]], [CC[1][0][1], CC[1][0][0]]]]  # yellow
    return cm11

def R(CC):
    cm12 = [[[CC[0][0][0], CC[2][1][1]], [CC[0][1][0], CC[2][1][0]]],  # red
            [[CC[5][1][1], CC[5][1][0]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[2][0][0], CC[2][0][1]], [CC[1][0][1], CC[1][0][0]]],  # white
            [[CC[3][0][1], CC[3][1][1]], [CC[3][0][0], CC[3][1][0]]],  # green
            [[CC[4][0][0], CC[4][0][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
            [[CC[5][0][0], CC[5][0][1]], [CC[0][1][1], CC[0][0][1]]]]  # yellow
    return cm12

def Rrev(CC):
    cm11 = [[[CC[0][0][0], CC[5][1][1]], [CC[0][1][0], CC[5][1][0]]],  # red
            [[CC[2][1][1], CC[2][1][0]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[2][0][0], CC[2][0][1]], [CC[0][1][1], CC[0][0][1]]],  # white
            [[CC[3][1][0], CC[3][0][0]], [CC[3][1][1], CC[3][0][1]]],  # green
            [[CC[4][0][0], CC[4][0][1]], [CC[4][1][0], CC[4][1][1]]],  # blue
            [[CC[5][0][0], CC[5][0][1]], [CC[1][0][1], CC[1][0][0]]]]  # yellow
    return cm11

def D(CC):
    cm13 = [[[CC[0][0][0], CC[0][0][1]], [CC[0][1][0], CC[0][1][1]]],  # red
            [[CC[1][1][1], CC[1][0][1]], [CC[1][1][0], CC[1][0][0]]],  # orange
            [[CC[2][0][0], CC[4][1][1]], [CC[2][1][0], CC[4][1][0]]],  # white
            [[CC[3][0][0], CC[2][0][1]], [CC[3][1][0], CC[2][1][1]]],  # green
            [[CC[5][1][1], CC[4][0][1]], [CC[5][1][0], CC[4][0][0]]],  # blue
            [[CC[3][1][1], CC[5][0][1]], [CC[3][0][1], CC[5][0][0]]]]  # yellow
    return cm13

def Drev(CC):
    cm14 = [[[CC[0][0][0], CC[0][0][1]], [CC[0][1][0], CC[0][1][1]]],  # red
            [[CC[1][0][1], CC[1][1][1]], [CC[1][0][0], CC[1][1][0]]],  # orange
            [[CC[2][0][0], CC[3][0][1]], [CC[2][1][0], CC[3][1][1]]],  # white
            [[CC[3][0][0], CC[5][1][0]], [CC[3][1][0], CC[5][0][0]]],  # green
            [[CC[4][0][1], CC[5][0][1]], [CC[4][1][1], CC[5][1][1]]],  # blue
            [[CC[4][1][0], CC[4][0][0]], [CC[5][1][0], CC[5][0][0]]]]  # yellow
    return cm14

def U(CC):
    cm18 = [[[CC[0][1][1], CC[0][0][1]], [CC[0][1][0], CC[0][0][0]]],  # red
            [[CC[1][0][0], CC[1][0][1]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[3][0][0], CC[2][0][1]], [CC[3][1][0], CC[2][1][1]]],  # white
            [[CC[5][1][1], CC[3][0][1]], [CC[5][0][1], CC[3][1][1]]],  # green
            [[CC[4][0][0], CC[2][1][0]], [CC[4][1][0], CC[2][0][0]]],  # blue
            [[CC[5][0][0], CC[4][0][1]], [CC[5][1][0], CC[4][1][1]]]]  # yellow
    return cm18

def Urev(CC):
    cm17 = [[[CC[0][1][0], CC[0][0][0]], [CC[0][1][1], CC[0][0][1]]],  # red
            [[CC[1][0][0], CC[1][0][1]], [CC[1][1][0], CC[1][1][1]]],  # orange
            [[CC[4][1][1], CC[2][0][1]], [CC[4][0][1], CC[2][1][1]]],  # white
            [[CC[2][1][0], CC[3][0][1]], [CC[2][0][0], CC[3][1][1]]],  # green
            [[CC[4][0][0], CC[5][0][1]], [CC[4][1][0], CC[5][1][1]]],  # blue
            [[CC[5][0][0], CC[3][1][0]], [CC[5][1][0], CC[3][0][0]]]]  # yellow
    return cm17

def toPddlState(CC):
    cube1 = '(cube1 ' + CC[0][0][0] + ' ' + CC[2][0][0] + ' ' + CC[4][0][0] + ')'
    cube2 = '(cube2 ' + CC[1][0][0] + ' ' + CC[2][0][1] + ' ' + CC[4][0][1] + ')'
    cube3 = '(cube3 ' + CC[0][0][1] + ' ' + CC[5][0][1] + ' ' + CC[4][1][1] + ')'
    cube4 = '(cube4 ' + CC[1][0][1] + ' ' + CC[5][0][0] + ' ' + CC[4][1][0] + ')'
    
    var_to_append = [cube1, cube2, cube3, cube4]
    return var_to_append

cube_actions = {
    'U': U,
    'Urev': Urev,
    'D': D,
    'Drev': Drev,
    'F': F,
    'Frev': Frev,
    'B': B,
    'Brev': Brev,
    'R': R,
    'Rrev': Rrev,
    'L': L,
    'Lrev': Lrev,

    # For 2x2, you can perform the same action twice to achieve a 180-degree rotation
    'U2': lambda x: U(U(x)),
    'D2': lambda x: D(D(x)),
    'F2': lambda x: F(F(x)),
    'B2': lambda x: B(B(x)),
    'R2': lambda x: R(R(x)),
    'L2': lambda x: L(L(x)),
}



