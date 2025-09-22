import numpy as np

marks = np.array([80,75,90,85])

print("Max Marks:",marks.max())
print("Min Marks:",marks.min())
print("Average Marks:",marks.mean())

data = np.array([10,20,30,40,50])

print("First 3 elements:",data[:3])
print("Reversed:",data[::-1])
print("Sum:",np.sum(data))
print("Standard Deviation:",np.std(data))