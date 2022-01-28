/*
 * Programmer name: Jeremy M
 * Date: 10/13/17
 * Purpose: To learn decisions in Java
 * Input: Code
 * Process: Match code to category
 * Output: Category number
 */
import java.util.Scanner;
public class DecisionsExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String employeeCode="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a employee Code (A, D or G)");
		employeeCode=input.next();
		
		//Match Code to Output
		if(employeeCode.equals("A"))
		{
			System.out.println("You belong to Category 1");
		}
		else if(employeeCode.equals("D"))
		{
			System.out.println("You belong to Category 2");
		}
		else if(employeeCode.equals("G"))
		{
			System.out.println("You belong to Category 3");
		}
		else
		{
			System.out.println("invalid code");
		}
		input.close();
	}

}
