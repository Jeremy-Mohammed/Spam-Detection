/*Example 3 - Arrays
 * Programmer name: Jeremy M
 * Date: 11/28/17
 * Purpose: Learn about arrays
 */
import java.util.Scanner;
public class Example3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String daysofweek[]={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
		Scanner input=new Scanner(System.in);
		int daynumber=0;
		System.out.println("Enter a number (1-7)");
		daynumber=input.nextInt();
		if (daynumber>=1 && daynumber<=7)
		{
			System.out.println("Day " + daynumber + " is " + daysofweek[daynumber-1]);
		}
		else
		{
			System.out.println("Invalid input");
		}
		input.close();
		

	}

}
