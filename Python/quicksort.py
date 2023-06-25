import random
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def print_arr(arr):
    for i in arr:
        print(i, end=" ")
    print()


ch = int(input(
    "Enter your choice:\n1.Read from file\n2.Generate random array\n=>"
))
if ch == 1:
    filename = input("Enter file name: ")
    with open(filename, 'r') as f:
        arr = [int(x) for x in f.read().split()]
elif ch == 2:
    n = int(input("Enter number of elements: "))
    arr = [random.randint(0, 100000000) for _ in range(n)]
else:
    print("Invalid choice")

print("The array is : ")
print_arr(arr)
start = time.time()
sorted_arr = quicksort(arr)
end = time.time()
print("The sorted array is : ")
print_arr(sorted_arr)

print("The timetaken to sort array of {} elements is {} ms"
      .format(n, (end - start)*1000))
