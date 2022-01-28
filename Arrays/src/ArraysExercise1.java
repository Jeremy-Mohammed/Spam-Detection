/*
 * Programmer name: Jeremy M
 * Date: 11/29/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		String durhamschools[]=new String[5];
		Scanner input=new Scanner(System.in);
		
		//Loop inputs
		for(int i=0; i < durhamschools.length;i++)
		{
			System.out.println("Enter a school in the Durham Region");
			durhamschools[i]=input.nextLine();
		}
		
		//Output
		System.out.println("Schools in the Durham Region:");
		for(int i=0; i < durhamschools.length;i++)
		{
			System.out.println(durhamschools[i]);
		}
		input.close();

	}

}
