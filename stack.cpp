#include <iostream>
#include<cstdlib>

using namespace std;
// Creating a NODE Structure
struct Node
{
int data;
struct Node *next;
};

// Creating a class STACK
class Stack
{
struct Node *top;
public:
Stack() // constructor
{
top=NULL;
}
void push(); // to insert a Node
int pop(); // to delete a Node
void print(); // to print the stack data
};

//a)
// PUSH Operation
void Stack::push()
{
int value;
struct Node *ptr;
cout<<"Enter a number to insert: ";
cin>>value;
ptr=new Node;
ptr->data=value;
ptr->next=NULL;
if(top!=NULL)
ptr->next=top;
top=ptr;
cout<<"New Node is inserted to the stack.\n"<<endl;

}
//b)
// POP Operation
int Stack::pop()
{
struct Node *temp;
if(top==NULL)
{
cout<<"\nThe stack is empty!!!";
return 0;
}
temp=top;
top=top->next;
int value=temp->data;
//deleting top Node
delete temp;
return value;
}
//c)
// print stack elements
void Stack::print()
{
struct Node *ptr1=top;
cout<<"\nThe stack elements are\n";
while(ptr1!=NULL)
{
cout<<ptr1->data<<" ";
ptr1=ptr1->next;
}
cout<<"\n";
}

// Driver program for testing
int main()
{
Stack s;
s.push();
s.push();
s.push();
s.push();
s.print();
cout << s.pop() << " Popped from stack\n";
cout<<"\nAfter popping one element\n";
s.print();
return 0;
}