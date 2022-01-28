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
    int push(); 
    string pop(); 
    bool isEmpty();
    string toString();
    string peek();
    int count();
    ~Stack(); 
};

//Push function
int Stack::push()
{
	//Insert data
	string value;
	int num;
	struct Node *ptr;
	cout<<"Enter data: ";
	cin>>value;
	//Add data and shift info
	ptr=new Node;
	ptr->data=value;
	ptr->next=NULL;
	if(top!=NULL)
	ptr->next=top;
	top=ptr;
	num=num+1;
	return num;
}

//isEmpty function
bool Stack::isEmpty(){
	if(top==NULL){
		cout<<"Stack is empty";
		return true;
	}
}

//count function
int Stack::count(){
	Stack *s = new Stack();
	int num;
	if(s.push()!=NULL){
		num = s.push();
	}
	if (s.isEmpty==true){
		num=0;
	}
	else{
		num=1;
	}
	return num;
}

//Pop function
string Stack::pop(){
	struct Node *temp;
	//moving stack
	temp=top;
	top=top->next;
	string value=temp->data;
	//delete temp variable
	delete temp;
	return value;
}

int main() {
  Stack *s = new Stack();
  return 0;
}
