/*
 * Programmer Name: Jeremy Mohammed
 * Purpose: To learn user-defined methods in Java
 * Date: 12/12/17
 */
import java.util.*;
public class Example5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int yearofbirth=0, currentyear=0;
		Scanner input=new Scanner(System.in);
		
		//User input
		System.out.println("Enter your year of birth: ");
		yearofbirth=input.nextInt();
		System.out.println("Enter the current year: ");
		currentyear=input.nextInt();
		
		//Output
		System.out.println("In 2016, you were " + calculateage(yearofbirth) + " years old.");
		System.out.println("In " + currentyear + " you are " + calculateage(yearofbirth,currentyear) + " years old.");
		input.close();
	}
	
	//Age in 2016
	public static int calculateage(int yearofbirth)
	{
		int yrs;
		yrs=2016-yearofbirth;
			return yrs;
	}
	//Current age
	public static int calculateage(int yearofbirth, int currentyear)
	{
		int yrs;
		yrs=currentyear-yearofbirth;
		return yrs;
	}
}
