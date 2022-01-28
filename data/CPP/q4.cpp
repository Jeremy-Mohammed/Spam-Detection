/* Jeremy Mohammed 100753165
CSCI 1061
Final Exam
Question 4
*/
#include <iostream>
#include <cstring>
#include <list>
#include <vector>
#include <bits/stdc++.h> 
using namespace std;

void printList(list<string> s){ //Print items from list
    list<string>::const_iterator i;
    for(i = s.begin(); i != s.end(); ++i){
        cout << *i << " ";
		cout << endl;
    }
}

void hist(list<string> x){ //Count name occurence
    int range = x.size(); //Size of list
    int occur = 0; //Number of occurences
    vector<string> List2; //Object for checking occurences
    vector<string> Array2; //Object for output
	
    for (auto i: x){ //Appends and creates memory for list
        List2.push_back(i);
    }
	
    for (int j = 0; j<range; j++){//Set occurences
        for (int i = 0; i<Array2.size(); i++){
            if (List2[j] == Array2[i]){
                occur = 1;
            }
        }
        if (occur == 0){
            Array2.push_back(List2[j]);
        }
        occur = 0;
    }

    int range2 = Array2.size();
    for (int i = 0; i<range2; i++){//Output occurence amounts
        cout << Array2[i] << " occurs " << count(List2.begin(),List2.end(), Array2[i]) << " time(s)."<< endl;
    }
}

list<string> merge(list<string> x, list<string> y){ //Merge lists
    vector<string> merged; //Object for final merge
    vector<string> xList2; //Object for 1st list
    vector<string> yList2; //Oject for 2nd list
    int range = x.size();
    int occur = 0;
    int range2 = y.size();
    int occur2 = 0;
	
    list<string>::const_iterator i;
    for(i = xList2.begin(); i != xList2.end(); ++i){
        xList2.push_back(i);
		cout << endl;
    }

    for (auto i: y){ //Appends and creates memory for list
        yList2.push_back(i);
    }

    for (int j = 0; j<range; j++){ //Check for occurence (wont duplicate)
        for (int i = 0; i<merged.size(); i++){
            if (xList2[j] == merged[i]){
                occur = 1;
            }
        }
        if (occur == 0){
            merged.push_back(xList2[j]);
        }
        occur = 0;

    }

    for (int j = 0; j<range2; j++){ //Check for occurence2 (wont duplicate)
        for (int i = 0; i<merged.size(); i++){
            if (yList2[j] == merged[i]){
                occur2 = 1;
            }
        }
        if (occur2 == 0){
            merged.push_back(yList2[j]);
        }
        occur2 = 0;
    }
    int range3 = merged.size(); //Create final list size

    list<string> FinalList;
    for (int i = 0; i<range3 ;i++){ //Output final list
        FinalList.push_back(merged[i]);
    }
    return FinalList;
}

//Test code
int main() { 
    list<string> x = {"Alan","Alice", "Ben", "Elena", "John", "Alan", "Ben", "Alan"};
    list <string> y = {"Ben", "John", "Ben", "Elena", "Richard", "Jeremy"};   
    list<string> z;
    hist(x);
    z = merge(x,y);
    printList(z);
    return 0; 
}