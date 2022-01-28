/*
 * Programmer name: Jeremy M
 * Date: 11/14/17
 * Purpose: Use skills we have learn this far
 * Menu based program -
 * Multiple Options
 */
import java.util.*;
public class Draft2 {

	public static void main(String[] args) {
		
		//Declare variables
		String Option = "0";
		String CChoice = "";
		int Computer = 0;
		Random r = new Random();
		Scanner input = new Scanner(System.in);
		
		while (Option.equals("3") == false)
		{	
			//Reset variables
			String Start = "";
			String Decision = "";
			String Choice = "";
			
			//Menu output
			System.out.println("\n\n\n\n\n_________________________________________________");
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
			
			//Rock, paper, scissors (Option 1)
			if (Option.equals("1"))
			{
				//Output pick & rules
				System.out.println("\n\n\n ---------------------");
				System.out.println("(Rock, Paper, Scissors)");
				System.out.println(" ---------------------\n");
				System.out.println("Rules");
				System.out.println("_______________________________________________________\n");
				System.out.println("1. You must pick 'Rock', 'Paper', or 'Scissors'");
				System.out.println("2. The computer will pick one of the choices as well");
				System.out.println("3. The winner is chosen based on the following system\n");
				System.out.println("\t      (Beats)(Beats)     (Beats)");
				System.out.println("\t-> Paper > Rock > Scissors >-");
				System.out.println("\t|                           |");
				System.out.println("\t-<_________________________<-\n");
				System.out.println("4. If the computer and player choose the same option\n   the game will end in a draw\n");
				System.out.println("___________________________________________________________\n");
				
				//Begin or end game
				while (Start.equals("YES") == false && Start.equals("NO") == false)
				{
					System.out.println("  Once you understand the rules please input 'Yes' to start");
					System.out.println("  or input 'No' to go back to the main menu");
					Start = input.next();
					Start = Start.toUpperCase();//Upper case only
					
					//Go with game
					if (Start.equals("YES"))
					{
						while (Decision.equals(""))
						{
							//Game
							System.out.println("\n\n\n\n\n___________________________________________________________\n");
							System.out.println("Computer has chosen\n");
							
							//Computer choice
							Computer = r.nextInt(3) + 1;
							
							//User choice
							System.out.println("Please choose rock, paper, or scissors");
							Choice = input.next();
							Choice = Choice.toUpperCase();//Upper case only
							
							//Matching
							if (Computer == 1 && Choice.equals("ROCK"))//Rock and Rock
							{
								Decision = "Tie";
							}
							else if (Computer == 2 && Choice.equals("ROCK"))//Paper and Rock
							{
								Decision = "Computer Wins!";
							}
							else if (Computer == 3 && Choice.equals("ROCK"))//Scissors and Rock
							{
								Decision = "Player Wins!";
							}
							else if (Computer == 1 && Choice.equals("PAPER"))//Rock and Paper
							{
								Decision = "Player Wins!";
							}
							else if (Computer == 2 && Choice.equals("PAPER"))//Paper and Paper
							{
								Decision = "Tie";
							}
							else if (Computer == 3 && Choice.equals("PAPER"))//Scissors and Paper
							{
								Decision = "Computer Wins!";
							}
							else if (Computer == 1 && Choice.equals("SCISSORS"))//Rock and Scissors
							{
								Decision = "Computer Wins!";
							}
							else if (Computer == 2 && Choice.equals("SCISSORS"))//Paper and Scissors
							{
								Decision = "Player Wins!";
							}
							else if (Computer == 3 && Choice.equals("SCISSORS"))//Scissors and Scissors
							{
								Decision = "Tie";
							}
							else //Invalid Input
							{
								System.out.println(" -------------");	
								System.out.println("(Invalid Input)");
								System.out.println(" -------------");	
								continue;
							}
							
							//Computer to English
							if (Computer == 1)
							{
								CChoice = "ROCK";//Rock
							}
							else if (Computer == 2)
							{
								CChoice = "PAPER";//Paper
							}
							else if (Computer == 3)
							{
								CChoice = "SCISSORS";//Scissors
							}
							
							//Output
							System.out.println("\n\n\n\n\n___________________________________________________________\n");
							System.out.println("Computer Pick: " + CChoice);
							System.out.println("Player Pick: " + Choice);
							System.out.println("\nDecision: " + Decision + "\n");
							
							//Again?
							while (true)
							{
								System.out.println("Would you like to play again? (Yes or No)");
								Choice = input.next();
								Choice = Choice.toUpperCase();//Upper case only
								if (Choice.equals("YES"))//Play again
								{
									Decision="";
									break;
								}
								else if (Choice.equals("NO"))//Return to menu
								{
									System.out.println("\n\n\n\n\n -----------------");
									System.out.println("(Returning to menu)");
									System.out.println(" -----------------\n");	
									break;
								}
								else //Invalid input
								{
									System.out.println(" -------------");	
									System.out.println("(Invalid Input)");
									System.out.println(" -------------\n\n");	
									continue;
								}
							}
							//Back to menu
							if (Choice.equals("NO"))
							{
								break;
							}
						}
							
					}
					//Go back to menu
					else if (Start.equals ("NO"))
					{
						System.out.println("\n\n\n\n\n -----------------");
						System.out.println("(Returning to menu)");
						System.out.println(" -----------------\n");	
					}
					//Invalid input
					else
					{
						System.out.println("\n");
						System.out.println("___________________________________________________________\n");
					}
				}
				//Reset to menu
				Option = "0";
			}
			//String handling functions (Option 2)
			else if (Option.equals("2"))
			{

				//Output pick
				System.out.println("\n\n\n -------------------------");
				System.out.println("(String Handling Functions)");
				System.out.println(" -------------------------\n");
				
				//Reset to menu
				Option = "0";
			}
		}
		//Close imports
		input.close();
		
		//Output end (Option 3)
		System.out.println(" \n\n\n-------");
		System.out.println("(Goodbye)");
		System.out.println(" -------\n");
	}
}