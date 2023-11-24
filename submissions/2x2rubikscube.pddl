(define
    (problem rubiks-cube-shuffle)
    (:domain rubiks-cube-2x2)
    (:objects top bottom left right front back
            white yellow orange red green blue
            top_0 top_1 top_2 top_3
            bottom_0 bottom_1 bottom_2 bottom_3
            left_0 left_1 left_2 left_3
            right_0 right_1 right_2 right_3
            front_0 front_1 front_2 front_3
            back_0 back_1 back_2 back_3
            U R L F B D U’ R’ L’ F’ B’ D’)

    (:predicates
        (at ?t ?c)
        (map ?t ?c)
        (corner ?c1 ?c2 ?c3)
        (adjacent ?f1 ?f2)
        (allowed ?m)
    )

    (:init
        (map top_0 white) (map top_1 white) (map top_2 white) (map top_3 white)
        (map bottom_0 yellow) (map bottom_1 yellow) (map bottom_2 yellow) (map bottom_3 yellow)
        (map left_0 blue) (map left_1 blue) (map left_2 orange) (map left_3 orange)
        (map right_0 green) (map right_1 green) (map right_2 red) (map right_3 red)
        (map front_0 orange) (map front_1 orange) (map front_2 green) (map front_3 green)
        (map back_0 red) (map back_1 red) (map back_2 blue) (map back_3 blue)

        (adjacent top left) (adjacent top right) (adjacent top front) (adjacent top back)
        (adjacent left back) (adjacent left front) (adjacent left bottom)
        (adjacent right back) (adjacent right front) (adjacent right bottom)
        (adjacent front bottom) (adjacent front back)
        (adjacent back bottom)
    )

    (:goal
        (and
            (map top_0 white) (map top_1 white) (map top_2 white) (map top_3 white)
            (map bottom_0 yellow) (map bottom_1 yellow) (map bottom_2 yellow) (map bottom_3 yellow)
            (map left_0 orange) (map left_1 orange) (map left_2 orange) (map left_3 orange)
            (map right_0 red) (map right_1 red) (map right_2 red) (map right_3 red)
            (map front_0 green) (map front_1 green) (map front_2 green) (map front_3 green)
            (map back_0 blue) (map back_1 blue) (map back_2 blue) (map back_3 blue)

            (corner red white blue)
            (corner orange white blue)
            (corner red yellow blue)
            (corner orange yellow blue)
            (corner red white green)
            (corner orange white green)
            (corner red yellow green)
            (corner orange yellow green)

            (adjacent top left) (adjacent top right) (adjacent top front) (adjacent top back)
            (adjacent left back) (adjacent left front) (adjacent left bottom)
            (adjacent right back) (adjacent right front) (adjacent right bottom)
            (adjacent front bottom)
            (adjacent back bottom)
        )
    )

    (:action rotate
        :parameters (?t1 ?t2 ?t3 ?t4 ?m)
        :precondition (and
            (at t1 t1)
            (at t2 t2)
            (at t3 t3)
            (at t4 t4)
            (adjacent t1 t2)
            (adjacent t2 t3)
            (adjacent t3 t4)
            (adjacent t4 t1)
            (allowed m)
        )
        :effect (and
            (at t1 t2)
            (at t2 t3)
            (at t3 t4)
            (at t4 t1)
        )
    )

    (:action rotate_inverse
        :parameters (?t1 ?t2 ?t3 ?t4 ?m)
        :precondition (and
            (at t1 t1)
            (at t2 t2)
            (at t3 t3)
            (at t4 t4)
            (adjacent t1 t4)
            (adjacent t2 t1)
            (adjacent t3 t2)
            (adjacent t4 t3)
            (allowed m)
        )
        :effect (and
            (at t1 t4)
            (at t2 t1)
            (at t3 t2)
            (at t4 t3)
        )
    )
)