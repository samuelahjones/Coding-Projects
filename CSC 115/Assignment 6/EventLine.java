/*
 * EventLine
 * 
 * A class to simulate a lineup of people waiting to enter
 * a sports/music event. Some people come alone and go to 
 * the back of the line, others bribe their way to a certain 
 * position. Sometimes someone buys a bunch of tickets at 
 * once so multiple people can be removed from the line and 
 * enter the event at the same time.
 */
public class EventLine {
	Queue<Person> lineup;
	//Do not add any other fields

	public EventLine() {
		//Do not change the constructor in any way
		lineup = new GenericQueue<Person>();
	}
	
	/*
	 * Purpose: add a person to the line to enter the event
	 * Parameter: Person p - the person to add
	 * Returns void - nothing
	 */
	public void enterLine(Person p) {
		lineup.enqueue(p);
	}
	
	/*
	 * Purpose: gets the number of people in line
	 * Parameters: none
	 * Returns: int - number of people in line
	 */
	public int peopleInLine() {
		int sum = lineup.size();
		return sum; // so it compiles
	}
	
	/*
	 * Purpose: handle the first person in line
	            (allow them to purchase their ticket
				 and enter into the event venue)
	 * Parameter: none
	 * Returns: Person - the person who gets their ticket
	 *                   and is no longer waiting in line
	 */
	public Person handleOne() { // throws Exception
		try {  
			Person handle = lineup.dequeue();
			return handle;
		} catch (QueueEmptyException e) {
			return null;
		}
		// return handle; // so it compiles
	}
	
	/*
	 * Purpose: handle a whole group of people waiting in line
	 *          (allow a group to buy a number of tickets 
	 *           and all enter the event venue)
	 * Parameters: int num - the number of people
	 * Returns int - the number of people who were successfully
	 *               able to be removed from the line
	 */
	public int handleMultiple(int num) {
		int sum = 0;
		try {
			for( int i = 0; i < num; i++) {
				lineup.dequeue();
				sum++;
			}
			return sum;
		} catch (QueueEmptyException e) {
			return sum;
		}
		 // so it compiles
	}
	
	/*
	 * Purpose: accept a bribe to put someone into a specific
	 *          position in the line to get into the event
	 * Parameters: Person p - the person entering the line
	 *             int pos - the position they are trying to get to
	 * Returns boolean - true if person added to line, false otherwise
	 */
	public boolean premiumEntry(Person p, int pos) throws Exception {
		if( pos < 0 ) {
			return false;
		}
		if( pos > lineup.size() ) {
			return false;
		}
		Queue<Person> newLine = new GenericQueue<Person>();
		int size = this.lineup.size();
		size +=1;
		try {
			int i = 0;
			while( i < size ) {
				if( i == pos ) {
					// System.out.println("Here" + i);
					newLine.enqueue(p);
				} else {
					Person handle = lineup.dequeue();
					newLine.enqueue(handle);
				}
				i++;
			}
			// System.out.println(newLine.size());
			if( newLine.size() == size ) {
				lineup = newLine;
				// System.out.println("Here");
				return true;
			}
			return false;
		} catch (QueueEmptyException e) {
			// throw new Exception();
			return false;
		}
		// so it compiles
	}
	
}
	
	