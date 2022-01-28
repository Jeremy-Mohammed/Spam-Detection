/*
 * Programmer name: Jeremy M
 * Date: 11/30/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);	
		String Staff[]=new String[8];
		int Member[]=new int[2];
		
		//User input
		for(int i=0;i<Staff.length;i++)
		{
			System.out.println("Enter teaching or non-teaching staff: (T or N)");
			Staff[i]=input.next();
			Staff[i]=Staff[i].toUpperCase();
			
			//Match
			if (Staff[i].equals("T"))
			{
				Member[0]++;
			}
			else if (Staff[i].equals("N"))
			{
				Member[1]++;
			}
		}
		
		//Output
		System.out.println("Teaching Staff\t\tNon-teaching Staff");
		System.out.println(Member[0] + "\t\t\t" + Member[1]);
		input.close();

	}
	
}
