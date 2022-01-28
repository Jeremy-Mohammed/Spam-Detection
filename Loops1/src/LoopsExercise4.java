/*
 * Programmer name: Jeremy M
 * Date: 11/3/17
 * Purpose: To learn while loops in java
 * Input: Price
 * Process: Find average
 * Output: Prices and average
 */
import java.util.Scanner;

public class LoopsExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int counter=1;
		float price=0;
		float total=0;
		float average=0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the price of 10 items");
		
		//Loop for price input
		while (counter<=10)
		{
			price = input.nextFloat();
			total = total+price;
			//Output price
			System.out.println("Item " + counter + ": $" + price);
			counter=counter+1;
		}
		
		//Find average
		average=total/10;
		
		//Output average
		System.out.println ("The average price is: $" + average);
		input.close();
	}

}
