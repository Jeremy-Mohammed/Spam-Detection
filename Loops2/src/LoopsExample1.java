/*
 * Programmer name: Jeremy M
 * Date: 11/7/17
 * Purpose: To learn do while loops in java
 * Output: Counter
 */
public class LoopsExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int counter = 4;
		
		//Loops at least once before checking condition
		do
		{
			System.out.println("Counter=" + counter);
			counter = counter + 1;
		}while (counter <=3);

	}

}
