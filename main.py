'''
This program test the Perceptron class.
The goal is to predict which points are above or under a random line
generated with a method.
'''

from random import random, randint
from perceptron import Perceptron
import numpy as np


'''
This method generates a random line.
'''
def generate_line() -> tuple[int,int]:
    m = randint(-100,100)
    q = randint(-100,100)
    return (m,q)

'''
This method generate random points, that you can use as data 
for training and testing, given in input a line's equation and
the num of points.
'''
def generate_points_and_targets(m: int, q: int, num_points: int) -> tuple[list[tuple[int,int]],list[int]]:
    # 0 if is above
    # 1 is is under
    points = []
    targets = []
    
    for _ in range(num_points):

        # This is the random point
        x = randint(-1000,1000) * random()
        y = randint(-1000,1000) * random()

        # Y value in the line associeted with the x generated before
        y_ = x*m + q 

        # Code to see if the point is above or under the line.
        if y - y_ >= 0: 
            points.append((x,y))
            targets.append(0) # Is above
        else:  
            points.append((x,y))
            targets.append(1) # Is down
    

    return (points,targets)
        
if __name__ == '__main__':  
    m, q = generate_line()

    num_points = 100

    # Code to generate the training data.
    points, targets = generate_points_and_targets(m,q,num_points)

    perceptron = Perceptron()

    perceptron.fit(np.array(points),targets)

    # Here i generate the new points that i will use to check the 
    # performance of the perceptron.
    new_points, new_targets = generate_points_and_targets(m,q,num_points)

    result = perceptron.predict(new_points)

    correct_answers = 0
    
    # Loop to see which answers are corrected.
    for i in range(len(result)):
        print("OUTPUT:" + str(result[i]) + "| EXPECTED:" + str(new_targets[i]))
        if result[i] == new_targets[i]: correct_answers += 1
        else: print("ERROR!")

    print("ACCURACY: " + str((correct_answers * 100) / num_points) + "%")