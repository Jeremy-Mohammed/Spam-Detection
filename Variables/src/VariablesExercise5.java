/*
 * Programmer name: Jeremy M
 * Date: 10/5/17
 * Purpose: To learn variables in Java
 * Input: Pay
 * Process: Finding raise, final pay
 * Output: Basic pay, raise, final pay
 */
import java.util.Scanner;
public class VariablesExercise5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Input Basic Pay
		Scanner input = new Scanner(System.in);
		System.out.println("What is the basic pay of employee 1?");
		float BPay1 = input.nextFloat();
		System.out.println("What is the basic pay of employee 2?");
		float BPay2 = input.nextFloat();
		System.out.println("What is the basic pay of employee 3?");
		float BPay3 = input.nextFloat();
		input.close();
		
		//Calculate raise
		float Raise1 = (float) (BPay1 * 0.02);
		float RPay1 = Raise1 + BPay1;
		float Raise2 = (float) (BPay2 * 0.04);
		float RPay2 = Raise2 + BPay2;
		float Raise3 = (float) (BPay3 * 0.01);
		float RPay3 = Raise3 + BPay3;
		
		//Output total
		System.out.println("Employee 1");
		System.out.println("Basic Pay: $" + BPay1 + "\nRaise Amount: $" + Raise1 + "\nPay With Raise: $" + RPay1);
		System.out.println("\nEmployee 2");
		System.out.println("Basic Pay: $" + BPay2 + "\nRaise Amount: $" + Raise2 + "\nPay With Raise: $" + RPay2);
		System.out.println("\nEmployee 3");
		System.out.println("Basic Pay: $" + BPay3 + "\nRaise Amount: $" + Raise3 + "\nPay With Raise: $" + RPay3);

	}
            
}