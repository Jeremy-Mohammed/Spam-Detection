/*
 * Programmer name: Jeremy M
 * Date: 10/19/17
 * Purpose: To learn logical operators in Java
 * Input: Code
 * Process: Match code to info
 * Output: Info
 */
import java.util.Scanner;
public class LogicalOperatorsExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		int Fee=0;
		String Pro="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a Code (RV or 1, OS or 2, OV or 3)");
		Code=input.next();
		
		//Match Code to Info
		if(Code.equals("RV")||Code.equals("1"))
		{
			Pro="Rabies Vaccination";
			Fee=15;
		}
		else if(Code.equals("OS")||Code.equals("2"))
		{
			Pro="Other Shots";
			Fee=5;
		}
		else if(Code.equals("OV")||Code.equals("3"))
		{
			Pro="Office Visit";
			Fee=10;
		}
		else
		{
			System.out.println("Invalid code province code");
			Pro="-";
			Fee=0;
		}
		input.close();
		
		//Output
		System.out.println("\nProcedure: " + Pro);
		System.out.println("Fee: $" + Fee);




	}

}
