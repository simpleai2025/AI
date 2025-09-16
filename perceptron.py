import numpy as np
from random import uniform

'''
This class represent a simple perceptron.
'''
class Perceptron:

    def __init__(self, learning_rate = 0.01, num_iteration = 1000) -> None:
        # Here i create the perceptron
        self.learning_rate = learning_rate
        self.num_iteration = num_iteration
        self.act_func = self.step_func
        self.weights = None
        self.bias = None

    '''
    This method is for training the perceptron, given in input:
    X: numpy array that contains the training data.
    y: array that contains the target training data.
    '''
    def fit(self,X,y) -> None:
        _, n_features = X.shape # Shape gives in output the num of rows and columns.

        self.weights = np.array([uniform(-1,1) for _ in range(n_features)])
        self.bias = 0

        # To be sure that in the targets there are only 0 and 1 as output.
        y_ = np.array([1 if x > 0 else 0 for x in y])

        for _ in range(self.num_iteration):
            for idx,xi in enumerate(X):
                # Here there is the moltiplication beetween the weights and the relative 
                # values in xi.
                #All the results are added together.
                #At the end bias is added to the result that is stored in linear_output.
                linear_output = np.dot(xi,self.weights) + self.bias 

                # In y_predicted there are the results of the model's prediction
                y_predicted = self.act_func(linear_output)

                # This is the formula about how to train a perceptron and
                # find the correct weights.
                update = self.learning_rate * (y_[idx] - y_predicted) 
                self.weights += update * xi
                self.bias += update

    '''
    In this method perceptron does a prediction, given in input:
    X: new data
    '''
    def predict(self,X):
        linear_output = np.dot(X,self.weights) + self.bias
        return self.act_func(linear_output)

    '''
    This function return an array with only 0 and 1, given in input an array.
    '''
    def step_func(self,x):
        return np.where(x >= 0, 1, 0)
    


        