#include <iostream>

using namespace std;

class Person {
    public:
        int getAge();
        void setAge(int age);
    private:
        string fName;
        string lName;
        int age;
        bool isEmployed;
        bool isStudent;
	
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
	//p1->age = 20;
    p1->setAge(20);
    cout<<p1->getAge()<<endl;
    
	
	return 0;
}
