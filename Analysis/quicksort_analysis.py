import random
import matplotlib.pyplot as pyplot
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


n = [0, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
time_taken = []
print("Quicksort")
print("No of Elements\t\tTime in ms")
for i in n:
    arr = [random.randint(0, 100000) for _ in range(i)]
    start = time.time()
    quicksort(arr)
    end = time.time()
    time_taken.append((end - start) * 1000)
    print(i, "\t\t\t", (end - start) * 1000)

pyplot.title("Quicksort")
pyplot.xlabel("No of elements")
pyplot.ylabel("Time in ms")
pyplot.plot(n, time_taken)
pyplot.show()
