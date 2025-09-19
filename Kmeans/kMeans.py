import random
import math
import matplotlib.pyplot as plt
import numpy as np

'''
Method to generate unlabel data randomly, given the
number of points.
'''
def generate_unlabeled_data(num_points):
    
    #key = (x,y)
    #values = (x,y) coordinates of the centroid
    X = {}

    for _ in range(num_points):
        # x and y between -100 and 100
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        X[(x,y)] = tuple()
    
    return X

'''
Method to calculate the centroid closest to the point given in input.
'''
def calculate_centroid(point,centroids):

    x,y = point

    #sort the centroids list based on the euclidean distance between the centroids and the point
    centroid = sorted(centroids,key= lambda c : math.sqrt((c[0]-x)**2 + (c[1]-y)**2))[0]
    
    return centroid
   

'''
Method to generate k centroids.
'''
def generate_centroid(k):

    centroids = []

    for _ in range(k):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        while (x,y) in centroids:
            # Two centroids can't have the same coordinate
            x = random.randint(-100,100)
            y = random.randint(-100,100)
        centroids.append((x,y))
    
    return centroids

'''
Method to recalculate the coordinates of the centroids based
on the middle value of the points associated with that cluster.
'''
def recalculate_centroid(centroid,cluster):

    if cluster == []:
        return centroid

    sx = sum([x for x,_ in cluster])
    sy = sum([y for _,y in cluster])
    
    return (round(sx/len(cluster),2),round(sy/len(cluster),2))

'''
Method to find the points closest to the centroid given in input.
'''
def calculate_cluster(centroid,X):
    
    cluster =  []

    for point in X:
        if X[point] == centroid:
            cluster.append(point)
    
    return cluster

'''
This method return the sum of all the euclidean distance between the points
and the centroid associeted with them. At the end the sum is divided by the number
of points in the training set.
'''
def calculate_error(X):

    error = 0

    for point,cluster in X.items():
        x, y = point
        x2,y2 = cluster
        error += math.sqrt((x2-x)**2 + (y2-y)**2)
    
    return round(error/len(X),2)






'''
This method implements the k-means algorithm.
k: number of centroids
X: training set
'''
def k_means(k,X):

    centroids = generate_centroid(k) 

    while True:

        #To stop the loop if the training is over.
        old_X = {point:X[point] for point in X}

        for point in X:
            X[point] = calculate_centroid(point,centroids)

        #I stop when the centroids associeted with the points are not changed.
        if old_X == X:
            break
        
        for i in range(len(centroids)):
            cluster = calculate_cluster(centroids[i],X)
            centroids[i] = recalculate_centroid(centroids[i],cluster)

        print(calculate_error(X))
    

    return X, centroids
        
    
    



if __name__ == '__main__':

    k = 5
    num_points = 50

    X = generate_unlabeled_data(num_points)
    X,centroids = k_means(k,X)


    #Code to visualize the clusters and the points in a diagram.
    #Every cluster is associated to a number.

    x_points = np.array([point[0] for point in X])
    y_points = np.array([point[1] for point in X])

    x_centroids = np.array([x for x,_ in centroids])
    y_centroids = np.array([y for _,y in centroids])


    plt.plot(x_points, y_points, 'o')
    plt.plot(x_centroids, y_centroids, 'o',color="red")

    c = 1
    for centroid in centroids:
        plt.annotate(str(c),xy = centroid)
        for point in X:
            if X[point] == centroid:
                plt.annotate(str(c),xy = point)
        c += 1
        


    plt.show()




