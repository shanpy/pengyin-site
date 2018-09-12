.. title: Algorithm and Data Structure Basics - Dynamic Programming
.. date: 2015-09-01
.. modified: 2015-09-03
.. category: Algorithm & Data Structure
.. tags: Java, Algorithm, Data Structure, Dynamic Programming
.. slug: algorithm-and-data-structure-basics-dynamic-programming
.. authors: Pengyin Shan
.. description: I wrote this post to record some basic knowledge about dynamic programming algorithm for future reference. Code is written mainly in Java.

###Reference List

- <a href="http://www.th7.cn/Program/java/2011-07-07/29801.shtml">Dynamic Programming (Chinese)</a>

- <a href="http://www.cnblogs.com/pengyingh/articles/2396427.html">Dynamic Programming (Chinese)</a>

- <a href="http://blog.csdn.net/biangren/article/details/8038605">Java Dynamic Programming: Longest Common Sequence (Chinese)</a>

- <a href="http://www.programcreek.com/2013/02/leetcode-maximum-subarray-java/">LeetCode - Maximum Subarray (Java)</a>

###Basic Idea

**Dynamic Programming (DP)** is used to get the **best result** in the process of making decisions. It is for a problem with **multiple stages** of decision making.

For one problem, A decision of **best solution** may depend on the best solutions in smaller problems.

In this case, DP suggests to get the best solution for **all** small stages **only once**, and **store** these solutions, no matter if they'll be useful in the future or not.

Finally, user can combine small best solutions to get the final solution. *Never repeat the process of getting same small solution.*

####Four Steps of Dynamic Programming

1. Describe the structure of the best solution.

2. Use **recursion** to define the value of best solution

3. **From bottom to top**, calculate the value of best solution

4. Combine all results to get the final solution

###Longest Common Sequence, LCS

>Assume you have two strings. Output their longest common sub-string. Sub-string has two cases: continuous from origin string or non-continuous from original string.
>For example, you have two string: `BDCABA` and `ABCBDAB`. You can output BCBA or BDAB for non-continuous longest sub-string, with length of 4.

####Idea

Assume we have two input strings: `A="a0,a1,...,am-1"`, `B="b0,b1,...bn-1"`.

Assume we have a LCS `Z="z0,z1,...zk-1"`.

There are three possibilities for this assumption:

1. if `am-1 = bn-1`, we can conclude `zk-1 = am-1 = bn-1` (Otherwise Z cannot be LCS). And we can conclude `z0,z1...zk-2` is the LCS for `a0,a1,...am-2` and `b0,b1,...bn-2`

2. if `am-1 != bn-1`, we can conclude *if `zk-1 != am-1`*, then `z0,z1,...zk-2` is the LCS for `a0,a1,...am-2` and `b0,b1,...bn-1`.

3. if `am-1 != bn-1`, we can conclude *if `zk-2 != bn-1`*, then `z0,z1,...zk-2` is the LCS for `a0,a1,...am-1` and `b0,b1,...bn-2`

Based on rules above, we can divide this problem to many smaller problem. For example, if we want to get LCS for `a0,a1,...am-2` and `b0,b1,...bn-2`, then we need to apply rules above to get `z0,z1z...zk-3` for `a0,a1,...am-3` and `b0,b1,...bn-3`, assuming `am-2 = bm-2`.

####Create Array to Store Solutions

We want to create a two-dimensional array `c[i][j]`. It is used to record the length of LCS for `X[i]` and `Y[j]`.

>Since we are calculating **from bottom to top**, we already get `c[i-1][j-1]`, `c[i-1][j]` and `c[i][j-1]` before we get `c[i][j]`. Since we can know if `X[i]=Y[j]` or not, we can calculate the value of `c[i][j]` based on three rules above.

The graph below is from <a href="http://blog.csdn.net/biangren/article/details/8038605">this post</a>, expressing the math idea and calculation process for this problem:

../images/articles/2015/algorithm/lcs_math.png 

Using two input string `BDCABA` and `ABCBDAB`:

../images/articles/2015/algorithm/lcs_graph.png 

>You may notice only when we move to left-top direction, we can find a character for LCS. So we need to create another two-dimensional array to record moving direction

####Code for Non-continuous LCS

Following code is from <a href="http://blog.sina.com.cn/s/blog_5d4646fd0100qitg.html">this post</a>, written by *BirdMan*:

    :::java
    public class LCS{

        int[][] lcsLength(char[] x,char[] y){
            int m = x.length;
            int n = y.length;
            int i,j;

            int[][] c = new int[m][n];
            int[][] b = new int[m][n];
            for(i = 1;i < m;i++)
                c[i][0] = 0;
            for(j = 0;j < n;j++)
                c[0][j] = 0;

            for(i = 1;i < m;i++){
                for(j = 1;j < n;j++){
                    //Case with same character
                    if(x[i] == y[j]){
                        c[i][j] = c[i - 1][j - 1] + 1;
                        b[i][j] = 1; //in graph, this means going to left-top
                    }
                    else if(c[i - 1][j] >= c[i][j - 1]){
                        c[i][j] = c[i - 1][j];
                        b[i][j] = 2; //in graph, this means going to top
                    }else{
                        c[i][j] = c[i][j - 1];
                        b[i][j] = 3; //in graph, this means going to left
                    }
                }
            }
            return b;
        }

        void printLCS(int[][] b,char[] x,int i,int j){
            if(i == 0 || j == 0)
                return;
            if(b[i][j] == 1){
                //Only want the left-top direction. i.e. b[i][j]=1
                printLCS(b,x,i - 1,j - 1);
                System.out.print(i + ":" + x[i] + "\t");
            }else if(b[i][j] == 2)
                printLCS(b,x,i - 1,j);
            else
                printLCS(b,x,i,j - 1);
        }

        public static void main(String[] args) {
            /*Important: here we need a empty string/char at the beginning of each input, because if you check the graph, position (0,0) has no character. Out matrix with character start from position 1.
            */
            char[] x = {' ','A','B'};
            char[] y = {' ','B','D'};
            LCS lcs = new LCS();
            lcs.printLCS(lcs.lcsLength(x, y), x, x.length-1, y.length-1);
        }

}

###Maximum Subarray

I learned this problem main from <a href="http://www.programcreek.com/2013/02/leetcode-maximum-subarray-java/">LeetCode - Maximum Subarray (Java)</a>.

>You have a array of integers(may include negative number). You want to find a continuous subarray so that the sum of subarray is maximized. For example, assume you have `{-12, 1, -3, 4, -1, 2, 1, -5, 4}`. The maximum subarray is `6`.

Rules we need to follow:

- We should ignore the sum of the previous `n-1` elements if `nth` element is greater than the sum.

Code from same post:

    :::java
    public class MaxSubarray {

        public static void main(String[] args) {
            int[] test = { -2, 1, -3, 4, -1, 2, 1, -5, 4};
            System.out.println("result: " + maxSubArray(test));

        }

        static int maxSubArray(int[] A) {
            int max = A[0];
            int[] sum = new int[A.length];
            sum[0] = A[0];

            for (int i = 1; i < A.length; i++) {
                /*Compare current value with the sum of previous sum and this value.
                Two cases:
                1. Assume current value is non-negative.
                    1.1 If the new sum of previous sum and current value is larger than current value, previous sum must be non-negative. In this case, take the new sum.
                    1.2 If the new sum of previous sum and current value is smaller than current value, previous sum must be negative value. In this case, drop previous sum and re-start from current value (because current value is larger).
                2. if current value is negative, we still want to keep previous sum because new sum must be smaller than previous sum
                */
                sum[i] = Math.max(A[i], sum[i - 1] + A[i]);
                //max is the maximum subarray value
                max = Math.max(max, sum[i]);
            }

            return max;
        }

    }

There can be a similar solution, using a `temp` variable. Following code is my full solution on <a href="https://www.hackerrank.com/challenges/maxsubarray">HackerRank</a> :

    :::java
    import java.io.*;
    import java.util.*;
    import java.text.*;
    import java.math.*;
    import java.util.regex.*;

    /*
    test case input:
    6
    1
    1
    6
    -1 -2 -3 -4 -5 -6
    2
    1 -2
    3
    1 2 3
    1
    -10
    6
    1 -1 -1 -1 -1 5

    test case output:

    1 1
    -1 -1
    1 1
    6 6
    -10 -10
    5 6
    */

    public class Solution {

        public static void main(String[] args) throws IOException{
            BufferedReader bd = new BufferedReader(new InputStreamReader(System.in));
            int cases = Integer.parseInt(bd.readLine());
            for(int i=0; i<cases; i++){
                String line = bd.readLine();
                if(line != null){
                    int howmany = Integer.parseInt(line);
                    float[] a = new float[howmany];
                    String nums = bd.readLine();
                    for(int j=0; j<a.length; j++){
                        int index = nums.indexOf(" ");
                        if(index != -1 && index<a.length){
                            //Use parseFloat for passing negative numbers
                            a[j] = Float.parseFloat(nums.substring(0,index));
                            nums = nums.substring(index+1, nums.length());
                        }
                        else
                            a[j] = Float.parseFloat(nums);
                    }
                    int first = getMaxCon(a);
                    int second = getMaxNonCon(a);
                    System.out.print(first + " " + second);
                }
                System.out.println("");
            }
        }

        static int getMaxCon(float[] a){
            float temp = a[0];
            float max = a[0];
            for(int i=1; i<a.length; i++){
                if (temp < 0)
                    temp = a[i];
                else{
                    temp += a[i];
                }
                if (temp > max){
                    max = temp;
                }
            }
            return (int)max;
        }

        static int getMaxNonCon(float[] a){
            //For non-continous option, no need to add replace part
            float temp = a[0];
            for(int i=1; i<a.length; i++){
                if(a[i] + temp > temp)
                    temp += a[i];
            }
            return (int)temp;
        }
    }


>My current problem is both methods above has time complexity of O(n), which is not very efficient if there exists lot of numbers. Is there any way to improve it?

###Stock Problem

*This problem can be done by DP or Non-DP method.*

Stock problem can be concluded to a **finding maximum sum of array elements' differences**, with different constrains.

Following problems assume you cannot sell and buy stock on the same day:

####What if you can sell/maintain/buy stocks with unlimited time?

I met this problem on <a href="https://www.hackerrank.com/challenges/stockmax">hackerank.com</a>. In this problem, you can only buy one stock once per day, but you can choose to sell all your current stocks in one day.

So far I figured a solution with `O(n)` runtime complexity:

    :::java
    /*
    Example Input:
    3
    3
    5 3 2
    3
    1 2 100
    4
    1 3 1 2
    Example Output:
    0
    197
    3
    */

    import java.io.*;
    import java.util.*;
    import java.text.*;
    import java.math.*;
    import java.util.regex.*;

    public class Solution {

        public static void main(String[] args) throws IOException{
                BufferedReader bd = new BufferedReader(new InputStreamReader(System.in));
                int cases = Integer.parseInt(bd.readLine());
                for(int i=0; i<cases; i++){
                    String line = bd.readLine();
                    if(line != null){
                        int howmany = Integer.parseInt(line);
                        int[] a = new int[howmany];
                        String nums = bd.readLine();
                        for(int j=0; j<a.length; j++){
                            int index = nums.indexOf(" ");
                            if(index != -1 && index<a.length){
                                //Use parseFloat for passing negative numbers
                                a[j] = Integer.parseInt(nums.substring(0,index));
                                nums = nums.substring(index+1, nums.length());
                            }
                            else
                                a[j] = Integer.parseInt(nums);
                        }
                        System.out.println(countStock(a));
                    }
                }
        }

        /*
        This solution assume two pointers from the end of array.
        Last pointer try to find positive benefit, counting difference with the value of first pointer.
        O(n) running time
        */
        static int countStock(int[] a){
            int last = a.length-1;
            int first = a.length-2;
            int sum = 0;
            while(first>=0 && last>=0){
                if(a[last]-a[first]>0){
                    sum += a[last]-a[first];
                    first --;
                }else{
                    first --;
                    last = first + 1;
                }
            }
            if(sum<0)
                sum = 0;
            return sum;
        }

####What if you can only buy stock once and sell stock once?

Then the problem is turning to *finding out the largest different between two elements in array*. i.e.Find smallest and largest elements in array, while smallest element should in the front of the largest element. Following is my code:

    :::java
    static int countStock(int[] a){
        int smallest = a[0];
        int largest = a[0];
        int diff = 0;

        for(int i=1; i<a.length; i++){

            //Count diff. Reset smallest and largest if a[i]<a[i-1]
            if(a[i-1]>a[i]){
                diff = max(diff, largest - smallest);
                smallest = a[i];
                largest = a[i];
            }
            else{
                if(a[i]<smallest){
                    smallest = a[i];
                }
                if(a[i]>largest){
                    largest = a[i];
                }
            }
        }

        if(diff<0)
            return 0;
        else
            return diff;
    }

####What if you can only trade stock with a maximum of n times?

My idea is that we can use same idea as the first stock problem (2 pointers). Since we can only count `n` times of benefits, we can store all benefits in a sorted array (in descending order), then get the sum of first `n` elements.

    :::java
     //O(mn): m is the size of input array, n is the size of times
     static int countStockNTimes(int[] a, int n){
            int last = a.length-1;
            int first = a.length-2;
            int max = 0;
            int[] sums = new int[n];
            while(first>=0 && last>=0){
                if(a[last]-a[first]>0){
                    addToSortedArray(sum, a[last]-a[first]);
                    first --;
                }else{
                    first --;
                    last = first + 1;
                }
            }
            for(int i=0; i<n; i++){
                max += sum[i];
            }
            if(max<0)
                max = 0;
            return max;
    }

    //O(n) time complexity
    void addToSortedArray(int[] sum, int diff){
        for(int i=0; i<sum.length-1; i++){
            if(diff<sum[i] && diff>sum[i+1])
                sum[i+1] = diff;
        }
    }
