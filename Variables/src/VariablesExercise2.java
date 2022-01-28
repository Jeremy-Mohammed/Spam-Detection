/*
 * Programmer name: Jeremy M
 * Date: 10/2/17
 * Purpose: To learn variables in Java
 * Input: Names, birth, address
 * Output: Names, birth, address
 */
import java.util.Scanner;
public class VariablesExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		String Name="";
		String Date="";
		String Address="";
		
		//Input name, date of birth, address
		Scanner input = new Scanner(System.in);
		System.out.println("Enter your name");
		Name = input.next();
		System.out.println("Enter your date of birth");
		Date = input.next();
		System.out.println("Enter your Address");
		Address = input.next();
		input.close();
		
		//Output info
		System.out.println("My name is " + Name);
		System.out.println("My date of birth is " + Date);
		System.out.println("My address is " + Address);
		

	}

}
