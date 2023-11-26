
# import pandas as pd
# import matplotlib.pyplot as plt

# def bubble_sort(arr):
#     global iterations
#     iterations = 1
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 print(arr)
#                 iterations = iterations + 1
#     return iterations

# # # Test the correctness
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array is:", arr)
# print(iterations)




# Create a DataFrame to store array sizes and corresponding iterations



import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    global bubble_iterations
    bubble_iterations = 1
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                bubble_iterations = bubble_iterations + 1
    return bubble_iterations


def selection_sort_iterations(arr):
    n = len(arr)
    selection_iterations = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            selection_iterations += 1
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return selection_iterations




# Create a DataFrame to store array sizes and corresponding iterations
data = {'Array Size': [], 'selection_Iterations': [], 'bubble_iterations': []}

# Perform selection sort for array sizes from 1 to 100
for size in range(1, 21):
    test_array = list(range(size, 0, -1))  # Reverse sorted array for worst-case scenario
    selection_iterations = selection_sort_iterations(test_array)
    
    data['Array Size'].append(size)
    data['selection_Iterations'].append(selection_iterations)

for size in range(1, 21):
    test_array = list(range(size, 0, -1))  # Reverse sorted array for worst-case scenario
    bubble_iterations = bubble_sort(test_array)
    
    #data['Array Size'].append(size)
    data['bubble_iterations'].append(bubble_iterations)


df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Define input sizes
input_sizes = range(1, 101)

# Calculate bubble sort iterations
bubble_sort_iterations = []
for n in input_sizes:
    array = list(range(n, 0, -1))  # Reverse sorted array
    swapped = True
    iterations = 0
    while swapped:
        swapped = False
        for j in range(n - iterations - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        iterations += 1
    bubble_sort_iterations.append(iterations)

# Calculate selection sort iterations
selection_sort_iterations = []
for n in input_sizes:
    array = list(range(n, 0, -1))  # Reverse sorted array
    iterations = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        iterations += 1
    selection_sort_iterations.append(iterations)

# Plot the graph
plt.plot(input_sizes, bubble_sort_iterations, label='Bubble Sort')
plt.plot(input_sizes, selection_sort_iterations, label='Selection Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Iterations')
plt.title('Comparison of Bubble Sort and Selection Sort Iterations')
plt.legend()
plt.grid(True)
plt.show()
