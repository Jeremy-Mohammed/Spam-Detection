#include <iostream> 
using namespace std;  
void func(int x, int y)
{
int t = x;
x = y;
y = t;
cout<<x;
cout<<y;
cout<<t;
} 
int main() {
	func(1,2);
}

