import java.util.*;
import java.io.*;

class MergeSort{
    static Scanner sc = new Scanner(System.in);
    public static ArrayList<Integer> mergeSort(ArrayList<Integer> array){
        if (array.size() <= 1)
            return array;
        int mid = array.size()/2;
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();
        for (int i = 0;i < mid ; i++) left.add(array.get(i));  
        for (int i = mid;i < array.size() ; i++) right.add(array.get(i));
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }
    public static ArrayList<Integer> merge(ArrayList<Integer> arr1 , ArrayList<Integer> arr2){
        ArrayList<Integer> merged = new ArrayList<>();
        while (arr1.size() > 0 && arr2.size() > 0){
            if(arr1.get(0) < arr2.get(0)){
                merged.add(arr1.get(0));
                arr1.remove(0);
            }else if(arr1.get(0) > arr2.get(0)){
                merged.add(arr2.get(0));
                arr2.remove(0);
            }else{
                merged.add(arr1.get(0));
                merged.add(arr2.get(0));
                arr1.remove(0);arr2.remove(0);
            }
        }
        while (arr1.size()>0){
            merged.add(arr1.get(0));
            arr1.remove(0);
        }
        while (arr2.size()>0){
            merged.add(arr2.get(0));
            arr2.remove(0);
        }
        return merged;
    }
    public static ArrayList<Integer> readFromFile(){
        try{
            ArrayList<Integer> arr = new ArrayList<>();
            System.out.println("Enter the file name (Make sure each elements are in new line): ");
            String fileName = sc.next();
            Scanner sfile = new Scanner(new File(fileName));
            while(sfile.hasNextInt())
                arr.add(sfile.nextInt());
            return arr;
        }catch(Exception e){
            System.out.println(e);   
        }
        return null;
    }
    public static ArrayList<Integer> generateRandomArray(){
        System.out.println("Enter the size of array : ");
        Random r = new Random();
        int size = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0;i<size;i++) arr.add(r.nextInt(1000000));
        return arr;
    }
    public static void printArray(ArrayList<Integer> arr){
        for(int i : arr) System.out.print(i+" ");
        System.out.println();
    }
    public static void main(String[] args) {
        System.out.println("Enter your choice :\n1.Read from file\n2.Randomly generated array ");
        int choice = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        switch(choice){
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
        arr = mergeSort(arr);
        long end = System.nanoTime();
        printArray(arr);
        System.out.println("Time taken : "+(end-start)/1000+" microseconds");
    }
}