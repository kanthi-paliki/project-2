import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
n = int(input("Enter no. of data points: "))
for i in range(n):
    x1 = int(input("Enter independent variables: "))
    y1 = int(input("Enter dependent variables: "))
    x.append(x1)
    y.append(y1)
X = sum(x)/n
Y = sum(y)/n

x_val = []
y_val = []
for i in range(n):
    x_val.append( X-x[i])
for i in range(n):
    y_val.append(Y-y[i])

p_xy_val = []
for i in range(n):
    p_xy_val.append(x_val[i]*y_val[i])

sq_x_val = []
for i in range(n):
    sq_x_val.append(x_val[i]*x_val[i])

m = sum(p_xy_val)/sum(sq_x_val)
c = Y-m*X
print("Least Square Method:Best fittest line : Y = ",m,"x +",c)

x = np.linspace(-5,5,100)
y = m*x+c
plt.plot(x,y)
plt.show()