# use Monte Carlo method to calculate pi
def calc_pi(points_n):
    import random
    import math
    # randomly generate n points on a square
    point_in = 0.0

    random.seed(a=1)
    for i in range(1, points_n+1):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x**2+y**2)
        if dist <= 1.0:
            point_in += 1

    pi = 4 * (point_in/points_n)
    print(pi)

calc_pi(10000)
calc_pi(100000)
calc_pi(1000000)
calc_pi(10000000)
calc_pi(100000000)
