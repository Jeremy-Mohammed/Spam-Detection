#include <iostream>

using namespace std;

int main (){
	
	char mark;
	cout << "Please enter the mark "<< endl;
	cin >> mark;
	
	switch (mark) {
		case 'A':
		cout << "Awesome!" << endl;
		break;
		case 'B':
		cout << "Good work!" << endl;
		break;
		case 'C':
		cout << "Keep at it!" << endl;
		break;
		case 'D':
		cout << "Try again!" << endl;
		break;
		case 'F':
		cout << "Please schedule an apppoinment with your professor!" << endl;
		break;
		default:
		cout << "This is not a reaal grade!" << endl;
	}
	
	return 0;
}
