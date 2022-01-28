/*
 * Programmer name: Jeremy M
 * Date: 10/20/17
 * Purpose: To learn logical operators in Java
 * Input: Years
 * Process: Match years to info
 * Output: Info
 */
import java.util.Scanner;
public class LogicalOperatorsExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Years = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Years of skiing experience: ");
		Years = input.nextInt();
		
		//Match Years to Output
		if (Years >= 9)
		{
			System.out.println("You have been placed in Professional Class");
		}
		else if (Years <=8 && Years >=6)
		{
			System.out.println("You have been placed in Advanced Class");
		}
		else if (Years <=5 && Years >=3)
		{
			System.out.println("You have been placed in Intermediate Class");
		}
		else if (Years <=2 && Years >=1)
		{
			System.out.println("You have been placed in Novice Class");
		}
		else
		{
			System.out.println("You have been placed in Beginner Class");
		}
		input.close();



	}

}
