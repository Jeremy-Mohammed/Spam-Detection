/*
 * Programmer name: Jeremy M
 * Date: 11/29/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);	
		int Grade[]=new int[4];
		int Students[]=new int[2];
		String Name="";
		
		//User input
		System.out.println("Enter name:");
		Name=input.next();
		for(int i=0;i<Grade.length;i++)
		{
			System.out.println("Enter grade " + (i+1) + ":");
			
			//Match
			Grade[i]=input.nextInt();
			
			if (Grade[i]>=50 && Grade[i]<=100)
			{
				Students[0]++;
			}
			else if (Grade[i]<50)
			{
				Students[1]++;
			}
		}
		
		//Output
		System.out.println(Name +" has passed " + Students[0] + " and has failed " + Students[1] + " courses");
		input.close();
	}

}
