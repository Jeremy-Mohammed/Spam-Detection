/*
 * Programmer name: Jeremy M
 * Date: 10/13/17
 * Purpose: To learn decisions in Java
 * Input: Average
 * Process: Match average to letter grade
 * Output: Letter grade
 */
import java.util.Scanner;
public class DecisionsExample4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int average=0;
		String gradeLetter="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter your average:");
		average=input.nextInt();
		
		//Find Grade Letter
		if (average>=90)
		{
			gradeLetter="A";
		}
		else if (average>=70)
		{
			gradeLetter="B";
		}
		else if (average>=60)
		{
			gradeLetter="C";
		}
		else if (average>=50)
		{
			gradeLetter="D";
		}
		else
		{
			gradeLetter="F";
		}
		
		//Output
		System.out.println("With an average of " + average + "% your grade is " + gradeLetter);
		input.close();

	}
}
