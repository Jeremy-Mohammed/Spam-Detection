/*
 * Programmer name: Jeremy M
 * Date: 11/29/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);	
		int num=0;
		String letter[]={"A","B","C","E","F","G","H","I","J","K","L","M","P","Q","R","S","T","U","V","W","Y","Z"};

		//User input
		System.out.println("Enter an number from (1-26) : ");
		num=input.nextInt();
		
		//Check for valid input
		if (num>=1 && num <=26)
		{
		System.out.println("Alphabet "+num+" is the letter "+letter[num-1]);
		}
		else
		{
			System.out.println("Invalid input");
		}
		input.close();

	}

}
