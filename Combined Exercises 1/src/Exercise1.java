/*
 * Programmer name: Jeremy M
 * Date: 10/30/17
 * Purpose: To practice Java skills
 * Input: Name, age, grade
 * Process: Pick option
 * Output: Option
 */
import java.util.Scanner;
public class Exercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Code = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("What is your name?");
		String Name = input.next();
		System.out.print("What is your age?");
		String Age = input.next();
		System.out.print("What is your grade level?");
		String Grade = input.next();
		System.out.print("Please enter a code (1, 2, 3):");
		Code = input.nextInt();
		
		//Match Code to Output
		if (Code == 1)
		{
			System.out.println("Name: " + Name);
		}
		else if (Code == 2)
		{
			System.out.println("Age: " + Age);
		}
		else if (Code == 3)
		{
			System.out.println("Grade Level: " + Grade);
		}
		else
		{
			System.out.println("Invalid input");
		}
		input.close();

	}

}
