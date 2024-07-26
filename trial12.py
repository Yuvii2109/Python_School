import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0,10.0,0.1)
a = np.cos(x)
b = np.sin(x)
c = np.tan(x)
plt.plot(x,a,'b')
plt.plot(x,b,'r')
plt.plot(x,c,'k')
plt.show()
