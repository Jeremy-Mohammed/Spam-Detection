/*
 * Programmer name: Jeremy M
 * Date: 11/9/17
 * Purpose: To learn for loops in java
 * Input: Name, age
 * Process: Age > 18 
 * Output: Message
 */
import java.util.Scanner;
public class ForLoopsExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String name="";
		int age=0;
		Scanner input = new Scanner(System.in);
		 
		for (int i=8; i>=0; i=i-1)
		{
			//User Input
			System.out.print("Enter your name:");
			name = input.next();
			System.out.print("Enter your age:");
			age = input.nextInt();
			
			//Output
			if (age>18)
			{
				System.out.println("\n" + name + ": Adult Student\n");
			}
			else
			{
				System.out.println("");
			}	
		}
		input.close();

	}

}
