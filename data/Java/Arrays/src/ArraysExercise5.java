/*
 * Programmer name: Jeremy M
 * Date: 11/30/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);	
		int Score[]=new int[20];
		int Students[]=new int[4];
		
		//User input
		for(int i=0;i<Score.length;i++)
		{
			System.out.println("Enter score " + (i+1) + ":");
			Score[i]=input.nextInt();
			
			if (Score[i]>=80 && Score[i]<=100)
			{
				Students[0]++;
			}
			else if (Score[i]>=60 && Score[i]<=79)
			{
				Students[1]++;
			}
			else if (Score[i]>=50 && Score[i]<=59)
			{
				Students[2]++;
			}
			else if (Score[i]<50)
			{
				Students[3]++;
			}
		}
		
		//Output
		System.out.println("Range\t\tStudents");
		System.out.println("80-100 Marks\t" + Students[0]);
		System.out.println("60-79 Marks\t" + Students[1]);
		System.out.println("50-59 Marks\t" + Students[2]);
		System.out.println("Below 50 Marks\t" + Students[3]);
		input.close();
	}

}
