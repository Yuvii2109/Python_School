import numpy as np
import matplotlib.pyplot as plt
year =np.array([2015,2016,2017,2018,2019])
gper = np.array([78,90,89,79,85])
bper = np.array([65,87,92,87,90])
plt.plot(year,gper,color="b",linewidth=2,linestyle='dashdot',marker='s')
plt.plot(year,bper,color="r",linewidth=2,linestyle='dashdot',marker='s')
plt.title("Year wise percentage")
plt.ylabel("Percentage")
plt.xlabel("Year")
plt.show()
