//Print function is added to the stack.h header file

//and test program to test the generic stack
//Stack.h
#ifndef STACK_H
#define STACK_H
#include <iostream>
using namespace std;

// This class template creates a dynamic stack of
// of any data type. It has a pop function that
// returns a bool. The parameter to the pop function
// is passed by reference and should be the item on
// the list if it was able to pop something.

template <class T>
class Stack
{
private:
   // Structure for the stack nodes
   struct StackNode
   {
       T value; // Value in the node
       StackNode *next; // Pointer to the next node
   };

   StackNode *top; // Pointer to the stack top

public:
   // Constructor
   Stack()
   {
       top = NULL;
   }

   // Destructor
   ~Stack();

   // Stack operations
   void push(T);
   void pop(T&);
   bool isEmpty();
   void print();

};

//*********************************************************
// Destructor *
//*********************************************************
template <class T>
Stack<T>::~Stack()
{
   StackNode *nodePtr, *nextNode;

   // Position nodePtr at the top of the stack
   nodePtr = top;

   // Traverse the list deleting each node
   while (nodePtr != NULL)
   {
       nextNode = nodePtr->next;
       delete nodePtr;
       nodePtr = nextNode;
   }
}

//*********************************************************
// Member function push pushes the argument onto the *
// stack. *
//*********************************************************
template <class T>
void Stack<T>::push(T item)
{
   StackNode *newNode; // Pointer to a new node

   // Allocate a new node and store num there
   newNode = new StackNode;
   newNode->value = item;

   // If there are no nodes in the list make newNode
   // the first node
   if (isEmpty())
   {
       top = newNode;
       newNode->next = NULL;
   }
   else // Otherwise, insert newNode before top
   {
       newNode->next = top;
       top = newNode;
   }
}

//*********************************************************
// Member function to print elements from the stack*
//*********************************************************
template <class T>
void Stack<T>::print()
{
   StackNode *temp=top;
   T item;
   // Traverse the stack until the temp node is not null
   while (temp != NULL)
   {
       item = temp->value;
       cout<<item<<endl;
       temp = temp->next;
   }
}

//*********************************************************
// Member function pop pops the value at the top of the *
// stack off, and copies it into the variable passed as an*
// argument. *
//*********************************************************
template <class T>
void Stack<T>::pop(T &item)
{
   StackNode *temp; // Temporary pointer

   // First make sure the stack isn't empty
   if (isEmpty())
   {
       cout << "ERROR! The stack is empty.\n";
   }
   else
   {
       item = top->value;
       temp = top->next;
       delete top;
       top = temp;
   }
}

//*********************************************************
// Member function isEmpty returns true if the stack is *
// empty, or false otherwise. *
//*********************************************************
template <class T>
bool Stack<T>::isEmpty()
{
   bool status;

   if (!top)
   {
       status = true;
   }
   else
   {
       status = false;
   }
   return status;
}
#endif

---------------------------------------------------------------------


//test program for stack
#include <iostream>
#include <string>
#include "Stack.h"
using namespace std;

int main()
{

   //stack for integers
   Stack<int> stack;
   stack.push(2);
   stack.push(3);
   stack.push(4);

   int top=0;
  
   cout<<"--->integer stack<---"<<endl;
   cout<<"Integer stack"<<endl;
   cout<<"---------------"<<endl;
   stack.print();
   cout<<"Popping integers"<<endl;
   cout<<"---------------"<<endl;
   stack.pop(top);
   cout<<top<<endl;
   stack.pop(top);
   cout<<top<<endl;
   stack.pop(top);
   cout<<top<<endl;

   //stack for characters
   Stack<char> charstack;
   charstack.push('a');
   charstack.push('b');
   charstack.push('c');

   char ch;
  
   cout<<"--->Character stack<---"<<endl;
   cout<<"Character stack"<<endl;
   cout<<"---------------"<<endl;
   charstack.print();
   cout<<"Popping characters elements"<<endl;
   cout<<"---------------"<<endl;
   charstack.pop(ch);
   cout<<ch<<endl;
   charstack.pop(ch);
   cout<<ch<<endl;
   charstack.pop(ch);
   cout<<ch<<endl;

   //stack for string
   Stack<string> stringStack;
   stringStack.push("windows");
   stringStack.push("apple");
   stringStack.push("unix");

   string os;
  
   cout<<"--->String stack<---"<<endl;
   cout<<"String stack"<<endl;
   cout<<"---------------"<<endl;
   stringStack.print();
   cout<<"Popping strings elements"<<endl;
   cout<<"---------------"<<endl;
   stringStack.pop(os);
   cout<<os<<endl;
   stringStack.pop(os);
   cout<<os<<endl;
   stringStack.pop(os);
   cout<<os<<endl;

  

   system("pause");
   return 0;
}