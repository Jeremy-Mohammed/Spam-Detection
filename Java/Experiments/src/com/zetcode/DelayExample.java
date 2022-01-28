package com.zetcode;

public class DelayExample {

	public static void main(String[] args) {
		// TODO Auto-generated method 
			  System.out.println("Hi");
			  for (int i = 0; i < 10; i++)
			  {
			  System.out.println("Number of itartion = " + i);
			  System.out.println("Wait:");
			  try
			  {
			  Thread.sleep(4000);  
			 
			  }catch (InterruptedException ie)
			  {
			  System.out.println(ie.getMessage());
			  }
			  }
			  }

	}


