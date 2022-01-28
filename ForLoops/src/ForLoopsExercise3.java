/*
 * Programmer name: Jeremy M
 * Date: 11/9/17
 * Purpose: To learn for loops in java
 * Input: Grades
 * Process: Match grades to category
 * Output: Format info
 */
import java.util.Scanner;
public class ForLoopsExercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int G1=0, G2=0, G3=0, G4=0, G5=0, G6=0, grade=0;
		Scanner input = new Scanner(System.in);
		 
		for (int i=10; i>=0; i=i-1)
		{
			//User Input
			System.out.print("Enter a grade:");
			grade = input.nextInt();
			
			//Adding to groups
			if (grade<50)
			{
				G1 = G1+1;
			}
			else if (grade<60)
			{
				G2 = G2+1;
			}
			else if (grade<70)
			{
				G3 = G3+1;
			}
			else if (grade<80)
			{
				G4 = G4+1;
			}	
			else if (grade<90)
			{
				G5 = G5+1;
			}	
			else if (grade<=100)
			{
				G6 = G6+1;
			}	
			else
			{
				System.out.println("\nInvalid grade\n");
			}	
		}
		
		//Output
		System.out.println("\n\t Grade\t\t\tNumber of Students");
		System.out.println("\t90-100%\t\t\t\t" + G6);
		System.out.println("\t80-89%\t\t\t\t" + G5);
		System.out.println("\t70-79%\t\t\t\t" + G4);
		System.out.println("\t60-69%\t\t\t\t" + G3);
		System.out.println("\t50-59%\t\t\t\t" + G2);
		System.out.println("\tBelow 50%\t\t\t" + G1);
		input.close();
	}

}
