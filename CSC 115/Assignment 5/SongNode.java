public class SongNode {
	    
	private Song data;
	protected SongNode next;

	public SongNode (Song data) {
		this.data = data;
		this.next = null;
	}

	/*
	 * Purpose: get the data value of this Node
	 * Parameters: nothing	 
	 * Returns: Song - the data value (a song)
	 */
	public Song getData() {
		return data;
	}
	
	/*
	 * Purpose: get the next node in this list
	 * Parameters: nothing
	 * Returns: SongNode - the next node
	 */
	public SongNode getNext() {
		return next;
	}

	/*
	 * Purpose: update the next reference for this node
	 * Parameters: SongNode next - the new next
	 * Returns: void - nothing
	 */
	public void setNext(SongNode next) {
		this.next = next;
	}

}