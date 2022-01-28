/*
 * Programmer name: Jeremy M
 * Date: 11/13/17
 * Purpose: To learn string handling functions in java
 */
public class StringFnsExample3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Replaces first set word with new word
		String string1= "Programming in Python is fun";
		String str1="Python";
		String str2="Java";
		System.out.println(string1.replaceFirst(str1, str2));
		//Replaces all set words with new word
		string1="It is PA day. It is a long weekend";
		str1="It";
		str2="It's";
		System.out.println(string1.replaceAll(str1, str2));
		/*
		 * Compares two strings, ignoring case considerations
		 * 
		 * Compares the first letter of two strings in an integer value
		 * 
		 * Identifies what character a string starts with
		 * 
		 * Identifies what character a string starts with
		 */

	}

}
