/*
 * Programmer name: Jeremy M
 * Date: 10/10/17
 * Purpose: To learn variables in Java
 * Input: Hours
 * Process: Add up hours
 * Output: Time report
 */
import java.util.Scanner;
public class VariablesExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input Hours
		Scanner input = new Scanner(System.in);
		System.out.println("How many hours did you work on Monday?");
		float Monday = input.nextFloat();
		System.out.println("How many hours did you work on Tuesday?");
		float Tuesday = input.nextFloat();
		System.out.println("How many hours did you work on Wednesday?");
		float Wednesday = input.nextFloat();
		System.out.println("How many hours did you work on Thursday?");
		float Thursday = input.nextFloat();
		System.out.println("How many hours did you work on Friday?");
		float Friday = input.nextFloat();
		System.out.println("How many hours did you work on Saturday?");
		float Saturday = input.nextFloat();
		System.out.println("How many hours did you work on Sunday?");
		float Sunday = input.nextFloat();
		input.close();
		
		//Find total hours
		float Weekdays = (Monday + Tuesday + Wednesday + Thursday + Friday);
		float Weekends = (Saturday + Sunday);
		
		//Output report
		System.out.println("Day\t\t\tHours Worked");
		System.out.println("\nMonday\t\t\t" + Monday);
		System.out.println("Tuesday\t\t\t" + Tuesday);
		System.out.println("Wednesday\t\t" + Wednesday);
		System.out.println("Thursday\t\t" + Thursday);
		System.out.println("Friday\t\t\t" + Friday);
		System.out.println("Total Weekday Hours\t" + Weekdays);
		System.out.println("\nSaturday\t\t" + Saturday);
		System.out.println("Sunday\t\t\t" + Sunday);
		System.out.println("Total Weekend Hours\t" + Weekends);
		

	}

}
