/*
 * Programmer name: Jeremy M
 * Date: 11/3/17
 * Purpose: This program asks the user to input 2 numbers
 * liberals and conservatives
 */
import java.util.Scanner;
public class LoopsExample4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int startNumber=0,endNumber=0;
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number you would like to start at: ");
		startNumber=input.nextInt();
		System.out.print("Enter a number you would like to end at: ");
		endNumber=input.nextInt();
		
		//Verify whether start number is less than end number
		if(startNumber>endNumber)
		{
			System.out.println("Start number should be lower than end numbers:");
			System.exit(0);
		}
		startNumber = startNumber + 1;
		while(startNumber < endNumber)
		{
			System.out.print(startNumber + " ");
			startNumber = startNumber +1;
		}
		input.close();
		

	}

}
