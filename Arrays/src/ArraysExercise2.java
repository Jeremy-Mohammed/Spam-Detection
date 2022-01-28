/*
 * Programmer name: Jeremy M
 * Date: 11/29/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int temperature[]=new int[7];
		String degree[]=new String[3];
		degree[0]="Pleasant Day";
		degree[1]="Cold Day";
		degree[2]="Chilly Day";
		int temp=0;
		Scanner input=new Scanner(System.in);
		
		//Enter temperature and match
		for (int i=0; i < temperature.length;i++)
		{
			System.out.println("Please enter the temperature: ");
			temp=input.nextInt();
			
			if (temp >=15 && temp<=20)
			{
				System.out.println(degree[0]);
			}
			else if (temp >=5 && temp <=14)
			{
				System.out.println(degree[1]);
			}
			else if (temp <=5 )
			{
				System.out.println(degree[2]);
			}
		}
		
		input.close();
		

	}

}
