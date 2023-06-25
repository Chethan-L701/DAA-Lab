#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <istream>
#include <random>
#include <chrono>

std::vector<int> operator+(const std::vector<int> &a, const std::vector<int> &b) {
    std::vector<int> c;
    c.reserve(a.size() + b.size());
    c.insert(c.end(), a.begin(), a.end());
    c.insert(c.end(), b.begin(), b.end());
    return c; 
}

std::vector<int> quicksort(std::vector<int> arr) {
    if (arr.size() <= 1) {
        return arr;
    }
    int pivot = arr[arr.size() / 2];
    std::vector<int> less;
    std::vector<int> greater;
    std::vector<int> equal;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] < pivot) less.push_back(arr[i]);
        else if (arr[i] > pivot) greater.push_back(arr[i]);
        else equal.push_back(arr[i]);
    }
    return quicksort(less) + equal + quicksort(greater);
}

void operator<<(std::ostream &os, const std::vector<int> &v) {
    for (int i = 0; i < v.size(); i++) {
        os << v[i] << " ";
    }
    os << "\n";
}

int main() {
    srand(time(0));
    int n, ch;
    std::vector<int> arr;
    std::cout<<"Enter the size of the array: ";
    std::cin>>n;
    std::cout<<"Enter your choice:\n1.Generate numbers Randomly\n2.Read numbers from a file\n";
    std::cin>>ch;
    if (ch == 1) {
        for (int i = 0; i < n; i++) {
            arr.push_back(rand() % 100000000);
        }
    } else if (ch == 2) {
        std::cout<<"Enter the name of the file: ";
        std::string filename;
        std::cin>>filename;
        std::ifstream file(filename);
        for (int i = 0; i < n; i++) {
            file >> arr[i];
        }
    }
    std::cout<<"The array is: \n"<<arr;
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> sarr = quicksort(arr);
    auto end = std::chrono::high_resolution_clock::now();
    std::cout<<"The sorted array is: \n"<<sarr;
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout<<"The time taken is: "<<duration<<" microseconds";
    return 0;
}

