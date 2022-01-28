#include <iostream>

using namespace std;

class Person {
    public:
        int getAge();
        void setAge(int age);
		
	Person();//The default construct used to initialize object's variable
	Person(string f, string l, int a, bool e, bool s);
    public:
        string fName;
        string lName;
        int age;
        bool isEmployed;
        bool isStudent;
	
};

Person::Person(){
	fName = "FNU";
	lName = "LNU";
	age = -1;
	isEmployed = false;
	isStudent = false;
};
Person::Person(string f, string l, int a, bool e, bool s){
	fName = f;
	lName = l;
	age = a;
	isEmployed = e;
	isStudent = s;
};
void Person::setAge(int a){
    if (a< 0){
        age = -1;
    }
    else{
        age = a;
    }
}

int Person::getAge(){
    return age;
}

int main(){
	Person *p1 = new Person();
	
	cout<< "fName = "<<p1->fName<<" lName = " << p1->lName << " age = " << p1->age<<
	" isEmployed = " << p1->isEmployed << " isStudent = " << p1->isStudent<<endl;
	//p1->age = 20;
    //p1->setAge(20);
    //cout<<p1->getAge()<<endl;
    
	Person *p2 = new Person("John", "Omoyinmy", 20, false, true);
	cout<<p2->fName<<endl;
	cout<<p2->lName<<endl;
	cout<<p2->age<<endl;
	cout<<p2->isEmployed<<endl;
	cout<<p2->isStudent<<endl;
	
	return 0;
}
