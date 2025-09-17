from random import random,randint
from math import sqrt

'''
Method that generate a dataset that contains points coordinates.
P = (x,y,z) where z is the quadrant number that contains the point.
'''
def generate_dataset(num_points: int) -> list[tuple[float,float,int]]:

    points = []

    for _ in range(num_points):

        #Code to generate the points
        x = randint(-100, 100) + random()
        y = randint(-100, 100) + random()

        #Code to calculate the quadrant number
        if x > 0 and y < 0: points.append((x, y, 4))
        elif x < 0 and y < 0: points.append((x, y, 3))
        elif x < 0 and y > 0: points.append((x, y, 2))
        else: points.append((x, y, 1))

    
    return points

'''
This method return the euclidean distance between two points given in input.
'''
def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

'''
This method implents the nearest neighbour algorithm.
X: training data
point: (x,y) used to predict the quadrant number
'''
def nearest_neighbour(X: list[tuple[float,float,int]], point: tuple[float,float]) -> int:
    x_point, y_point = point
    #List that contains all the euclidean distance between the point given in input
    #and the points in the training dataset.
    #Each element of the list is a tuple, where the first element is the distance
    #and the second is the quadrant number of the point in the dataset used to calculate
    #the euclidean distance.
    distance_list = [(euclidean_distance(x, y, x_point, y_point), z) for x, y, z in X]
    #Here i sort the distance list considering only the euclidean distance.
    #After the sort, a return the quadrant number of the first element in
    #the sorted list. That is the quadrant number of the cloaset dataset point 
    #to the point given in input.
    return sorted(distance_list, key = lambda e: e[0])[0][1]

def k_nearest_neighbour(X: list[tuple[float,float,int]], point: tuple[float,float], k = 5) -> int:
    x_point, y_point = point
    #Same code as the nearest_neighbour version.
    distance_list = [(euclidean_distance(x, y, x_point, y_point),z) for x, y, z in X]
    #Here i take the k points closest to the point given in input.
    kdistance_list = sorted(distance_list, key = lambda e: e[0])[0:k]
    #Here i have all the quadrant number of the k points taken before.
    #I will use it to calculate the most recurring quadrant number in that k points.
    output_list = [e[1] for e in kdistance_list]
    #Code to return the most recurring quadrant number 
    return max(kdistance_list, key = lambda e : output_list.count(e[1]))[1]

    


if __name__ == '__main__':

    points = generate_dataset(10000)
    
    point = (0.5,-0.5)

    print(nearest_neighbour(points, point))
    print(k_nearest_neighbour(points, point))

        
