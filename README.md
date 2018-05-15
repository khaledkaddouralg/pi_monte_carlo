# estimation of pi use monte carlo method

# algorithme:

step 1: initialize a counter with 0
step 2: for 1 to number of point (ex : 20000):
            create point p(x, y) uniformly (x and y in[-1, 1])
            calculate the distance from origin
            if the distanc < rayon increment the value of the counter by 1
step 3: divide the counter on the number of point
step 4: the result obtained is pi/4 so we must multiply by 4 to obtain pi
