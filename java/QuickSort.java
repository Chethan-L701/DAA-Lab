import java.io.*;
import java.util.*;

public class QuickSort {

    static Scanner sc = new Scanner(System.in);
    public static ArrayList<Integer> quickSort(ArrayList<Integer> arr) {
        if (arr.size() <= 1) {
            return arr;
        }
        int pivot = arr.get(0);
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();
        ArrayList<Integer> mid = new ArrayList<>();
        for (int val : arr) {
            if (val < pivot) {
                left.add(val);
            } else if (val > pivot) {
                right.add(val);
            } else {
                mid.add(val);
            }
        }
        ArrayList<Integer> res = new ArrayList<>();
        res.addAll(quickSort(left));
        res.addAll(mid);
        res.addAll(quickSort(right));
        return res;
    }
    public static ArrayList<Integer> readFromFile() {
        try {
            ArrayList<Integer> arr = new ArrayList<>();
            System.out.println(
                    "Enter the file name (Make sure each elements are in new line): ");
            String fileName = sc.next();
            Scanner sfile = new Scanner(new File(fileName));
            while (sfile.hasNextInt()) {
                arr.add(sfile.nextInt());
            }
            return arr;
        } catch (Exception e) {
            System.out.println(e);
        }
        return null;
    }

    public static ArrayList<Integer> generateRandomArray() {
        System.out.println("Enter the size of array : ");
        Random r = new Random();
        int size = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            arr.add(r.nextInt(1000000));
        }
        return arr;
    }

    public static void printArray(ArrayList<Integer> arr) {
        for (int i : arr)
            System.out.print(i + " ");
        System.out.println();
    }
    public static void main(String[] args) {
        System.out.println(
                "Enter your choice :\n1.Read from file\n2.Randomly generated array ");
        int choice = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        switch (choice) {
            case 1:
                arr = readFromFile();
                break;
            case 2:
                arr = generateRandomArray();
                break;
            default:
                System.out.println("Invalid choice");
                break;
        }
        System.out.println("The array is  : ");
        printArray(arr);
        System.out.println("Sorted array is : ");
        long start = System.nanoTime();
        arr = quickSort(arr);
        long end = System.nanoTime();
        printArray(arr);
        System.out.println("Time taken : " + (end - start) / 1000 +
                " microseconds");
    }
}
