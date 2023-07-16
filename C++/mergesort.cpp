#include <iostream>
#include <vector>
#include <fstream>
#include <istream>
#include <chrono>

std::vector<int> operator+(std::vector<int> arr1, std::vector<int> arr2){
    int i = 0, j = 0;
    std::vector<int> merged;
    while(i < arr1.size() && j <arr2.size()){
        if(arr1[i] < arr2[j]){
            merged.push_back(arr1[i]);
            i++;
        }
        else if(arr2[j] < arr1[i]){
            merged.push_back(arr2[j]);
            j++;
        }
        else{
            merged.push_back(arr1[i]);
            merged.push_back(arr2[j]);
            i++;j++;
        }
    }
    if(i < arr1.size()) merged.insert(merged.end(),arr1.begin()+i,arr1.end());
    if(j < arr2.size()) merged.insert(merged.end(),arr2.begin()+j,arr2.end());
    return merged;
}

std::vector<int> mergesort(std::vector<int> arr) {
    if ( arr.size() <= 1 )
        return arr;
    int mid = arr.size() / 2;
    return(
        mergesort(std::vector<int>(arr.begin(),arr.begin()+mid))
        + mergesort(std::vector<int>(arr.begin()+mid,arr.end()))
    );
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
    std::vector<int> sarr = mergesort(arr);
    auto end = std::chrono::high_resolution_clock::now();
    std::cout<<"The sorted array is: \n"<<sarr;
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout<<"The time taken is: "<<duration<<" microseconds";
    return 0;
}