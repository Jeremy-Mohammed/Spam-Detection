// A C++ Program to Implement a Calendar 
// of an year 
#include<iostream> 
using namespace std; 
int dayNumber(int day, int month, int year) 
{ 
  
    static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1,  4, 6, 2, 4 }; 
    year -= month < 3; 
    return ( year + year/4 - year/100 + year/400 + t[month-1] + day) % 7; 
} 

string getMonthName(int monthNumber) 
{ 
    string months[] = {"January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"}; 
    return (months[monthNumber]); 
} 

int numberOfDays (int monthNumber, int year) 
{ 
    // January 
    if (monthNumber == 0 || monthNumber == 2 || monthNumber == 4 || monthNumber == 6 || 
	monthNumber == 7 || monthNumber == 9 || monthNumber == 11) 
        return (31); 
  
    // February 
    if (monthNumber == 1) 
    { 
        // If the year is leap then February has 
        // 29 days 
        if (year % 400 == 0 || 
                (year % 4 == 0 && year % 100 != 0)) 
            return (29); 
        else
            return (28); 
    } 
    // April 
    if (monthNumber == 3 || monthNumber == 5 || monthNumber == 8 || monthNumber == 10) 
        return (30); 
} 
  
// Function to print the calendar of the given year 
void printCalendar(int year) 
{ 
    cout<<("         Calendar - ")<<(year); 
    int days; 
  
    // Index of the day from 0 to 6 
    int current = dayNumber (1, 1, year); 
  
    // i --> Iterate through all the months 
    // j --> Iterate through all the days of the 
    //       month - i 
    for (int i = 0; i < 12; i++) 
    { 
        days = numberOfDays (i, year); 
  
        // Print the current month name 
        cout<<("\n  ------------")<<(getMonthName (i).c_str())<<("-------------\n");
  
        // Print the columns 
        cout<<("  Sun  Mon  Tue  Wed  Thu  Fri  Sat\n"); 
  
        // Print appropriate spaces 
        int k; 
        for (k = 0; k < current; k++) 
            cout<<("     "); 
  
        for (int j = 1; j <= days; j++) 
        { 
            printf("%5d", j); 
  
            if (++k > 6) 
            { 
                k = 0; 
                cout<<("\n"); 
            } 
        } 
        cout<<("\n"); 
        current = k; 
    } 
  
    return; 
} 
  
// Driver Program to check above funtions 
int main() 
{ 
    int year = 2019; 
    printCalendar(year); 
  
    return (0); 
} 