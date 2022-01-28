/*
 * Programmer name: Jeremy M
 * Date: 11/3/17
 * Purpose: To learn while loops in java
 * Output: 10 - 20 even, 15 - 25 odd
 */
public class LoopsExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int startNumber1=10,endNumber1=24;
		int startNumber2=15,endNumber2=25;
		
		//Output even numbers 10 - 20
		while(startNumber1 <= endNumber1)
		{
			System.out.print(startNumber1 + " ");
			startNumber1 = startNumber1 +2;
		}
		
		//Output odd numbers 15 - 25
		while(startNumber2 <= endNumber2)
		{
			System.out.print(startNumber2 + " ");
			startNumber2 = startNumber2 +2;
		}
		

	}

}
