/*
 * Programmer name: Jeremy M
 * Date: 10/17/17
 * Purpose: To learn decisions in Java
 * Input: Code
 * Process: Match code to product
 * Output: Message
 */
import java.util.Scanner;
public class Decisions2Exercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Do you prefer Pepsi(P) or Coca Cola(C)?");
		Code=input.next();
		
		//Match Code to Output
		if(Code.equals("C"))
		{
			System.out.println("Thank you for choosing Coca Cola");
		}
		else if(Code.equals("P"))
		{
			System.out.println("Thank you for choosing Pepsi");
		}
		else
		{
			System.out.println("Invalid Code");
		}
		input.close();

	}

}
