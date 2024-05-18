import matplotlib.pyplot as plt
import numpy as np
import time

# Make array for sort
arr = np.random.randint(1, 100, 20)

# Make table design
fig, ax = plt.subplots()
ax.bar(range(len(arr)), arr, color="blue")
ax.axis("off")
plt.title("Bubble Sort")
plt.show()
