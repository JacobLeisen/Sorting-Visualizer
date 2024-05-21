import matplotlib.pyplot as plt
import numpy as np

def update_bars(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        fig.canvas.draw()
        plt.pause(0.01)

def bubble_sort(arr):
    for i in range(n-1):
        swapped = False
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
                update_bars(arr, bars)
        if not swapped:
            break
    plt.show()

# Add selection sort
def selection_sort(arr):
    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        update_bars(arr, bars)
    plt.show()


# Make table parameters
fig, ax = plt.subplots()
arr = np.random.randint(1, 100, 10)
n = len(arr) 
bars = ax.bar(range(n), arr, align='center')
ax.axis("off")
fig.patch.set_facecolor('lightgrey')
ax.set_title("Sort")
bubble_sort(arr)









# Add insertion sort

# Add Button to pick which sort and update title

# Add Speed Buttons

# Add Size Buttons



