/*
 * represents a line-up to get into the venue of a music concert
 */

public class ConcertLine {

	private PriorityQueue attendees;
	private Attendee[] att;
	private int customSize;
	private int count;

	/* 
 	 * constructor that initializes attendees to a default-sized priority queue
	 */
	public ConcertLine() {
		attendees = new HeapPriorityQueue();
		customSize = -1;
		count = 0;
		att = new Attendee[10000];
	}

	/* 
	 * constructor that initializes attendees to a priority queue of given size
	 */
	public ConcertLine(int size) {
		attendees = new HeapPriorityQueue(size);
		customSize = size;
		count = 0;
		att = new Attendee[size*10000];
	}


	/* Purpose: add given Attendee to attendees line or prints
	 *          a notification message if attendees is full
	 * Parameters: Attendee a - the attendee who just arrived at
	 *             the concert and wants to enter the venue
	 * Returns: void - nothing
	 */
	public void addAttendee(Attendee a) {
		if( isAttendeeFull() == -1 ) {
			System.out.println("Concert line is full can NOT add more attendee");
			return;
		}
		attendees.insert(a);
		att[count] = a;
		count++;
	}

	public int isAttendeeFull() {
		if( customSize != -1 ) {
			if( count == customSize ) {
				return -1;
			}
			return 1;
		}
		if( count == 10000 ) {
			return -1;
		}
		return 1;
	}
	/* Purpose: gets the number of attendees waiting to get in
	 * Parameters: none
	 * Returns: int - number of attendees waiting to get in
	 */
	public int numAttendeesWaiting() {
		return attendees.size(); // so it compiles
	}


	/* Purpose: removes and returns the next attendee from attendees
	 * Parameters: none
	 * Returns: Attendee - the next attendee, null if there are no more
	 *                     attendees waiting to get into the venue.
	 */
	public Attendee nextAttendee() {
		if( count == 0 ) {
			return null;
		}

		try {
			Comparable<Attendee> next = attendees.removeMin();
			Attendee out = null;
			return findAttendee(next, 0, out); // so it compiles
		} catch(HeapEmptyException e) {
			return null;
		}
	}

	public Attendee findAttendee( Comparable<Attendee> cur, int at, Attendee out ) {
		if( at == att.length ) {
			return out;
		}
		if( cur.equals(att[at])) {
			Attendee G = new Attendee(att[at].getName(), att[at].getEventTicket(), att[at].getArrivalTime());
			out = G;
			// System.out.println("HERE2");
			// System.out.println(out);
			return out;
		}
		out = findAttendee (cur, at+1, out);
		// System.out.println("HERE1");
		// System.out.println(out);
		return out;
	}
}

