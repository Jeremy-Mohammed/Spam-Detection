/*
 * Programmer name: Jeremy M
 * Date: 10/20/17
 * Purpose: To learn logical operators in Java
 * Input: Books
 * Process: Match books to scholarship award
 * Output: Scholarship award
 */
import java.util.Scanner;
public class LogicalOperatorsExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Books = 0;
		int Scholar = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Number of books read: ");
		Books = input.nextInt();
		
		//Find Scholar
		if (Books >= 50)
		{
			Scholar = 1000;
		}
		else if (Books <=49 && Books >=40)
		{
			Scholar = 500;
		}
		else if (Books <=39 && Books >=20)
		{
			Scholar = 250;
		}
		else
		{
			Scholar = 0;
			
		}
		input.close();
			
		//Output
		System.out.print("Scholar Amount Awarded: $" + Scholar);


	}

}
