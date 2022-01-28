#include <iostream>
using namespace std;

double average(double num1, double num2);
double average(double num1, double num2, double num3);

int main(){
	cout << "Please enter 3 numbers: "<<endl;
	
	double num1,num2,num3;
	cin>>num1>>num2>>num3;
	
	
	double result = average(num1,num2);
	
	cout << result<<endl;
	
	double result1 = average(num1,num2,num3);
	cout << result1<<endl;
	
	return 0;
}

double average (double num1, double num2, double num3){
	double average = ((num1+num2+num3)/3);
	return average;
}

double average (double num1, double num2){
	double average = ((num1+num2)/2);
	return average;
}