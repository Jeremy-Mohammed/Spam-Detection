/*
 * Programmer name: Jeremy M
 * Date: 11/7/17
 * Purpose: To learn do while loops in java
 * Output: Sum of 1-30
 */
public class LoopsExercise2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int number = 1;
		int sum = 0;
		
		//Add all numbers
		do
		{
			sum = sum + number;
			number+=1;
			
		}while (number <=30);

		//Output
		System.out.println("Total sum of 1-30: " + sum);
	}

}
