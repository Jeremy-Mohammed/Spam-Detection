/*
 * Programmer name: Jeremy M
 * Date: 10/10/17
 * Purpose: To learn variables in Java
 * Input: Inches
 * Output: Centimeters
 */
import java.util.Scanner;
public class VariablesExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input Length
		Scanner input = new Scanner(System.in);
		System.out.println("What is the length of the desk in inches?");
		float Inches = input.nextInt();
		input.close();
		
		//Inches to centimeters
		float INtoCM = (float) 2.54;
		float Centimeters = Inches*INtoCM;
		
		//Output centimeters
		System.out.println("The desk is " + Centimeters + "cm in length.");

	}

}
