/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: Code
 * Process: Match code to info
 * Output: Info
 */
import java.util.Scanner;
public class SwitchCaseExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String StateCode = "";
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a state code:");
		StateCode = input.next();
		
		//Match State to Output
		switch(StateCode){
			case "H":
				System.out.println("State Code: H");
				System.out.println("State Name: Hawaii");
				System.out.println("Shipping Charge: $25.00");
				break;
			case "O":
				System.out.println("State Code:O ");
				System.out.println("State Name: Oregon");
				System.out.println("Shipping Charge: $30.00");
				break;
			case "C":
				System.out.println("State Code: C");
				System.out.println("State Name: California");
				System.out.println("Shipping Charge: $32.50");
				break;
			case "T":
				System.out.println("State Code: T");
				System.out.println("State Name: Texas");
				System.out.println("Shipping Charge: $45.00");
				break;
			default:
				System.out.println("State Name: Other");
				System.out.println("No service in this state");
				break;
			
		}
		input.close();

	}

}
