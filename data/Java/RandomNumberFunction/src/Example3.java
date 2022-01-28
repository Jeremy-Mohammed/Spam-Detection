/*Example 3
 * Programmer name: Jeremy M
 * Date: 11/121/17
 * Purpose: Use random function
 *
 * Program compares a random number and a number inputed 
 * by the user to output a message
 */
import java.util.*;

public class Example3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random r1=new Random();
		int number1, number2;
		number1 =r1.nextInt(5)+1;
		Scanner input=new Scanner(System.in);
		System.out.println("Enter a number between 1 and 5");
		number2 = input.nextInt();
		if (number1 == number2)
		{
			System.out.println("You guessed the right number:");
		}
		else if (number1 > number2)
		{
			System.out.println("You guessed too low:");
		}
		else if (number1 < number2)
		{
			System.out.println("You guessed too high:");
		}
		input.close();

	}

}
