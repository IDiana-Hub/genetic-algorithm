import math
import random
import matplotlib.pyplot as plt
def ar(i,N):
    if i<0: return N+i
    if i>=N: return i-N
    return i
def reproduction(X): 
    B=[]
    for i in range(20):
        B.append([])
        for j in range(100):
            B[i].append((X[i][j]+X[ar(i-1, 20)][j])/2)
    return B
def select(X):
    global Y, Min, Hmin
    B=[]
    n=0; hmin=100; h=[]; Nhmin=0
    for i in range(40):
        h.append(0)
        for j in range(100):
            h[i] += math.fabs(Y[j]-X[i][j])
        if(h[i]<hmin):
            hmin=h[i]
            Nhmin=i
        if h[i]<Hmin: Hmin=h[i]  
    for i in range(20):
        B.append(X[Nhmin])
        h[Nhmin]+=100
        hmin=100
        for j in range(40):
            if(h[j]<hmin):
                hmin=h[j]
                Nhmin=j
    Min.append(B[0])
    return B
def mutation(X,n):
    N=random.randint(0,20)
    M=random.randint(0,100)
    for i in range(N):
        d = random.randint(-5,5)
        for j in range(M):
            X[ar(i+d, 20)][ar(j+d,100)]+=d/n
    return X
        

X=[]; Y=[]; Min=[]; x=[]; Hmin=100
#создание первого поколения
for i in range(20):
    X.append([])
    for j in range(100):
        X[i].append(random.random()*3)
for j in range(100):
    Y.append(1+math.sin(j*0.1))
    x.append(j*0.1)
i=0
N=random.randint(0,20)
M=random.randint(0,100)
while (Hmin>25)and(i<500):
    i+=1
    X+=reproduction(X)
    X=select(X)
    X=mutation(X,i)
print(i, Hmin)
plt.figure(1)
plt.plot(x, Y, color="red")
for n in range(i):
    plt.plot(x, Min[n])
plt.figure(2)
plt.plot(x, Y, color="red")
plt.plot(x, Min[i-1])
plt.show()
