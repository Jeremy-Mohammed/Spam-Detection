/*Example 5 - Arrays
 * Programmer name: Jeremy M
 * Date: 11/28/17
 * Purpose: Learn about arrays
 */
import java.util.*;
public class Example5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String durhamtowns[]=new String[5];
		Scanner input=new Scanner(System.in);
		for(int i=0; i < durhamtowns.length;i++)
		{
			System.out.println("Enter a town in the Durham Region");
			durhamtowns[i]=input.next();
		}
		System.out.println("Towns in Durham region are:");
		for(int i=0; i < durhamtowns.length;i++)
		{
			System.out.println(durhamtowns[i]);
		}
		input.close();
	}

}
