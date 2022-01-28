/*
 * Programmer name: Jeremy M
 * Date: 10/10/17
 * Purpose: To learn variables in Java
 * Input: Numbers
 * Output: Numbers in one line
 */
import java.util.Scanner;
public class VariablesExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input Numbers
		Scanner input = new Scanner(System.in);
		System.out.println("What is the first number?");
		int First = input.nextInt();
		System.out.println("What is the second number?");
		int Second = input.nextInt();
		System.out.println("What is the third number?");
		int Third = input.nextInt();
		System.out.println("What is the fourth number?");
		int Fourth = input.nextInt();
		input.close();
		
		//Output Numbers together
		System.out.println(First + "," + Second + "," + Third + "," + Fourth);
		

	}

}
