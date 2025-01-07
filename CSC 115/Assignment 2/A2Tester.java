import java.util.Arrays;

public class A2Tester {
	
	private static int testPassCount = 0;
	private static int testCount = 0;
	private static double THRESHOLD = 0.1; // allowable margin of error for floating point results
	
	
	public static void main(String[] args) {
		/* Tests for methods inside Fundraiser.java */
		testConstructor();
		testMoneyRaised();
		testMoneySpent();
		testMostExpensive();
		testAddToFundraiser();
		
		/* Tests for methods inside A2Exercises.java */
		testTotalMoneyRaised();
		testTotalSpent();
		testMostExpensiveItems();
		testAverageOfMostExpensive();
		
		System.out.println();
		System.out.println("PASSED " +testPassCount+ " / " +testCount+ " TESTS");
	}
		
	public static void testConstructor() {
		System.out.println("\nTesting Fundraiser Constructor");
		String nameResult;
		AuctionItem[] itemsResult;
	
		// Testing default constructor
		// (the constructor with 0 arguments)
		
		Fundraiser f0 = new Fundraiser();
		nameResult = f0.getName();
		displayResults(nameResult==null, "empty constructor name");
		itemsResult = f0.getItems();
		displayResults(itemsResult==null, "empty constructor items");
	
		// Setting up AuctionItems for Fundraiser objects
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a1, a2, a3};

		// Testing second constructor with f1 and f2
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Community Fundraiser", arr2);
		
		String expectedName;
		AuctionItem[] expectedItems;
						
		nameResult = f1.getName();
		itemsResult = f1.getItems();
		expectedName = new String("Family Fundraiser");
		expectedItems = arr1;
		displayResults(expectedName.equals(nameResult), "f1 constructor name");
		displayResults(Arrays.equals(itemsResult,expectedItems), "f1 constructor items");
	
		nameResult = f2.getName();
		itemsResult = f2.getItems();
		expectedName = new String("Community Fundraiser");
		expectedItems = arr2;
		displayResults(expectedName.equals(nameResult), "f2 constructor name");
		displayResults(Arrays.equals(itemsResult,expectedItems), "f2 constructor items");

	}
	
	public static void testMoneyRaised() {
		System.out.println("\nTesting moneyRaised");
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a1, a2};
		AuctionItem[] arr3 = {a1, a2, a3};
		AuctionItem[] arr4 = {a2, a3};
		
		Fundraiser f0a = new Fundraiser();
		Fundraiser f0b = new Fundraiser("empty", arr0);
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		Fundraiser f4 = new Fundraiser("Community Fundraiser", arr4);
		
		int result = 0;
		int expected = 0;
		
		result = f1.moneyRaised();
		expected = 4;
		displayResults(result==expected, "money raised in fundraiser with 1 item");
		
		result = f2.moneyRaised();
		expected = 39;
		displayResults(result==expected, "money raised in fundraiser with 2 items");
		
		result = f0b.moneyRaised();
		expected = 0;
		displayResults(result==expected, "money raised in empty fundraiser");
		
		result = f0a.moneyRaised();
		expected = 0;
		displayResults(result==expected, "money raised with nulls");
		
		// Write more tests here
			
	}
	
	public static void testMoneySpent() {
		System.out.println("\nTesting moneySpent");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a1, a2};
		AuctionItem[] arr3 = {a1, a2, a3};
		AuctionItem[] arr4 = {a2, a3};
		AuctionItem[] arr5 = {a1, a2, a3, a4, a5};
		AuctionItem[] arr6 = {a1, a2, a3, a4, a5, a6, a7};
		
		Fundraiser f0a = new Fundraiser();
		Fundraiser f0b = new Fundraiser("empty", arr0);
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		Fundraiser f4 = new Fundraiser("Community Fundraiser", arr4);
		Fundraiser f5 = new Fundraiser("Regional Fundraiser", arr5);
		Fundraiser f6 = new Fundraiser("Global Fundraiser", arr6);
		
		String bidderName;
		int result;
		int expected;
		
		bidderName = new String("Sam");
		result = f1.moneySpent(bidderName);
		expected = 4;
		displayResults(result==expected, "amount "+bidderName+" spent at f1");
		
		bidderName = new String("Ali");
		result = f1.moneySpent(bidderName);
		expected = 0;
		displayResults(result==expected, "amount "+bidderName+" spent at f1");
		
		bidderName = new String("Sam");
		result = f2.moneySpent(bidderName);
		expected = 4;
		displayResults(result==expected, "amount "+bidderName+" spent at f2");
		
		bidderName = new String("Ali");
		result = f2.moneySpent(bidderName);
		expected = 35;
		displayResults(result==expected, "amount "+bidderName+" spent at f2");
		
		// add more tests here
		
	}
	
	public static void testMostExpensive() {
		System.out.println("\nTesting mostExpensive");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");
		
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a1, a2};
		AuctionItem[] arr3 = {a2, a1};

		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		
		AuctionItem result;
		AuctionItem expected;
		
		result = f1.mostExpensive();
		expected = a1;
		displayResults(result.equals(expected), "mostExpensive in f1");
		
		result = f2.mostExpensive();
		expected = a2;
		displayResults(result.equals(expected), "mostExpensive in f2");
		
		result = f3.mostExpensive();
		expected = a2;
		displayResults(result.equals(expected), "mostExpensive in f3");
		
		// add more tests here
		
	}
	
	public static boolean equal(AuctionItem[] a1, AuctionItem[] a2) {
		boolean equal = true;
		if ((a1 == null || a2 == null) && a1 != a2) { // one is null
			equal = false;
		} else if (a1.length != a2.length) { // different lengths
			equal = false;
		} else {
			int i = 0; 
			while (i < a1.length && equal == true) {
				if (!a1[i].equals(a2[i])) {
					equal = false;
				}
				i++;
			}
		}
		return equal;
	}
	
	public static void testAddToFundraiser() {
		System.out.println("\nTesting addToFundraiser");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a1, a2, a3};
		AuctionItem[] arr0AfterAdd = {a5};
		AuctionItem[] arr1AfterAdd = {a1, a6};
		AuctionItem[] arr2AfterAdd1 = {a1, a2, a3, a7};
		AuctionItem[] arr2AfterAdd2 = {a1, a2, a3, a7, a4};
		
		Fundraiser f0 = new Fundraiser();
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr0);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr1);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr2);
		
		AuctionItem[] result;
		AuctionItem[] expected;
		
		f1.addToFundraiser(a5);
		result = f1.getItems();
		expected = arr0AfterAdd;
		displayResults(equal(result,expected), "added a5 to f1");
		
		f2.addToFundraiser(a6);
		result = f2.getItems();
		expected = arr1AfterAdd;
		displayResults(equal(result,expected), "added a6 to f2");
		
		f3.addToFundraiser(a7);
		result = f3.getItems();
		expected = arr2AfterAdd1;
		displayResults(equal(result,expected), "added a7 to f3");
		
		f3.addToFundraiser(a4);
		result = f3.getItems();
		expected = arr2AfterAdd2;
		displayResults(equal(result,expected), "added a4 to f3");
		
		// Add more tests here
		
	}
	
	
	public static void testTotalMoneyRaised() {
		System.out.println("\nTesting totalMoneyRaised");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");	
		AuctionItem a8 = new AuctionItem("ancient coin", 350, "Alex");
		AuctionItem a9 = new AuctionItem("handcrafted earrings", 175, "Alex");
		AuctionItem a10= new AuctionItem("vintage hat", 75, "Sam");		
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a2, a3, a4, a5};
		AuctionItem[] arr3 = {a6, a7, a8, a9, a10};		
		
		Fundraiser f0a = new Fundraiser();
		Fundraiser f0b = new Fundraiser("empty", arr0);
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		
		Fundraiser[] fundraisers0 = {};
		Fundraiser[] fundraisers1 = {f1, f2};
		Fundraiser[] fundraisers2 = {f3, f0a, f2, f0b, f1};
		
		int result = 0;
		int expected = 0;
		
		result = A2Exercises.totalMoneyRaised(fundraisers0);
		// System.out.println(result);
		expected = 0;
		displayResults(result==expected, "total money raised in empty array of fundraisers");
		
		result = A2Exercises.totalMoneyRaised(fundraisers1);
		// System.out.println(result);
		expected = 4+35+220+80+40;
		displayResults(result==expected, "total money raised in fundraisers1");
		
		result = A2Exercises.totalMoneyRaised(fundraisers2);
		// System.out.println(result);
		expected = 4+35+220+80+40+180+20+350+175+75;
		displayResults(result==expected, "total money raised in fundraisers2");
		
		// add more tests here
		
	}
	
	public static void testTotalSpent() {
		System.out.println("\nTesting totalSpent");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");	
		AuctionItem a8 = new AuctionItem("ancient coin", 350, "Alex");
		AuctionItem a9 = new AuctionItem("handcrafted earrings", 175, "Alex");
		AuctionItem a10= new AuctionItem("vintage hat", 75, "Sam");		
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a2, a3, a4, a5};
		AuctionItem[] arr3 = {a6, a7, a8, a9, a10};		
		
		Fundraiser f0a = new Fundraiser();
		Fundraiser f0b = new Fundraiser("empty", arr0);
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		
		Fundraiser[] fundraisers0 = {};
		Fundraiser[] fundraisers1 = {f1, f2};
		Fundraiser[] fundraisers2 = {f3, f0a, f2, f0b, f1};
		
		int expected = 0;
		int result = 0;
		String toFind = "";
		
		toFind = "Ali";
		result = A2Exercises.totalSpent(fundraisers0, toFind);
		expected = 0;
		displayResults(result==expected, "total spent by "+toFind+" in empty array");
		
		toFind = "Ali";
		result = A2Exercises.totalSpent(fundraisers1, toFind);
		// System.out.println(result);
		expected = 255;
		displayResults(result==expected, "total spent by "+toFind+" in fundraisers1");
		
		toFind = "Lee";
		result = A2Exercises.totalSpent(fundraisers1, toFind);
		// System.out.println(result);
		expected = 80;
		displayResults(result==expected, "total spent by "+toFind+" in fundraisers1");
		
		toFind = "Sam";
		result = A2Exercises.totalSpent(fundraisers2, toFind);
		// System.out.println(result);
		expected = 139;
		displayResults(result==expected, "total spent by "+toFind+" in fundraisers2");

		toFind = "Ali";
		result = A2Exercises.totalSpent(fundraisers2, toFind);
		// System.out.println(result);
		expected = 255;
		displayResults(result==expected, "total spent by "+toFind+" in fundraisers2");
		
		toFind = "Lee";
		result = A2Exercises.totalSpent(fundraisers2, toFind);
		// System.out.println(result);
		expected = 80;
		displayResults(result==expected, "total spent by "+toFind+" in fundraisers2");
		
		// add more tests here
		
	}
	
	public static void testMostExpensiveItems() {
		System.out.println("\nTesting mostExpensiveItems");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");	
		AuctionItem a8 = new AuctionItem("ancient coin", 350, "Alex");
		AuctionItem a9 = new AuctionItem("handcrafted earrings", 175, "Alex");
		AuctionItem a10= new AuctionItem("vintage hat", 75, "Sam");		
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a2, a3, a4, a5};
		AuctionItem[] arr3 = {a6, a7, a8, a9, a10};		
		
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		
		Fundraiser[] fundraisers0 = {};
		Fundraiser[] fundraisers1 = {f1, f2};
		Fundraiser[] fundraisers2 = {f3, f2, f1};
		
		AuctionItem[] result;
		
		result = A2Exercises.mostExpensiveItems(fundraisers0);
		AuctionItem[] expected0 = {};
		displayResults(equal(result, expected0), "most expensive items in empty fundraiser array");
		
		result = A2Exercises.mostExpensiveItems(fundraisers1);
		AuctionItem[] expected1 = {a1, a3};
		displayResults(equal(result, expected1), "most expensive items in fundraisers1");
		
		result = A2Exercises.mostExpensiveItems(fundraisers2);
		AuctionItem[] expected2 = {a8, a3, a1};
		displayResults(equal(result, expected2), "most expensive items in fundraisers2");
		
		// add more tests here
		
			
	}
	
	public static void testAverageOfMostExpensive() {
		System.out.println("\nTesting averageOfMostExpensive");
		
		AuctionItem a1 = new AuctionItem("colorful seashell", 4, "Sam");
		AuctionItem a2 = new AuctionItem("autographed photo", 35, "Ali");
		AuctionItem a3 = new AuctionItem("event ticket", 220, "Ali");
		AuctionItem a4 = new AuctionItem("fitness package", 80, "Lee");
		AuctionItem a5 = new AuctionItem("gift basket", 40, "Sam");
		AuctionItem a6 = new AuctionItem("painting", 180, "Noah");
		AuctionItem a7 = new AuctionItem("baseball cards", 20, "Sam");	
		AuctionItem a8 = new AuctionItem("ancient coin", 350, "Alex");
		AuctionItem a9 = new AuctionItem("handcrafted earrings", 175, "Alex");
		AuctionItem a10= new AuctionItem("vintage hat", 75, "Sam");		
		
		AuctionItem[] arr0 = {};
		AuctionItem[] arr1 = {a1};
		AuctionItem[] arr2 = {a2, a3, a4, a5};
		AuctionItem[] arr3 = {a6, a7, a8, a9, a10};		
		
		Fundraiser f1 = new Fundraiser("Family Fundraiser", arr1);
		Fundraiser f2 = new Fundraiser("Fall Fundraiser", arr2);
		Fundraiser f3 = new Fundraiser("Team Fundraiser", arr3);
		
		Fundraiser[] fundraisers0 = {};
		Fundraiser[] fundraisers1 = {f1, f2};
		Fundraiser[] fundraisers2 = {f3, f2, f1};
		
		double result = 0.9;
		double expected = 0.0;
		
		result = A2Exercises.averageOfMostExpensive(fundraisers0);
		expected = 0.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "average of expensive items in empty fundraiser array");
		
		result = A2Exercises.averageOfMostExpensive(fundraisers1);
		expected = (4.0+220.0)/2.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "average of expensive items in fundraisers1");
		
		result = A2Exercises.averageOfMostExpensive(fundraisers2);
		expected = (350.0+220.0+4.0)/3.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "average of expensive items in fundraisers1");
		
		// add more tests here
		
		
	}
	
	public static void displayResults (boolean passed, String testName) {
		testCount++;
		if (passed) {
			System.out.println ("Passed test: " + testName);
			testPassCount++;
		} else {
			System.out.println ("Failed test: " + testName + " at line "
				+ Thread.currentThread().getStackTrace()[2].getLineNumber());
		}
    }

}