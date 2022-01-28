/*
 * Programmer name: Jeremy M
 * Date: 11/7/17
 * Purpose: To learn do while loops in java
 * Output: 1-20, squared, cubed
 */
public class LoopsExercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		int number = 1;
		int squared = 0;
		int cubed = 0;
		
		//Output format
		System.out.println("Number\t\tSquared\t\tCubed");
		
		//Loop
		do
		{	
			//Calculate 
			squared = number*number;
			cubed =  number*number*number;
			
			//Output
			System.out.println(number + "\t\t" + squared + "\t\t" + cubed);
			number+=1;
			
		}while (number <=20);

	}

}
