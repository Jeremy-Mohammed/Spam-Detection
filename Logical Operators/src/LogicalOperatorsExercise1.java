/*
 * Programmer name: Jeremy M
 * Date: 10/19/17
 * Purpose: To learn logical operators in Java
 * Input: Persons
 * Process: Persons*Charge
 * Output: Cost
 */
import java.util.Scanner;
public class LogicalOperatorsExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Persons = 0;
		int Charge = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the amount of people registered:  ");
		Persons = input.nextInt();
		
		//Find Charge
		if (Persons > 11)
		{
			Charge = Persons*60;
		}
		else if (Persons <=10 && Persons >=5)
		{
			Charge = Persons*80;
		}
		else if (Persons <=4 || Persons >=1)
		{
			Charge = Persons*100;
		}
		else
		{
			Charge = Persons*0;
			
		}
		input.close();
			
		//Output
		System.out.print("$" + Charge + " is owed by the company.");

	}

}
