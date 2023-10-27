(define
(problem rubiks-cube-shuffle-10)
(:domain rubiks-cube-2x2)
(:objects yellow white blue green orange red)
(:init
    (cube1 blue yellow orange)
    (cube2 yellow blue blue)
    (cube3 white blue red)
    (cube4 green orange red)
    (cube5 blue green yellow)
    (cube6 orange yellow orange)
    (cube7 red red green)
    (cube8 white blue yellow)
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