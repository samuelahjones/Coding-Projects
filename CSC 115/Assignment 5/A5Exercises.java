public class A5Exercises {

	/*
	 * Purpose: change all occurrences of x to y in the given list
	 * Parameters: List<T> theList - the list to search through
	 *			   T x - the value to change
	 *			   T y = the value to change all x's to
	 * Returns: void - nothing
	 */
	public static<T> void changeXToY(List<T> theList, T x, T y) {
		int size = theList.size();
		changeXToYRec(theList, 0, x, y, size);
	}

	public static<T> void changeXToYRec( List<T> theList, int position, T x, T y, int size) {
		if( position == size ) {
			return;
		} else {
			if( theList.get(position) == x ) {
				theList.change(position, y);
				changeXToYRec(theList, position+1, x, y, size);
			} else {
				changeXToYRec(theList, position+1, x, y, size);
			}
		}
	}
	
	/*
	 * Purpose: count the total number of odd values in this list
	 * Parameters: List<Integer> theList - the list of Integers
	 * Returns: int - the total number of odd values found
	 */
	public static int countOdd(List<Integer> theList) {
		return countOddRec(theList, 0, 0, theList.size()); // so it compiles
	}

	public static int countOddRec( List<Integer> theList, int odd, int position, int size ) {
		if( position == size ) {
			return odd;
		} else {
			if( theList.get(position)%2 != 0 ) {
				return countOddRec(theList, odd+1, position+1, size);
			} else {
				return countOddRec(theList, odd, position+1, size);
			}
		}
	}
	

	/*
	 * Purpose: get the largest sequence of odd values found in a row
	 * Parameters: List<Integer> theList - the list of Integers
	 * Returns: int - the largest sequence of odd values found in a row
	 */
	public static int countMostOddInARow(List<Integer> theList) {
		return countMostOddInARowRec(theList, 0, 0, 0, theList.size()); // so it compiles
	}

	public static int countMostOddInARowRec( List<Integer> theList, int count, int odd, int position, int size ) {
		if( position == size ) {
			if( odd > count ) {
				count = odd;
			}
			return count;
		} else {
			if( theList.get(position)%2 != 0 ) {
				return countMostOddInARowRec(theList, count, odd+1, position+1, size);
			} else {
				if( odd > count ) {
					count = odd;
				}
				return countMostOddInARowRec(theList, count, 0, position+1, size);
			}
		}
	}
	
	
	/*
	 * Purpose: count the elements found in between the first two x's
	 * Parameters: List<Integer> theList - the list of Integers
	 *             int x - the values to search for
	 * Returns: int - the number of values in the list found 
	 *                between the first 2 occurrences if x,
	 *                or -1 if there are not 2 x's in the list.
	 */
	public static int countBetweenX(List<Integer> theList, int x) {
		return countBetweenXRec(theList, x, 0, theList.size(), 0, 0); // so it compiles
	}

	public static int countBetweenXRec( List<Integer> theList, int x, int position, int size, int between, int i ) {
		if( position == size ) {
			return -1;
		} else {
			if( theList.get(position) == x && i == 0 ) {
				return countBetweenXRec(theList, x, position+1, size, between, 1);
			} else if( theList.get(position) == x ) {
				return between;
			} else if( i == 1 ) {
				return countBetweenXRec(theList, x, position+1, size, between+1, i);
			} else {
				return countBetweenXRec(theList, x, position+1, size, between, i);
			}
		}

	}
	
}