/*
 * Programmer name: Jeremy M
 * Date: 10/13/17
 * Purpose: To learn decisions in Java
 * Input: Grade
 * Process: Match grade to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class DecisionsExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int gradeLevel=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter your grade level (9-12):");
		gradeLevel=input.nextInt();
		
		//Match Grade to Output
		if (gradeLevel == 9)
		{
			System.out.println("You will be participating in \'Take our kids to work\' day");
		}
		else if (gradeLevel == 10)
		{
			System.out.println("You will be writing the Literacy test");
		}
		else if (gradeLevel == 11)
		{
			System.out.println("You will be researching your post secondary options");
		}
		else if (gradeLevel == 12)
		{
			System.out.println("You will be attending the University Fair");
		}
		else
		{
			System.out.println("Invalid choice");
		}
		input.close();
		}

	}

