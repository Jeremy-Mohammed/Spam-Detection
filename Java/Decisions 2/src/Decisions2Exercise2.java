/*
 * Programmer name: Jeremy M
 * Date: 10/17/17
 * Purpose: To learn decisions in Java
 * Input: Number of items
 * Process: Compare to 20
 * Output: Phrase
 */
import java.util.Scanner;
public class Decisions2Exercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int items=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter the number of items made on the daily average");
		items=input.nextInt();
		
		//Match Items to Output
		if(items>=20)
		{
			System.out.println("Well done, you have earned a pay raise");
		}
		else
		{
			System.out.println("You have been fired");
		}
		input.close();

	}

}
