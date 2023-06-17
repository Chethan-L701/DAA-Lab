#include <iostream>
#include <random>
#include <chrono>
void selection_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        std::cout << "\rProgress : " << ((i+1)*100.0)/n << "%";
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min]) min = j;
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}
void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << " ";
    std::cout << std::endl;
}
int main () {
    srand(time(0));
    int n, choice;
    std::cout << "Enter number of elements: ";
    std::cin >> n;
    int arr[n];
    std::cout << "Enter your choice : \n1.Fill the Array Randomly \n2.Fill the Array Manually\n=>";
    std::cin >> choice;
    if (choice == 1) {
        std::cout << "The array is being filled randomly...\n";
        std::cout << "Enter the upper limit of the array:";
        int upper_limit;
        std::cin >> upper_limit;
        for (int i = 0; i < n; i++)
            arr[i] = rand() % upper_limit;
    }else{
        std::cout << "The array is being filled manually...\n";
        std::cout << "Enter the elements: ";
        for (int i = 0; i < n; i++)
            std::cin >> arr[i];
    }
    std::cout << "The array is : ";
    print_array(arr, n);
    std::cout << "The array is being sorted...\n";
    auto start = std::chrono::high_resolution_clock::now();
    selection_sort(arr, n);
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "The sorted array is : \n ";
    print_array(arr, n);
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    std::cout << "The time taken to sort " << n << " elements is : " 
        << duration.count() << " nanoseconds" << std::endl;
    return 0;
}
