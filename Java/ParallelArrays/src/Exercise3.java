/*
 * Programmer name: Jeremy M
 * Date: 12/1/17
 * Purpose: Learn about parallel arrays
 */
import java.util.Scanner;
public class Exercise3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);
		String Name="";
		String Course[]=new String[3];
		int Students[]=new int[3];
		int Total=0;
		
		//User input
		System.out.print("Teacher Name:");
		Name = input.next();
		for(int i=0; i < Course.length; i++)
		{
			System.out.println("Input Course Name, Number of Students");
			Course[i] = input.next();
			Students[i] = input.nextInt();
			Total=Total+Students[i];
		}

		//Output
		System.out.println("\nReport for " + Name + "\nCourse Name\t\t\tNumber of Students");
		for(int i=0; i < Course.length; i++)
		{
			System.out.println(Course[i] + "\t\t\t\t" + Students[i]);
		}
		System.out.println("Total: " + Total + " Students");
		input.close();

	}

}
