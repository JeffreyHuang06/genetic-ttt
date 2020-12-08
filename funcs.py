import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))
    # return np.tanh(x)

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))
    # return 1 - sigmoid(x)**2
    
def ReLU(x):
    return x * (x > 0)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
