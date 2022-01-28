#include <iostream>

using namespace std;

int main () {
	
	//Declaration
	int round = 1;
	int guess;
	int ran;
	int try1 = 5;
	int num = 5;
	srand(time(0));
	
	//Output title card
	cout<<"-----------------------------"<<endl;
	cout<<"Welcome to guess That number!"<<endl;
	cout<<"-----------------------------"<<endl;
	
	//Loop rounds
	while (try1>0) {
		cout<<""<<endl<<"round "<<round<<endl;
		
		//Generate ran
		ran = (rand() % num) + 1;
		
		//Loop tries
		while (try1>0) {
			
			//Input guess
			cout<<"guess a number less than "<<num<<": ";
			cin>>guess;
			try1 -=1;
			
			//Check guess against ran
			if (guess == ran){
				//Correct move on
				cout<<"Correct! The number was "<<ran<<endl;
				break;
			}
			else if (try1==0){
				//Incorrect game over
				cout<<""<<endl<<"Incorrect! Out of guesses :("<<endl;
				break;
			}
			else{
				//Incorrect try1 again
				cout<<"Incorrect! try1 again ("<<try1<<" tries remaining)"<<endl;
				continue;
			}
		}
		
		//End game
		if (try1==0){
			break;
		}
		
		//Fix variables for next round
		else{
			round++;
			num = num*2;
			try1 = 5;
		}
	}
	cout<<"Game Over!!!"<<endl;
	return 0;
}

