#include <iostream>
#include <string>

using namespace std;

//A class for Person
class Person {
  public:
    Person(); //a default constructor
    Person(string f, string l, int a, bool e);
    ~Person(); //a default destructor
    string toString();
    //Sometimes for short functions we will include
    //the function defintion in the class declaration.
    string getFirstName() {return firstName;};
    void setFirstName(string f) {firstName = f;};
    string getLastName() {return lastName;};
    void setLastName(string l) {lastName = l;};
    bool setAge(int a); //mutator function
    int getAge() {return age;}; //accessor function
    bool isEmployed() { return employed;};
    void setEmployed(bool e) {employed = e;};
  private:
    string firstName;
    string lastName;
    int age; //in years
    bool employed;
};

Person::Person() {
  firstName = "FNU";
  lastName = "LNU";
  age = -1;
  employed = false;
}

Person::Person(string f, string l, int a, bool e) {
  firstName = f;
  lastName = l;
  if(!setAge(a)) {
    age = -1;
  }
  employed = e;
}

Person::~Person() {
  cout << "destructor called!" << endl;
}

string Person::toString() {
  string pstring = "";

  //Add values of variables to pstring
  pstring += firstName + " " + lastName
          + " is a " + to_string(age) + " year old who is ";
  if (employed) {
    pstring += "employed.\n";
  } else {
    pstring += "unemployed.\n";
  }

  return pstring;
}

bool Person::setAge(int a) {
  //check if age is legal value
  if ((a < -1) || (a > 140)) {
    return false;
  } else {
    age = a;
    return true;
  }
}


int main() {
  //Create a dynamic Person variable
  Person *p1 = new Person();
  p1->setFirstName("Big");
  p1->setLastName("Bird");
  p1->setAge(46);
  p1->setEmployed(false);
  cout << p1->toString();

  Person *p2 = new Person("Big", "Bird", 81, false);
  cout << p2->toString();


  delete p1;
  delete p2;
}