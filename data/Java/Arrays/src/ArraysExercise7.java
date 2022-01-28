/*
 * Programmer name: Jeremy M
 * Date: 11/30/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class ArraysExercise7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);	
		int Sales[]=new int[10];
		int Counter=1;
		int Total=0;
		
		//User input
		do
		{
			System.out.println("Enter sales for salesman " + Counter + ":");
			Sales[Counter-1]=input.nextInt();
			Total=Total+Sales[Counter-1];
			Counter++;
		}while(Counter<=10);
		
		//Output
		Counter = 1;
		System.out.println("Salesman Number\t\tSales Amount");
		for (int i=0;i<Sales.length;i++)
		{
			System.out.println(Counter + "\t\t\t$" +  Sales[i]);
			Counter++;
		}
		System.out.println("Overall Sales: $" + Total);
		
		//Match
		Counter = 1;
		System.out.println("\nThose Over $5000\nSalesman Number\t\tSales Amount");
		for(int i=0;i<Sales.length;i++)
		{
			if (Sales[i]>5000)
			{
				System.out.println(Counter + "\t\t\t$" +  Sales[i]);
			}
			Counter++;
		}
		input.close();
	}

}
