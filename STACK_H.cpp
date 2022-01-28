#include<iostream>

#include<cstdlib>

#include<cstring>

using namespace std;

template<class T>

class Stack

{

    // declare stack array arr

    T *arr;

   

    // to store the index of the top most element

    int top;

   

    // to store the current capacity of arr

    int size;

   

    public:

       

        Stack()

        {

            // declare an array of size 1

            arr = new T[1];

               

            // set initial capacity to 1

            size = 1;

               

            top = -1;

        }

       

        // function to check if the stack is empty

        bool isEmpty()

        {

            if(top == -1)

                return true;

            return false;

        }

       

        void push(T x)

        {

            // if stack is full

            if(top == size - 1)

                // resize the array to double the original capacity

                resize();

               

            arr[++top] = x;

        }

       

        // pop element from stack

        T peek()

        {

            // if stack is empty

            if(isEmpty())

                return (T)NULL;

           

            // return the top most element of the stack

            return arr[top];

        }

       

        // pop element from stack

        void pop()

        {

            // if stack is not empty

            if(!isEmpty())

                // pop top most element

                top--;

        }

       

        // resize the array to double the original capacity

        void resize()

        {

            // create a new string array double the size of arr

            char *temp = new T[2 * size];

            int i;

           

            for( i = 0 ; i < size ; i++ )

                // cop contents of arr to temp

                temp[i] = arr[i];

           

            // set capacity to double the original capacity

            size *= 2;

           

            // set temp as the new stack array

            arr = temp;

        }

       

};

int main()

{

    Stack<char> ob;

   

    cout<<"Please input String:\n";

    string str;

    cin>>str;

   

    int i;

   

    for( i = 0 ; i < str.length() ; i++ )

        ob.push( str[i] );

       

    cout<<"\nContents of stack ...\n";

       

    while( !ob.isEmpty() )

    {

        cout<<ob.peek();

       

        ob.pop();

       

        cout<<endl;

    }

   

    return 0;

}