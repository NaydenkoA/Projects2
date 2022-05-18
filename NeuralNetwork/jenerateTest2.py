import numpy as np
import random as rd
import math as mh

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

def createMatrix(n,p):
    a = np.zeros((n,n))
    v = [0,1,1,1,1]
    for i in range(0,p):
        z = rd.randint(3, 5)
        x = rd.randint(0,n-1-z)
        y = rd.randint(0,n-1-z)
        a[x][y]=1
        for j in range(1,z):
            for k in range(1,z):
                a[x+j][y+k]=v[rd.randint(0,4)]
    return a

def AddRailing(a,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if a[i][j]==0:
                s1 = a[i-1][j-1]+a[i][j-1]+a[i+1][j-1]
                s2 = a[i-1][j]+a[i][j]+a[i+1][j]
                s3 = a[i-1][j+1]+a[i][j+1]+a[i+1][j+1]
                if s1+s2+s3<=3:
                    a[i][j]=rd.randint(0,1)
    return a

def convert(x):
    a = np.zeros((1,100))
    k = 0
    for i in range(0,10):
        for j in range(0,10):
            a[0][k]=x[i][j]
            k=k+1
    return a

def Precision(test,ideal):
    count = 0
    for i in range(0, 100):
        if test[0][i]>0.5:
            x=1
        else:
            x=0
        if ideal[0][i]==x:
            count=count+1
    return count/100


n = 1000
test = np.zeros((n,1,100))
ideal = np.zeros((n,1,100))
for i in range(0,n):
    x = createMatrix(10,rd.randint(3,4))
    test[i]=convert(AddRailing(x,10))
    ideal[i]=convert(x)
q = NN(100)
q.newLayer(300)
q.newLayer(100)
q.learnGD(test,ideal,1000,0.7,0.3)
x = createMatrix(10,rd.randint(3,4))
q.predict(convert(AddRailing(x,10)))
print(x)
q.showLastResult()
print(Precision(q.outputs,convert(x)))
