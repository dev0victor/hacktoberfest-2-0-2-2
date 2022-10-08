#include <bits/stdc++.h>
using namespace std;

// ALL the below functions must be present in heapsort program 

void heapify(int arr[], int n, int i){
    int largest = i;
    int left = 2*i;
    int right = 2*i + 1;
    if(left <= n && arr[left] > arr[largest]){
        largest = left;
    }
    if(right <= n && arr[right] > arr[largest]){
        largest = right;
    }

    if(largest != i){
        swap(arr[i],arr[largest]);
        heapify(arr, n, largest);
    }
    return;
}

void buildHeap(int arr[], int n){
    for(int i = n/2; i >=1 ; i--){
        int node = i;
        heapify(arr, n , i);
    }
    return;
}

void heapSort(int arr[], int n){
    buildHeap(arr,n);
    for(int i = n; i > 1; i--){
        swap(arr[i],arr[1]);
        heapify(arr,i-1,1);
    }
    return;
}

int main(){
    //Driver CODE
    int n;
    cin >> n;
    int arr[n+1];
    for(int i = 1; i <= n; i++){
        cin >> arr[i];
    }
    heapSort(arr,n);
    for(int i = 1; i <= n; i++){
        cout << arr[i] << " ";
    }
}
