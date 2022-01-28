/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn loops in java
 * Input: Subject, marks
 * Process: Average
 * Output: Format
 */
import java.util.Scanner;
public class FinalLoops4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int Sales=0;
		String Name="";
		Scanner input = new Scanner(System.in);
		String Continue="Y";
		
		System.out.println("Salesman Name\t\t\t\t\tSales Amount");
		
		//Groups
		do
		{
				
			//User Input
			System.out.print("Enter Salesmans name:");
			Name = input.next();
			System.out.print("Enter Sales Amount:");
			Sales= input.nextInt();
			
			//Add to groups, output
			if (Sales >= 2000)
				{
				System.out.println(Name + "\t\t\t\t\t\t" + Sales);
				}
			else
				{ 
				System.out.println("");
				}
	
			//Continue
			System.out.print("Would you like to continue? (Y or N)");
			Continue = input.next();
			Continue=Continue.toUpperCase();
			if (Continue.equals("Y"))
				{
				Continue = "Y";
				}
			else
				{
				Continue = "N";
				}
		}while (Continue.equals("Y"));
		input.close();


	}

}
