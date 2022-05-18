import numpy as np
import math as mh
import random as rd

def activatingFunction(x, ifDerivate = False, type = "sigmoid"):
    if type == "sigmoid":
        if ifDerivate == 0:
            return 1/(1+np.exp(-x))
        else:
            return x*(1-x)
    if type == "none":
        if ifDerivate == 0:
            return x
    if type == "step":
        if x >= 0:
            return 1
        else:
            return 0
    return 0

class NLayer:
    def __init__(self, n, m, type = "sigmoid", firstScatter = 1):
        self.lastLayer = n
        self.layerSize = m
        self.type = type
        self.layer = 2*(np.random.rand(n, m)-0.5)*firstScatter
        self.bias = 2*(np.random.rand(1, m)-0.5)*firstScatter
        self.outputs = np.zeros((1, m))
        self.weightsChanges = np.zeros((n, m))
        self.biasChanges = np.zeros((1, m))
    def excit(self,inputs):
        self.inputs = inputs
        self.outputs = activatingFunction(np.dot(inputs,self.layer) + self.bias,0,self.type)
        return self.outputs
    def updateLayer(self,changeLayer):
        self.layer = self.layer + changeLayer
        self.weightsChanges = changeLayer
    def updateBias(self, changeBias):
        self.bias = self.bias + changeBias
        self.biasChanges = changeBias


class NN:
    def __init__(self,n):
        self.inputs = np.zeros(n)
        self.outputs = np.zeros(n)
        self.lastLayerSize = n
        self.layers = np.array([],dtype=object)
    def showLastResult(self):
        print(self.outputs)
    def newLayer(self,n,type = "sigmoid"):
        a = NLayer(self.lastLayerSize,n,type)
        self.layers = np.append(self.layers,a)
        self.lastLayerSize = n
    def predict(self,inputs):
        self.inputs = inputs
        n = len(self.layers)
        if n==0:
            self.outputs = inputs
        else:
            self.outputs = self.layers[0].excit(inputs)
            if n>1:
                for i in range(1,n):
                    self.outputs = self.layers[i].excit(self.outputs)
    def gradientDescent(self,ideal,E=0,b=0):
        n = len(self.layers)
        delta = (ideal - self.outputs) * activatingFunction(self.outputs, 1, self.layers[n - 1].type)
        grad = np.dot(self.layers[n-1].inputs.transpose(), delta)
        dw = E*grad + b*self.layers[n-1].weightsChanges
        self.layers[n-1].updateLayer(dw)
        dw = E*delta + b*self.layers[n-1].biasChanges
        self.layers[n - 1].updateBias(dw)
        for i in range(1, n):
            x = self.layers[n - i].layer.transpose()
            delta = activatingFunction(self.layers[n-1-i].outputs, 1, self.layers[n-i-1].type) * np.dot(delta, x)
            grad = np.dot(self.layers[n-1-i].inputs.transpose(), delta)
            dw = E * grad + b * self.layers[n-1-i].weightsChanges
            self.layers[n-1-i].updateLayer(dw)
            dw = E * delta + b * self.layers[n-1-i].biasChanges
            self.layers[n-1-i].updateBias(dw)
    def learnGD(self, testingSet, testingSetIdeal, Epohs, E, b):
        x=0
        print("starting learning")
        for i in range(1, Epohs+1):
            n = len(testingSet)
            for j in range(0, n):
                self.predict(testingSet[j])
                self.gradientDescent(testingSetIdeal[j], E, b)
            if (Epohs/i)%10==0:
                print("Learned percent:")
                x = x + 10
                print(x)
        print("done")

if __name__=="__main__":
    n = NN(2)
    n.newLayer(2)
    n.newLayer(1)
    test = np.array([[[1,1]],[[0,1]],[[1,0]],[[0,0]]])
    ideal = np.array([[[0]],[[1]],[[1]],[[0]]])
    n.learnGD(test,ideal,1000,0.7,0.3)
    n.predict([[1,1]])
    n.showLastResult()
    n.predict([[1,0]])
    n.showLastResult()
    n.predict([[0,1]])
    n.showLastResult()
    n.predict([[0,0]])
    n.showLastResult()











