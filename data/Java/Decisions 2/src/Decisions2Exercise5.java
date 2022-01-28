/*
 * Programmer name: Jeremy M
 * Date: 10/17/17
 * Purpose: To learn decisions in Java
 * Input: Average
 * Process: Match average to message
 * Output: Message
 */
import java.util.Scanner;
public class Decisions2Exercise5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int average=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.println("Enter your average:");
		average=input.nextInt();
		
		//Match Average to Output
		if (average>=90)
		{
			System.out.println("You have been granted admission to the program");
		}
		else if (average>=80)
		{
			System.out.println("You have been granted an interview for the program");
		}
		else
		{
			System.out.println("You do not have the requirements to enter the program");
		}
		input.close();

	}

}
