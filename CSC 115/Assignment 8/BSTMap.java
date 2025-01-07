import java.util.*;

public class BSTMap<K extends Comparable<K>, V > implements  Map<K, V>  {
    
	BinarySearchTree<K,V> bst;

	public BSTMap () {
		bst = new BinarySearchTree<K,V>();
	}

	public boolean containsKey(K key) {
		try {
			V found = this.bst.find(key);
			return true;
		} catch (KeyNotFoundException e) {
			return false;
		} 
	}

	public V get (K key) throws KeyNotFoundException {
		try {
			V found = this.bst.find(key);
			return found;
		} catch (KeyNotFoundException e) {
			throw new KeyNotFoundException();
		} 
	}

	public List<Entry<K,V> >	entryList() {
		return this.bst.entryList(); // so it compiles
	}

	public void put (K key, V value) {
		bst.insert(key, value);
	}

	public int size() {
		return this.bst.size(); // so it compiles
	}

	public void clear() {
		this.bst.clear();
	}

}