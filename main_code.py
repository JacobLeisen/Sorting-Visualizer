import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

# This function updates the bars on the visual when the new values of the array
def update_bars(arr, bars, highlighted=None):
        for i, (bar, val) in enumerate(zip(bars, arr)):
            bar.set_height(val)
            if highlighted and i in highlighted:
                bar.set_color('red')
            else:
                bar.set_color('blue')

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
    for i in range(current_size-1):
        swapped = False
        for j in range(1, current_size-i):
            swapped_indices = []
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
                swapped_indices.extend([j, j-1])
                update_bars(arr, bars, swapped_indices)
        if not swapped:
            break
    plt.show()

# Classic selection sort
def selection_sort(arr):
    
    for i in range(current_size - 1):
        min_index = i
        swapped_indices = []
        for j in range(i, current_size):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swapped_indices.extend([i, min_index])
        update_bars(arr, bars, swapped_indices)
    plt.show()

# Resets the bars to a new array
def bar_reset():
    global arr
    arr = np.random.randint(1, 100, current_size)
    update_bars(arr, bars)

# Changes the amount of bars
def change_size(num):
    if 0 <= num < len(size_ranges):
        global current_size, current_size_index, bars
        current_size = size_ranges[num]
        current_size_index = num 
        for bar in bars:
            bar.remove()

        bar_width = 0.8  # Adjust as needed
        spacing = 0.1  # Adjust as needed
        total_width = bar_width * current_size + spacing * (current_size - 1)

        # Recreate the bar plot with the new size
        arr = np.random.randint(1, 100, current_size)
        bars = ax.bar(range(current_size), arr, align='center', width=bar_width)
        ax.set_xlim(-0.5, total_width + 5.5)  # Adjust the x-axis limits to fit all bars

        bar_reset()


# Make table parameters
fig, ax = plt.subplots()
# Sizes of array available
size_ranges = [10, 25, 50, 100]
current_size = size_ranges[1]
current_size_index = 1
arr = np.random.randint(1, 100, current_size)
pause_time = 0.01
bars = ax.bar(range(current_size), arr, align='center')
ax.axis("off")
fig.patch.set_facecolor('lightgrey')
ax.set_title("Sort Visualizer")


# Add Button for Bubble Sort
bubble_button_ax = plt.axes([0.01, 0.03, 0.16, 0.075])
bubble_button = Button(bubble_button_ax, "Bubble Sort")
bubble_button.on_clicked(lambda event: sort_button_click(bubble_sort))

# Add Button for Selection Sort
selection_button_ax = plt.axes([0.2, 0.03, 0.16, 0.075])
selection_button = Button(selection_button_ax, "Selection Sort")
selection_button.on_clicked(lambda event: sort_button_click(selection_sort))

# Add Speed Buttons
faster_ax = plt.axes([0.2, 0.9, 0.15, 0.075])
faster_button = Button(faster_ax, "Faster")
faster_button.on_clicked(lambda event: change_speed(0.5))

slower_ax = plt.axes([0.01, 0.9, 0.15, 0.075])
slower_button = Button(slower_ax, "Slower")
slower_button.on_clicked(lambda event: change_speed(2))

# Reset button
reset_ax = plt.axes([0.01, 0.8, 0.15, 0.075])
reset_button = Button(reset_ax, "reset")
reset_button.on_clicked(lambda event: bar_reset())

# Add Size Buttons
bigger_ax = plt.axes([0.64, 0.9, 0.15, 0.075])
bigger_button = Button(bigger_ax, "More Bars")
bigger_button.on_clicked(lambda event: change_size(current_size_index + 1))

smaller_ax = plt.axes([0.84, 0.9, 0.15, 0.075])
smaller_button = Button(smaller_ax, "Less Bars")
smaller_button.on_clicked(lambda event: change_size(current_size_index - 1))


plt.show()



# Add insertion sort



# Make colors change when being selected



