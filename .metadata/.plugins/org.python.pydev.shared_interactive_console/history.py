import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import numpy as np
import os
import matplotlib.pyplot as plt
import GradientDescent as GD
data = np.loadtxt('./ex1data1.txt')
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import numpy as np
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.array([1 2 3 4 5 6])
x = np.array([1, 2, 3, 4, 5, 6])
x
y = np.array([10,11,12,13,15,16])
y
z = 2 * x + 3 * y
z
ax = Axes3D(plt.figure(1))
ax.plot3D(xs=x, ys=y,zs=z)
y = np.array([10,11,12,13,14,15])
z
z = 2 * x + 3 * y
ax.plot3D(xs=x, ys=y,zs=z)
ax.plot3D(xs=x, ys=y,zs=z)
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([10,11,12,13,14,15])
z = 2 * x + 3 * y
ax.plot3D(xs=x, ys=y,zs=z)
ax = Axes3D(plt.figure(1))
ax.plot3D(xs=x, ys=y,zs=z)
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import numpy as np
data = np.loadtxt('./ex1data2.txt')
