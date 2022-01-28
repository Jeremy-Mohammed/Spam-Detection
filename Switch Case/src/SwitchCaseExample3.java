/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: Code
 * Process: Match code to month
 * Output: Month
 */
import java.util.Scanner;
public class SwitchCaseExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Month = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a month (1-12)");
		Month = input.nextInt();
		
		//Match Month to Output
		switch(Month){
			case 1:
				System.out.println("January");
				break;
			case 2:
				System.out.println("February");
				break;
			case 3:
				System.out.println("March");
				break;
			case 4:
				System.out.println("April");
				break;
			case 5:
				System.out.println("May");
				break;
			case 6:
				System.out.println("June");
				break;
			case 7:
				System.out.println("July");
				break;
			case 8:
				System.out.println("August");
				break;
			case 9:
				System.out.println("September");
				break;
			case 10:
				System.out.println("October");
				break;
			case 11:
				System.out.println("November");
				break;
			case 12:
				System.out.println("December");
				break;
			default:
				System.out.println("Invalid Code");
				break;
			
		}
		input.close();


	}

}
