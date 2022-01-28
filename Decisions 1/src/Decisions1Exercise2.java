/*
 * Programmer name: Jeremy M
 * Date: 10/16/17
 * Purpose: To learn decisions in Java
 * Input: Age
 * Process: Match age to grade
 * Output: Grade
 */
import java.util.Scanner;
public class Decisions1Exercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int age=0;
		
		//User Input
		Scanner input=new Scanner(System.in);
		System.out.print("Enter age:");
		age=input.nextInt();
		
		//Match Age to Output
		if (age==4)
		{
			System.out.println("You are in Junior Kindergarten");
		}
		else if (age==5)
		{
			System.out.println("You are in Senior Kindergarten");
		}
		else if (age==6)
		{
			System.out.println("You are in Grade 1");
		}
		else
		{
			System.out.println("Grade unknown");
		}
		input.close();

	}

}
