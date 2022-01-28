/*
 * Programmer name: Jeremy M
 * Date: 11/3/17
 * Purpose: To learn while loops in java
 * Input: Number
 * Process: Find multiples
 * Output: First 10 multiples
 */
import java.util.Scanner;
public class LoopsExercise5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int counter=1;
		float number=0;
		float answer=0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number");
		number = input.nextFloat();
		
		//Output numbers
		while(counter <= 10)
		{
			
			answer=number*counter;
			System.out.println(number + "*" + counter + " = " + answer);
			counter = counter +1;
		}
		input.close();
		


	}

}
