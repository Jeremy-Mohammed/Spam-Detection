#include <iostream>
#include <fstream>

using namespace std;

int main(){
	string filename;
	int size = 5;
	string data[size];
	
	cout <<"Please enter the filename: " <<endl;
	cin >> filename;
	
	ofstream myOutput(filename);
	
	cout << "Enter " << size << " items: "<<endl;
	for (int i=0; i<size; i++){
		cin >> data[i];
	}
	
	cout << "Display arrays items: " <<endl;
	for (int i=0; i<size; i++){
		myOutput << data[i] << endl;
	}
	
	myOutput.close();
	return 0;
	
	
	
}