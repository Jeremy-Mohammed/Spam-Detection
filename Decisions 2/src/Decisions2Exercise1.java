/*
 * Programmer name: Jeremy M
 * Date: 10/17/17
 * Purpose: To learn decisions in Java
 * Input: Code
 * Process: Match code to car
 * Output: Model and company name
 */
import java.util.Scanner;
public class Decisions2Exercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		String Model="";
		String Company="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a Code (EX, EP, MDX, TL)");
		Code=input.next();
		
		//Find Model and Company
		if(Code.equals("EX"))
		{
			Model="Expedition";
			Company="Ford";
		}
		else if(Code.equals("EP"))
		{
			Model="Explorer";
			Company="Ford";
		}
		else if(Code.equals("MDX"))
		{
			Model="Acura MDX";
			Company="Acura";
		}
		else if(Code.equals("TL"))
		{
			Model="Acura 3.2TL";
			Company="Acura";
		}

		else
		{
			System.out.println("Invalid code");
			Model="-";
			Company="-";
		}
		input.close();
		
		//Output
		System.out.println("Model Name: " + Model);
		System.out.println("Company Name: " + Company);


	}

}
