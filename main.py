from lsystem import lsystem
from output import run_turtle


def main():
    # # Coch Curve
    # rules = {
    #         'F': 'F+F-F-FF+F+F-F',
    # }
    # my_res = lsystem('F+F+F+F', rules=rules, limit=3)
    # run_turtle(my_res, angle=90, step=5.0, pos=(0, 0))

    # Tree
    rules = {
            'B': 'A[+B][-B]AB',
            'A': 'AA'
    }
    my_res = lsystem('B', rules=rules, limit=3)
    run_turtle(my_res, angle=45, step=7.0, pos=(0, -400))

    # # Sticks
    # rules = {
    #         'F': 'FF',
    #         'X': 'F[+X]F[-X]+X'
    # }
    # my_res = lsystem('X', rules=rules, limit=6)
    # run_turtle(my_res, angle=20, step=5.0, pos=(0, -400))

    # # Crystal
    # rules = {
    #         'F': 'FF+F++F+F',
    # }
    # my_res = lsystem('F+F+F+F', rules=rules, limit=5)
    # run_turtle(my_res, angle=90, scale=1.0, pos=(350, -375))

    # Mine Spiral
    rules = {
            'F': 'F+>F'
    }
    my_res = lsystem('F', rules=rules, limit=10)
    run_turtle(my_res, angle=15, step=2.0, scale=1.006, pos=(0, 0))

    # # Mine flower
    # rules = {
    #         'H': 'F++F++F++F++F++F-----H'
    # }
    # my_res = lsystem('H', rules=rules, limit=12)
    # run_turtle(my_res, angle=30, step=50.0, scale=1.02, pos=(0, 0))

    # print(my_res)


if __name__ == '__main__':
    main()
