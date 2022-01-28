/* Jeremy Mohammed 100753165
CSCI 1061
Final Exam
Question 2
*/
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
class Document{
    public:
		Document() { 
         text =""; 
		}
		Document(string text){ 
			this->text = text; 
		}
		string getText() const{ 
			return this->text;
		}
		virtual void print() const; 

private:
    string text;
};

class Email : public Document
{
    public:

		//Constructors
        Email(string c, string s, string r, string t);

		//Get methods
        string getContent() {
			return content;
			}
        string getSender() {
			return sender;
			}
        string getRecipient() {
			return recipient;
			}
        string getTitle() {
			return title;
			}
		//Set methods
        void setContent(string);
        void setSender(string);
        void setRecipient(string);
        void setTitle(string);


        virtual void print();

    private:
        string sender;
        string recipient;
        string title;

        string content;
};

//Constuctor
Email::Email(string c, string s, string r, string t){
    setContent(c);
    setSender(s);
    setRecipient(r);
    setTitle(t);
}

//Set methods
void Email::setSender(string s){
    sender = s;
}

void Email::setRecipient(string r){
    recipient = r;
}

void Email::setTitle(string t){
    title = t;
}

void Email::setContent(string c){
    content = c;
}

void Email::print(){
    //Output
    cout<< "Email Information:" << endl;
    cout << "================="<< endl;
    cout << "Sender: "<< getSender() << endl;
    cout << "Recipient: "<< getRecipient() <<  endl;
    cout << "Content: "<< getContent() << endl;
}

bool ContainsKeyword(Document *, string s){//Check for same keyword
    if(s == Document::getText()){
        return true;
    }
    else{
        return false;
    }
}
//Test code
int main(){ 
	Document *d; 
	d = new Email("Programming in C++", "Larry", "Curly", "Programming");
	d->print(); // Test for print function
	if (ContainsKeyword(d,"C++")) 
		cout << "C++ is in the e-mail." << endl; 
	else 
		cout << "C++ is NOT in the e-mail." << endl;
 
  return 0;
}