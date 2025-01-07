public class A5Tester {
	private static int testPassCount = 0;
	private static int testCount = 0;
	private static double THRESHOLD = 0.1; // allowable margin of error for floating point results
	
    public static void main(String[] args) {
		
		/* Linked List Recursion Exercises: */
		testCountSongs();
		testTotalDuration();
		testCountSongsByArtist();
		testContainsArtist();
		testLongestSong();
		testTotalTimeUntilArtist();

		/* Recursion Exercises using the List ADT */
		testChangeXToY();
		testCountOdd();
		testCountMostOddInARow();
		testCountBetweenX();
		
		System.out.println("Passed " + testPassCount + " / " + testCount + " tests");
	}
	
	public static void testCountSongs() {
		System.out.println("\nTesting countSongs");
		
		LinkedSongList list0 = new LinkedSongList();
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		int result = 0;
		int expected = 0;
		
		result = list1.countSongs();
		expected = 1;
		displayResults(result==expected, "countSongs in list1");
		
		result = list2.countSongs();
		expected = 4;
		displayResults(result==expected, "countSongs in list2");
		
		result = list3.countSongs();
		expected = 12;
		displayResults(result==expected, "countSongs in list3");
		
		// Write more tests here
		
		System.out.println();		
	}
	
	public static void testTotalDuration() {
		System.out.println("\nTesting totalDuration");
		
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		int result = 0;
		int expected = 0;
		
		result = list1.totalDuration();
		expected = 219;
		displayResults(result==expected, "totalDuration in list1");
		
		result = list2.totalDuration();
		expected = 219+225+237+243;
		displayResults(result==expected, "totalDuration in list2");
		
		result = list3.totalDuration();
		expected = 219+225+237+243+310+272+201+253+263+245+293+195;
		displayResults(result==expected, "totalDuration in list3");
		
		// Write more tests here
		
		System.out.println();
	}
	
	public static void testCountSongsByArtist() {
		System.out.println("\nTesting countSongsByArtist");
		
		LinkedSongList list0 = new LinkedSongList();
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		int result = 0;
		int expected = 0;
		String artistToFind = new String("Taylor Swift");
		
		result = list0.countSongsByArtist(artistToFind);
		expected = 0;
		displayResults(result==expected, "songs by "+artistToFind+" in empty list");
		
		result = list1.countSongsByArtist(artistToFind);
		// System.out.println(result);;
		expected = 1;
		displayResults(result==expected, "songs by "+artistToFind+" in list1");
		
		result = list2.countSongsByArtist(artistToFind);
		expected = 3;
		displayResults(result==expected, "songs by "+artistToFind+" in list2");
		
		artistToFind = new String("Beyonce");
		result = list2.countSongsByArtist(artistToFind);
		expected = 1;
		displayResults(result==expected, "songs by "+artistToFind+" in list2");
		
		// Write more tests here
		
		System.out.println();
	}
	
	public static void testContainsArtist() {
		System.out.println("\nTesting containsArtist");
		
		LinkedSongList list0 = new LinkedSongList();
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		boolean result = false;
		boolean expected = false;
		String artistToFind = new String("Taylor Swift");
		
		result = list0.containsArtist(artistToFind);
		expected = false;
		displayResults(result==expected, "list0 contains "+artistToFind);
		
		result = list1.containsArtist(artistToFind);
		expected = true;
		displayResults(result==expected, "list1 contains "+artistToFind);
		
		artistToFind = new String("Toto");
		
		result = list1.containsArtist(artistToFind);
		expected = false;
		displayResults(result==expected, "list1 contains "+artistToFind);
		
		result = list2.containsArtist(artistToFind);
		expected = false;
		displayResults(result==expected, "list2 contains "+artistToFind);
		
		artistToFind = new String("Taylor Swift");
		
		result = list2.containsArtist(artistToFind);
		expected = true;
		displayResults(result==expected, "list2 contains "+artistToFind);
		
		result = list3.containsArtist(artistToFind);
		expected = true;
		displayResults(result==expected, "list3 contains "+artistToFind);
		
		artistToFind = new String("Miley Cyrus");
		
		result = list3.containsArtist(artistToFind);
		expected = true;
		displayResults(result==expected, "list3 contains "+artistToFind);
				
		// Write more tests here
		
		System.out.println();
	}
	
	public static void testLongestSong() {
		System.out.println("Testing longestSong");
		
		LinkedSongList list0 = new LinkedSongList();
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		Song result = null;
		Song expected = null;
		
		result = list0.longestSong();
		displayResults(result==null, "longest song in list1");
				
		result = list1.longestSong();
		expected = s1;
		displayResults(result.equals(expected), "longest song in list1");
		
		result = list2.longestSong();
		expected = s4;
		displayResults(result.equals(expected), "longest song in list2");
		
		result = list3.longestSong();
		expected = s5;
		displayResults(result.equals(expected), "longest song in list3");
		
		// TODO: add more tests here
		
		System.out.println();
	}

	public static void testTotalTimeUntilArtist() {
		System.out.println("\nTesting totalTimeUntilArtist");
		
		LinkedSongList list0 = new LinkedSongList();
		LinkedSongList list1 = new LinkedSongList();
		LinkedSongList list2 = new LinkedSongList();
		LinkedSongList list3 = new LinkedSongList();
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song s5  = new Song("Anti-Hero", "Taylor Swift", 310);
		Song s6  = new Song("Africa", "Toto", 272);
		Song s7  = new Song("Single Ladies", "Beyonce", 201);
		Song s8  = new Song("Irreplaceable", "Beyonce", 253);
		Song s9  = new Song("Blank Space", "Taylor Swift", 263);
		Song s10 = new Song("Bad Blood", "Taylor Swift", 245);
		Song s11 = new Song("Thunderstruck", "AC/DC", 293);
		Song s12 = new Song("Flowers", "Miley Cyrus", 195);
		
		Song[] songs1 = {s1}; 
		Song[] songs2 = {s1, s2, s3, s4}; 
		Song[] songs3 = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12}; 
		list1.buildFromArray(songs1);
		list2.buildFromArray(songs2);
		list3.buildFromArray(songs3);
		
		int result = 0;
		int expected = 0;
		String artistToFind = new String("Taylor Swift");
		
		result = list0.totalTimeUntilArtist(artistToFind);
		expected = -1;
		displayResults(result==expected, "total duration of songs until song by "+artistToFind);
		
		result = list1.totalTimeUntilArtist(artistToFind);
		expected = 0;
		displayResults(result==expected, "total duration of songs until song by "+artistToFind);
		
		artistToFind = new String("Beyonce");
		result = list2.totalTimeUntilArtist(artistToFind);
		expected = 219;
		displayResults(result==expected, "total duration of songs until song by "+artistToFind);
		
		artistToFind = new String("Toto");
		result = list3.totalTimeUntilArtist(artistToFind);
		expected = 219+225+237+243+310;
		displayResults(result==expected, "total duration of songs until song by "+artistToFind);
		
		artistToFind = new String("AC/DC");
		result = list3.totalTimeUntilArtist(artistToFind);
		expected = 219+225+237+243+310+272+201+253+263+245;
		displayResults(result==expected, "total duration of songs until song by "+artistToFind);
		
		// TODO: add more tests here
		
		System.out.println();
	}
	
	public static void testChangeXToY() {
		System.out.println("\nTesting changeXToY");
		SinglyLinkedList<Song> list0 = new SinglyLinkedList<Song>();
		SinglyLinkedList<Integer> list1 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<String> list2 = new SinglyLinkedList<String>();
		SinglyLinkedList<Song> list3 = new SinglyLinkedList<Song>();
		Integer[] arr1 = {9, 3, 1, 2, 3, 3, 4, 2, 1, 2, 1, 1};
		String[]  arr2 = {"test", "the", "test", "to", "test", "the", "test"};
		
		Song s1  = new Song("Shake it off", "Taylor Swift", 219);
		Song s2  = new Song("Halo", "Beyonce", 225);
		Song s3  = new Song("Love Story", "Taylor Swift", 237);
		Song s4  = new Song("22", "Taylor Swift", 243);
		Song[] arr3 = {s1, s2, s2, s1, s3, s4, s1};
		
		list1.buildFromArray(arr1); // list1: {9, 3, 1, 2, 3, 3, 4, 2, 1, 2, 1, 1}
		list2.buildFromArray(arr2); // list2: {"test", "the", "test", "to", "test", "the", "test"};
		list3.buildFromArray(arr3);
		
		String result = "";
		String expected = "";		
		
		A5Exercises.changeXToY(list0, s1, s2);
		result = list0.toString();
		expected = "{}";
		displayResults(result.equals(expected), "change all in empty list");
		
		list0.add(s1);
		list0.add(s3);
		A5Exercises.changeXToY(list0, s1, s3);
		result = list0.toString();
		expected = "{Love Story - Taylor Swift (237), Love Story - Taylor Swift (237)}";
		// System.out.println(result);
		displayResults(result.equals(expected), "change all "+s1+" to "+s3);
		
		A5Exercises.changeXToY(list1, 2, 4);
		result = list1.toString();
		expected = "{9, 3, 1, 4, 3, 3, 4, 4, 1, 4, 1, 1}";
		displayResults(result.equals(expected), "change all 2s to 4s");
				
		A5Exercises.changeXToY(list1, 1, 3);
		result = list1.toString();
		expected = "{9, 3, 3, 4, 3, 3, 4, 4, 3, 4, 3, 3}";
		displayResults(result.equals(expected), "change all 1s to 3s");
		
		// Write more tests here
		
		System.out.println();
	}
	
	public static void testCountOdd() {
		System.out.println("\nTesting countOdd");
		
		SinglyLinkedList<Integer> list0 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list1 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list2 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list3 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list4 = new SinglyLinkedList<Integer>();
		Integer[] arr1 = {3}; 
		Integer[] arr2 = {3, 1, 7, 5, 0, 4}; 
		Integer[] arr3 = {2, 6, 8, 4};
		Integer[] arr4 = {2, 6, 8, 4, 7};

		list1.buildFromArray(arr1);
		list2.buildFromArray(arr2);
		list3.buildFromArray(arr3);
		list4.buildFromArray(arr4);
				
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.countOdd(list1);
		expected = 1;
		displayResults(result==expected, "countOdd in list1");
		
		result = A5Exercises.countOdd(list2);
		expected = 4;
		displayResults(result==expected, "countOdd in list2");
		
		result = A5Exercises.countOdd(list3);
		expected = 0;
		displayResults(result==expected, "countOdd in list3");
		
		result = A5Exercises.countOdd(list4);
		expected = 1;
		displayResults(result==expected, "countOdd in list4");
		
		// write more test here
		
		System.out.println();
	}
	
	public static void testCountMostOddInARow() {
		System.out.println("\nTesting countMostOddInARow");
		SinglyLinkedList<Integer> list0 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list1 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list2 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list3 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list4 = new SinglyLinkedList<Integer>();
		Integer[] arr1 = {3}; 
		Integer[] arr2 = {2}; 
		Integer[] arr3 = {3, 1, 7, 5, 0, 4}; 
		Integer[] arr4 = {3, 2, 1, 7, 6, 5, 1, 7, 4}; 
											 
		list1.buildFromArray(arr1);
		list2.buildFromArray(arr2);
		list3.buildFromArray(arr3);
		list4.buildFromArray(arr4);
				
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.countMostOddInARow(list0);
		expected = 0;
		displayResults(result==expected, "countMostOddInARow in empty list");
		
		result = A5Exercises.countMostOddInARow(list1);
		expected = 1;
		displayResults(result==expected, "countMostOddInARow in list with 1 element (odd)");
		
		result = A5Exercises.countMostOddInARow(list2);
		expected = 0;
		displayResults(result==expected, "countMostOddInARow in list with 1 element (even)");
		
		result = A5Exercises.countMostOddInARow(list3);
		expected = 4;
		displayResults(result==expected, "countMostOddInARow in list with 4 in a row");
		
		result = A5Exercises.countMostOddInARow(list4);
		expected = 3;
		displayResults(result==expected, "countMostOddInARow in list with 1, 2, then 3 in a row");
		
		// Write more tests here
		
		System.out.println();
	}
	
	public static void testCountBetweenX() {
		System.out.println("\nTesting countBetweenX");
		SinglyLinkedList<Integer> list0 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list1 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list2 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list3 = new SinglyLinkedList<Integer>();
		SinglyLinkedList<Integer> list4 = new SinglyLinkedList<Integer>();
		Integer[] arr1 = {4}; 
		Integer[] arr2 = {5, 5}; 
		Integer[] arr3 = {1, 4, 1}; 
		Integer[] arr4 = {1, 2, 3, 4, 2, 5, 2, 3}; 
											 
		list1.buildFromArray(arr1);
		list2.buildFromArray(arr2);
		list3.buildFromArray(arr3);
		list4.buildFromArray(arr4);
				
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.countBetweenX(list0, 1);
		expected = -1;
		displayResults(result==expected, "count between 1s in empty list");
		
		result = A5Exercises.countBetweenX(list1, 4);
		expected = -1;
		displayResults(result==expected, "count between 4s in {4}");
		
		result = A5Exercises.countBetweenX(list2, 5);
		expected = 0;
		displayResults(result==expected, "count between 5s in {5, 5}");
		
		result = A5Exercises.countBetweenX(list3, 1);
		expected = 1;
		displayResults(result==expected, "count between 1s in {1, 4, 1}");
		
		result = A5Exercises.countBetweenX(list4, 2);
		expected = 2;
		displayResults(result==expected, "count between 2s in {1, 2, 3, 4, 2, 5, 2, 3}");
		
		result = A5Exercises.countBetweenX(list4, 3);
		expected = 4;
		displayResults(result==expected, "count between 3s in {1, 2, 3, 4, 2, 5, 2, 3}");
		
		// Write more tests here
		
		System.out.println();
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