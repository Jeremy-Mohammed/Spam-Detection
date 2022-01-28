/*Example 4 - Arrays
 * Programmer name: Jeremy M
 * Date: 11/28/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class Example4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double grades[]=new double[5];
		Scanner input=new Scanner(System.in);
		for(int i=0; i< grades.length;i++)
		{
			System.out.println("Enter the grade for student " + (i+1));
			grades[i]=input.nextDouble();
		}
		for(int i=0;i<grades.length;i++)
		{
			System.out.println("Student " + (i+1 +" scored " + grades[i]));
		}
		input.close();

	}

}
