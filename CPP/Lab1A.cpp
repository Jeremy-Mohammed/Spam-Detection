#include <iostream>

using namespace std;

int main(){
	
	//Initialize Variables
	double wage;
	int year;
	string name;
	
	//Input Data
	cout << "Name: ";
	getline(cin,name);	
	cout << "Birth Year: ";
	cin>>year;	
	cout << "Hourly Wage ($): ";
	cin>>wage;
	
	//Output Data
	cout <<name << " is "<< 2019-year<< " years old and requests an hourly wage of $"<< wage<< "."<<endl;
	
	
	
	return 0;
}