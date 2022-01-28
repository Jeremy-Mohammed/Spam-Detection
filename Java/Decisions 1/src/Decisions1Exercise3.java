/*
 * Programmer name: Jeremy M
 * Date: 10/16/17
 * Purpose: To learn decisions in Java
 * Input: Sales
 * Process: Calculate commission
 * Output: Commission
 */
import java.util.Scanner;
public class Decisions1Exercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		float sales=0;
		float CR=0;
		float Commission=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter sales amount:");
		sales=input.nextInt();
		
		//Find CR
		if (sales>=300)
		{
			CR=(float) 0.03;
		}
		else if (sales>=100)
		{
			CR=(float) 0.01;
		}
		else
		{
		}
		
		//Process Commission
		Commission=(float)(sales*CR);
		
		//Output
		System.out.println("Sales Amount: $" + sales);
		System.out.println("Commission Amount: $" + Commission);
		input.close();


	}

}
