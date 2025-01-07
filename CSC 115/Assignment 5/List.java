public interface List<T> {

	/* 
	 * Purpose: add data to the back of the list
	 * Parameters: T data - the data to add
	 * Returns: nothing
	 * Precondition: data is not null
	 */
	public void add(T data);

	/* 
	 * Purpose: get the element at given position in the list
	 * Parameters: int position - the position to get the element
	 * Returns: T - the element
	 * Preconditions: 0 <= position < size()
	 */
	public T get(int position);
	
	/* 
	 * Purpose: change the value of the element at the given position
	 * Parameters: int position - the position of the element to update
	 *             T newValue - the value to set the element to
	 * Returns: void - nothing
	 * Preconditions: 0 <= position < size()
	 */
	public void change(int position, T newValue);

	/* 
	 * Purpose: removes the element from the front of the list
	 * Parameters: none
	 * Returns: T - the element removed
	 */
	public T removeFront();
	
	/* 
	 * Purpose: removes the element from the back of the list
	 * Parameters: none
	 * Returns: T - the element removed
	 */
	public T removeBack();
	
	/* 
	 * Purpose: get the current size of the list
	 * Parameters: none
	 * Returns: int - number of elements in list
	 */
	public int size(); 
	
	/* 
	 * Purpose: determines if the list is empty
	 * Parameters: none
	 * Returns: boolean - true if empty, false otherwise
	 */
	public boolean isEmpty();
}