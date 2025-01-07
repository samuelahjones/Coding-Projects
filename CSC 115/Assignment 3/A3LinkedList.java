// Name: Samuel Jones
// Student number: v01003688

public class A3LinkedList implements A3List {
	private A3Node head;
	private A3Node tail;
	private int length;
	
	public A3LinkedList() {
		head = null;
		tail = null;
		length = 0;
	}
	
	public void addFront(String s) {
		A3Node add = new A3Node(s);
		if( head != null ) {
			add.next = head;
			head.prev = add;
		} else {
			tail = add;
		}
		head = add;
		length++;
	}

	public void addBack(String s) {
		A3Node add = new A3Node(s);
		if( tail != null ) {
			add.prev = tail;
			tail.next = add;
		} else {
			head = add;
		}
		tail = add;
		length++;
	}
	
	public int size() {
		return length;
	}
	
	public boolean isEmpty() {
		return length==0;
	}
	
	public void removeFront() {
		if( isEmpty() == false ) {
			A3Node cur = head;
			head = cur.next;
			head.prev = null;
			length--;
		}
	}
	
	public void removeBack() {
		if( isEmpty() == false ) {
			A3Node cur = tail;
			tail = cur.prev;
			tail.next = null;
			length--;
		}
	}
	
	
	
	//////////////////
	/* PART 2 BELOW */
	//////////////////
	
	public void removeMiddle() {
		if( isEmpty() == false ) {
			if( length == 2 ) {
				A3Node cur = head; 
				A3Node nod1 = cur.next;
				cur = nod1.next;
				nod1.next = null;
				nod1.prev = null;
				cur.next = null;
				cur.prev = null;
				head = null;
				tail = null;
				length = 0;
			} else if( length%2 == 0 ) {
				// even
				int a = length / 2;
				int b = a + 1;
				A3Node cur = head;
				int i = 1;
				while( cur != null ) {
					if( i == a ) {
						A3Node nod1 = cur.prev;
						nod1.next = cur.next;
						nod1 = cur.next;
						nod1.prev = cur.prev;
						nod1 = cur;
						cur = cur.next;
						nod1.prev = null;
						nod1.next = null;
					} else if( i == b) {
						A3Node nod1 = cur.prev;
						nod1.next = cur.next;
						nod1 = cur.next;
						nod1.prev = cur.prev;
						nod1 = cur;
						cur = cur.next;
						nod1.prev = null;
						nod1.next = null;
					} else {
						cur = cur.next;
					}
					i++;
				}
				length -= 2;
			}else if(length == 1) {
				head = null;
				tail = null;
				length = 0;
			} else {
				int a = (length / 2) + 1;
				int i = 1;
				A3Node cur = head;
				while( cur != null ) {
					if( i == a ) {
						A3Node nod1 = cur.prev;
						nod1.next = cur.next;
						nod1 = cur.next;
						nod1.prev = cur.prev;
						nod1 = cur;
						cur = cur.next;
						nod1.prev = null;
						nod1.next = null;
					} else {
						cur = cur.next;
					}
					i++;
				}
				length--;
			}
		}
	}
	
	
	public void interleave(A3LinkedList other) {
		if( other.length == this.length ) {
			if( this.length > 1 ) {
				if( this.length == 2 ) {
					A3Node cur1 = this.head;
					A3Node cur2 = other.head;
					A3Node list1 = cur1.prev;
					A3Node list2 = cur2.prev;
					list1.next = cur2;
					list2.next = cur1;
					cur1.prev = list2;
					cur2.prev = list1;
					other.tail = cur1;
					this.tail = cur2;
				} else if( this.length%2 == 0 ) {
					A3Node cur1 = this.head;
					A3Node cur2 = other.head; 
					int i = 0;
					int j = 2;
					while( i < this.length ) {
						if( i == this.length - 1 ) {
							other.tail = cur1;
							this.tail = cur2;
						} else if( j == 1) {
							A3Node list1 = cur1.prev;
							A3Node list2 = cur2.prev;
							list1.next = cur2;
							list2.next = cur1;
							cur1.prev = list2;
							cur2.prev = list1;
							list1 = cur1;
							list2 = cur2;
							cur1 = cur1.next;
							cur2 = cur2.next;
							list1.next = cur2;
							list2.next = cur1;
							cur1.prev = list2;
							cur2.prev = list1;
							j = 2;
						} else {
							cur1 = cur1.next;
							cur2 = cur2.next;
							j = 1;
						}
						i++;
					}
				} else {
					A3Node cur1 = this.head;
					A3Node cur2 = other.head; 
					int i = 0;
					int j = 2;
					while( i < this.length ) {
						if( j == 1) {
							A3Node list1 = cur1.prev;
							A3Node list2 = cur2.prev;
							list1.next = cur2;
							list2.next = cur1;
							cur1.prev = list2;
							cur2.prev = list1;
							list1 = cur1;
							list2 = cur2;
							cur1 = cur1.next;
							cur2 = cur2.next;
							list1.next = cur2;
							list2.next = cur1;
							cur1.prev = list2;
							cur2.prev = list1;
							j = 2;
						} else {
							cur1 = cur1.next;
							cur2 = cur2.next;
							j = 1;
						}
						i++;
					}
				}
			}
		}
	}
	
	
	
	////////////////////////////////////////
	/* METHODS BELOW TO HELP WITH TESTING */
	////////////////////////////////////////
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from front to back
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String frontToBack() {
		String result = "{";
		A3Node cur = head;
		while (cur != null) {
			result += cur.getData();
			cur = cur.next;
		}
		result += "}";
		return result;
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from back to front
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String backToFront() {
		String result = "{";
		A3Node cur = tail;
		while (cur != null) {
			result += cur.getData();
			cur = cur.prev;
		}
		result += "}";
		return result;
	}
}
	