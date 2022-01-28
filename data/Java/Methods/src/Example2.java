/*
 * Programmer Name: Jeremy Mohammed
 * Purpose: To learn user-defined methods in Java
 * Date: 12/12/17
 */
public class Example2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int answer=0;
		answer=add();
		System.out.println("Sum= " + answer);
		System.out.println("Difference= " + subtract());
		System.out.println("Product= " + product());
		System.out.println("Quotient= " + quotient());
	
	}
	//Add
	public static int add()
	{
		int number1=10, number2=20, sum=0;
		sum=number1 + number2;
		return sum;
	}
	//Subtract
	public static int subtract()
	{
		int number1=100, number2=20, difference=0;
		difference=number1 - number2;
		return difference;
	}
	//Product
	public static int product()
	{
		int number1=10, number2=20, product=0;
		product=number1 * number2;
		return product;
	}
	//Quotient
	public static int quotient()
	{
		int number1=20, number2=10, quotient=0;
		quotient=number1 / number2;
		return quotient;
	}
	

}
