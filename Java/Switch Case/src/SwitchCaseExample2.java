/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: Code
 * Process: Match code to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class SwitchCaseExample2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String eventCode = "";
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a event code:");
		eventCode = input.next();
		
		//Match Code to Output
		switch(eventCode){
			case "S":
				System.out.println("This is a social event");
				break;
			case "R":
				System.out.println("This is a religious holiday event");
				break;
			case "G":
				System.out.println("This is a sporting event");
				break;
			default:
				System.out.println("This event code does not exist");
				break;
			
		}
		input.close();


	}

}
