/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn loops in java
 * Input: Name, Sport
 * Process: Format
 * Output: Format
 */
import java.util.Scanner;
public class FinalLoops2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Name="";
		String Sport="";
		
		Scanner input = new Scanner(System.in);

		System.out.println("Enter three a sports team and the sport they play:\n\n");
		System.out.println("\tSports Teams");
		System.out.println("Team Name\t\tSport");
		 
		for (int i=3; i>0; i=i-1)
		{
			//User Input
			Name = input.next();
			Sport = input.next();
					
			//Output
			System.out.println(Name + "\t\t\t" + Sport);
			
		}
		input.close();
	}

}
