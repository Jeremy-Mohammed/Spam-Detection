/*Parallel Arrays Example 1
 * Programmer name: Jeremy M
 * Date: 11/30/17
 * Purpose: Learn about parallel arrays
 */
import java.util.*;
public class Example1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);
		/*Parallel Arrays are 2 or more arrays that
		 * have the same size String array*/
		String itemNames[]=new String[4];
		double itemPrices[]=new double[4];
		
		//Ask for user input
		for(int i=0; i <itemNames.length;i++)
		{
			System.out.println("Please enter the item name: ");
			itemNames[i]=input.next();
			System.out.println("Please enter the item price: ");
			itemPrices[i]=input.nextDouble();
		}
		System.out.println("Item Name\t\tItem Price");
		//Printing information
		for(int i=0; i <itemNames.length;i++)
		{
			System.out.println(itemNames[i] + "\t\t\t" + itemPrices[i]);
		}		
		input.close();
	}

}
