import java.util.*;

class SelectionSort {
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
    public static int[] selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print("\rProgress : "+((i+1)*100.0)/arr.length+"%");
            int min = i;
            for (int j = i + 1; j < arr.length; j++)
                if (arr[j] < arr[min]) min = j;
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
        return arr;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("Enter the size of array : ");
        int n = sc.nextInt();
        System.out.println("Enter your choice : \n1.Fill the Array Randomly \n2.Fill the Array Manually");
        System.out.print("=>");
        int choice = sc.nextInt();
        int[] arr = new int[n];
        if (choice == 1) {
            System.out.println("The array is being filled randomly...");
            System.out.println("Enter the upper bound of array : ");
            int upperBound = sc.nextInt();
            for (int i = 0; i < n; i++)
                arr[i] = rand.nextInt(upperBound);
            System.out.println("The array is :");
            printArray(arr);
        }else if (choice == 2) {
            System.out.println("The array is being filled manually...");
            System.out.println("Enter the array elements : ");
            for (int i = 0; i < n; i++)
                arr[i] = sc.nextInt();
            System.out.println("The array is :");
            printArray(arr);
        }
        System.out.println("Sorting the array...");
        long start = System.nanoTime();
        int [] sortedArr = selectionSort(arr);
        long end = System.nanoTime();
        System.out.println("\nThe sorted array is :");
        printArray(sortedArr);
        System.out.println("Time taken to sort " + n + " elements: " + (end - start) + " ns");
        sc.close();
    }
}
