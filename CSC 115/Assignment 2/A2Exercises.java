public class A2Exercises {
	
	/*
	 * Purpose: get the total money raised across all fundraisers
	 *          in the given array
	 * Parameters: Fundraiser[] array - the array of fundraisers
	 * Returns: int: total money raised across all fundraisers
	 * Precondition: the array is not null
	 */	
	public static int totalMoneyRaised(Fundraiser[] array) {
		int sum = 0;
		for( int i = 0; i < array.length; i++ ) {
			sum += array[i].moneyRaised();
		}
		return sum; // so it compiles
	}
	
	/*
	 * Purpose: get the total money spent on winning auctions 
	 *          by people with the provided name
	 * Parameters: Fundraiser[] array - the array of fundraisers
	 *             String name - the name to search for
	 * Returns: int: total money raised across all fundraisers
	 * Precondition: the array and name are not null
	 */	
	public static  int totalSpent(Fundraiser[] array, String name) {
		int sum = 0;
		for( int i = 0; i < array.length; i++ ) {
			if( array[i].getName() != null ) {
				sum += array[i].moneySpent(name);
			}
		}
		return sum; // so it compiles
	}

	/*
	 * Purpose: create a new array of AuctionItems that contains
	 *          only the most expensive item from each fundraiser
	 * Parameters: Fundraiser[] array - the array of fundraisers
	 * Returns: AuctionItem[]: the array of most expensive items
	 * Precondition: the array is not null
	 */	
	public static AuctionItem[] mostExpensiveItems(Fundraiser[] array) {
		if( array == null ) {
			return null;
		}
		AuctionItem[] most = new AuctionItem[array.length];
		for( int i = 0; i < array.length; i++ ) {
			most[i] =  array[i].mostExpensive();
		}
		return most; // so it compiles
	}
	
	/*
	 * Purpose: calculate and return the average price of the most
	 *          expensive items from each fundraiser in the array
	 * Parameters: Fundraiser[] array - the array of fundraisers
	 * Returns: double - the average price of the most expensive items
	 * Precondition: the array is not null
	 */	
	public static double averageOfMostExpensive(Fundraiser[] array) {
		double avg = 0.0;
		if( array == null ) {
			return 0.0;
		}
		AuctionItem[] most = mostExpensiveItems(array);
		double sum = 0.0;
		double item = 0.0;
		for( int i = 0; i < most.length; i++ ) {
			sum += most[i].getHighestBid();
			item++;
		} 
		avg = sum / item;
		System.out.println(avg);
		return avg; // so it compiles
	}
	// xaZzaasXDSWXCDWCEFECGERTGVRVFTGVHTYHTRGETRHGVRGBTEGTYEBHYJTERBGERTY TRFREGRTHTHRTYHR
}