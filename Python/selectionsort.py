import random
import time


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def selectionSort(arr):
    for i in range(len(arr)):
        print("\rProgress  : {}%".format(((i+1)*100)/len(arr)), end="")
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


n = int(input("Enter the number of elements: "))
ch = int(input(
    """
    Enter the choice:
    1.Fill the array randomly
    2.Fill the array with user input
    =>
    """
))

if ch == 1:
    print("The array is being filled randomly...")
    upper = int(input("Enter the Upper limit: "))
    arr = [random.randint(1, upper) for i in range(n)]
else:
    print("Enter the elements: ")
    arr = [int(input("arr[{}] = ".format(i))) for i in range(n)]
print("The array is : ")
printArray(arr)
print("The array is being sorted...")
start = time.time()
sorted_arr = selectionSort(arr)
end = time.time()
print("\nThe sorted array is : ")
printArray(sorted_arr)
print("The time taken to sort {} elements is {} ms"
      .format(n, (end - start)*1000))
