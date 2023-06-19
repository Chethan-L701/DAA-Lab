import random
import time
import matplotlib.pyplot as plt


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


n = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
time_taken = []

for i in n:
    list = [random.randint(0, 1000000) for i in range(i)]
    start = time.time()
    selection_sort(list)
    end = time.time()
    time_taken.append((end-start)*1000)
plt.title("Selection Sort")
plt.xlabel("Number of elements")
plt.xlim(0, 5000)
plt.ylabel("Time taken in milliseconds(ms)")
plt.plot(n, time_taken)
plt.show()
