.. title: Algorithm and Data Structure Basics - Recursion
.. date: 2015-09-02
.. category: Algorithm & Data Structure
.. tags: Java, Algorithm, Data Structure, Recursion
.. slug: algorithm-and-data-structure-basics-recursion
.. authors: Pengyin Shan
.. description: I wrote this post to record some basic knowledge about using recursion for future reference. Code is written mainly in Java.

###Reference List

- <a href="http://www.nowamagic.net/librarys/veda/detail/2314">Understand Recursion (Chinese)</a>

- <a href="http://blog.csdn.net/wangjinyu501/article/details/8248492">Recursion (Chinese)</a>

###Common Model of Recursion

    :::java
    Obj recursion(Obj o){
        if(baseCondition){
            /*
            You need to return here, so that recursion part can use the basic value which is returned back
            */
            return baseConditionResult;
        }else{
            o = some_expression;
            recursion(o);
        }
    }

*If there are other expression before or after recursion call, make sure you run it after each call back, because these expressions are part of method, and you want to call the full method for each recursion. Check "Hanoi" example below for detail.*

###Problem in Recursion

Since system using **stack** to save return values from each callback, it's really easy to get memory overflow problem.

###Hanoi

####Rule

1. Move plate when number of plate is `1` (In code below, we want to printout basic value);

2. If number of plates on a tower is more than `1` (assume `n`), move first `n-1` plate, then move the bottom plate.

####Code

    :::java
    /**
    Result:
        Dist 1 from A  to C
        Dist 2 from A to B
        Dist 1 from C  to B
        Dist 3 from A to C
        Dist 1 from B  to A
        Dist 2 from B to C
        Dist 1 from A  to C
    */
    public class Hanoi {

        static int nDisks = 3;

        public static void doTowers(int topN, char from, char inter, char to){
            if(topN == 1)
                System.out.println("Dist " + topN + " from " + from + " to " + to);
            else{
                //Move top n-1 from start tower to mid tower
                doTowers(topN-1, from, to, inter);
                System.out.println("Dist " + topN + " from " + from + " to " + to);
                //Move top n-1 from mid tower to end tower
                doTowers(topN-1, inter, from, to);
            }
        }

        public static void main(String[] args) {
            doTowers(nDisks, 'A', 'B', 'C');
        }

    }

To make code looks clear, I draw a draft of the sequence of recursion call for the code above. Note the purpose numbers are the sequence of call:

../images/articles/2015/algorithm/hanoi_graph.png 

###Merge Sort

####Code

    :::java
    /*
    Output:
    72 90 45 126 54
    45 54 72 90 126
    */
    public class MergeSort {

        private long[] theArray;
        private int nElems;

        public MergeSort(int max){
            theArray = new long[max];
            nElems = 0;
        }

        public void insert(long value){
            theArray[nElems] = value;
            nElems++;
        }

        public void display(){
            for(int j=0; j<nElems; j++){
                System.out.print(theArray[j] + " ");
            }
            System.out.println("");
        }

        public void mergeSort(){
            long[] workspace = new long[nElems];
            recMergeSort(workspace, 0, nElems-1);
        }

        private void recMergeSort(long[] workspace, int lowerBound, int upperBound){
            if(lowerBound == upperBound)
                return;
            else{
                int mid = (lowerBound + upperBound)/2;
                recMergeSort(workspace, lowerBound, mid);
                recMergeSort(workspace, mid+1, upperBound);
                merge(workspace,lowerBound, mid+1, upperBound);
            }
        }

        private void merge(long[] workspace, int lowPtr, int highPtr, int upperBound){
            int j=0;
            int lowerBound = lowPtr;
            int mid = highPtr-1;
            int n = upperBound - lowerBound +1; //# of items

            while(lowPtr <= mid && highPtr <= upperBound){
                if(theArray[lowPtr]<theArray[highPtr]){
                    workspace[j++] = theArray[lowPtr++];
                }else{
                    workspace[j++] = theArray[highPtr++];
                }
            }

            while(lowPtr <= mid){ //upper side are gone, some lower side left
                workspace[j++] = theArray[lowPtr++];
            }
            while(highPtr<=upperBound){ //lower side are gone, some upperside left
                workspace[j++] = theArray[highPtr++];
            }

            for(j=0; j<n; j++){//copy back
                theArray[lowerBound+j] = workspace[j];
            }
        }

        public static void main(String[] args) {
            int maxSize = 100;
            MergeSort arr = new MergeSort(maxSize);
            arr.insert(72);
            arr.insert(90);
            arr.insert(45);
            arr.insert(126);
            arr.insert(54);
            arr.display();

            arr.mergeSort();
            arr.display();
        }

    }

###Binary Search

    :::java
    /**
    Output:
        45 54 72 90 126
        Found 54
    **/
    class BinarySearch {

        private long[] a;
        private int nElems; //count how many existing elements in array

        public BinarySearch(int max){
            a = new long[max];
            nElems = 0;
        }

        public int size(){
            return nElems;
        }

        public int find(long searchKey){
            return recFind(searchKey, 0, nElems-1);
        }

        private int recFind(long searchKey, int lowerBound, int upperBound){
            int curIn;

            curIn = (lowerBound + upperBound)/2;
            if(a[curIn] == searchKey){
                return curIn;
            }
            else if(lowerBound > upperBound){
                return nElems; //cannot find
            }
            else{
                if(a[curIn]<searchKey)
                    return recFind(searchKey, curIn+1, upperBound); //check larger half
                else
                    return recFind(searchKey, lowerBound, curIn-1);
            }
        }

        public void insert(long value){
            int j;
            for(j=0; j<nElems; j++){
                if(a[j]>value){
                    break;
                }
            }
            for(int k=nElems; k>j; k--){
                a[k] = a[k-1];
            }
            a[j] = value;
            nElems ++;
        }

        public void display(){
            for(int j=0; j<nElems; j++){
                System.out.print(a[j] + " ");
            }
            System.out.println(" ");
        }

        public static void main(String[] args) {
            int maxSize = 100;
            BinarySearch arr = new BinarySearch(maxSize);
            arr.insert(72);
            arr.insert(90);
            arr.insert(45);
            arr.insert(126);
            arr.insert(54);
            arr.display();

            int searchKey = 54;
            if(arr.find(searchKey) != arr.size())
                System.out.println("Found " + searchKey);
            else
                System.out.println("Can't find " + searchKey);
        }

    }


###Word Recursion (Anagram)

####Idea

Assume a word has `n` letters:

1. List right-most `n-1` letters

2. Rotate all `n` letters

3. Do two steps above `n` times

####Code

    :::java
    /**
    If you input 'test', you will get:
      1 test
      2 tets
      3 tste
      4 tset
      5 ttes
      6 ttse
      7 estt
      8 estt
      9 etts
     10 etst
     11 etst
     12 etts
     13 stte
     14 stet
     15 stet
     16 stte
     17 sett
     18 sett
     19 ttes
     20 ttse
     21 test
     22 tets
     23 tste
     24 tset
    **/
    public class WordRecurtion {

        static int size;
        static int count;
        static char[] arrChar = new char[100];

        public static void main(String[] args) throws IOException{
            System.out.print("Enter a word: ");
            String input = getString();
            size = input.length();
            count = 0;
            for(int j=0; j<size; j++){
                arrChar[j] = input.charAt(j);
            }
            doAnagram(size);
        }
        public static void doAnagram(int newSize){
            if(newSize == 1)
              return;
            for(int j=0; j<newSize; j++){
              doAnagram(newSize-1);
              if(newSize==2)
                displayWord();
              //Starting from every two words, rotate after each recursion
              rotate(newSize);
            }
          }

          //Rotate word one position to right
          public static void rotate(int newSize){
            int j;
            int position = size - newSize;
            char temp = arrChar[position];
            for(j=position+1; j<size; j++){
              arrChar[j-1] = arrChar[j];
            }
            arrChar[j-1] = temp;
          }

          public static void displayWord(){
            if(count<99)
              System.out.print(" ");
            if(count<9)
              System.out.print(" ");
            System.out.print(++count + " ");
            for(int j=0; j<size; j++)
              System.out.print(arrChar[j]);
            System.out.println(" ");
          }

          public static String getString() throws IOException{
            InputStreamReader isr = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(isr);
            String s = br.readLine();
            return s;
          }
    }


###Height of B-Tree

####Code

This is my code from hankerrank.com:

    :::java
        /*
        class Node
           int data;
           Node left;
           Node right;
        */
       int height(Node root)
        {
             Node current = root;
             if(current == null){
                return 0;
             }
             if(height(current.left)>height(current.right))
                 return 1 + height(current.left);
             else
                 return 1 + height(current.right);
        }

###Decide if B-Tree is Balanced

Following method is taken from <a href ="http://www.nowamagic.net/librarys/veda/detail/2314">this post</a>:

    :::java
    /*
    class Node
       int data;
       Node left;
       Node right;
    */
    //Return depth of tree if tree is balanced. Otherwise return -1
    int isBalenced(Node root)
    {
         Node current = root;
         if(current == null){
            return 0; //return 0 for null node
         }

         int left = isBalenced(current.left);
         int right = isBalenced(current.right);

         if(left>=0 && right>=0 && left-right<=1 || left-right >= -1){
            if(left<right)
                return right + 1;
            else
                return left + 1;
        }else{
            return -1;
        }
    }