/*
 * Programmer name: Jeremy M
 * Date: 11/6/17
 * Purpose: To learn while loops in java
 * Input: Ages
 * Process: Match age to category
 * Output: Info
 */
import java.util.Scanner;
public class LoopsExercise6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int counter=1;
		int Group1=0;
		int Group2=0;
		int Group3=0;
		int age=0;			
		Scanner input = new Scanner(System.in);
		
		//Input 10 students
		while(counter <= 10)
		{
			//User Input
			System.out.print("Enter an age:");
			age = input.nextInt();
			counter = counter+1;
			
			//Adding to groups
			if (age>=19)
			{
				Group3 = Group3+1;
			}
			else if (age>=16)
			{
				Group2 = Group2+1;
			}
			else if (age>=13)
			{
				Group1 = Group1+1;
			}	
			else
			{
				System.out.println("Invalid age");
			}	
			
		}
		
		input.close();
		System.out.println("Age Group\t\t\tNumber of Students\n");
		System.out.println("13 - 15\t\t\t\t" + Group1);
		System.out.println("16 - 18\t\t\t\t" + Group2);
		System.out.println("Above 18\t\t\t" + Group3);
	}

}
