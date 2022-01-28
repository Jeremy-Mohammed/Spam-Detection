/*
 * Programmer name: Jeremy M
 * Date: 11/6/17
 * Purpose: To learn while loops in java
 * Input: Scores, number of students
 * Process: Match age to category
 * Output: Info
 */
import java.util.Scanner;
public class LoopsExercise7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int Counter=0;
		int Student=1;
		int StudentS=0;
		float Average=0;
		float AverageF=0;
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the Number of Students: ");
		Student = input.nextInt();
		
		//Input scores
		while(Student >= 1)
		{
			Counter = Counter + 1;
			//User Input
			System.out.print("Enter the scores for Student " + Counter + ": ");
			StudentS = input.nextInt();
			Student = Student-1;
			
			//Average total
			Average = Average + StudentS;	
		}

		//Average final
		AverageF = Average/Counter;
		input.close();
		System.out.println("Number of Students in class: " + Counter);
		System.out.println("Average Score: " + AverageF);
	}

}
