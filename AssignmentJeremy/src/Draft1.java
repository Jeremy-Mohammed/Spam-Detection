/*
 * Programmer name: Jeremy M
 * Date: 11/14/17
 * Purpose: Menu
 * Input: Option
 * Output: Menu, options
 */
import java.util.*;
public class Draft1 {

	public static void main(String[] args) {
		
		//Declare variables
		String Option = "0";
		Scanner input = new Scanner(System.in);
		
		while (Option.equals("0"))
		{
			//Menu output
			System.out.println("\n_________________________________________________");
			System.out.println(" ___  ___      _        ___  ___                 ");
			System.out.println(" |  |/  |     (_)       |  |/  |                 ");
			System.out.println(" | .  . | __ _ _ _ __   | .  . | ___ _ __  _   _ ");
			System.out.println(" | ||/| |/ _` | | '_  ) | ||/| |/ _ | '_ )| | | |");
			System.out.println(" | |  | | (_| | | | | | | |  | |  __/ | | | |_| |");
			System.out.println(" |_|  |_)|__,_|_|_| |_| |_|  |_/(___|_| |_||__,_|");
			System.out.println("_________________________________________________\n");
			System.out.println("\t    Please choose a menu option\n");
			System.out.println(" ------------------------");
			System.out.println("(1. Rock, Paper, Scissors)");
			System.out.println(" ------------------------\n");
			System.out.println(" ----------------------------");
			System.out.println("(2. String Handling Functions)");
			System.out.println(" ----------------------------\n");
			System.out.println(" -------");
			System.out.println("(3. Exit)");
			System.out.println(" -------\n");
			
			//Option pick
			Option = input.next();
			
			if (Option.equals("1"))
			{
				//Output pick
				System.out.println(" ---------------------");
				System.out.println("(Rock, Paper, Scissors)");
				System.out.println(" ---------------------\n");
				Option = "0";
			}
			else if (Option.equals("2"))
			{

				//Output pick
				System.out.println(" -------------------------");
				System.out.println("(String Handling Functions)");
				System.out.println(" -------------------------\n");
				Option = "0";
				
			}
			else if (Option.equals("3"))
			{
				//Output pick
				System.out.println(" -------");
				System.out.println("(Goodbye)");
				System.out.println(" -------\n");
			}
			
			
		}
		//Close imports
		input.close();
	}

}
