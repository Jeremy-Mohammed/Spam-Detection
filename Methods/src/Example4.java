/*
 * Programmer Name: Jeremy Mohammed
 * Purpose: To learn user-defined methods in Java
 * Date: 12/12/17
 */
import java.util.*;
public class Example4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);
		System.out.println("Please input the price of the item:");
		double price = input.nextDouble();
		System.out.println("The taxes on this item= $" + calculatetax(price));
		input.close();
	}
	
	//Tax
	public static double calculatetax(double price)
	{
		double tax=price*0.13;
		return tax;
	}
}
