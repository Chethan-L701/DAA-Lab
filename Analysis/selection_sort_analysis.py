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


n = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
time_taken = []

for i in n:
    arr = [random.randint(0, 1000000) for i in range(i)]
    start = time.time()
    selection_sort(arr)
    end = time.time()
    time_taken.append((end-start)*1000)


print("Selection Sort")
print("No. of elements:\tTime taken in milliseconds")
for i in range(len(n)):
    print(n[i], "\t\t\t", time_taken[i])


plt.title("Selection Sort")
plt.xlabel("Number of elements")
plt.xlim(0, 5500)
plt.ylabel("Time taken in milliseconds(ms)")
plt.plot(n, time_taken)
plt.show()
