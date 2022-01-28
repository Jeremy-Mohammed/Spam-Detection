/*
 * Programmer name: Jeremy M
 * Date: 12/1/17
 * Purpose: Learn about parallel arrays
 */
import java.util.Scanner;
public class Exercise1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		Scanner input=new Scanner(System.in);
		String EmployeeCode[]=new String[3];
		String EmployeeName[]=new String[3];
		String EmployeeDesig[]=new String[3];
		
		//User input
		for(int i=0; i < EmployeeCode.length; i++)
		{
			System.out.println("Input Employee Code, Employee Name, Employee Designation");
			EmployeeCode[i] = input.next();
			EmployeeName[i] = input.next();
			EmployeeDesig[i] = input.next();
		}

		//Output
		System.out.println("\nEmployee Code\t\tEmployee Name\t\tEmployee Designation");
		for(int i=0; i < EmployeeCode.length; i++)
		{
			System.out.println(EmployeeCode[i] + "\t\t\t" + EmployeeName[i] + "\t\t\t" + EmployeeDesig[i]);
		}
		input.close();
	}

}
