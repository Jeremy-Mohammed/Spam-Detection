#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

//Create a node struct to store
//one item of date in the Stack class
struct Node {
  string data;
  Node *next; //points to the next node in the Stack
};

class Stack {
  public:
    Stack(); //constructor
    ~Stack(); //deconstructor
    void push(string d); //pushes a node containing d
                         //onto the top of the Stack
    string pop(); //pop the top node of of the Stack
                  //and return the string stored in the node
    string toString(); //save Stack contents to a string
    //check if Stack is empty
    bool isEmpty() {return (top == NULL);};
  private:
    Node *top; //point to the top item in the Stack
};

Stack::Stack() {
  top = NULL; //initialize to an empty Stack
              //One that has top point to nothing
}

Stack::~Stack() {
  //Has to free up all of the memory allocated to nodes
  //in the Stack
  while (!isEmpty()) {
    pop();
  }
}

void Stack::push(string d) {
  Node *newtop = new Node;
  newtop->data = d;
  newtop->next = top; //point new node's next to the
                      //old top of the stack
  top = newtop; //make new node the top of the stack
}

string Stack::pop() {
  //pop the top of the stack if stack is not empty
  if (!isEmpty()) {
    string value = top->data; //set aside current value in top
    Node *oldtop = top; //create oldtop to point to top
    top = top->next; //reassign top of stack to be second
                     //top node
    delete oldtop; //delete the node being popped
    return value; //return value of popped node
  } else {
      cout << "ERROR: you can't pop from empty stack!\n";
      exit(1);
  }
}

string Stack::toString() {
  string result = "(top) -> ";
  Node *current = top;
  while (current != NULL) {
    result += current->data + " -> ";
    current = current->next;
  }
  result += "NULL";
  return result;
}


int main() {
  Stack *s = new Stack();
  cout<< s->toString() << endl;
  s->push("Blaze");
  cout<< s->toString() << endl;
  s->push("Sadie");
  cout<< s->toString() << endl;
  while (!s->isEmpty()) {
    cout << "Stack content popped: " << s->pop() << endl;
  }
  cout<< s->toString() << endl;
  delete s;
  return 0;
}