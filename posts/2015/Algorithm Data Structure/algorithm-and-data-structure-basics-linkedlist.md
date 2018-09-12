.. title: Algorithm and Data Structure Basics - Linked List
.. date: 2015-09-02
.. modified: 2015-09-03
.. category: Algorithm & Data Structure
.. tags: Java, Algorithm, Data Structure, Linked List
.. slug: algorithm-and-data-structure-basics-linkedlist
.. authors: Pengyin Shan
.. description: I wrote this post to record some basic knowledge about using Linked List for future reference. Code is written mainly in Java.

###Reference List

- <a href="http://www.linuxidc.com/Linux/2014-04/99926.htm">Merge Sort for Single Linked List Java (Chinese)</a>

- *Data Structures and Algorithms in Java (Second Edition)*, written by *Robert Lafore*, Chinese Version

###Efficiency of Linked List

Insertion and Deletion **at the head of linked list** is really quick. It need `O(1)` time complexity.

####Compare with Array

Both array and linked list need `O(N)` time complexity for searching and insertion/deletion to certain node. However, linked list may still be a better option, because it **does not need to move** anything when it does these operations. Linked list can save lots of time expecially if there exists a large amount of elements.

Linked list is also better at saving space. Linked list also gives flexibility of expanding size.

So if we don't know exact size of data, linked list can be a better option comparing to array.

###ADT

You can create `stack` using linked list. When you create `push` and `pop` method, just insert/remove first element from head of linked list.

###Insertion Sort for Sorted Linked List

If you have a un-sorted array, you can take all elements out, and insert them to a sorted linked list. Then after you deleting all elements and re-put them to array, this array will become a sorted one.

    :::java
    /*
      Insert Node at the end of a linked list
      head pointer input could be NULL as well for empty list
      Node is defined as
      class Node {
         int data;
         Node next;
      }
    */
    class SortedList{
      private Node head; //head of linked list

      public SortedList(){
        head = null;
        //constructor for empty list
      }

      //Constructor for taking a array of nodes as parameter
      public SortedList(Node[] nodearray){
        head = null;
        for(int j=0; j<nodearray.length; j++){
          insert(nodearray[j]);
        }
      }

      public void insert(Node insertNode){
        Node currentNode = new Node();
        currentNode = head;

        if(currentNode.next == null){
          //Skip this process. Insert insertNode if there is only one node in linked list
        }

        //Do insertion sort. Left most is always the largest one
        while(currentNode.next != null && insertNode.data > currentNode.next.data){
          Node temp = currentNode.next;
          currentNode.next = insertNode;
          insertNode.next = temp;
          currentNode = currentNode.next;
        }
      }
    }

###Iterator

Iterator is used as a reference so that it can point to any node in linked list, in order to find and change certain node.

####Class of Iterator

    :::java
    class ListIterator(){
      private Node current; //current node in linked list that iterator is pointing to
      //private Node previous;  for doubly linked list
      private LinkedList currentList; //current linked list
    }

####Main Class

You may have different iterators for one linked list. Each iterator points to a certain node.

    :::java
    public static void main(...){
      LinkedList l = new LinkedList();
      ListIterator iter = l.getIterator();
      Node point = iter.getCurrent(); //get current node in iterator
      //point.next...
    }

####Possible Methods

You can add following possible methods to your iterator:

- reset(): Make iterator point to head of linked list

- nextLink(): Make iterator point to next node

- getCurrent(): return current node

- atEnd(): return `true` if iterator is pointing to end of linked list

- insertAfter()/insertBefore()/deletCurretn(): operation for insertion/deletion

###Merge Two Sorted Linked Lists/Merge Sort Single Linked List

You can check **Merge Two Sorted Linked Lists** on <a href="https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/submissions/code/13529242">hackerrank.com</a>.

####Idea

To merge two sorted linked lists, you just need to create a new node and always get the smaller node from two source linked lists. Every time a node is passed, move `header` to next node.

To merge sort a single linked list, you need to have two pointer: `p` and `f`. Every time if `p` points to next node, `f` should point to the node after the next one. In this case, when `f` finish walking through **a certain part of linked list**, `p` is **on the half** of that linked list.

Recursively call the method above for first part(start from origin head) of linked list and second part(start from `p`) for division process. Then merge result using same method as merging two sorted linked lists

####Code

#####Code for merging two sorted linked list, on hackerrank.com:

    :::java
    /*
      Insert Node at the end of a linked list
      head pointer input could be NULL as well for empty list
      Node is defined as
      class Node {
         int data;
         Node next;
      }
    */

    Node MergeLists(Node headA, Node headB) {
            Node c = new Node();
            Node result = c;

            while (headA != null && headB != null ){
                if (headA.data <= headB.data){
                    c.next = headA;
                    headA = headA.next;
                }else {
                    c.next = headB;
                    headB = headB.next;
                }
                c = c.next;
            }

            if(headA == null){
                c.next = headB;
            }else{
                c.next = headA;
            }

            return result.next;
            //result is a empty node. result.next (i.e. c.next) is the start of new linked list
        }

#####Code for merging single linked list, divide part:

    :::java
    /*
      Insert Node at the end of a linked list
      head pointer input could be NULL as well for empty list
      Node is defined as
      class Node {
         int data;
         Node next;
      }
    */
    public class Solution {
    public Node sortList(Node head) {

        if (head == null || head.next == null){
            return head;
        }

        ListNode p = head;
        ListNode f = head.next;

        while ( f.next !=null && f.next.next !=null ){
            p = p.next;
            f = f.next.next;
        }

        //Perform division to second half of linked list
        ListNode h2 = sortList(p.next);
        p.next = null;

        /*
        Perform divide to first half of linked list (starting from head),then merge division result.
        'MergeLists' method is the code in first part
        */
        return MergeLists(sortList(head),h2);
    }

###Flatten a Doubly Linked List

This is a question from the book *Programming Interview Exposed*. Following graph is a example of a doubly linked list, from <a href="http://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/">this post</a>:

../images/articles/2015/algorithm/double_linkedlist.png 

####Idea

Generally, each child linked list can be flattened as a single linked list, which can be appended to the end of result linked list. Each time you encounter a node with a child, append the child (and thus the child list) to the **end of the first level** and update the **tail pointer**.

This is a description of algorithm:

    :::command
    Start at the beginning of the first level
    While you are not at the end of the first level
        If the current node has a child
            Append the child to the end of the first level
            Update the tail pointer
        Advance to next node

####Code

    :::java
    /*
      Insert Node at the end of a linked list
      head pointer input could be NULL as well for empty list
      Node is defined as
      class Node {
         int data;
         Node next;
         Node prev;
         Node child;
      }
    */
    void flattenList(Node head, Node tail){
        Node currentNode = new Node();
        currentNode = head;

        while(currentNode != null){
            if(currentNode.child != null)
                append(currentNode.child, tail);
        }
        currentNode = currentNode.next
    }

    /*
    Append the child list to the end of the tail and update the tail;
    */
    void append(Node child, Node tail){
        Node currentNode = new Node();

        //Append child list to tail
        tail.next = child;
        child.prev = tail;

        //Find the new tail, which should be the end of the child list
        currentNode = child;
        while(currentNode.next != null){
            currentNode = currentNode.next;
        }

        //Update the tail pointer now that currentNode is the new tail
        tail = currentNode;
    }

###Unflatten Previous Linked List

####Idea

To unflatten previous linked list, you can do following:

    :::command
    Explore Path:
        While not at the end
            If current node has a child
                Separate the child from its previous node
                Explore path beginning with the child
            Go onto the next node

####Code

    :::java
    /*
      Insert Node at the end of a linked list
      head pointer input could be NULL as well for empty list
      Node is defined as
      class Node {
         int data;
         Node next;
         Node prev;
         Node child;
      }
    */
    void unflattenList(Node start, Node tail){
        Node currentNode = new Node();

        exploreAndSeparate(start);

        //Update the tail pointer
        currentNode = start;
        while(currentNode.next != null)
            current = current.next
        tail = currentNode;
    }

    //exploreAndSeparate actually does the recursion and separation
    void exploreAndSeparate(Node childListStart){
        Node currentNode = new Node();
        currentNode = childListStart;

        while(currentNode.next != null){
            //Check if currentNode is a start of a child list
            if(currentNode.child != null){
                //Broken child list from origin list. i.e. original prev node should point to null now
                currentNode.child.prev.next = null;
                //Split new child list out. Remember original parent can still do node.child to get this child list
                currentNode.child.prev = null;

                //Run recursion so that all childs from child node can be split
                exploreAndSeparate(currentNode.child);
            }
            currentNode = currentNode.next;
        }
    }
