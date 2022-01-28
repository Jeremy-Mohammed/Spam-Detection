/*
 * Programmer name: Jeremy M
 * Date: 11/3/17
 * Purpose: To demonstrate the use of loops
 * liberals and conservatives
 */
import java.util.Scanner;
public class LoopsExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Variable to keep track of the user choice
		String choice ="";
		
		//variables to keep track of the liberals and conservatives
		int lCounter = 0;//For liberals
		int cCounter = 0;//For conservatives 
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a choice (C or L):");
		choice = input.next();
		
		//loop while choice is C or L
		while (choice.equals("C")|| choice.equals("L"))
		{
			//Keep track of Liberals
			if (choice.equals("L"))
			{
				lCounter = lCounter + 1;
			}
			//keep track of Conservatives
			else if (choice.equals("C"))
			{
				cCounter++;//Same as cCounter=cCounter + 1
			}
			System.out.print("Enter a choice (C or L)");
			choice=input.next();
		}
		System.out.println("Total Liberals: " + lCounter);
		System.out.println("Total Conservatives: " + cCounter);
		input.close();
		
	}

}
