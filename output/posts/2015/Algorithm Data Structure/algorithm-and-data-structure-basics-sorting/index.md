.. title: Algorithm and Data Structure Basics - Sorting
.. date: 2015-09-11
.. category: Algorithm & Data Structure
.. tags: Java, Algorithm, Data Structure, Sorting
.. slug: algorithm-and-data-structure-basics-sorting
.. authors: Pengyin Shan
.. description: Recently I got a few free time besides my work, since my team's current project is coming to an end. I want to take this time to review some knowledge about Algorithms and Data Structures, so that I can have better way of solving problems in my next project. The main idea of this post coming from *Introduction to Algorithms (Third Edition/Chinese Version)*.

###Reference List

- **Introduction to Algorithms (Third Edition/Chinese Version)**, written by *Thomas H.Cormen*, *Charles E.Leiserson*, *Ronald L.Rivest* and *Clifford Stein*, and translated by *Jianping Yin*, *Yun Xu*, *Gang Wang*, *Xiaoguang Liu*, *Ming Su*, *Hengming Zou* and *HongZhi Wang*.

- **Data Structures and Algorithms in Java (Second Edition/Chinese Version)**, written by *Robert Lafore*, and translated by *Xiaoyun Ji*, *Yan Zhao*, *Xi Zeng* and *Xiaohan Di*.

###Terminology & Runtime Analysis

*This part serves as a reading note for Introduction to Algorithms (Third Edition), Chapter 1 and Chapter 2, to clarify some basic terms of Algorithms*.

`Algorithm` is the process of reading a value or a collection of value as **input**, and product a value or a collection of value as **output**.

A sequence of input (with constrains) from a algorithm question is called a `instance` of that question.

####Runtime Analysis

From the book *Introduction to Algorithms*, the reason we are focusing on **worst case running time** is:

1. The worst running time gives a upper limitation running time for any input.

2. For some special algorithms, users can easily get worst case, such as searching for record which may not exist in database.

3. There is lots of times that the *average running time* is the same as the *worst running time*.

###Basic Insertion Sort, with Analysis for Algorithm Questions

Insertion sort is very useful for a **small** amount of input.

In book *Introduction to Algorithms*, insertion sort is described as the same process of someone sorting a group of pokers in a poker game. All elements on one side of your current item (i.e. the item that is supposed to be sorted) is in order.

Pseudo-code for Insertion Sort:

    :::vim
    /*
    * In following code, left side of key is always being sorted, in acceding order.
    * In comparing process, starting from the element on the left of key, then moving towards start of array.
    */
    for j=2 to A.length
        key = A[j]
        i = j-1

        //This loops means all sorted elements begin to move one space to end of array, so that key can be inserted to gap
        while i>0 and A[i] > key
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

###Basic Selection Sort

To perform selection sort, you are given a array of numbers: `A`.

1. You find the smallest element in A, then exchange this element with the element in A[0]

2. Starting from A[1], find the smallest element then changing with A[1]

3. Continue this process until you reach A[A.length-1]

Code in Java:

    :::java
    public void selectionSort(int[] A){
        int out, in, min;

        for(out=0; out<A.length-1; out++){
            min = A[out];
            for(in=out+1; in<A.length; in++){
                if(a[in]<min)
                    min = a[in];
                swap(A[out], min);
            }
        }
    }


###Basic Merge Sort

Merge sort uses `divide-and-concur` mode:

1. Divide original question to smaller questions. For each sub-question, it is a instance of original question.

2. Solution these sub-questions by using `recursion`. When the sub-question is small enough, solve this sub-question.

3. Concur/Merge these sub-solutions to the solution of original question.

The process of merge sort is:

1. Divide the array of `n` elements to two sub-array. Each sub-array should have `n/2` elements.

2. Recursively repeating the first step to sub-arrays until each sub-array only have one element (i.e. Being sorted already).

3. Merge all sorted arrays to one sorted array.

The merge process is the key part of merge sort. From *Introduction to Algorithms*, A function `merge(A, p, q, r)` can be used to perform merge process, where `A` is the array, and `p <= q <= r`. This process assumes that `A[p:q]` and `A[q+1:r]` has been sorted. At the end of merge process, `A[p:r]` should be sorted.

In *Introduction to Algorithms*, a **poker example** is used to describe the merge process. The merge process is to chose a smaller one from the top of two piled poker, and put that poker to a new pile. Repeat this process until one pile is empty.

Since we most perform `n` steps to merge, the running time of merge is $theta (n)$.

For Merge Sort in Java, please refer to <a href="./blog/algorithm-and-data-structure-basics-recursion">this post</a>.

###Tips and Comments

- From *Introduction to Algorithms*, if you have a binary number, moving all digits one position to left means multiplying it by two. if you move all digits *k* position to left, you multiply origin number by $2^k$.

Other parts are working in process :)