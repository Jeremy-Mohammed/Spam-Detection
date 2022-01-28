#include <iostream>
using namespace std;

struct Node {
  string data;
  Node *next; 
};

class Stack {
  private:
    Node *top; 
	
  public:
    Stack();
    void push(string d); 
    string pop(); 
    bool isEmpty();
    string toString();
    string peek();
    int count();
    ~Stack(); 
};

int main() {
  Stack *s = new Stack();

  return 0;
}