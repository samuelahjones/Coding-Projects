public class LinkedSongList {
	// DO NOT ADD ANY MORE FIELDS OR METHODS
	private SongNode head;
	
	public LinkedSongList() {
		head = null;
	}

	public void addFront (Song s) {
		SongNode n = new SongNode(s);
		n.next = head;
		head = n;
	}

	public void addBack (Song s){
		SongNode n = new SongNode(s);
		if (head == null) {
			head = n;
		} else {
			addBackRec(head, n);
		}
	}
	
	private void addBackRec(SongNode cur, SongNode n) {
		if (cur.next == null) {
			cur.next = n;
		} else {
			addBackRec(cur.next, n);
		}
	}

	public boolean isEmpty() {
		return head == null;
	}

	public Song get (int position) {
		return getRec(head, 0, position);
	}
	
	private Song getRec(SongNode cur, int i, int position) {
		if (i == position) {
			return cur.getData();
		} else {
			return getRec(cur.next, i+1, position);
		}
	}

	/* Purpose: create a string representation of list
	 * Parameters: nothing	 
	 * Returns: String - the string representation of the list
	 */
	public String toString() {
		if (head == null) {
			return "{}";
		} else {
			return "{" + toStringRec(head) + "}";
		}
	}
	
	
	private String toStringRec(SongNode cur) {
		if (cur == null) {
			return "";
		} else if (cur.next == null) {
			return cur.getData().toString();
		} else {
			return cur.getData().toString() + ", " + toStringRec(cur.next);
		}
	}

	/*
	 * Purpose: Insert all elements from array into this linked list
	 * Parameters: Song[] array - the elements to add to this list
	 * Returns void - nothing
	 */
	public void buildFromArray(Song[] array) {
		buildFromArrayRec(array, array.length-1);
	}
	
	private void buildFromArrayRec(Song[] array, int i) {
		if (i < 0) {
			return;
		} else {
			addFront(array[i]);
			buildFromArrayRec(array, i-1);
		}
	}
	

	/*
	 * Purpose: gets the total number of songs in this list
	 * Parameters: none
	 * Returns: int - the number of songs in this list
	 */
	public int countSongs() {
		return countSongsRec( head,0 ); // so it compiles
	}

	public int countSongsRec( SongNode cur, int count ) {
		if( cur == null ) {
			return count;
		} else {
			count++;
			return countSongsRec( cur.next, count );
		}
	}
	
		
	/*
	 * Purpose: gets the total duration of all songs in this list
	 * Parameters: none
	 * Returns: int - the total duration of all songs in this list
	 */
	public int totalDuration() {
		return totalDurationRec(head, 0); // so it compiles
	}

	public int totalDurationRec( SongNode cur, int t ) {
		if( cur == null ) {
			return t;
		} else {
			t += cur.getData().getDuration();
			return totalDurationRec(cur.next, t);
		}
	}
	
	
	/*
	 * Purpose: counts the songs in this list by an artist with artistName
	 * Parameters: String artistName - the name of the artist to search for
	 * Returns: int - number of songs by artistName
	 */
	public int countSongsByArtist(String artistName) {
		return countSongsByArtistRec(head, 0, artistName); // so it compiles
	}
	
	public int countSongsByArtistRec( SongNode cur, int count, String artistName ) {
		if( cur == null ) {
			return count;
		} else {
			String artist = cur.getData().getArtist();
			if( artistName.equals(artist) ) {
				return countSongsByArtistRec(cur.next, count+1, artistName);
			} else {
				return countSongsByArtistRec(cur.next, count, artistName);
			}
		}
	}
	
	/*
	 * Purpose: determines whether this list contains a song by artistName
	 * Parameters: String artistName - the name of the artist to search for
	 * Returns: boolean - true if a song by artistName is found
	 */
	public boolean containsArtist(String artistName) {
		return containsArtistRec(head, false, artistName); // so it compiles
	}

	public boolean containsArtistRec( SongNode cur, boolean contains, String artistName ) {
		if( cur == null ) {
			return contains;
		} else {
			String artist = cur.getData().getArtist();
			if( artistName.equals(artist) ) {
				return containsArtistRec(cur.next, true, artistName);
			} else {
				return containsArtistRec(cur.next, contains, artistName);
			}
		}
	}
	
	
	/*
	 * Purpose: gets the longest song in the list
	 * Parameters: none
	 * Returns Song - the longest song in the list
	 *                or null if the list is empty
	 */
	public Song longestSong() {
		if( head == null ) {
			return null;
		}
		SongNode cur = head;
		Song longest = cur.getData(); 
		return longestSongRec(head, longest, 0, 0); // so it compiles
	}
	
	public Song longestSongRec( SongNode cur, Song longest, int time, int x ) {
		if( cur == null && x == 0 ) {
			return null;
		} else if ( cur == null ) {
			return longest;
		} else {
			int t = cur.getData().getDuration();
			if( x == 0 ) {
				longest = cur.getData();
				time = cur.getData().getDuration();
				return longestSongRec(cur.next, longest, time, 1);
			} else if( t > time ) {
				longest = cur.getData();
				time = cur.getData().getDuration();
				return longestSongRec(cur.next, longest, time, 1);
			} else {
				return longestSongRec(cur.next, longest, time, 1);
			}
		}
	}
		
	/*
	 * Purpose: get the total duration of all songs in the list
	 *          before the first song by artistName
	 * Parameters: String artistName - the artist name to search for
	 * Returns int - the duration of all songs before the first
	 *               song by artistName, or -1 if no song by 
	 *               artistName is found.
	 */
	public int totalTimeUntilArtist(String artistName) {
		return totalTimeUntilArtistRec(head, 0, artistName, 0); // so it compiles
	}

	public int totalTimeUntilArtistRec( SongNode cur, int time, String artistName, int x ) {
		if( cur == null && x == 0 ) {
			return -1;
		} else if( cur == null ) {
			return -1;
		} else {
			if( artistName.equals(cur.getData().getArtist()) ) {
				return time;
			} else {
				time += cur.getData().getDuration();
				return totalTimeUntilArtistRec(cur.next, time, artistName, 1);
			}
		}
	}
	
}