/*
 * Programmer Name: Jeremy Mohammed
 * Purpose: To learn user-defined methods in Java
 * Date: 12/12/17
 */
import java.util.*;
public class Example3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int number1=0, number2=0;
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the first number: ");
		number1=input.nextInt();
		System.out.println("Enter the second number: ");
		number2=input.nextInt();
		//Calling the calculate method and passing arguments
		calculate(number1,number2);
		input.close();
	}

	//Calculate
	public static void calculate(int n1, int n2)
	{
		int result=n1+n2;
		System.out.println("Result of addition= " + result);
	}
}
