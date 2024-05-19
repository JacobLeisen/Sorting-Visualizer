import matplotlib.pyplot as plt
import numpy as np

def update_bars(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        fig.canvas.draw()
        plt.pause(0.1)

def bubble_sort(arr):
    n = len(arr) 
    bars = ax.bar(range(n), arr, align='center')
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
                update_bars(arr, bars)
    plt.show()



fig, ax = plt.subplots()
ax.axis("off")
arr = np.random.randint(1, 100, 20)
bubble_sort(arr)
    