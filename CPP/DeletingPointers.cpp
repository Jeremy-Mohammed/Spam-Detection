#include<iostream>
using namespace std;
typedef int* IntPtr;

int main(){
    IntPtr p1 = new int;
    *p1 = 43;

    cout<<"*p1 = " << *p1 <<"\t";

    IntPtr p2 = new int;
    p2 = p1;

    cout << "Value and address of p2 before deleting p1: " <<endl;
    cout<< "*p2 = " << *p2 << "\t" << "p2 = " << p2 <<endl;

    delete(p1);
    
    cout << "Value and address of p2 after deleting p1: " <<endl;
    cout<< "*p2 = " << *p2 << "\t" << "p2 = " << p2 <<endl;

    return 0;
}