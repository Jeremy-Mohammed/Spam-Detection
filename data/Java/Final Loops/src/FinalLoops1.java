/*
 * Programmer name: Jeremy M
 * Date: 11/10/17
 * Purpose: To learn loops in java
 * Input: Number
 * Process: Square number, average
 * Output: Number, square, average
 */
import java.util.Scanner;
public class FinalLoops1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int N1=0;
		int Sq=0;
		float AvN1=0;
		float AvSq=0;
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter three Numbers:\n\n\n");
		System.out.println("\t\tNumber\t\tSquare");
		 
		for (int i=3; i>0; i=i-1)
		{
			//User Input
			N1 = input.nextInt();
			
			//Square, averages
			Sq=N1*N1;
			AvN1=AvN1+N1;
			AvSq=AvSq+Sq;
					
			//Output
			System.out.print("\t\t  " + N1 + "\t\t  " + Sq);
			
		}
		input.close();
		
		//Average
		AvN1=AvN1/3;
		AvSq=AvSq/3;
		System.out.println("\n    Average\t " + AvN1 + "\t\t " + AvSq);
		

	}

}
