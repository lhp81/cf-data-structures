data-structures
===============

[![Build Status](https://travis-ci.org/lhp81/cf-data-structures.png?branch=master)](https://travis-ci.org/lhp81/cf-data-structures)

This repository holds code for a number of classic data structures, implemented in Python and written for the [Code Fellows](http://www.codefellows.org/) Python Bootcamp, taught by [Cris Ewing](https://www.github.com/cewing/).

All data structures were created using TDD.

These data structures are:

* **Single Linked List** _A Single Linked List that can…_
 * insert(val) will insert the value 'val' at the head of the list
 * pop() will pop the first value off the head of the list and return it.
 * size() will return the length of the list
 * search(val) will return the node containing 'val' in the list, if present, else None
 * remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list
 * print() will print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')"

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