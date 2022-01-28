#include <iostream>
#include <string>

using namespace std;

//A declaration for a person class
class Person {
  public:
    Person(); //the default constructor
    Person(string f, string l, int a, bool e);
    ~Person(); //a default destructor
    void toString();
  private:
    string firstName;
    string lastName;
    int age;
    bool isEmployed;
};

//definitions of functions in Person class
Person::Person() {
  firstName = "FNU";
  lastName = "LNU";
  age = -1;
  isEmployed = false;
}

Person::Person(string f, string l, int a, bool e) {
  firstName = f;
  lastName = l;
  age = a;
  isEmployed = e;
}

Person::~Person() {
  cout << "Destroying one person object!" << endl;
}

void Person::toString() {
  cout << "First name: " << firstName << endl;
  cout << "Last name: " << lastName << endl;
  if (age == -1) {
    cout << "age: unknown" << endl;
  } else {
    cout << "age (in years): " << age << endl;
  }
  if (isEmployed) {
    cout << "Employed?: Yes" << endl;
  } else {
    cout << "Employed?: No" << endl;
  }
}

int main() {
  //create a dynamic Person variable
  Person *p1 = new Person();
  p1->toString(); //same as (*p1).toString();
  delete p1;

  Person *p2 = new Person("Han", "Solo", 67, true);
  p2->toString();
  delete p2;

  return 0;
}