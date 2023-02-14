import numpy 
import time 
 
# Creating array object
"""
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]] )
print(arr)

"""
x=numpy.random.rand(1000000000)
start=time.time()
mean_np=numpy.mean(x)
print(time.time()-start)