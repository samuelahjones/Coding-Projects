public class Song {
	private String title;
	private String artist;
	private int duration; // in seconds
	
	public Song (String title, String artist, int duration) {
		this.title = title;
		this.artist = artist;
		this.duration = duration;
	}
	
	/*
	* Purpose: get the title of the song
	* Parameters: nothing
	* Returns: String - title
	*/
	public String getTitle() {
		return title;
	}
	
	/*
	* Purpose: get the artist of the song
	* Parameters: none
	* Returns: String - artist
	*/
	public String getArtist() {
		return artist;
	}
	
	/*
	* Purpose: get the duration of the song (in seconds)
	* Parameters: none
	* Returns: int - duration
	*/
	public int getDuration() {
		return duration;
	}
	
	/*
	* Purpose: generates a string representation of a song
	* Parameters: none
	* Returns: String - representation of the song
	*/
	public String toString() {
		return title + " - " + artist + " (" + duration + ")";
	}
	
	/*
	* Purpose: determines whether this Song is the same as other
	* Parameters: Song - the song to compare to
	* Returns: boolean - true if they are equal, false otherwise
	*/
	public boolean equals(Song other) {
		return this.title.equals(other.getTitle())
			&& this.artist.equals(other.getArtist())
				&& this.duration == other.duration;
	}
}
