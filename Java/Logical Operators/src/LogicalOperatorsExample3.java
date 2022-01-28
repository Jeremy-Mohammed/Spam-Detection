/*
 * Programmer name: Jeremy M
 * Date: 10/19/17
 * Purpose: To learn logical operators in Java
 * Input: Grade
 * Process: Match grade to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class LogicalOperatorsExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Grade = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a student's grade: ");
		Grade = input.nextInt();
		
		//Match Grade to Output
		if (Grade < 12)
		{
			System.out.println("The grade does not exist");
		}
		else if (Grade == 11 || Grade == 12)
		{
			System.out.println("You are the senior students in high school");
		}
		else if (Grade == 9 || Grade == 10)
		{
			System.out.println("You are the junior students in high school");
		}
		else if (Grade >= 1 && Grade <=8)
		{
			System.out.println("Elementary school grade");
		}
		else
		{
			System.out.println("Invalid grade");
		}
		input.close();
			

	}

}
