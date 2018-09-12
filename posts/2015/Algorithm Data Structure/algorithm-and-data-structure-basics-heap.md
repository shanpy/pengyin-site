.. title: Algorithm and Data Structure Basics - Heap
.. date: 2015-09-03
.. category: Algorithm & Data Structure
.. tags: Java, Algorithm, Data Structure, Heap
.. slug: algorithm-and-data-structure-basics-heap
.. authors: Pengyin Shan
.. description: I wrote this post to record some basic knowledge about using Heap for future reference. Code is written mainly in Java.

###Reference List

- *Data Structures and Algorithms in Java (Second Edition)*, written by *Robert Lafore*, Chinese Version

###Basic Information

Heap is a type of tree. If you create a **priority queue** from heap. The time complexity for insertion and deletion is `O(logN)`. However, heap doesn't support traversal and search by value, because all path in heap is following descending/ascending order.

Heap has following features:

- It is a **complete binary tree**. A complete binary tree means every layer except leaf layer has full nodes.

- Heap is normally implemented by a array

- For each node in heap, the value of this node is larger or equal to the value of its child nodes (Maximum Heap). If current node is smaller or equal to its child nodes, the heap is Minimum Heap.

Following is the graph for array implementation of heap, taken from *Data Structures and Algorithms in Java (Second Edition)*:

../images/articles/2015/algorithm/heap_array.PNG 

>As you can see, if the index of a random element in array is `x`, then the index of its parent node is `(x-1)/2`. The index of its left child node is `2*x+1`. The index of its right child node is `2*x+2`

*In Java, `/` will get floor integer value*.

>All nodes which have index larger than `n/2` are leaf nodes, assuming there are n elements in array.

###Remove

In heap, remove means removing the root of the heap. This root is always the largest/smallest value of all elements. For the heap array, root always has index `0`.

You need two steps to find removing process:

1. Take root of heap out

2. Fill the root hold by move the last element to root, then reverse and change nodes until heap is correct.

Detail of steps:

1. Remove root by using `max = heapArray[o];`

2. Move last element to root by using `heapArray[0] = heapArray[N-1]; N--;`

3. Move this new root to bottom, until it's smaller than its parent node and larger than its child nodes. To do this, check if root is smaller than it's **larger child**. If so, swap root and its larger child. Repeat this.

####Code

    :::java
    //We assume each node has a attribute 'key', which determine the value/priority of this node
    public Node remove(){
        Node root = heapArray[0];
        heapArray[0] = heapArray[--currentSize]; //Move last element to root position
        trickleDown[o]; //trickleDown new root
        return root;
    }

    void trackleDown(int index){
        int largetChild;
        Node current = heapArray[index]; //current Node

        //while index is not on leaf node
        while(index < currentSize/2){
            int leftChild = 2*index + 1;
            int rightChild = leftChild + 1;

            //Get larger child
            if(rightChild < currentSize && heapArray[leftChild].getKey() < heapArray[rightChild].getKey()){
                largerChild = rightChild;
            }else
                largerChild = leftChild;

            //Break while loop when current value is larger than larger child value
            if(current.getKey() >= heapArray[largerChild].getKey())
                break;
            /*
            If not break loop, move child to current position.
            Go to another loop starting from larger child position.
            current keeps the same
            */
            heapArray[index] = heapArray[largerChild];
            index = largerChild;
        }

        heapArray[index] = current; //After loop, assign new root to proper position
    }

###Insert

Insertion can by down by following step:

1. Put the new element to end of array(i.e. end of heap): `heapArray[N] = insertNode; N++;`

2. Recursively moving this node so that it will be larger than its child elements and smaller than its parent node. i.e. if node is smaller larger than its parent node, swap this node and its parent node.

####Code

    :::java
    //We assume each node has a attribute 'key', which determine the value/priority of this node
    public boolean insert(int key){
        if(currentSize == maxSize)
            return false; //no more room for insertion
        Node newNode = new Node(key);
        heapArray[currentSize] = newNode;
        currentSize++;
        trickleUp(currentSize);
        return true;
    }

    void trickleUp(int index){
        int parent = (index-1)/2; //get parent index
        Node current = heapArray[index]; //get current node

        while(index>0 && heapArray[parent].getKey()<bottom.getKey()){
            heapArray[index] = heapArray[parent];
            index = parent; //Now parent index should be current index
            parent = (parent-1)/2; //Get new parent index
        }

        heapArray[index] = current; //after while loop, assign current node to final place
    }

###Change Value

Working in process...