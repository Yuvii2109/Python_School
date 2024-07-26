import numpy as np
import matplotlib.pyplot as plt
section = ['a','b','c','d','e','f']
nofstud = [ 2,34,52,5,5,1]
plt.pie( nofstud,labels= section,autopct="%2.2f%%")
plt.show()
