#include <iostream>
using namespace std;
void swap(int& i, int& j)
{
    int temp=i;
    i=j;
    j=temp;
}
    
int main()
{
    //Declaring array and size of array
    int size = 5;
    int array[size];
    int temp;
    cout << "Enter 5 integers:" << endl;
//Input for array
    for(int i=0; i < size; i++)
    {
        cin >> array[i];
    }
    
    cout << "Integers in Ascending Order" << endl;
    //Ordering numbers in ascending order
    for(int i=0;i<size;i++)
    {        
        for(int j=i+1;j<size;j++)
        {
            if(array[i]>array[j])
            {
                int temp1 = array[i];
                int temp2 = array[j];
                swap(temp1,temp2);
                
                array[i] = temp1;
                array[j] = temp2;
                
                
            }
        }
    }
    
    for(int i=0; i<size;i++)
    {
        cout << array[i] << endl;
    }
}