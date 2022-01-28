/*
 * Programmer name: Jeremy M
 * Date: 10/3/17
 * Purpose: Using the Scanner package for user input for strings and integers 
 */
import java.util.Scanner;
public class VariableExample4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Declare variables
		String studentFirstname = "";
		String studentLastname = "";
		int studentNumber = 0;
		//Accept user input using the Scanner object
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the student's first name:");
		studentFirstname = input.next();
		System.out.print("Enter the student's last name:");
		studentLastname = input.next();
		System.out.print("Enter the student number:");
		studentNumber = input.nextInt();
		//Displaying student details
		System.out.println("Student first name: " + studentFirstname);
		System.out.println("Student last name: " + studentLastname);
		System.out.println("Student number: " + studentNumber);
		input.close();

	}

}
