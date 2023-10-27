import os
import sys
import random
import getopt
import re

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

# for reference
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

############

def toPddlState(CC):
    cube1 = '(cube1 ' + CC[0][0][0] + ' ' + CC[1][0][0] + ' ' + CC[2][0][0] + ')'
    cube2 = '(cube2 ' + CC[0][0][1] + ' ' + CC[1][0][1] + ' ' + CC[3][0][0] + ')'
    cube3 = '(cube3 ' + CC[0][1][0] + ' ' + CC[3][1][0] + ' ' + CC[4][0][0] + ')'
    cube4 = '(cube4 ' + CC[0][1][1] + ' ' + CC[3][1][1] + ' ' + CC[4][0][1] + ')'
    cube5 = '(cube5 ' + CC[5][0][0] + ' ' + CC[1][1][0] + ' ' + CC[2][1][0] + ')'
    cube6 = '(cube6 ' + CC[5][0][1] + ' ' + CC[1][1][1] + ' ' + CC[3][1][1] + ')'
    cube7 = '(cube7 ' + CC[5][1][0] + ' ' + CC[3][0][1] + ' ' + CC[4][1][0] + ')'
    cube8 = '(cube8 ' + CC[5][1][1] + ' ' + CC[3][0][0] + ' ' + CC[4][1][1] + ')'
    
    var_to_append = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8]
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

# check that we dont make suboptimal moves
def check_not_optimal(face, last_face, second_to_last_face):
    # print(face, last_face, second_to_last_face)
    if face == last_face:
        return True
    if face == second_to_last_face:
        if ((face in ['F','B']) and (last_face in ['F', 'B'])) or ((face in ['L', 'R']) and (last_face in ['L', 'R'])) or ((face in ['U', 'D']) and (last_face in ['U', 'D'])):
            return True
    return False

# create random rules to initialise a random state
# uses the check_not_optimal function
def genRandomState(moves_to_shuffle, actions):
    move_list = []
    CC = cubeInit()
    for i in range(moves_to_shuffle):
        move = random.choice(actions)

        if i > 1:
            current_move = move
            last_move = move_list[-1]
            second_to_last_move = move_list[-2]
            while check_not_optimal(current_move[0].upper(), last_move[0].upper(), second_to_last_move[0].upper()):
                move = random.choice(actions)
                current_move = move
        if i > 0:
            last_move = move_list[-1]
            while move[0] == last_move[0]:
                move = random.choice(actions)

        move_list.append(move)
        CC = cube_actions[move](CC)

    return CC, move_list

def toPddl(CC, problem_name):
    init_facts = toPddlState(CC) 
    init = '\n    '.join(init_facts)
    problem_pddl = f'''(define
(problem {problem_name})
(:domain rubiks-cube-2x2)
(:objects yellow white blue green orange red)
(:init
    {init}
)
(:goal
    (and
        (corner1 red white blue)
        (corner2 orange white blue)
        (corner3 red yellow blue)
        (corner4 orange yellow blue)
        (corner5 red white green)
        (corner6 orange white green)
        (corner7 red yellow green)
        (corner8 orange yellow green)
    )
)
)
'''
    return problem_pddl

def generate(moves_to_shuffle, actions):
    CC, gen_actions = genRandomState(moves_to_shuffle, actions)
    pddl = toPddl(CC, 'rubiks-cube-shuffle-{0}'.format(moves_to_shuffle))

    plan_actions = []
    for a in gen_actions[::-1]:
        if a.endswith('rev'):
            plan_actions += [a[:-3]]
        else:
            plan_actions += [a + 'rev']
    plan = '(' + ')\n('.join(plan_actions) + ')\n'
    return pddl, plan

def save_init_pddl(output):
    pddl_content = output[0]   
    with open('init_domain.pddl', 'w') as file:
        file.write(pddl_content)     
    print("The PDDL saved to init_domain.pddl")

def visualize_2x2_cube(pddl_filename):
    with open(pddl_filename, 'r') as file:
        content = file.readlines()
    init_start = content.index("(:init\n") + 1
    init_end = content.index(")\n", init_start)
    init_state = content[init_start:init_end]
    cubes = {}
    for line in init_state:
        cube, *colors = re.findall(r"\w+", line)
        cubes[cube] = colors
    faces = ['U', 'F', 'R', 'L', 'B', 'D']
    for face in faces:
        print(f"Face {face}:")
        if face == 'U':
            print(cubes['cube1'][0], cubes['cube2'][0])
            print(cubes['cube5'][1], cubes['cube6'][1])
        elif face == 'F':
            print(cubes['cube5'][0], cubes['cube6'][0])
            print(cubes['cube7'][1], cubes['cube8'][1])
        elif face == 'R':
            print(cubes['cube2'][2], cubes['cube6'][2])
            print(cubes['cube4'][1], cubes['cube8'][2])
        elif face == 'L':
            print(cubes['cube1'][2], cubes['cube5'][2])
            print(cubes['cube3'][0], cubes['cube7'][2])
        elif face == 'B':
            print(cubes['cube3'][1], cubes['cube4'][0])
            print(cubes['cube7'][0], cubes['cube8'][0])
        elif face == 'D':
            print(cubes['cube3'][2], cubes['cube4'][2])
            print(cubes['cube7'][1], cubes['cube8'][1])
        print()

