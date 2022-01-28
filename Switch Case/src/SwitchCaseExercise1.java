/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: Category
 * Process: Match category to info
 * Output: Info
 */
import java.util.Scanner;
public class SwitchCaseExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Category = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a hurricane category:");
		Category = input.nextInt();
		
		//Match Category to Output
		switch(Category){
			case 1:
				System.out.println("74-95 mph or 64-82 kt or 119-153 km/hr");
				break;
			case 2:
				System.out.println("96-110 mph 83-95 kt or 154-177 km/hr");
				break;
			case 3:
				System.out.println("111-130 mph 96-113 kt or 178-209 km/hr");
				break;
			case 4:
				System.out.println("131-155 mph 114-135 kt or 210-249 km/hr");
				break;
			case 5:
				System.out.println("greater than 155 mph or 135 kt or 259 km/hr");
				break;
			default:
				System.out.println("Invalid Code");
				break;
			
		}
		input.close();


	}

}
