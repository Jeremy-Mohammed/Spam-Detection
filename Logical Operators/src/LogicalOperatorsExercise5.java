/*
 * Programmer name: Jeremy M
 * Date: 10/20/17
 * Purpose: To learn logical operators in Java
 * Input: Price
 * Process: Price - discount
 * Output: Price, discounted price
 */
import java.util.Scanner;
public class LogicalOperatorsExercise5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		float Price = 0;
		float Discount = 0;
		
		//User Input
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the price:  ");
		Price = input.nextInt();
		
		//Find Discount
		if (Price > 250)
		{
			Discount = (float) (Price*0.75);
		}
		else if (Price <=250 && Price >=151)
		{
			Discount = (float) (Price*0.8);
		}
		else if (Price <=150 && Price >=100)
		{
			Discount = (float) (Price*0.9);
		}
		else
		{
			Discount = Price*1;
			
		}
		input.close();
		
		
		//Output
		System.out.println("Price: $" + Price);
		System.out.println("Price with Discount: $" + Discount);


	}

}
