#include <iostream> 
using namespace std;  
int out_of_order (){
	double a[10] = {1.2, 2.1, 3.3, 3.5, 4.5, 7.9, 8.4, 8.7, 9.9, 10.0};
	for (int i=0;i<10;i++){
		if (i == 9){
			return (i-10);
		}
		else if (a[i] <= a[i+1]){
			continue;
		}
		else{
			return (i);
		}
	}
}
int main() {
	cout<<out_of_order();
}
