/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn loops in java
 * Input: Subject, marks
 * Process: Average
 * Output: Format
 */
import java.util.Scanner;
public class FinalLoops3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		String Name="";
		int Mark=0;
		String Subject="";
		float Average=0;

		
		Scanner input = new Scanner(System.in);

		System.out.println("Input Name:\n\n");
		Name = input.next();
		System.out.println("\t" + Name + "'s Marks");
		System.out.println("Subject\t\tMark");
		 
		for (int i=4; i>0; i=i-1)
		{
			//User Input
			Subject = input.next();
			Mark = input.nextInt();
			Average=Average+Mark;
					
			//Output
			System.out.println(Subject + "\t\t" + Mark);
			
			
		}
		input.close();
		
		//Output Average
		Average=Average/4;
		System.out.println("Average\t" + Average);

	}

}
