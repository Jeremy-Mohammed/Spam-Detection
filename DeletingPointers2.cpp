#include<iostream>
using namespace std;
typedef int* IntPtr;

int main(){
    int array[5];

    for (int i = 0; i<5; i++){
        array[i]=1;
    }

    IntPtr p1;
    p1 = new int[5];

    for (int i = 0; i<5; i++){
        *(p1+i) = i;
        cout << "p1i" << i << "i value: "
        << p1[i] << "\t"
        << "p1i" << i << "i address: "
        << p1+i << endl;
    }
    return 0;
}