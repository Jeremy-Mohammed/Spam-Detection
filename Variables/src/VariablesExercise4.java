/*
 * Programmer name: Jeremy M
 * Date: 10/5/17
 * Purpose: To learn variables in Java
 * Input: Names, age
 * Process: Finding average
 * Output: Display ages, average
 */
import java.util.Scanner;
public class VariablesExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input info
		Scanner input = new Scanner(System.in);
		System.out.println("What is the first siblings age?");
		float Age1 = input.nextFloat();
		System.out.println("What is the second siblings age?");
		float Age2 = input.nextFloat();
		System.out.println("What is the third siblings age?");
		float Age3 = input.nextFloat();
		System.out.println("What is the fourth siblings age?");
		float Age4 = input.nextFloat();
		input.close();
		
		//Calculate average
		float Average = (Age1 + Age2 + Age3 + Age4)/4;
		
		//Output total
		System.out.println("\nThe ages of the siblings are " + Age1 + ", " + Age2 + ", " + Age3 + ", " + Age4 + ".");
		System.out.println("The average of ages is " + Average + ".");


	}

}
