/*
 * Programmer name: Jeremy M
 * Date: 11/7/17
 * Purpose: To learn do while loops in java
 * Input: Vote
 * Process: Add vote to category
 * Output: Categories
 */
import java.util.Scanner;
public class LoopsExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Variable to keep track of the user choice
		String choice ="";
		
		//Variables to keep track of the liberals and conservatives
		int lCounter = 0, cCounter = 0;
		Scanner input = new Scanner(System.in);
		
		//Input vote
		do 
		{
			//User input
			System.out.print("Enter a choice (C or L)");
			choice=input.next();
			if (choice.equals("L"))
			{
				lCounter = lCounter + 1;
			}
			else if (choice.equals("C"))
			{
				cCounter++;					
			}
		}while (choice.equals("C")|| choice.equals("L"));

		//Output
		System.out.println("Total Liberals: " + lCounter);
		System.out.println("Total Conservatives: " + cCounter);
		input.close();
	}

}
