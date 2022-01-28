/*
 * Programmer name: Jeremy M
 * Date: 10/16/17
 * Purpose: To learn decisions in Java
 * Input: Code
 * Process: Match code to price
 * Output: Price
 */
import java.util.Scanner;
public class Decisions1Exercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a Code (G, D, M)");
		Code=input.next();
		
		//Match Code to Output
		if(Code.equals("G"))
		{
			System.out.println("Price of item is $2.99");
		}
		else if(Code.equals("D"))
		{
			System.out.println("Price of item is $5.99");
		}
		else if(Code.equals("M"))
		{
			System.out.println("Price of item is $.99");
		}
		else
		{
			System.out.println("invalid code");
		}
		input.close();

	}

}
