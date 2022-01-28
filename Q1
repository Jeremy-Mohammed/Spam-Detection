/* Jeremy Mohammed 100753165
CSCI 1061
Final Exam
Question 1
*/#include <iostream>
#include <cstdlib>
using namespace std;

class DynamicArray{
    public:
    DynamicArray();
    DynamicArray(int n);
    DynamicArray(DynamicArray &);
    ~DynamicArray();
    //Operator functions
    DynamicArray & operator=(const DynamicArray &t);
    private:
        double * ptr;
        int size;

//friend operators
friend double operator+(const DynamicArray &t, const DynamicArray &s);
friend ostream & operator<<(ostream & os, const DynamicArray &t);
friend istream & operator>>(istream & is, DynamicArray &t);
};

//Default Constructor
DynamicArray::DynamicArray(){
    ptr = nullptr;
    size = 0;
}

//Constructor
DynamicArray::DynamicArray(int n){
    size = n;
    ptr = new double[n];
    for (int i = 0; i < n; i++)
    {
        ptr[i] = 0;
    }
}

//Copy Constructor
DynamicArray::DynamicArray(DynamicArray &t){
    size = t.size;
}
//Deconstructor
DynamicArray::~DynamicArray(){
    delete[] ptr;
}

//Member Operators
DynamicArray & DynamicArray::operator=(const DynamicArray &t){
    size = t.size;
    delete[] ptr;
    return *this;

}
//Friend Operators
double operator+(const DynamicArray &t, const DynamicArray &s){
    double* Array = new double[t.size];
    for (int i = 0; i < t.size; i++){
        Array[i] = t.ptr[i] + s.ptr[i];
    }
	return *Array;
}

ostream & operator<<(ostream & os, const DynamicArray &t){
    os << "[";
    for (int i = 0; i < t.size; i++){
        os << t.ptr[i] << " ";
    }
    os << "]";
	return os;	
}

istream & operator>>(istream & is, DynamicArray &t){
    cout << "Enter Doubles" << endl;
    for (int i = 0; i < t.size; i++)
    {
     
    return is;
}


int main(){
    int dim;
    cout << "Enter the dimension of the array: ";
    cin >> dim;
    DynamicArray x;   // Test for default constructor
    DynamicArray y(dim);  // Test the second constructor
    cin >> y;    // Test operator>>
    DynamicArray z = y;                   
    x = y + z;                             
    cout << "Sum is: " << x << endl;     
    return 0;
}