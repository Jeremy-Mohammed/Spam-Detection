/*
 * Programmer name: Jeremy M
 * Date: 11/7/17
 * Purpose: To learn do while loops in java
 * Input: Age
 * Process: Match age to category
 * Output: Category
 */
import java.util.Scanner;
public class LoopsExample2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int age = 0;
		Scanner input = new Scanner (System.in);
		String answer = "";
		
		//Input age
		do 
		{
			//User input
			System.out.print("Enter an age: ");
			age = input.nextInt();
			
			//Output
			if (age == 10)
			{
				System.out.println("You are in Grade 5");
			}
			else if (age == 11)
			{
				System.out.println("You are in Grade 6");
			}
			else
			{
				System.out.println("Unknown");
			}
			
			//Continue?
			System.out.print("Do you wish to continue(y/n)?");
			answer = input.next();
			answer = answer.toUpperCase();
		}while(answer.equals("Y"));
		input.close();

	}

}
