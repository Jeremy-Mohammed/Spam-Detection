/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: College year
 * Process: Match year to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class SwitchCaseExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int CollegeYear = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a college year");
		CollegeYear = input.nextInt();
		
		//Match Year to Output
		switch(CollegeYear){
			case 1:
				System.out.println("Freshman");
				break;
			case 2:
				System.out.println("Sophomore");
				break;
			case 3:
				System.out.println("Junior");
				break;
			case 4:
				System.out.println("Senior");
				break;
			default:
				System.out.println("Invalid Code");
				break;
			
		}
		input.close();

	}

}
