#include <iostream>
using namespace std;

void printCalendar(string month, int year);

int main( )
{
	string month; int year; string choice;
	//Loop functions choice
	do{
		//Choose function
		cout<<"Year"<<endl<<"Month"<<endl<<"Cancel"<<endl<<"Choice: ";
		cin>>choice;
		
		//Month choice
		if (choice == "Month"){
			//Input month and year
			cout<<"Enter a month: ";
			cin>>month;
			cout<<"Enter a year: ";
			cin>>year;
			//Call printMonth functiom
			printCalendar(month,year);
		}
		
		//Year choice
		else if (choice == "Year"){
			//Input year
			cout<<"Enter a year: ";
			cin>>year;
			//Call printYear function
			printCalendar("NA",year);
		}
	//Close if cancel chosen
	}while(choice != "Cancel");
		return 0;
}


//Figure out what starting day of each month is
int dayNumber(int day, int month, int year) 
{ 
    static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1,  4, 6, 2, 4 }; 
    year -= month < 3; 
    return ( year + year/4 - year/100 + year/400 + t[month-1] + day) % 7; 
} 

//Sets month name
string getMonthName(int monthNumber) 
{ 
    string months[] = {"January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"}; 
    return (months[monthNumber]); 
} 

//Sets days for given month
int numberOfDays (int monthNumber, int year) 
{ 
    //Months with 31 days 
    if (monthNumber == 0 || monthNumber == 2 || monthNumber == 4 || monthNumber == 6 || 
	monthNumber == 7 || monthNumber == 9 || monthNumber == 11) 
        return (31); 
  
    //February 
    if (monthNumber == 1) 
    { 
        //Feb has 29 days if leap year
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) 
            return (29); 
        else
            return (28); 
    } 
    //Months with 30 days
    if (monthNumber == 3 || monthNumber == 5 || monthNumber == 8 || monthNumber == 10) 
        return (30); 
} 
  
//Prints calendar of given month and or year
void printCalendar(string chooseMonth, int year) 
{
    cout<<("         Calendar - ")<<(year); 
    int days; 
  
    //Index of the day from 0 to 6 
    int current = dayNumber (1, 1, year); 
  
    //Iterate through all the months 
    for (int i = 0; i < 12; i++) {
        days = numberOfDays (i, year); 
		
		//Pick between year or month
		if (chooseMonth == "NA" || chooseMonth == getMonthName (i).c_str()){
			
			//Print month name 
			cout<<("\n  ------------")<<(getMonthName (i).c_str())<<("-------------\n");
			
			//Print the columns 
			cout<<("  Sun  Mon  Tue  Wed  Thu  Fri  Sat\n"); 
	  
			//Print spacing
			int k; 
			for (k = 0; k < current; k++) 
				cout<<("     "); 
	  
			//Iterate through all the days of the month
			for (int j = 1; j <= days; j++) 
			{ 
				printf("%5d", j); 
	  
				if (++k > 6) 
				{ 
					k = 0; 
					cout<<("\n"); 
				} 
			} 
		//Reset week
        cout<<("\n"); 
        current = k; 
		}
    } 
    return; 
} 