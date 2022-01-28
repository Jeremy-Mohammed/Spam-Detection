/*
 * Programmer name: Jeremy M
 * Date: 10/3/17
 * Purpose: Using the Scanner package for user input for integers 
 */
import java.util.Scanner;
public class VariableExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int length = 0;
		int width = 0;
		int area = 0;
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the length");
		length = input.nextInt();
		System.out.print("Enter the width");
		width = input.nextInt();
		input.close();
		
		area = length*width;
		System.out.println("Area of the rectangle: " + area);

	}

}
