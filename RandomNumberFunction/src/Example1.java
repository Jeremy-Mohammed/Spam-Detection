/*Example 1
 * Programmer name: Jeremy M
 * Date: 11/121/17
 * Purpose: Use random function
 */
import java.util.Random;
public class Example1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Display 5 numbers between 0 and 100
		Random r = new Random();
		System.out.println("First number: " + r.nextInt(100));
		System.out.println("Second number: " + r.nextInt(100));
		System.out.println("Third number: " + r.nextInt(100));
		System.out.println("Fourth number: " + r.nextInt(100));
		System.out.println("Fifth number: " + r.nextInt(100));

	}

}
