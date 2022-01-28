package com.zetcode;
public class UpperCaseTrials {
	public static void main(String[] args) {
		String S1 = "";
		String s1 = "";
		String Start = "HIIIIIII";
		Start =Start.toLowerCase();
		S1 = Start.substring(0, 1).toUpperCase();
		s1 = S1 + Start.substring(1);
				
		System.out.println(s1);
		

}
}