/*
 * Programmer name: Jeremy M
 * Date: 10/17/17
 * Purpose: To learn decisions in Java
 * Input: Code, price
 * Process: Calculate tax, total
 * Output: Tax rate, price, tax, total, province
 */
import java.util.Scanner;
public class Decisions2Exercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		float Price=0;
		double TaxR=0;
		String Pro="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a Code (ON, QC, BC, AB)");
		Code=input.next();
		System.out.print("Enter the price of the item");
		Price=input.nextFloat();
		
		//Match Code to Info
		if(Code.equals("ON"))
		{
			Pro="Ontario";
			TaxR=13;
		}
		else if(Code.equals("QC"))
		{
			Pro="Quebec";
			TaxR=1;
		}
		else if(Code.equals("BC"))
		{
			Pro="British Columbia";
			TaxR=12;
		}
		else if(Code.equals("AB"))
		{
			Pro="Alberta";
			TaxR=7;
		}

		else
		{
			System.out.println("Invalid code province code");
			Pro="-";
			TaxR=0;
		}
		input.close();
		
		//Process Total
		float Tax=(float) (Price*TaxR/100);
		float Total=(float) (Price+Tax);
		
		//Output
		System.out.println("\nSales tax in " + Pro + " is " + TaxR + "%");
		System.out.println("Price of item: $" + Price);
		System.out.println("Sales tax: $" + Tax);
		System.out.println("Total with Taxes: $" + Total);
		System.out.println("Province: " + Pro);



	}

}
