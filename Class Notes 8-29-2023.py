import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hi there!")

#we need to write a code to import matplotlib. 

#1. Create a virtual envrionment , open terminal and type this, py -3 -m venv #then name it what you want 
#2. Activate the virtual environment .name - \recapvenv\Scripts\activate
#.3 Install the third part libraries. example ##pip3 install matplotlib