/*
 * Programmer name: Jeremy M
 * Date: 10/31/17
 * Purpose: To practice Java skills
 * Input: Eggs
 * Process: Cost
 * Output: Total cost, eggs
 */
import java.util.Scanner;
public class Exercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		float CostPP = 0;
		float Total = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("How many eggs are to be purchase?");
		int Eggs = input.nextInt();
		
		//Find Costpp
		if (Eggs>133)
		{
			CostPP = (float) 0.35/12;
		}
		else if (Eggs>=73)
		{
			CostPP = (float) 0.40/12;
		}
		else if (Eggs>=37)
		{
			CostPP = (float) 0.45/12;
		}
		else if (Eggs>=0)
		{
			CostPP = (float) 0.50/12;
		}
		else
		{
			CostPP = (float) 0;
		}
		
		//Process Total
		Total = Eggs*CostPP;
		
		//Output
		System.out.println("Eggs purchased: " + Eggs);
		System.out.println("Bill: $" + Total);
		input.close();
	}

}

