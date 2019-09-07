import numpy as np
a = np.random.randint(1, 21, 15)
print("Array of 15 numbers :\n" , a)
b = a.reshape((3, 5))
print("\nReshaped array in 3*5 :\n" , b)
c = np.amax(b, axis=1).reshape(-1,1)
print(" \nMaximum element of each row \n" , c)
d = np.where(b == np.amax(b, axis=1).reshape(-1,1),0,b)
print("\nMax elements replaced with 0's :\n", d)


