#include <iostream> 
using namespace std; 

class Person {
    public:
        int getAge();
        void setAge(int age);
        string getfName();
        void setfName(string fName);
        string getlName();
        void setlName(string lName);
        string fName;
        string lName;
        int age;
		
	Person();
	Person(string f, string l, int a);
	
};
void Person::setAge(int a){
    age = a;
}

int Person::getAge(){
    return age;
}
void Person::setfName(string f){
    fName = f;
}

string Person::getfName(){
    return fName;
}
void Person::setlName(string l){
    lName = l;
}

string Person::getlName(){
    return lName;
}

Person::Person(){
	fName = "Rohollah";
	lName = "Moosavi";
	age = 25;
};
Person::Person(string f, string l, int a){
	fName = f;
	lName = l;
	age = a;
};





int main(){
	Person *p1 = new Person();
	Person *p2 = new Person("Jeremy", "Mohammed", 18);
	
	cout<<"Person 1 (Default Constructor):"<<endl<<p1->fName<<" "<<p1->lName
	<<", Age: "<<p1->getAge()<<endl<<endl;
	
    p1->setAge(28);
    p1->setfName("Jushy");
    p1->setlName("Jag");
	
	cout<<"Person 1 (Setter/Getter):"<<endl<<p1->getfName()<<" "<<p1->getlName()
	<<", Age: "<<p1->getAge()<<endl<<endl;
    
	cout<<"Person 2 (Constructor):"<<endl<<p2->fName<<" "<<p2->lName
	<<", Age: "<<p2->age<<endl;
	
	return 0;
}
