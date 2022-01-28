/*
 * Programmer name: Jeremy M
 * Date: 10/19/17
 * Purpose: To learn logical operators in Java
 * Input: Age
 * Process: Match age to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class LogicalOperatorsExample2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int age=0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a student's age:");
		age = input.nextInt();
		
		//Match Age to Output
		if (age < 0)
		{
			System.out.println("Invalid age");
		}
		else if (age >=3 && age <= 12)
		{
			System.out.println("Child");
		}
		else if (age >=13 && age <= 19)
		{
			System.out.println("Teen");
		}
		else if (age >=20 && age <= 64)
		{
			System.out.println("Adult");
		}
		else if (age >=65)
		{
			System.out.println("Senior Citizen");
		}
		else
		{
			System.out.println("Infant");
		}
		input.close();

	}

}
