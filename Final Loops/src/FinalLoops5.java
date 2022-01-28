/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn loops in java
 * Input: Names
 * Process: Add to groups
 * Output: Groups
 */
import java.util.Scanner;
public class FinalLoops5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int NTotal=0;
		int TTotal=0;
		String StaffT="";
		String Staff="";
		Scanner input = new Scanner(System.in);
		String Continue="Y";
		
		System.out.println("Teaching Staff\t\t\tNon-Teaching Staff");
		
		//Groups
		while (Continue.equals("Y"))
		{
				
			//User Input
			System.out.print("Enter staff member name:");
			Staff = input.next();
			System.out.print("(T)eaching Staff or (N)on-Teaching Staff?");
			StaffT= input.next();
			StaffT=StaffT.toUpperCase();
			
			//Add to groups, output
			if (StaffT.equals("T"))
				{
				System.out.println(Staff);
				TTotal+=1;
				}
			else if (StaffT.equals("N"))
				{ 
				System.out.println("\t\t\t\t" + Staff);
				NTotal+=1;
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
		}
		input.close();

		//Output
		System.out.println("Total: " + TTotal + "\t\t\tTotal: " + NTotal);


	}

}
