/*
 * Programmer name: Jeremy M
 * Date: 10/19/17
 * Purpose: To learn logical operators in Java
 * Input: Value
 * Process: Match value to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class LogicalOperatorsExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Value=0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number");
		Value = input.nextInt();
		
		//Match Value to Output
			if(Value >= 1500 && Value <=3000)
			{
				System.out.println("Within Range");
			}
			else
			{
				System.out.println("Out of Range");
			}
			input.close();

	}

}
