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
	
	//cout << "Display arrays items: " <<endl;
	for (int i=0; i<size; i++){
		myOutput << data[i] << endl;
	}
	
	myOutput.close();
	
	//Reading from file
	cout << "Reading from the file with name " << filename <<endl;
	ifstream myInput(filename);
	
	//Read from the filename
	while (!myInput.eof())[
	string line;
	myInput >> line;
	cout << line <<endl;
	}
	
	myInput.close();
	return 0;
	
	
	
}