#include <iostream>
#include <string>
#include<fstream>

using namespace std;

int main(){

	//Defines and declare file input
	ifstream infile;
	string ifileName="word.txt";

	//openning input file
	infile.open(ifileName);

	//Check if file exists
	if(!infile){
		cout<<"File cannot be opened";
		exit(0);
	}

	//Reading line
	string line;
	int num;
	int nums[length(line)];
	char cha;
	while(getline(infile,line)){
		for(int j=0;j<length(line);j++){
			for(int i=0;i<length(line);i++){
				if (cha == 'a'
				|| cha == 'e'
				|| cha == 'i'
				|| cha == 'o'
				|| cha == 'u'
				|| cha == 'A'
				|| cha == 'E'
				|| cha == 'I'
				|| cha == 'O'
				|| cha == 'U'){
				num=num+1;}
				if (cha ==' '){
					break;
				}
			}
			nums[j]=num;
		}
	}
	
	int ans;
	ans=nums[0]
	int j;
	for(j=1;j<length(line);j++){
		if (nums[j-1]<nums[j]){
			ans=nums[j];
		}
	}
	
	cout<<"The "<< ans<< " had the most vowels"<<endl;

	//closing file
	infile.close();

	return 0;

}