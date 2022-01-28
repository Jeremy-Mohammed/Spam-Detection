/*
 * Programmer name: Jeremy M
 * Date: 11/14/17
 * Purpose: Use skills we have learn this far
 * Menu based program -
 * Multiple Options
 */
import java.util.*;
public class Final {

	public static void main(String[] args) {
		
		//Declare variables
		Random r = new Random();
		Scanner input = new Scanner(System.in);
		
		while (true)
		{	
			//Reset variables
			String Option = "0";
			String CChoice = "";
			int Computer = 0;
			String Start = "YES2";
			String Decision = "";
			String Choice = "";
			String S1 = "";
			String S11 = "";
			String S21 = "";
			String S2 = "";
			int Compare = 0;
			String Pass = "PAPAYA";
			String FName = "";
			String MName = "";
			String LName = "";
			String Guess = "";
			int Hint = 1;
			int Loop = 1;
			int Number = 0;
			int N1 = 0;
			int N2 = 0;
			int N3 = 0;
			int N4 = 0;
			int N5 = 0;
			int N6 = 0;
			
			//Menu output
			System.out.println("_________________________________________________");
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
			System.out.println(" ------------");
			System.out.println("(3. Lotto 649)");
			System.out.println(" ------------\n");
			System.out.println(" -------");
			System.out.println("(4. Exit)");
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
				System.out.println("_______________________________________________________\n");
				System.out.println("Rules\n");
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
							System.out.println("\n\n\n___________________________________________________________\n");
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
							System.out.println("Player Pick: " + Choice);
							System.out.println("Computer Pick: " + CChoice);
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
									System.out.println("\n\n\n -------------");	
									System.out.println("(Invalid Input)");
									System.out.println(" -------------\n");	
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
						System.out.println("\n\n\n -------------");	
						System.out.println("(Invalid Input)");
						System.out.println(" -------------\n");	
						System.out.println("___________________________________________________________\n");
					}
				}
				//Reset to menu
				continue;
			}
			//String handling functions (Option 2)
			else if (Option.equals("2"))
			{
				//Menu pick
				while (true)
				{
					//Reset variables 
					Hint = 1;
					Start = "YES2";
					
					//Output menu
					System.out.println("\n\n\n -------------------------");
					System.out.println("(String Handling Functions)");
					System.out.println(" -------------------------\n");
					System.out.println("_________________________________________________\n");
					System.out.println("\t    Please choose a menu option\n");
					System.out.println(" ----------------------");
					System.out.println("(1. Sort Alphabetically)");
					System.out.println(" ----------------------\n");
					System.out.println(" ---------------------");
					System.out.println("(2. Guess the password)");
					System.out.println(" ---------------------\n");
					System.out.println(" -------------------");
					System.out.println("(3. Print my Initals)");
					System.out.println(" -------------------\n");
					System.out.println(" -------");
					System.out.println("(4. Exit)");
					System.out.println(" -------\n");
					System.out.println("_________________________________________________\n");
				
					//User input
					Choice = input.next();
					
					//Sort alphabetically
					if (Choice.equals("1"))
					{
						//Title
						System.out.println(" -------------------");
						System.out.println("(Sort Alphabetically)");
						System.out.println(" -------------------\n");
						System.out.println("_________________________________________________\n");
						
						//Input strings
						System.out.println("Input two words\n");
						System.out.print("First Word: ");
						S1 = input.next();
						System.out.print("Second Word: ");
						S2 = input.next();
						
						//Functions
						S1 = S1.toLowerCase();
						S11 = S1.substring(0, 1).toUpperCase();
						S1 = S11 + S1.substring(1);//Upper case first letter
						S2 = S2.toLowerCase();
						S21 = S2.substring(0, 1).toUpperCase();
						S2 = S21 + S2.substring(1);//Upper case first letter
						Compare = S1.compareTo(S2);//Compare
						
						//Output
						System.out.println("\nOrder:\n");
						if (Compare <0)
						{
							System.out.println("\n" + S1 + "\t" + S2);
						}
						else
						{
							System.out.println("\n" + S2 + "\t" + S1);
						}
						System.out.println("_________________________________________________\n");
					}
					
					//Guess the password
					else if (Choice.equals("2"))
					{
						//Title
						System.out.println(" ------------------");
						System.out.println("(Guess the password)");
						System.out.println(" ------------------\n");
						
						while (Start.equals("YES2"))
						{
							//Guess
							System.out.println("_________________________________________________\n");
							System.out.print("Enter your guess: ");
							Guess = input.next();
							Guess = Guess.toUpperCase();
							
							//Compare
							if (Guess.equals(Pass))//Correct
							{
								System.out.println("\nYou have guessed the password!\nCongratulations!");
								break;
							}
							else//Incorrect
							{
								System.out.println("\nSorry, you are incorrect!");
								
								//Hint
								if (Hint == 1)//First hint
								{
									do
									{
										System.out.println("\nWould you like a hint? (Yes or No)\n");
										Choice = input.next();
										Choice = Choice.toUpperCase();//Upper case only
										if (Choice.equals("YES"))//Hint
										{
											System.out.println("Hint: Type of fruit\n");
											Hint = 2;
											break;
										}
										else if (Choice.equals("NO"))//No
										{
											break;
										}
										else //Invalid input
										{
											System.out.println("\n\n\n -------------");	
											System.out.println("(Invalid Input)");
											System.out.println(" -------------\n");	
											continue;
										}
									}while (true);
								}
								else if (Hint == 2)//Second hint
								{
									do
									{
										System.out.println("\nWould you like another hint? (Yes or No)\n");
										Choice = input.next();
										Choice = Choice.toUpperCase();//Upper case only
										if (Choice.equals("YES"))//Hint
										{
											System.out.println("Hint: The word is six letters long\n");
											Hint = 3;
											break;
										}
										else if (Choice.equals("NO"))//No
										{
											break;
										}
										else //Invalid input
										{
											System.out.println("\n\n\n -------------");	
											System.out.println("(Invalid Input)");
											System.out.println(" -------------\n");	
											continue;
										}
									}while (true);
								}
								else if (Hint == 3)//Third hint
								{
									do
									{
										System.out.println("\nWould you like a third hint? (Yes or No)\n");
										Choice = input.next();
										Choice = Choice.toUpperCase();//Upper case only
										if (Choice.equals("YES"))//Hint
										{
											System.out.println("Hint: The word has the letter 'A' three times in it\n");
											Hint = 4;
											break;
										}
										else if (Choice.equals("NO"))//No
										{
											break;
										}
										else //Invalid input
										{
											System.out.println("\n\n\n -------------");	
											System.out.println("(Invalid Input)");
											System.out.println(" -------------\n");	
											continue;
										}
									}while (true);
								}
								else if (Hint == 4)//Password
								{
									do
									{
										System.out.println("\nDo you give up? (Yes or No)\n");
										Choice = input.next();
										Choice = Choice.toUpperCase();//Upper case only
										if (Choice.equals("YES"))//Yes
										{
											System.out.println("The password is Papaya! \nGood luck next time!\n");
											Start = "YES1";
											Hint = 1;
											break;
										}
										else if (Choice.equals("NO"))//No
										{
											break;
										}
										else //Invalid input
										{
											System.out.println("\n\n\n -------------");	
											System.out.println("(Invalid Input)");
											System.out.println(" -------------\n");	
											continue;
										}
									}while (true);
								}
							}
						}
					}
					
					//Print my initials
					else if (Choice.equals("3"))
					{
						//Title
						System.out.println(" ----------------");
						System.out.println("(Print my Initals)");
						System.out.println(" ----------------\n");
						System.out.println("_________________________________________________\n");
						
						//Input name
						System.out.print("First Name: ");
						FName = input.next();
						System.out.print("Middle Name: ");
						MName = input.next();
						System.out.print("Last Name: ");
						LName = input.next();
						
						//Output initials
						System.out.print("\nInitials: " + FName.substring(0,1).toUpperCase() + ".");
						System.out.println(MName.substring(0,1).toUpperCase() + "." + LName.substring(0,1).toUpperCase() + ".");
					}
					
					//Exit
					else if (Choice.equals("4"))
					{
						System.out.println("\n\n\n\n\n -----------------");
						System.out.println("(Returning to menu)");
						System.out.println(" -----------------\n");	
						break;
					}
					
					//Invalid input
					else
					{
						System.out.println("\n\n\n\n\n -------------");	
						System.out.println("(Invalid Input)");
						System.out.println(" -------------");	
						
						//Reset to menu
						continue;
					}
				}
				//Reset to menu
				continue;
			}
			
			//Output lotto (Option 3)
			else if (Option.equals("3"))
			{
				//Output title and rules
				System.out.println("\n\n\n ---------");
				System.out.println("(Lotto 649)");
				System.out.println(" ---------");
				System.out.println("\n_________________________________________________\n");
				System.out.println("Please input six integers between 1 - 49");
				System.out.println("Do not duplicate any of your numbers");
				System.out.println("\n\nGood luck!");
				
				//Lotto numbers
				int L1 = r.nextInt(49)+1;
				int L2 = r.nextInt(49)+1;
				int L3 = r.nextInt(49)+1;
				int L4 = r.nextInt(49)+1;
				int L5 = r.nextInt(49)+1;
				int L6 = r.nextInt(49)+1;
				
				while (Loop<=6)
				{
					//Input
					System.out.print("\nInput Number " + Loop + ":");
					Number = input.nextInt();
					
					//Check for invalid input
					if (Number <1 || Number >49)
					{
						System.out.println("Number " + Loop + " is invalid\nEnter a new Number");
						continue;
					}
					//Check for duplicate
					else if (N1 == Number || N2 == Number || N3 == Number || N4 == Number || N5 == Number || N6 == Number)
					{
						System.out.println("Number " + Loop + " is a duplicate number\nEnter a new number");
						continue;
					}
					//Pass
					else
					{
						System.out.println("Number " + Loop + ": " + Number);
					}
					
					//Input to individual variable
					if (Loop == 1)
					{
						N1 = Number;
					}
					else if (Loop == 2)
					{
						N2 = Number;
					}
					else if (Loop == 3)
					{
						N3 = Number;
					}
					else if (Loop == 4)
					{
						N4 = Number;
					}
					else if (Loop == 5)
					{
						N5 = Number;
					}
					else if (Loop == 6)
					{
						N6 = Number;
					}
					
					//Loop
					Loop+=1;
				}
					
				//Output numbers
				System.out.println("\n\nYour Numbers: " + N1 + " " + N2 + " " + N3 + " " + N4 + " " + N5 + " " + N6);
				System.out.println("\nYour Numbers: " + L1 + " " + L2 + " " + L3 + " " + L4 + " " + L5 + " " + L6);
					
				//Compare
				if (N1 == L1 && N2 == L2 && N3 == L3 && N4 == L4 && N5 == L5 && N6 == L6)
				{
					System.out.println("\n\n ---------------");	
					System.out.println("(Congratulations)");
					System.out.println(" ---------------\n");	
					System.out.println("You have won Lotto 649!");	
				}
				else 
				{

					System.out.println("\nYou have lost");
					System.out.println("Better luck next time!");		
				}
				System.out.println("_________________________________________________\n\n\n\n");
				
				//Reset
				Loop = 1;
				continue;
			}
			//Output end (Option 4)
			else if (Option.equals("4"))
			{
				System.out.println("\n\n\n -------");
				System.out.println("(Goodbye)");
				System.out.println(" -------");
				
				//End
				break;
			}
			//Invalid input
			else
			{
				System.out.println("\n\n\n\n\n -------------");	
				System.out.println("(Invalid Input)");
				System.out.println(" -------------\n");	
				
				//Reset to menu
				continue;
			}
		}
		input.close();
	}
}