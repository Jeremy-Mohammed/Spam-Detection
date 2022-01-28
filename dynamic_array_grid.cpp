#include <iostream>

#include<cstdlib>

#include<ctime>

#include<iomanip>

using namespace std;

int main()

{

// dimensions

int N = 5;

int M = 5;

//seeding for random numbes

srand(time(NULL));

// dynamic allocation

int** array = new int*[N];

for(int i = 0; i < N; ++i)

array[i] = new int[M];

// fill array with random number from 1 to 10

for(int i = 0; i < N; ++i)

for(int j = 0; j < M; ++j)

array[i][j] = rand() % 10 + 1;;

// print array elements

cout<<"Array elements are:\n";

for(int i = 0; i < N; ++i)

{

for(int j = 0; j < M; ++j)

cout << setw(2)<<left<<array[i][j]<<" ";

cout<<endl;

}

//computing sum of elements

int sum=0;

for(int i = 0; i < N; ++i)

{

for(int j = 0; j < M; ++j)

sum+=array[i][j];

}

//print sum

cout<<"\nSum of all elements: "<<sum<<endl;

// free allocated memory

for(int i = 0; i < N; ++i)

delete [] array[i];

delete [] array;

return 0;

}