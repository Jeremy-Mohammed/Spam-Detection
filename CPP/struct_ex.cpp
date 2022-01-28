#include <iostream>
#include <string>

using namespace std;

//A composite structure for a person
struct Person {
  string firstName;
  string lastName;
  int age;
  bool isEmployed;
  bool isStudent;
};

Person* createPerson(string f, string l, int a, bool e, bool s);

int main() {
  //create an  automatic (ordinary) Person variable
  Person p;

  p.firstName = "Cookie";
  p.lastName = "Monster";
  p.age = 42;
  p.isEmployed = true;
  p.isStudent = false;

  cout << p.firstName << " " << p.lastName
       << " is a " << p.age << " year old." << endl;

  //create a dynamic Person variable
  Person *p2 = new Person;
  (*p2).firstName = "Big";  //There's a better way
                            //to do this!
  p2->lastName = "Bird";
  p2->age = 81;
  p2->isEmployed = true;
  p2->isStudent = false;

  cout << p2->firstName << " " << p2->lastName
       << " is a " << p2->age << " year old. ";
  if (p2->isEmployed) {
    cout << p2->firstName << " is also employed!"
         << endl;
  }

  delete p2;

  p2 = createPerson("Ernie", "LNU", 36, true, true);
  cout << p2->firstName << " " << p2->lastName
       << " is a " << p2->age << " year old. ";
  if (p2->isEmployed) {
    cout << p2->firstName << " is also employed!"
         << endl;
  }
  delete p2;

  return 0;
}

Person* createPerson(string f, string l, int a,
                     bool e, bool s) {
  Person *temp = new Person;
  temp->firstName = f;
  temp->lastName = l;
  temp->age = a;
  temp->isEmployed = e;
  temp->isStudent = s;
  return temp;
}