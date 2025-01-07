import java.util.*;

/*
 * An implementation of a binary search tree. This tree stores 
 * both keys and values associated with those keys.
 *
 * More information about binary search trees can be found here:
 * http://en.wikipedia.org/wiki/Binary_search_tree
 */
class BinarySearchTree <K extends Comparable<K>, V>  {

	public static final int BST_PREORDER  = 1;
	public static final int BST_POSTORDER = 2;
	public static final int BST_INORDER   = 3;

	// These are package friendly for the TreeView class
	BSTNode<K,V> root;
	int	count;

	public BinarySearchTree () {
		root = null;
		count = 0;
	}

	
	/* Purpose: Insert a new key-value element into the tree.  
	 *          If the key already exists in the tree, update 
	 *          the value stored at that node with the new value.
	 * Parameters: K key - the key for which the BST is ordered
     *	 		   V value - the value to associate with the key
	 * Returns: nothing
	 * Pre-Conditions: the tree is a valid binary search tree
	 */
	public void insert (K key, V value) {
		if( root == null ) {
			BSTNode<K,V> cur = new BSTNode<K,V>(key, value); 
			root = cur;
		} else {
			insRec(root, key, value);
		}
		count++;
	}

	public void insRec( BSTNode<K,V> cur, K key, V value) {
		if( cur.key.compareTo(key) == 0 ) {
			cur.value = value;
			return;
		} else if( cur.key.compareTo(key) < 0 ) {
			if( cur.left != null ) {
				insRec(cur.left, key, value);
			} else {
				BSTNode<K,V> ins = new BSTNode<K,V>(key, value); 
				cur.left = ins;
				return; 
			}
		} else {
			if( cur.right != null ) {
				insRec(cur.right, key, value);
			} else {
				BSTNode<K,V> ins = new BSTNode<K,V>(key, value); 
				cur.right = ins;
				return; 
			}
		}
	}

	/* 	
	 * Purpose: Get the value of the given key. 
	 * Parameters: K key - the key to search for
	 * Returns: V - the value associated with the key
	 * Pre-conditions: the tree is a valid binary search tree
	 * Throws: KeyNotFoundException if key isn't in the tree
	 */
	public V find (K key) throws KeyNotFoundException {
		try{
			return findRec(root, key);
		} catch (KeyNotFoundException e) {
			throw new KeyNotFoundException();
		}
	}

	public V findRec( BSTNode<K,V> cur, K key ) throws KeyNotFoundException {
		if( cur == null ) {
			throw new KeyNotFoundException();
		} 
		if( cur.key.compareTo(key) == 0 ) {
			return cur.value;
		} else {
			if( cur.key.compareTo(key) > 0 ) {
				try {
					return findRec(cur.right, key);
				} catch (KeyNotFoundException e) {
					throw new KeyNotFoundException();
				}
			} else {
				try {
					return findRec(cur.left, key);
				} catch (KeyNotFoundException e) {
					throw new KeyNotFoundException();
				}
			}
		}
	}

	/* 	
	 * Purpose: Get the number of nodes in the tree.
	 * Parameters: none
	 * Returns: int - the number of nodes in the tree. 
	 */
	public int size() {
		return count; // so it compiles
	}

	/*
	 * Purpose: Remove all nodes from the tree.
	 * Parameters: none
	 * Returns: nothing
	 */
	public void clear() {
		root = null;
	}

	/* 
	 * Purpose: Get the height of the tree. 
	 * Parameters: none
	 * Returns: int - the height of the tree
	 * Example: We define height as being the number of 
	 * arrows that need to be followed on the path from 
	 * the root to the deepest leaf node. This means that 
	 * a tree with one node (just the root) has height 0,
	 * and an empty tree (root is null) has height -1.
	 *
	 * See the assignment PDF and the test program for examples.
	 */
	public int height() {
		if( root == null ) {
			return -1;
		} else if( count == 1 ) {
			return 0;
		} else if( count == 2 ) {
			return 1;
		}
		int h = heightRec(root, -1, 0, 0);
		// go down each branch and get the height and compare to the next bratch over keeping the biggest height
		return h; // so it compiles
	}

	public int heightRec( BSTNode<K,V> cur, int a, int b, int c ) {
		if( cur == null ) {
			if( a > b ) {
				b = a;
			}
			return b;
		}
		a++;
		c++;
		int l = heightRec(cur.left, a, b, c);
		int r = heightRec(cur.right, a, b, c);
		if( l < r ) {
			b = r; 
		} else {
			b = l;
		}
		return b; 

	}

	/* 
	 * Purpose: Return a list of all the key-value Entry elements 
	 *          stored in the tree using a level-order traversal.
	 * Parameters: None
	 * Returns: List<Entry<K,V>> - a list of key-value entries
	 *
	 * Example: A level order traversal of a tree cannot be done 
	 *          without the help of a secondary data structure.
	 *
	 *          It is commonly implemented using a queue of nodes 
	 *          as the secondary data structure. You will still be 
	 *          adding the "visited" elements to l as you do in the 
	 *          other traversal methods but you will create an 
	 *          additional q to hold nodes still to visit. This is
	 *          similar to what we did in the worksheet on tree traversals.
	 *
	 * From wikipedia (they call it breadth-first), the algorithm 
	 * for level order is:
	 *
	 *  levelorder()
	 *      q = empty queue
	 *      q.enqueue(root)
	 *      while not q.empty do
	 *          node := q.dequeue()
	 *          visit(node)
	 *          if node.left != null then
	 *                q.enqueue(node.left)
	 *          if node.right != null then
	 *                q.enqueue(node.right)
	 *
	 * Note that you can use the Java LinkedList as a Queue
	 * and then use only the removeFirst() and addLast() methods on q
	 */
	public List<Entry<K,V>>	entryList() {
		// list to add all the nodes to
		List<Entry<K,V> > l = new LinkedList<Entry<K,V>>();
		
		// queue of nodes that need to be added
		LinkedList<BSTNode<K,V>> q = new LinkedList<BSTNode<K,V> >();
		q.push(root);
		int i = 0;
		while( q.isEmpty() != true ) {
			BSTNode<K,V> d = q.pop();
			// System.out.println(d.key);
			Entry<K,V> f = new Entry<K,V>(d.key, d.value);
			l.addLast(f);
			l.set(i, new Entry<K,V>(d.key, d.value));
			// System.out.println(f);
			if( d.left != null ) {
				q.push(d.left);
			}
			if( d.right != null ) {
				q.push(d.right);
			}
			i++;
		}
		return l;
	}


	/* 	
	 * Purpose: Get a list of all the key-value entries stored in the tree
	 * Parameters: int whichTraversal - the type of traversal to perform:
	 * Returns: List<Entry<K,V>> - a list of key-value entries
	 * Example: The list will be constructed by performing a traversal
	 * specified by the parameter whichTraversal.
	 * 
	 * If whichTraversal is:
	 *	 BST_PREORDER	perform a pre-order traversal
	 *	 BST_POSTORDER	perform a post-order traversal
	 *	 BST_INORDER	perform an in-order traversal
	 */
	public List<Entry<K,V> > entryList (int which) {
		List<Entry<K,V> > entries = new LinkedList<Entry<K,V> >();

		if (which == BST_PREORDER) {
			preOrderRec(root, entries);
		}
		else if (which == BST_INORDER) {
			inOrderRec(root, entries);
		}
		else if (which == BST_POSTORDER) {
			postOrderRec(root, entries);
		}
		return entries;
	}

	private void inOrderRec (BSTNode<K,V> n, List <Entry<K,V>> entries) {
		if( n == null ) {
			return;
		}
		inOrderRec(n.left, entries);
		Entry<K,V> l = new Entry<K,V>(n.key, n.value);
		entries.addLast(l);
		inOrderRec(n.right, entries);
	}

	private void preOrderRec (BSTNode<K,V> n, List <Entry<K,V>> entries) {
		if( n == null ) {
			return;
		}
		Entry<K,V> l = new Entry<K,V>(n.key, n.value);
		entries.addLast(l);
		inOrderRec(n.left, entries);
		inOrderRec(n.right, entries);
	}

	private void postOrderRec (BSTNode<K,V> n, List <Entry<K,V>> entries) {
		if( n == null ) {
			return;
		}
		inOrderRec(n.left, entries);
		inOrderRec(n.right, entries);
		Entry<K,V> l = new Entry<K,V>(n.key, n.value);
		entries.addLast(l);
	}
}