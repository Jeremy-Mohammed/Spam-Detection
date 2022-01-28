/*
 * Programmer name: Jeremy M
 * Date: 10/3/17
 * Purpose: Using the Scanner package for user input for strings & numbers with decimal points
 */
import java.util.Scanner;
public class VariableExample5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Declare Variables
		String petName = "";
		int petAge = 0;
		float petHeight = 0;
		
		//Accept user input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the name of your pet: ");
		petName = input.next();
		
		System.out.print("Enter the age of your pet: ");
		petAge = input.nextInt();
		
		System.out.println("Enter the height of your pet: ");
		petHeight = input.nextFloat();
		
		input.close();
		System.out.println("Hello " + petName + "\nAre you " + petAge + " years old?\nAre you " + petHeight + " ft. tall?");
		
		
		

	}

}
