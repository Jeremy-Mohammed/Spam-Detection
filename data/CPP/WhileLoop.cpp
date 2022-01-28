#include <iostream>

using namespace std;

int main(){
	int sum=0;
	int i=2;
	
	while (i<=100) {
		if (i%2 == 0) {
		sum = sum +i;
		}
		i=i++;
		sum=sum + i;
		i=i+2;
	}
	
	cout << sum <<endl;
	return 0;
}
