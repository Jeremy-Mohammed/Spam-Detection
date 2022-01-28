/*
 * Programmer name: Jeremy M
 * Date: 12/1/17
 * Purpose: Learn about parallel arrays
 */
import java.util.Scanner;
public class Exercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);
		String BookName[]=new String[5];
		float Price[]=new float[5];
		int Quantity[]=new int[5];
		float Total[]=new float[5];
		
		//User input
		for(int i=0; i < BookName.length; i++)
		{
			System.out.println("Input Book Name, Price, Quantity");
			BookName[i] = input.next();
			Price[i] = input.nextFloat();
			Quantity[i] = input.nextInt();
			Total[i]=Price[i]*Quantity[i];
		}

		//Output
		System.out.println("\nBook Nmae\t\tPrice\t\tQuantity Sold\t\tTotal Cost");
		for(int i=0; i < BookName.length; i++)
		{
			System.out.println(BookName[i] + "\t\t\t$" + Price[i] + "\t\t\t" + Quantity[i] + "\t\t$" + Total[i]);
		}
		input.close();

	}

}
