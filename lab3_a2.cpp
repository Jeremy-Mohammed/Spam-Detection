//1000 numbers -  real 0m0.100s, user 0m0.000s, sys 0m0.016s
//10000 numbers -  real 0m0.166s, user 0m0.000s, sys 0m0.031s
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
    int size = 10000;
    int array[size];
    int temp;
	int ran;
	int num = 100;
	srand(time(0));
    
    for(int i=0;i<size;i++)
    {        

		//Generate ran
		array[i] = (rand() % 100) + 1;
	
    }
    cout << "Integers in Ascending Order" << endl;
    //Ordering numbers in ascending order
    for(int i=0;i<size;i++)
    {        

		//Generate ran
		ran = (rand() % 100) + 1;
		
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