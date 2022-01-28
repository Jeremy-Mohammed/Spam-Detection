/*
 * Programmer name: Jeremy M
 * Date: 10/30/17
 * Purpose: To practice Java skills
 * Input: Copies
 * Process: Cost
 * Output: Total cost, cost per page, copies
 */
import java.util.Scanner;
public class Exercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		float CostPP = 0;
		float Total = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("How many copies are needed?");
		int Copies = input.nextInt();
		
		//Find CostPP
		if (Copies>1000)
		{
			CostPP = (float) 0.25;
		}
		else if (Copies>=750)
		{
			CostPP = (float) 0.26;
		}
		else if (Copies>=500)
		{
			CostPP = (float) 0.27;
		}
		else if (Copies>=100)
		{
			CostPP = (float) 0.28;
		}
		else if (Copies>=0)
		{
			CostPP = (float) 0.30;
		}
		
		//Process Total
		Total = (float) Copies*CostPP;
		
		//Output
		System.out.println("Number of Copies to be Printed: " + Copies);
		System.out.println("Price Per Copy: $" + CostPP);
		System.out.println("Total Cost: $" + Total);
		input.close();
	}

}
