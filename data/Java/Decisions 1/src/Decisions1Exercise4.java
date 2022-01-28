/*
 * Programmer name: Jeremy M
 * Date: 10/16/17
 * Purpose: To learn decisions in Java
 * Input: Code
 * Process: Match code to city
 * Output: City, population, province
 */
import java.util.Scanner;
public class Decisions1Exercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Code="";
		String City="";
		String Pop="";
		String Pro="";
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter a Code (T, M, V, O, E, C, R)");
		Code=input.next();
		
		//Match Code to Info
		if(Code.equals("T"))
		{
			Pro="Ontario";
			Pop="2 809 000";
			City="Toronto";
		}
		else if(Code.equals("M"))
		{
			Pro="Quebec";
			Pop="1 741 000";
			City="Montreal";
		}
		else if(Code.equals("V"))
		{
			Pro="British Columbia";
			Pop="647 000";
			City="Vancouver";
		}
		else if(Code.equals("O"))
		{
			Pro="Ontario";
			Pop="947 000";
			City="Ottawa";
		}
		else if(Code.equals("E"))
		{
			Pro="Alberta";
			Pop="928 000";
			City="Edmonton";
		}
		else if(Code.equals("C"))
		{
			Pro="Alberta";
			Pop="1 266 000";
			City="Calgary";
		}
		else if(Code.equals("R"))
		{
			Pro="Saskatchewan";
			Pop="216 000";
			City="Regina";
		}
		else
		{
			System.out.println("Invalid city code");
		}
		input.close();
		
		//Output
		System.out.println("City: " + City);
		System.out.println("Province: " + Pro);
		System.out.println("Population: " + Pop);

	}

}
