#!/usr/local/bin/python2.7
#-*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import GradientDescent3d as GD
from mpl_toolkits.mplot3d import Axes3D
##############数据归一化#######################
data = np.loadtxt('./ex1data2.txt')
data[:,0] = (data[:,0] - min(data[:,0])) / (max(data[:,0]) - min(data[:,0]))
data[:,2] = (data[:,2] - min(data[:,2])) / (max(data[:,2]) - min(data[:,2]))
##############读取文件内容并显示################
ax = Axes3D(plt.figure(1))
ax.scatter(data[:,0], data[:,1], data[:,2])
plt.title('The data Distribution')
print('The matrix dimension is:',data.shape)
#############初始化拟合直线#########
theta = np.random.rand(2,1)
bias = np.random.rand(1,1)
x1, x2 = np.meshgrid(data[:,0],data[:,1])
z = x1 * theta[0] + x2 * theta[1] + bias
ax.plot_surface(x1, x2, z, rstride=1, cstride=1, cmap='Greens')
#############进行拟合##############
x = np.column_stack([data[:,0],data[:,1]])
theta,bias = GD.GradientDescent(x.transpose(), data[:,2].transpose().reshape(1,47), theta, bias, 0.001, 0.001, 10000)
#############画出拟合后的结果#######
plt.figure(1)
z = x1 * theta[0] + x2 * theta[1] + bias
ax.plot_surface(x1, x2, z, rstride=1, cstride=1, cmap='Blues')
plt.show()