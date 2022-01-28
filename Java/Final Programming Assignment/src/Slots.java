/* Slots
 * Date: 12/11/17
 */
import java.util.*;
public class Slots {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare Variables
		int Tokens = 3;
		String Choice = "YES";
		Scanner input=new Scanner(System.in);
		Random r = new Random();
		int S1 = 0;
		int S2 = 0;
		int S3 = 0;
		
		//Unable to play
		if (Tokens <2)
		{
			System.out.println("You need a minimum of 2 tokens to enter this game.");
		}
		//Able to play
		else
		{
			while (Choice.equals("YES"))
			{
				//Menu and rules
				System.out.println("__________________________");
				System.out.println("   _____ _       _       ");
				System.out.println("  / ____| |     | |      ");
				System.out.println(" | (___ | | ___ | |_ ___ ");
				System.out.println("  |___ || |/ _ || __/ __|");
				System.out.println("  ____) | | (_) | |_(__ )");
				System.out.println(" |_____/|_|(___/(___|___/");
				System.out.println("__________________________\n\n");
				System.out.println(" ----------------------");
				System.out.println("(1/3 Figures - No Prize)");
				System.out.println(" ----------------------\n");
				System.out.println(" ---------------------------");
				System.out.println("(2/3 Figures - Double Tokens)");
				System.out.println(" ---------------------------\n");
				System.out.println(" ---------------------------");
				System.out.println("(3/3 Figures - Triple Tokens)");
				System.out.println(" ---------------------------\n\n");
				while (true)
				{	
					//Play?
					System.out.println("_________________________________________\n");
					System.out.println("Would you like to play Slots? (Yes or No)");
					System.out.println("_________________________________________\n\n");
				
					//Input choice
					Choice = input.next();
					Choice = Choice.toUpperCase();
					if (Choice.equals("NO"))//Back to menu
					{
						break;
					}
					else if (Choice.equals("YES"))//Play game
					{
						//Subtract cost
						Tokens-=2;
						
						//Random values
						S1 = r.nextInt(4)+1;
						S2 = r.nextInt(4)+1;
						S3 = r.nextInt(4)+1;

						Slots();
						System.out.println("|| |     __       | || |    _____     | || |    ______    | ||    | |");
						System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ____ `.  | ||    | |");
						System.out.println("|| |    `| |      | || |  |_/___) |   | || |   `'  __) |  | ||__  | |");
						System.out.println("|| |     | |      | || |   .'____.'   | || |   _  |__ '.  | ||  |_|_|_");
						System.out.println("|| |    _| |_     | || |  / /____     | || |  | |____) |  | ||        |");
						System.out.println("|| |   |_____|    | || |  |_______|   | || |   (______.'  | ||   _____|");
						System.out.println("|| |              | || |              | || |              | ||__|");
						DJ();
						//Time stamp
						try {
							Thread.sleep(500);
						} catch (InterruptedException e) {
							e.printStackTrace();
						} 
						System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                      ___...------...___");
						System.out.println("                  ...*                  *...");
						System.out.println("      ---------..*                          *..---------");
						System.out.println("__..**               _____ _       _                    **..__");
						System.out.println("||                  / ____| |     | |                       ||");
						System.out.println("||                 | (___ | | ___ | |_ ___                  ||");
						System.out.println("||                  |___ || |/ _ || __/ __|                 ||");
						System.out.println("||                  ____) | | (_) | |_(__ )                 ||");
						System.out.println("||                 |_____/|_|(___/ (__|___/                 ||");
						System.out.println("||                                                          ||");
						System.out.println("| '--------------------------------------------------------' |");
						System.out.println("______________________________________________________________    _____");
						System.out.println("| .----------------.  .----------------.  .----------------. | _-*     *-_");
						System.out.println("|| .--------------. || .--------------. || .--------------. || |         |");
						System.out.println("|| |     __       | || |    _____     | || |    ______    | ||  *-.___.-*");
						System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ____ `.  | ||    |   |");
						System.out.println("|| |    `| |      | || |  |_/___) |   | || |   `'  __) |  | ||__  |   |");
						System.out.println("|| |     | |      | || |   .'____.'   | || |   _  |__ '.  | ||  |_|___|_");
						System.out.println("|| |    _| |_     | || |  / /____     | || |  | |____) |  | ||          |");
						System.out.println("|| |   |_____|    | || |  |_______|   | || |   (______.'  | ||   _______|");
						System.out.println("|| |              | || |              | || |              | ||__|");
						DJ();
						//Time stamp
						try {
							Thread.sleep(500);
						} catch (InterruptedException e) {
							e.printStackTrace();
						} 
						System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                      ___...------...___");
						System.out.println("                  ...*                  *...");
						System.out.println("      ---------..*                          *..---------");
						System.out.println("__..**               _____ _       _                    **..__");
						System.out.println("||                  / ____| |     | |                       ||");
						System.out.println("||                 | (___ | | ___ | |_ ___                  ||");
						System.out.println("||                  |___ || |/ _ || __/ __|                 ||");
						System.out.println("||                  ____) | | (_) | |_(__ )                 ||");
						System.out.println("||                 |_____/|_|(___/ (__|___/                 ||");
						System.out.println("||                                                          ||");
						System.out.println("| '--------------------------------------------------------' |");
						System.out.println("______________________________________________________________");
						System.out.println("| .----------------.  .----------------.  .----------------. |");
						System.out.println("|| .--------------. || .--------------. || .--------------. ||");
						System.out.println("|| |     __       | || |    _____     | || |    ______    | ||");
						System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ____ `.  | ||");
						System.out.println("|| |    `| |      | || |  |_/___) |   | || |   `'  __) |  | ||   ______");
						System.out.println("|| |     | |      | || |   .'____.'   | || |   _  |__ '.  | ||_-*      *-_");
						System.out.println("|| |    _| |_     | || |  / /____     | || |  | |____) |  | |||          |");
						System.out.println("|| |   |_____|    | || |  |_______|   | || |   (______.'  | || *-.____.-*");
						System.out.println("|| |              | || |              | || |              | ||__|");
						DJ();
						//Time stamp
						try {
							Thread.sleep(500);
						} catch (InterruptedException e) {
							e.printStackTrace();
						}
						System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                      ___...------...___");
						System.out.println("                  ...*                  *...");
						System.out.println("      ---------..*                          *..---------");
						System.out.println("__..**               _____ _       _                    **..__");
						System.out.println("||                  / ____| |     | |                       ||");
						System.out.println("||                 | (___ | | ___ | |_ ___                  ||");
						System.out.println("||                  |___ || |/ _ || __/ __|                 ||");
						System.out.println("||                  ____) | | (_) | |_(__ )                 ||");
						System.out.println("||                 |_____/|_|(___/ (__|___/                 ||");
						System.out.println("||                                                          ||");
						System.out.println("| '--------------------------------------------------------' |");
						System.out.println("______________________________________________________________    _____");
						System.out.println("| .----------------.  .----------------.  .----------------. | _-*     *-_");
						System.out.println("|| .--------------. || .--------------. || .--------------. || |         |");
						System.out.println("|| |     __       | || |    _____     | || |    ______    | ||  *-.___.-*");
						System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ____ `.  | ||    |   |");
						System.out.println("|| |    `| |      | || |  |_/___) |   | || |   `'  __) |  | ||__  |   |");
						System.out.println("|| |     | |      | || |   .'____.'   | || |   _  |__ '.  | ||  |_|___|_");
						System.out.println("|| |    _| |_     | || |  / /____     | || |  | |____) |  | ||          |");
						System.out.println("|| |   |_____|    | || |  |_______|   | || |   (______.'  | ||   _______|");
						System.out.println("|| |              | || |              | || |              | ||__|");
						DJ();
						//Time stamp
						try {
							Thread.sleep(500);
						} catch (InterruptedException e) {
							e.printStackTrace();
						} 
						//Moving effect
						for (int i=10; i>0; i-=1)
						{
							Slots();
							System.out.println("|| |     __       | || |    _____     | || |    ______    | ||    | |");
							System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ____ `.  | ||    | |");
							System.out.println("|| |    `| |      | || |  |_/___) |   | || |   `'  __) |  | ||__  | |");
							System.out.println("|| |     | |      | || |   .'____.'   | || |   _  |__ '.  | ||  |_|_|_");
							System.out.println("|| |    _| |_     | || |  / /____     | || |  | |____) |  | ||        |");
							System.out.println("|| |   |_____|    | || |  |_______|   | || |   (______.'  | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							Slots();
							System.out.println("|| |   _    _     | || |   _    _     | || |   _    _     | ||    | |");
							System.out.println("|| |  | |  | |    | || |  | |  | |    | || |  | |  | |    | ||    | |");
							System.out.println("|| |  | |__| |_   | || |  | |__| |_   | || |  | |__| |_   | ||__  | |");
							System.out.println("|| |  |____   _|  | || |  |____   _|  | || |  |____   _|  | ||  |_|_|_");
							System.out.println("|| |      _| |_   | || |      _| |_   | || |      _| |_   | ||        |");
							System.out.println("|| |     |_____|  | || |     |_____|  | || |     |_____|  | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							Slots();
							System.out.println("|| |    ______    | || |     __       | || |   _    _     | ||    | |");
							System.out.println("|| |   / ____ `.  | || |    /  |      | || |  | |  | |    | ||    | |");
							System.out.println("|| |   `'  __) |  | || |    `| |      | || |  | |__| |_   | ||__  | |");
							System.out.println("|| |   _  |__ '.  | || |     | |      | || |  |____   _|  | ||  |_|_|_");
							System.out.println("|| |  | |____) |  | || |    _| |_     | || |      _| |_   | ||        |");
							System.out.println("|| |   (______.'  | || |   |_____|    | || |     |_____|  | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							Slots();
							System.out.println("|| |   _    _     | || |    ______    | || |    _____     | ||    | |");
							System.out.println("|| |  | |  | |    | || |   / ____ `.  | || |   / ___ `.   | ||    | |");
							System.out.println("|| |  | |__| |_   | || |   `'  __) |  | || |  |_/___) |   | ||__  | |");
							System.out.println("|| |  |____   _|  | || |   _  |__ '.  | || |   .'____.'   | ||  |_|_|_");
							System.out.println("|| |      _| |_   | || |  | |____) |  | || |  / /____     | ||        |");
							System.out.println("|| |     |_____|  | || |   (______.'  | || |  |_______|   | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}  
							Slots();
							System.out.println("|| |     __       | || |    _____     | || |    _____     | ||    | |");
							System.out.println("|| |    /  |      | || |   / ___ `.   | || |   / ___ `.   | ||    | |");
							System.out.println("|| |    `| |      | || |  |_/___) |   | || |  |_/___) |   | ||__  | |");
							System.out.println("|| |     | |      | || |   .'____.'   | || |   .'____.'   | ||  |_|_|_");
							System.out.println("|| |    _| |_     | || |  / /____     | || |  / /____     | ||        |");
							System.out.println("|| |   |_____|    | || |  |_______|   | || |  |_______|   | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							Slots();
							System.out.println("|| |    _____     | || |   _    _     | || |     __       | ||    | |");
							System.out.println("|| |   / ___ `.   | || |  | |  | |    | || |    /  |      | ||    | |");
							System.out.println("|| |  |_/___) |   | || |  | |__| |_   | || |    `| |      | ||__  | |");
							System.out.println("|| |   .'____.'   | || |  |____   _|  | || |     | |      | ||  |_|_|_");
							System.out.println("|| |  / /____     | || |      _| |_   | || |    _| |_     | ||        |");
							System.out.println("|| |  |_______|   | || |     |_____|  | || |   |_____|    | ||   _____|");
							System.out.println("|| |              | || |              | || |              | ||__|");
							DJ();
							//Time stamp
							try {
								Thread.sleep(100);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}  
						}
						//Output Numbers
						System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n__________________________");
						System.out.println("   _____ _       _       ");
						System.out.println("  / ____| |     | |      ");
						System.out.println(" | (___ | | ___ | |_ ___ ");
						System.out.println("  |___ || |/ _ || __/ __|");
						System.out.println("  ____) | | (_) | |_(__ )");
						System.out.println(" |_____/|_|(___/(___|___/");
						System.out.println("__________________________\n");
						//Time stamp
						try {
							Thread.sleep(1000);
						} catch (InterruptedException e) {
							e.printStackTrace();
						}  
						//Random 1
						Output(S1);
						//Random 2
						Output(S2);
						//Random 3
						Output(S3);
						System.out.println("____________________________________");
						System.out.println("| .------------------------------. |");
						System.out.println("||                                ||");
						System.out.println("||                                ||");
						System.out.println("||  ________    | || |     _____  ||");
						System.out.println("|| |_   ___ `.  | || |    |_. ._| ||");
						System.out.println("||   | |   `. | | || |      | |   ||");
						System.out.println("||   | |   `. | | || |   _  | |   ||");
						System.out.println("||  _| |___.' / | || |  | |_' |   ||");
						System.out.println("|| |________.'  | || |  `.___.'   ||");
						System.out.println("||                                ||");
						System.out.println("| '------------------------------' |");
						System.out.println("____________________________________");
						//Output prize
						
					}
				}
				

				
			}
		}
		input.close();
	}
	
	//Declare Methods
	//Slot bottom
	public static void DJ()
	{
		System.out.println("|| '--------------' || '--------------' || '--------------' ||");
		System.out.println("| '----------------'  '----------------'  '----------------' |");
		System.out.println("______________________________________________________________");
		System.out.println("| .--------------------------------------------------------. |");
		System.out.println("||                                                          ||");
		System.out.println("||                                                          ||");
		System.out.println("||               ________    | || |     _____               ||");
		System.out.println("||              |_   ___ `.  | || |    |_. ._|              ||");
		System.out.println("||                | |   `. | | || |      | |                ||");
		System.out.println("||                | |   `. | | || |   _  | |                ||");
		System.out.println("||               _| |___.' / | || |  | |_' |                ||");
		System.out.println("||              |________.'  | || |  `.___.'                ||");
		System.out.println("||                                                          ||");
		System.out.println("| '--------------------------------------------------------' |");
		System.out.println("______________________________________________________________");
	}
	
	//Slot top
	public static void Slots()
	{ 
		System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                      ___...------...___");
		System.out.println("                  ...*                  *...");
		System.out.println("      ---------..*                          *..---------");
		System.out.println("__..**               _____ _       _                    **..__");
		System.out.println("||                  / ____| |     | |                       ||    ___");
		System.out.println("||                 | (___ | | ___ | |_ ___                  || _-*   *-_");
		System.out.println("||                  |___ || |/ _ || __/ __|                 || |       |");
		System.out.println("||                  ____) | | (_) | |_(__ )                 ||  *-._.-*");
		System.out.println("||                 |_____/|_|(___/ (__|___/                 ||    | |");
		System.out.println("||                                                          ||    | |");
		System.out.println("| '--------------------------------------------------------' |    | |");
		System.out.println("______________________________________________________________    | |");
		System.out.println("| .----------------.  .----------------.  .----------------. |    | |");
		System.out.println("|| .--------------. || .--------------. || .--------------. ||    | |");
	}
	
	//Output Numbers
	public static void Output(int Slot)
	{
		System.out.println("______________________");
		System.out.println("| .----------------. |");
		System.out.println("|| .--------------. ||");
		if (Slot == 1)
		{
			System.out.println("|| |     __       | ||");
			System.out.println("|| |    /  |      | ||");
			System.out.println("|| |    `| |      | ||");
			System.out.println("|| |     | |      | ||");
			System.out.println("|| |    _| |_     | ||");
			System.out.println("|| |   |_____|    | ||");
		}
		else if (Slot == 2)
		{
			System.out.println("|| |    _____     | ||");
			System.out.println("|| |   / ___ `.   | ||");
			System.out.println("|| |  |_/___) |   | ||");
			System.out.println("|| |   .'____.'   | ||");
			System.out.println("|| |  / /____     | ||");
			System.out.println("|| |  |_______|   | ||");
		}
		else if (Slot == 3)
		{
			System.out.println("|| |    ______    | ||");
			System.out.println("|| |   / ____ `.  | ||");
			System.out.println("|| |   `'  __) |  | ||");
			System.out.println("|| |   _  |__ '.  | ||");
			System.out.println("|| |  | |____) |  | ||");
			System.out.println("|| |   (______.'  | ||");
		}
		else if (Slot == 4)
		{
			System.out.println("|| |   _    _     | ||");
			System.out.println("|| |  | |  | |    | ||");
			System.out.println("|| |  | |__| |_   | ||");
			System.out.println("|| |  |____   _|  | ||");
			System.out.println("|| |      _| |_   | ||");
			System.out.println("|| |     |_____|  | ||");
		}
		System.out.println("|| |              | ||");
		System.out.println("|| '--------------' ||");
		System.out.println("| '----------------' |");
		System.out.println("______________________");
		//Time stamp
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}  
	}
}