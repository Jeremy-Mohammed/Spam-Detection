/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn string handling functions in java
 */
public class StringFnsExample2 {
	
	public static void main(String[] args) {
		String test="Programming";
		System.out.println("Original String=" + test);
		//Takes a set piece of a string
		System.out.println("Using the substring founction " + test.substring(0,7));
		//Converts the entire string to lower case
		//Converts the entire string to upper case
		System.out.println("Original String=" + test);
		System.out.println("Using the toLowercase function " + test.toLowerCase());
		System.out.println("Original String=" + test);
		System.out.println("Using the toUppercase function " + test.toUpperCase());
		//Removes spaces from edges of string
		test = " Java ";
		System.out.println("Original String=" + test);
		System.out.println(test.trim());
		
	}
}
