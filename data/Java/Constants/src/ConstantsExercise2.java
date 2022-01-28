/*
 * Programmer name: Jeremy M
 * Date: 10/11/17
 * Purpose: To learn constants in Java
 * Input: Bill
 * Process: Tip, total bill
 * Output: Receipt 
 */
import java.util.Scanner;
public class ConstantsExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		final float TipRate = (float) 0.1;
		
		//Input bill
		Scanner input = new Scanner(System.in);
		System.out.println("What was the cost of your bill?");
		float Bill = input.nextInt();
		input.close();
		
		//Calculate tip, final bill
		float Tip = Bill*TipRate;
		float FBill = Tip + Bill;
		
		//Output Receipt
		System.out.println("Bill Amount: $" + Bill);
		System.out.println("Tip Amount: $" + Tip);
		System.out.println("Total Amount: $" + FBill);
		

	}

}
