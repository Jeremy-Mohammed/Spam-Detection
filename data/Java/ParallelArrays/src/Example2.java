/*Parallel Arrays Example 2
 * Programmer name: Jeremy M
 * Date: 11/30/17
 * Purpose: Learn about parallel arrays
 */
import java.util.*;
public class Example2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);
		
		int employeeCode[]=new int[5];
		String employeeName[]=new String[5];
		double employeeSalary[]=new double[5];
		
		for (int i=0; i<employeeCode.length;i++)
		{
			System.out.println("Enter the employee code: ");
			employeeCode[i]=input.nextInt();
			System.out.println("Enter the employee name: ");
			employeeName[i]=input.next();
			System.out.println("Enter the employee salary: ");
			employeeSalary[i]=input.nextDouble();
		}
		//Printing the output
		System.out.println("Employee Code\t\tEmployee Name\t\tEmployee Salary");
		for (int i=0; i<employeeCode.length;i++)
		{
			System.out.println(employeeCode[i] + "\t\t" + employeeName[i] + "\t\t" + employeeSalary[i]);
		}
		input.close();
	}

}
