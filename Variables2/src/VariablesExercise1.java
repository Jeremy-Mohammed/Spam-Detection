/*
 * Programmer name: Jeremy M
 * Date: 10/10/17
 * Purpose: To learn variables in Java
 * Input: Birth year, current year
 * Process: Current year - birth year
 * Output: Age
 */
import java.util.Scanner;
public class VariablesExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input Birth year, current year
		Scanner input = new Scanner(System.in);
		System.out.println("What is the year you were born?");
		int Birth = input.nextInt();
		System.out.println("What is the current year?");
		int Current = input.nextInt();
		input.close();
		
		//Find age
		int Age = Current - Birth; 
		
		//Output age
		System.out.println("You are/will be " + Age + ".");
		

	}

}
