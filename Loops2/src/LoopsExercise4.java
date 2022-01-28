/*
 * Programmer name: Jeremy M
 * Date: 11/8/17
 * Purpose: To learn while loops in java
 * Input: Name, mark
 * Process: Average
 * Output: Name, mark, average
 */
import java.util.Scanner;
public class LoopsExercise4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int Student=15;
		String StudentN="";
		int StudentS=0;
		float Average=0;
		float AverageF=0;
		Scanner input = new Scanner(System.in);

		System.out.println("Enter the name and scores for students: \n\n\n");
		System.out.println("Student Name\t\tMark");
		
		//Input scores, names
		do
		{
			//User Input
			StudentN = input.next();
			StudentS = input.nextInt();
			Student = Student-1;
			
			//Output info
			System.out.print(StudentN + "\t\t\t" + StudentS);
			
			
			//Average total
			Average = Average + StudentS;
		}while (Student >=1);

		//Average final
		AverageF = Average/15;
		input.close();
		System.out.println("Class Average: " + AverageF);

	}

}
