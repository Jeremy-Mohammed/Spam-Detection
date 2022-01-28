/*
 * Programmer name: Jeremy M
 * Date: 10/11/17
 * Purpose: To learn constants in Java
 * Input: Cost
 * Process: Tax, total cost
 * Output: Receipt
 */
import java.util.Scanner;
public class ConstantsExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		final float HSTRate = (float) 0.13;
		
		//Input cost
		Scanner input = new Scanner(System.in);
		System.out.println("What is the cost of the book?");
		float Cost = input.nextFloat();
		input.close();
		
		//Calculate tax, total cost
		float HST = Cost*HSTRate;
		float Total = HST + Cost;
		
		//Output receipt
		System.out.println("Book Cost: $" + Cost);
		System.out.println("HST (13%): $" + HST);
		System.out.println("Total Cost: $" + Total);
			

	}

}
