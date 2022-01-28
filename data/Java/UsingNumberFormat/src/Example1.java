import java.text.NumberFormat;
public class Example1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Declare variables
		double dollars=21.5;
		int num=1234;		System.out.println("Dollars+ " + dollars);
		double numWithDecimal=2.0/3.0;
		double sale=.15;
		
		//Output original
		System.out.println("Dollars= " + dollars);
		System.out.println("num= " + num);
		System.out.println("numWithDecimal= " + numWithDecimal);
		System.out.println("sale= " + sale);
		
		//Format
		NumberFormat money=NumberFormat.getCurrencyInstance();
		NumberFormat number=NumberFormat.getIntegerInstance();
		NumberFormat decimal=NumberFormat.getNumberInstance();
		NumberFormat percent=NumberFormat.getPercentInstance();
		
		//Output formatted
		System.out.println("money= " + money.format(dollars));
		System.out.println("number= " + number.format(num));
		System.out.println("decimal= " + decimal.format(numWithDecimal));
		System.out.println("percent= " + percent.format(sale));

	}

}
