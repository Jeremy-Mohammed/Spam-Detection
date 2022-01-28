/*Example 2
 * Programmer name: Jeremy M
 * Date: 11/121/17
 * Purpose: Use random function
 */
import java.util.*;
public class Example2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//This program generates a random number between 1 and 5
		Random rand=new Random();
		int number1=0;
		//Generates a random number between 1 and 5
		number1=rand.nextInt(5)+1;
		System.out.println(number1);
		//Generate number between 10 and 50
		number1=rand.nextInt(50)+10;
		System.out.println(number1);
	}

}
