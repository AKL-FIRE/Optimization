import numpy as np
import matplotlib.pyplot as plt
def GradientDescent(x,y,theta,bias,alpha,epsilon,count=1000):
    k=0
    J = []
    J.append(CalculateJ(x,y, theta,bias))
    while k <= count and J[k] >= epsilon:
        d1,d2 = CalculateDerivative(x,y, theta, bias)
        theta = theta + alpha * -d1
        bias = bias + alpha * -d2
        k = k + 1
        J.append(CalculateJ(x,y, theta,bias))
    plt.figure(2)
    plt.plot(range(k+1),J)
    plt.title('The cost function J(_theta)')
    plt.xlabel('iterator')
    plt.ylabel('J(_yheta)')
    return [theta,bias]

def CalculateH(x,theta,bias):
    return theta.transpose().dot(x) + bias;

def CalculateJ(x,y,theta,bias):
    length = x.shape[1]
    return (1.0 / (2.0 * length)) * np.sum((CalculateH(x, theta,bias) - y) ** 2,axis=1)

def CalculateDerivative(x,y,theta,bias):
    return (CalculateJ(x,y, theta+1e-5, bias) - CalculateJ(x,y, theta-1e-5, bias)) / 2e-5 , (CalculateJ(x,y, theta, bias+1e-5) - CalculateJ(x,y, theta, bias-1e-5)) / 2e-5