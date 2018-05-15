import math
import random


def dist_origin(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2);


def create_point():
    r = random.Random()
    return r.uniform(-1, 1), r.uniform(-1, 1)

# method monte carlo
def estimation_pi(nb_point, rayon):
    count = 0
    for i in range(0, nb_point):
        dis = dist_origin(create_point())
        if dis < rayon:
            count += 1
    return count / nb_point


# mean of number of test


def mean_resulte(nb_test):
    sum = 0.0
    for i in range(0, nb_test):
        sum += estimation_pi(10000, 1)*4
    return sum / nb_test;

# batch means method
def number_test(nb_test):
    for i in range(0, nb_test):
        print(" test numero ", i, " :", estimation_pi(10000, 1)*4)

#estimation_pi(10000, 1)

# number_test(25)

# print(mean_resulte(25))


