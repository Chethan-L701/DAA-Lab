import random
import time
import matplotlib.pyplot as plt


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


n = [0, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
time_taken = []

print("No. of elements:\tTime taken in milliseconds")
for i in n:
    arr = [random.randint(0, 1000000) for i in range(i)]
    start = time.time()
    selection_sort(arr)
    end = time.time()
    time_taken.append((end-start)*1000)
    print(i, "\t\t\t", (end-start)*1000)

plt.title("Selection Sort")
plt.xlabel("Number of elements")
plt.xlim(0, 10000)
plt.ylabel("Time taken in milliseconds(ms)")
plt.plot(n, time_taken)
plt.show()
