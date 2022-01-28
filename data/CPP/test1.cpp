/*
//Jeremy Mohammed - 100753165
#include <iostream>
using namespace std;

//Declare functions
int convertString(string line);
string convertInt(int num);

int main()
{
	//Declare varibles
	int num;
	string line;
	
	//Enter values
	cout<<"Enter a number: ";
	cin>>num;
	cout<<"Enter a string with only digits: ";
	cin>>line;
	
	//Output converted values
	cout<<convertInt(num)<<endl;
	cout<<convertString(line)<<endl;
	return 0;
}

//Converts string to int
int convertString (string line){
	int convert = stoi(line);
	return (convert);
}

//Convert int to string
string convertInt (int num){
	string converted = to_string(num);
	return (converted);
}
*/