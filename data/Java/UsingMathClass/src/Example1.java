
public class Example1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		double val=26.9, radius=12.5, areaofCircle=0.0;
		
		//Using the PI Constant
		areaofCircle=Math.PI*radius*radius;
		System.out.println("Area of the circle = " + areaofCircle);
		
		//Using the Math.abs (), Math.sqrt () and Math.round () methods
		System.out.println("The value is " + val);
	
		System.out.println("\n\nAbsolute value of val is ");
		System.out.println(Math.abs(val));

		System.out.println("\nAbsolute value of -val is");
		System.out.println(Math.abs(-val));

		System.out.println("\n\nThe square root of val is ");
		System.out.println(Math.sqrt(val));
		

		System.out.println("\n\nVal rounded is ");
		System.out.println(Math.round(val));

	}

}
