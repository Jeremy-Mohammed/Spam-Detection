#include <iostream>
#include<iomanip>
using namespace std;

int main(){

	//dimensions
	int N = 4;
	int M = 4;

	//random numbers
	srand(time(NULL));

	// dynamic allocation
	string** array = new string*[N];
	for(int i = 0; i < N; ++i)
		array[i] = new string[M];

	// fill array with random X/O
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < M; ++j)
			if((rand() % 10 + 1)<6){
			array[i][j] = 'X';;}
			else{
			array[i][j] = 'O';;}
	//print array
	for(int i = 0; i < N; ++i){
		for(int j = 0; j < M; ++j)
			cout << setw(2)<<left<<array[i][j]<<" ";
			cout<<endl;
	}

	//Delete array
	for(int i = 0; i < N; ++i)
		delete [] array[i];
		delete [] array;
	return 0;

}