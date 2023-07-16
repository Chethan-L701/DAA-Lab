import time
import random

def mergesort(uarr: list) -> list :
    if len(uarr) <= 1:
        return uarr;
    mid: int = len(uarr)//2
    return merge(mergesort(uarr[:mid]), mergesort(uarr[mid:]))

def merge(arr1: list, arr2: list) -> list :
    i: int = 0
    j: int = 0
    merged: list = []

    while (j < len(arr2)) and (i < len(arr1)) :
        if arr1[i] == arr2[j] :
            merged = merged + [arr1[i],arr2[j]]
            j+=1
            i+=1
        elif arr1[i] < arr2[j] :
            merged = merged + [arr1[i]]
            i+=1
        else:
            merged = merged + [arr2[j]]
            j+=1
    if i < len(arr1) :
        merged = merged + arr1[i:]
    if j < len(arr2) :
        merged = merged + arr2[j:]
    
    return merged


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
sorted_arr = mergesort(arr)
end = time.time()
print("The sorted array is : ")
print_arr(sorted_arr)

print("The timetaken to sort array of {} elements is {} ms"
      .format(n, (end - start)*1000))
