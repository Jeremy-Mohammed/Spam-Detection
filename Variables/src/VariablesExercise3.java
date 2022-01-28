/*
 * Programmer name: Jeremy M
 * Date: 10/5/17
 * Purpose: To learn variables in Java
 * Input: Expenses
 * Process: Expenses - scholar
 * Output: Total cost
 */
import java.util.Scanner;
public class VariablesExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		String Name="";
		
		//Input expenses
		System.out.println(" University Expenses Calculator");
		System.out.println("________________________________\n\n");
		Scanner input = new Scanner(System.in);
		System.out.println("What is the name of the university are you attending?");
		Name = input.next();
		System.out.println("What is the cost of rent?");
		float Rent = input.nextFloat();
		System.out.println("What is the cost of tuition?");
		float Tuition = input.nextFloat();
		System.out.println("What is the cost of books?");
		float Books = input.nextFloat();
		System.out.println("How much is the given scholarship worth?");
		float Scholar = input.nextFloat();
		System.out.println("");
		input.close();
		
		//Calculate total expenses
		float Total = Rent + Tuition + Books - Scholar;
		
		//Output total
		System.out.println("Attending " + Name + " will cost a total of $" + Total + ".");

	}

}
