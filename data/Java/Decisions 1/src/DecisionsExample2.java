/*
 * Programmer name: Jeremy M
 * Date: 10/13/17
 * Purpose: To learn decisions in Java
 * Input: Hours
 * Process: Match hours to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class DecisionsExample2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int hours=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter the number of hours worked per week");
		hours=input.nextInt();
		
		//Match Hours to Input
		if(hours<40)
		{
			System.out.println("You do not qualify for overtime pay");
		}
		else if (hours>=40)
		{
			System.out.println("Your overtime pay is twice your regular pay");
		}
		input.close();

	}

}
