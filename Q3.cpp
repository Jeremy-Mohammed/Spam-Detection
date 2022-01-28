/* Jeremy Mohammed 100753165
CSCI 1061
Final Exam
Question 3
*/
#include <iostream> 
using namespace std; 
    
template<class T> //Create template

class Stack { 
    int size;     // Maximum size of Stack 
    int top;      // Shows the index of top item 
    T *data;   // Points to a dynamic array holding stack items
public: 
    Stack(){
		data = new T[size]; //Declare array size
		top = -1;
	}
    Stack(int s): size(s),top(-1){
		data = new T[size]; //Set given array size
	} 
 
	void push(T x){  // Push an item on top of stack
		if (top >= (size - 1)) { //Stack is full
			cout << "Stack Overflow"; 
		} 
		else { 
			data[++top] = x; 
			cout << x << " pushed into stack\n"; 
		} 
	} 
	  
	void pop(){  // Pop an item from stack
		if (top < 0) { //Stack is empty
			cout << "Stack Underflow"; 
		} 
		else {
			top--; 
		}
	} 
	T peek(){  // Return the top item in the stack
		if (top < 0) {  //Stack is empty
			cout << "Stack is empty"; 
			return (T)NULL; 
		} 
		else { 
			cout << "Popped from stack" << endl; 
			return data[top];
		} 
	} 
	  
	bool isEmpty(){  // Check if stack is empty or not
		return (top < 0); 
	} 
}; 

int main(){  //Test code
    Stack<string> s(20); 
     s.push("John");
     s.push("Sue"); 
     s.push("Ted"); 
     s.pop();
    
    cout << s.peek() << " is top of stack" << endl; 
    
    return 0;
}