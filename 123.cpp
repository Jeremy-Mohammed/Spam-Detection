// Q2.cpp s

#include <iostream>

#include <cstring>

 

using namespace std;

class A{
	public:
	virtual void f(){cout << "AF" << endl;}
	void g(){cout << "AG" << endl;}
};
	
class B:public A{
	public:
	void f(){cout << "BF" << endl;}
	void g(){cout << "BG" << endl;}
};

int main(){
	B *x[2];
	x[0]=new A;
	x[1] = new B;
	
	for (int i=0;i<2;i++){
		x[i] -> f();
		x[i] -> g();
	}
	return 0;
}
		