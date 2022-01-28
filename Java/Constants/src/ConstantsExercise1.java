/*
 * Programmer name: Jeremy M
 * Date: 10/10/17
 * Purpose: To learn constants in Java
 * Input: Name, student number, average
 * Output: Format
 */
import java.util.Scanner;
public class ConstantsExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		final String School = "J. Clarke Richardson";
		
		//Input info
		Scanner input = new Scanner(System.in);
		System.out.println("What is your first name?");
		String Name = input.next();
		System.out.println("What is your Student Number?");
		String SNumber = input.next();
		System.out.println("What is your average?");
		String Average = input.next();
		input.close();
		
		//Output format
		System.out.println("Student Name: " + Name);
		System.out.println("Student Number: " + SNumber);
		System.out.println("Average Grade: " + Average + "%");
		System.out.println("School: " + School);
		

	}

}
