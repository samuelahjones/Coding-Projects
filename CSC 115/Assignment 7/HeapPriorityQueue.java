/*
* HeapPriorityQueue.java
*
* An implementation of a minimum PriorityQueue using a heap.
* based on the implementation in "Data Structures and Algorithms
* in Java", by Goodrich and Tamassia
*
* This implementation will throw a Runtime, HeapEmptyException
*	if the heap is empty and removeLow is called.
*
* This implementation will throw a Runtime, HeapFullException
*	if the heap is full and insert is called.
*
*/
@SuppressWarnings({"rawtypes", "unchecked"})
public class HeapPriorityQueue implements PriorityQueue {

	protected final static int DEFAULT_SIZE = 10000;
	
	protected Comparable[] storage;
	protected int currentSize;
	protected int customSize = 0;


	/*
	 * Constructor that initializes the array to hold DEFAULT_SIZE elements
	 */
	public HeapPriorityQueue() {
		currentSize = 0;
		storage = new Comparable[DEFAULT_SIZE];
		
		// if using a 1-based implementation, remember to allocate an 
		// extra space in the array since index 0 is not used. 
	}
	
	/*
	 * Constructor that initializes the array to hold size elements
	 */
	public HeapPriorityQueue(int size) {
		currentSize = 0;
		storage = new Comparable[size+1];
		customSize = size;
		
		// if using a 1-based implementation, remember to allocate an 
		// extra space in the array since index 0 is not used. 
	}

	public void insert (Comparable element) throws HeapFullException {
		// System.out.println(isFull());
		if( isFull() == true ) {
			throw new HeapFullException();
		}
		storage[currentSize + 1] = element;
		int i = currentSize + 1;
		currentSize++;
		bubbleUp(i);

		
		// When inserting the first element, choose whether to use 
		// a 0-based on 1-based implementation. Whatever you choose,
		// make sure your implementation for the rest of the program
		// is consistent with this choice.		
    }
	
	public void bubbleUp(int index) {
		int parent = index / 2;
		if( parent >= 1 ) {
			// System.out.println("HERE1");
			if( (storage[index].compareTo(storage[index/2])) < 0 ) {
				// System.out.println("HERE2");
				Comparable temp = storage[index];
				storage[index] = storage[index/2];
				storage[index/2] = temp;
				bubbleUp(index/2);
			}
		}
	}
			
	public Comparable removeMin() throws HeapEmptyException {
		if( currentSize == 0 ) {
			throw new HeapEmptyException();
		}
		int last = currentSize;
		Comparable min = storage[1];
		storage[1] = storage[last];
		currentSize--;
		bubbleDown(1);
		return min; // so it compiles
	}
	
	private void bubbleDown(int index) {
		if( index > currentSize ) {
			return;
		}
		int l = 2*index;
		int r = 2*index+1;
		// System.out.println( l );
		if( l <= currentSize && r <= currentSize ) {
			int comp =  storage[2*index].compareTo(storage[2*index+1]);
			if( comp > 0) { // right one is to be changed 
				int right = storage[index].compareTo(storage[2*index+1]);
				if( right > 0 ) {
					Comparable temp = storage[index];
					storage[index] = storage[2*index+1];
					storage[2*index+1] = temp;
					bubbleDown(2*index+1);
				}
			} else if( comp < 0 ) {
				int left = storage[index].compareTo(storage[2*index]);
				if( left > 0 ) {
					Comparable temp = storage[index];
					storage[index] = storage[2*index];
					storage[2*index] = temp;
					bubbleDown(2*index);
				}
			} else {
				int left = storage[index].compareTo(storage[2*index]);
				int right = storage[index].compareTo(storage[2*index+1]);
				if( left > 0 || right > 0 ) {
					if( left == 0 && right == 0 ) {
						return;
					}
					if( left >= right ) {
						Comparable temp = storage[index];
						storage[index] = storage[2*index];
						storage[2*index] = temp;
						bubbleDown(2*index);
					} else if( right > left ) {
						Comparable temp = storage[index];
						storage[index] = storage[2*index+1];
						storage[2*index+1] = temp;
						bubbleDown(2*index+1);
					}
				}
			}
		}
		if( l <= currentSize ) {
			// System.out.println("HERE1");
			int left = storage[index].compareTo(storage[2*index]);
			// int right = storage[index].compareTo(storage[2*index+1]);
			// System.out.println( left );
			if( left == 0 ) {
				return;
			}
			if( left > 0 ) {
				Comparable temp = storage[index];
				storage[index] = storage[2*index];
				storage[2*index] = temp;
				bubbleDown(2*index);
			}
		}
	}

	public boolean isEmpty(){
		if( currentSize == 0 ) {
			return true;
		}
		return false; // so it compiles
	}
	
	public boolean isFull() {
		if( customSize != 0 ) {
			// System.out.println("HERE");
			if( currentSize == customSize ) {
				return true;
			}
			return false;
		}
		if( currentSize == 10000 ) {
			return true;
		}
		return false; // so it compiles
	}
	
	public int size () {
		return currentSize; // so it compiles
	}

	public String toString() {
		String s = "";
		String sep = "";
		// This implementation of toString assumes you 
		// are using a 1-based approach. Update the initial
		// and final value for i if using a 0-based
		for(int i=1; i<=currentSize; i++) {
			s += sep + storage[i];
			sep = " ";
		}
		return s;
	}
}
