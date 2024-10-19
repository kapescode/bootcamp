import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,2,3,8,4,10,2.5])
plt.plot(ypoints, 'o:r')
#The o represents the data points will be marked with a circle (square, diamond, x, *). 
#The - represents a line that is connecting the data points. : for dotted line, -- for dashes or -. for dash dotted
#The r represents the colour red

plt.show()




