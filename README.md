data-structures
===============

[![Build Status](https://travis-ci.org/lhp81/cf-data-structures.png?branch=master)](https://travis-ci.org/lhp81/cf-data-structures)

This repository holds code for a number of classic data structures, implemented in Python and written for the [Code Fellows](http://www.codefellows.org/) Python Bootcamp, taught by [Cris Ewing](https://www.github.com/cewing/).

All data structures were created using TDD.

These data structures are:

* **Single Linked List** _A Single Linked List that can…_
 * insert(val): insert the value 'val' at the head of the list
 * pop(): pop the first value off the head of the list and return it.
 * size(): return the length of the list
 * search(val): return the node containing 'val' in the list, if present, else None
 * remove(node): remove the given node from the list, wherever it might be (node must be an item in the list
 * print(): print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')"

* **Stack** _A Stack that can implement two methods:_
 * push(data): adds a data element to the stack. The parameter is the data element to add to the stack.
 * pop(): removes a data element from the stack and returns the value of that data element.  If the stack is empty, attempts to call pop should raise an appropriate Python exception class.

* **Queue** _A Queue with the following methods:_
 * enqueue(value): adds value to the queue
 * dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
 * size(): return the size of the queue.  Should return 0 if the queue is empty.

* **Hash Table** _A naïve hash table with the following methods:_
 * get(key): returns the value stored with the given key
 * set(key, val): stores the given val using the given key
 * hash(key): hashes the key provided

* **Make Month** _A practical implementation of my naïve hash table._

 * This function takes two arguments, a numeric year and month, and returns a data structure that supports quickly looking up the day of week on which a date falls, when provided a numeric day value.

* **Binary Search Tree** _A binary search tree that can (and will) be extended._
 * insert(self, val): will insert the value val into the BST.  If val is already present, it will be ignored.
 * contains(self, val): will return True if val is in the BST, False if not.
 * size(self): will return the integer size of the BST (equal to the total number of values stored in the tree), 0 if the tree is empty.
 * depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
 * balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value.  An ideally-balanced tree should return 0.
 * in_order(self): will return a generator that will return the values in the tree using in-order traversal, one at a time.
 * pre_order(self): will return a generator that will return the values in the tree using pre-order traversal, one at a time.
 * post_order(self): will return a generator that will return the values in the tree using post_order traversal, one at a time.
 * breadth_first(self): will return a generator that will return the values in the tree using breadth-first traversal, one at a time.
 * delete(self, val): remove val from the tree if present, if not present this method is a no-op. Return None in all cases

* **Merge Sort** _A merge sort function that is unfortunately inefficient_
 * This consists of one function, merge_sort(l). The function will return a sorted list of the values in the given list. In creating this function I referred to [rosetta code's merge/sort pseudocode](http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort), which helped me to organize my thoughts, as did a thread on SO that nudged me towards combining my two conditions into one line (line 16).