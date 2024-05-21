import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

# This function updates the bars on the visual when the new values of the array
def update_bars(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        fig.canvas.draw()
        global pause_time
        plt.pause(pause_time)

# Calls the specific sort on the bars when button is clicked
def sort_button_click(func):
    func(arr)

# Change the speed of the array
def change_speed(multiplier):
    global pause_time 
    pause_time *= multiplier # Make sure changes global variable



# Classic bubble sort
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

# Classic selection sort
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
arr = np.random.randint(1, 100, 50)
n = len(arr) 
pause_time = 0.01
bars = ax.bar(range(n), arr, align='center')
ax.axis("off")
fig.patch.set_facecolor('lightgrey')
ax.set_title("Sort Visualizer")

# Add Button for Bubble Sort
bubble_button_ax = plt.axes([0.01, 0.03, 0.15, 0.075])
bubble_button = Button(bubble_button_ax, "Bubble Sort")
bubble_button.on_clicked(lambda event: sort_button_click(bubble_sort))

# Add Button for Selection Sort
selection_button_ax = plt.axes([0.2, 0.03, 0.15, 0.075])
selection_button = Button(selection_button_ax, "Selection Sort")
selection_button.on_clicked(lambda event: sort_button_click(selection_sort))

# Add Speed Buttons
faster_ax = plt.axes([0.2, 0.9, 0.15, 0.075])
faster_button = Button(faster_ax, "Faster")
faster_button.on_clicked(lambda event: change_speed(0.5))

slower_ax = plt.axes([0.01, 0.9, 0.15, 0.075])
slower_button = Button(slower_ax, "Slower")
slower_button.on_clicked(lambda event: change_speed(2))


plt.show()



# Add insertion sort





# Add Size Buttons



