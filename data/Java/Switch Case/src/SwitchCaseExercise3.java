/*
 * Programmer name: Jeremy M
 * Date: 10/24/17
 * Purpose: To learn switch cases in Java
 * Input: Code
 * Process: Match code to phrase
 * Output: Phrase
 */
import java.util.Scanner;
public class SwitchCaseExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Pizza = 0;
		float PizzaC = 0;
		int Pop = 0;
		int PopC = 0;
		float CostPi = 0;
		int CostPo = 0;
		float Total = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter how many pizzas:");
		Pizza = input.nextInt();
		System.out.print("Enter how many cases of pop:");
		Pop = input.nextInt();
		
		//Find PizzaC
		switch(Pizza){
			case 10:
				PizzaC = 7;
				break;
			default:
				PizzaC = (float) 8.50;
				break;
		}
		
		//Find PopC
		switch(Pop){
			case 5:
				PopC = 6;
				break;
			default:
				PopC = 8;
				break;
		}
		input.close();
		
		//Process Total
		CostPi = Pizza*PizzaC;
		CostPo = Pop*PopC;
		Total = CostPi + CostPo;
		
		//Output
		System.out.println("Pizza Cost: $" + CostPi);
		System.out.println("Pop Cost: $ " + CostPo);
		System.out.println("Total Cost: $ " + Total);


	}

}
