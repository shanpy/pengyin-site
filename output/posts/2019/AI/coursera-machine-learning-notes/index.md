.. title: Coursera Machine Learning Notes
.. date: 2019-04-29
.. category: AI
.. tags: Machine Learning
.. slug: coursera-machine-learning-notes
.. authors: Pengyin Shan
.. description: My study notes of coursera class: Machine Learning, taught by Andrew Ng from Stanford University

[TOC]

#Week 1

Two definitions of Machine Learning are offered. Arthur Samuel described it as: `the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.`

Tom Mitchell provides a more modern definition: `A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.`

Example: playing checkers.

- E = the experience of playing many games of checkers

- T = the task of playing checkers.

- P = the probability that the program will win the next game.

In general, any machine learning problem can be assigned to one of two broad classifications: Supervised learning and Unsupervised learning.

##Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into `regression` and `classification` problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

###Example 1

Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

###Example 2

(a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture

(b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.

##Unsupervised Learning

Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.

We can derive this structure by `clustering` the data based on relationships among the variables in the data.

With unsupervised learning there is no feedback based on the prediction results.

Example:

Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

##Model Representation

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function `h : X → Y` so that `h(x)` is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. 

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression problem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.

##Cost Function

We can measure the `accuracy` of our hypothesis function by using a cost function. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

![](/images/2019/AI/cost_function.png)

This function is otherwise called the "Squared error function", or "Mean squared error". The mean is halved `1/2` as a convenience for the computation of the gradient descent, as the derivative term of the square function will cancel out the `1/2` term.

If we try to think of it in visual terms, our training data set is scattered on the x-y plane. We are trying to make a straight line which passes through these scattered data points.

Our objective is to get the best possible line. The best possible line will be such so that the average squared vertical distances of the scattered points from the line will be the least. Ideally, the line should pass through all the points of our training data set. In such a case, the value of J will be 0. 

When \theta_1 =1, we get a slope of 1 which goes through every single data point in our model. Conversely, when \theta_1 =0.5, we see the vertical distance from our fit to the data points increase.

![](/images/2019/AI/cost_function_2.png)

A `contour plot` is a graph that contains many contour lines. A contour line of a two variable function has a constant value at all points of the same line. An example of such a graph is the one to the right below.

![](/images/2019/AI/cost_function_3.png)

##Gradient Descent
So we have our hypothesis function and we have a way of measuring how well it fits into the data. Now we need to estimate the parameters in the hypothesis function. That's where gradient descent comes in.

The points on our graph will be the result of the cost function using our hypothesis with those specific theta parameters. The graph below depicts such a setup.

![](/images/2019/AI/g_d.png)

We will know that we have succeeded when our cost function is at the very bottom of the pits in our graph, i.e. when its value is the minimum. The red arrows show the minimum points in the graph.

The way we do this is by taking the derivative (the tangential line to a function) of our cost function. **The slope of the tangent is the derivative at that point and it will give us a direction to move towards**. We make steps down the cost function in the direction with the steepest descent. The **size** of each step is determined by the parameter `α`, which is called the `learning rate`.

![](/images/2019/AI/g_d_2.png)

On a side note, we should adjust our parameter \alphaα to ensure that the gradient descent algorithm converges in a reasonable time. Failure to converge or too much time to obtain the minimum value imply that our step size is wrong.

![](/images/2019/AI/g_d_3.png)

![](/images/2019/AI/g_d_4.png)

The point of all this is that if we start with a guess for our hypothesis and then repeatedly apply these gradient descent equations, our hypothesis will become more and more accurate.

So, this is simply gradient descent on the original cost function J. This method looks at every example in the entire training set on every step, and is called `batch gradient descent`. Note that, while gradient descent can be susceptible to local minima in general, the optimization problem we have posed here for linear regression has only one global, and no other local, optima; thus gradient descent always converges (assuming the learning rate α is not too large) to the global minimum. Indeed, J is a `convex quadratic function`. 

##Linear Algebra Review

`Matrices` are 2-dimensional arrays. A `vector` is a matrix with one column and many rows, so vectors are a subset of matrices.

To add or subtract two matrices, their dimensions must be the same.

###Manipulation

We map the column of the vector onto each row of the matrix, multiplying each element and summing the result.

The result is a vector. The number of columns of the matrix must equal the number of rows of the vector.

An `m x n` matrix multiplied by an `n x 1` vector results in an `m x 1` vector.

![](/images/2019/AI/m_v.png)

An m x n matrix multiplied by an n x o matrix results in an m x o matrix.

To multiply two matrices, the number of columns of the first matrix must equal the number of rows of the second matrix.

Matrices are not commutative: `A∗B≠B∗A`

Matrices are associative: `(A∗B)∗C=A∗(B∗C)`

The `identity matrix`, when multiplied by any matrix of the same dimensions, results in the original matrix. It's just like multiplying numbers by 1. The identity matrix simply has 1's on the diagonal (upper left to lower right diagonal) and 0's elsewhere.

When multiplying the identity matrix after some matrix (A∗I), the square identity matrix's dimension should match the other matrix's columns. When multiplying the identity matrix before some other matrix (I∗A), the square identity matrix's dimension should match the other matrix's rows.

Multiplying by the `inverse` results in the identity matrix.

 Matrices that don't have an inverse are `singular` or degenerate.

The transposition of a matrix is like rotating the matrix 90° in clockwise direction and then reversing it.

#Week2: Linear Regression

##Multivariate Linear Regression

![](/images/2019/AI/m_l_r.png)

The multivariable form of the hypothesis function accommodating these multiple features is as follows:

```
hθ(x)=θ0+θ1x1+θ2x2+θ3x3+⋯+θnxn
```
Using the definition of matrix multiplication, our multivariable hypothesis function can be concisely represented as:

![](/images/2019/AI/m_l_r_2.png)

###Gradient Descent For Multiple Variables

![](/images/2019/AI/m_l_r_3.png)
![](/images/2019/AI/m_l_r_4.png)

###Feature Scaling

We can speed up gradient descent by having each of our input values in roughly the same range. This is because θ will descend quickly on small ranges and slowly on large ranges, and so will oscillate inefficiently down to the optimum when the variables are very uneven.

The way to prevent this is to modify the ranges of our input variables so that they are all roughly the same. Ideally:

![](/images/2019/AI/m_l_r_5.png)

Two techniques to help with this are `feature scaling` and `mean normalization`. 

Feature scaling involves dividing the input values by the range (i.e. the maximum value minus the minimum value) of the input variable, resulting in a new range of just 1. 

Mean normalization involves subtracting the average value for an input variable from the values for that input variable resulting in a new average value for the input variable of just zero. To implement both of these techniques, adjust your input values as shown in this formula:

![](/images/2019/AI/m_l_r_6.png)

Where μi is the average of all the values for feature (i) and s is the range of values `max - min`, or s is the standard deviation.

###Debug GD

Debugging gradient descent. Make a **plot** with number of iterations on the x-axis. Now plot the cost function, `J(θ)` over the number of iterations of gradient descent. If J(θ) ever increases, then you probably need to decrease α.

Automatic convergence test. Declare convergence if J(θ) decreases by less than E in one iteration, where E is some small value such as `10−3`. However in practice it's difficult to choose this threshold value.

![](/images/2019/AI/m_l_r_7.png)

###Features and Polynomial Regression

We can combine multiple features into one. For example, we can combine x1 and x2  into a new feature x3。
 
Our hypothesis function need not be linear (a straight line) if that does not fit the data well.

We can change the behavior or curve of our hypothesis function by making it a quadratic, cubic or square root function (or any other form).

One important thing to keep in mind is, if you choose your features this way then **feature scaling** becomes very important.

eg. if `x1` has range 1 - 1000 then range of `x2` becomes 1 - 1000000 and that of `x3` becomes 1 - 1000000000

##Normal Equation

In the "Normal Equation" method, we will minimize J by explicitly taking its derivatives with respect to the θj ’s, and setting them to zero. This allows us to find the optimum theta without iteration. The normal equation formula is given below:

![](/images/2019/AI/m_l_r_8.png)

###Noninvertability

When implementing the normal equation in octave we want to use the `pinv` function rather than `inv.` The `pinv` function will give you a value of \thetaθ even if `x transpose * x` is noninvertible. The common causes might be having :

1. Redundant features, where two features are very closely related (i.e. they are linearly dependent)
2. Too many features (e.g. `m ≤ n`). In this case, delete some features or use `regularization`.
Solutions to the above problems include deleting a feature that is linearly dependent with another or deleting one or more features when there are too many features

#Week3

##Logistic Regression

The classification problem is just like the regression problem, except that the values we now want to predict take on only a small number of **discrete** values. For now, we will focus on the binary classification problem in which y can take on only two values, 0 and 1. For instance, if we are trying to build a spam classifier for email, then `x^i` may be some features of a piece of email, and y may be 1 if it is a piece of spam mail, and 0 otherwise. Hence, `y∈{0,1}`. 

0 is also called the `negative class`, and 1 the `positive class`, and they are sometimes also denoted by the symbols `-` and `+`. Given `x^(i)`, the corresponding `y^(i)` is also called the `label` for the training example.

###Logistic/Sigmoid Function

it also doesn’t make sense for h(x) to take values larger than 1 or smaller than 0 when we know that y ∈ {0, 1}. To fix this, let’s change the form for our hypotheses h(x) to satisfy `0≤h(x)≤1`. This is accomplished by plugging `θTx` into the Logistic Function.

![](/images/2019/AI/lr_1.png)

The function `g(z)`, shown here, maps any real number to the `(0, 1)` interval, making it useful for transforming an arbitrary-valued function into a function better suited for classification.

`hθ(x)` will give us the probability that our output is `1`. For example, hθ(x)=0.7 gives us a probability of 70% that our output is 1. Our probability that our prediction is 0 is just the **complement** of our probability that it is 1 (e.g. if probability that it is 1 is 70%, then the probability that it is 0 is 30%).

###Decision Boundary

![](/images/2019/AI/lr_2.png)

![](/images/2019/AI/lr_3.png)

###Cost Function for Logistic Regression

![](/images/2019/AI/lr_4.png)

![](/images/2019/AI/lr_5.png)

If our correct answer 'y' is 0, then the cost function will be 0 if our hypothesis function also outputs 0. If our hypothesis approaches 1, then the cost function will approach infinity.

If our correct answer 'y' is 1, then the cost function will be 0 if our hypothesis function outputs 1. If our hypothesis approaches 0, then the cost function will approach infinity.

Writing the cost function in this way **guarantees** that `J(θ)` is convex for logistic regression.

####Simplified Cost Function & Gradient Descent

![](/images/2019/AI/lr_6.png)
![](/images/2019/AI/lr_7.png)

###Advanced Optimization

Sophisticated algorithms: `Conjugate gradient`, `BFGS`, and `L-BFGS`

![](/images/2019/AI/lr_8.png)

###One-vs-All

Since y = {0,1...n}, we divide our problem into `n+1` (+1 because the index starts at 0) binary classification problems; in each one, we predict the probability that 'y' is a member of one of our classes.

![](/images/2019/AI/lr_9.png)

##Overfitting

`Underfitting`, or `high bias`, is when the form of our hypothesis function h maps poorly to the trend of the data. It is usually caused by a function that is too simple or uses too few features. At the other extreme, `overfitting`, or `high variance`, is caused by a hypothesis function that fits the available data but does not generalize well to predict new data. It is usually caused by a complicated function that creates a lot of unnecessary curves and angles unrelated to the data.

This terminology is applied to both linear and logistic regression. There are two main options to address the issue of overfitting:

1. Reduce the number of features: Manually select which features to keep, or use a **model selection algorithm**.
2. `Regularization`: keep all the features, but reduce the magnitude of parameters `j(θ)`. Regularization works well when we have a lot of slightly useful features.

###Cost Function

![](/images/2019/AI/lr_10.png)

###Regularized Linear Regression

![](/images/2019/AI/lr_11.png)

###Regularized Logistic Regression

![](/images/2019/AI/lr_12.png)

#Week4

##Neural Networks

###Model Representation

![](/images/2019/AI/nn_1.png)
![](/images/2019/AI/nn_2.png)
![](/images/2019/AI/nn_3.png)

##Intuitions

![](/images/2019/AI/nn_4.png)
![](/images/2019/AI/nn_5.png)

###Muti-class Classification

![](/images/2019/AI/nn_6.png)

#Week5

##Cost Function & Back Propagation

###Cost Function

![](/images/2019/AI/cf_1.png)

###Backpropagation Algorithm

![](/images/2019/AI/bp_1.png)
![](/images/2019/AI/bp_2.png)
![](/images/2019/AI/bp_3.png)

###Backpropagation Intuition

![](/images/2019/AI/bp_4.png)
![](/images/2019/AI/bp_5.png)

###Unrolling Parameter

![](/images/2019/AI/bp_6.png)

###Gradient Checking

![](/images/2019/AI/bp_7.png)

###Random Initialization

![](/images/2019/AI/bp_8.png)

###Train the NN

1. pick a network architecture
2. choose the layout of your neural network, including how many hidden units in each layer and how many layers in total you want to have: `Number of input units = dimension of features x^(i)`
 
- Number of output units = number of classes
- Number of hidden units per layer = usually more the better (must balance with cost of computation as it increases with more hidden units) *Defaults: 1 hidden layer. If you have more than 1 hidden layer, then it is recommended that you have the same number of units in every hidden layer.*

![](/images/2019/AI/bp_9.png)

#Week6

##Evaluating Algorithm

###Evaluating a Hypothesis

Once we have done some trouble shooting for errors in our predictions by:

- Getting more training examples
- Trying smaller sets of features
- Trying additional features
- Trying polynomial features
- Increasing or decreasing λ

We can move on to evaluate our new hypothesis.

A hypothesis may have a low error for the training examples but still be inaccurate (because of `overfitting`). Thus, to evaluate a hypothesis, given a dataset of training examples, we can split up the data into two sets: a training set and a test set. Typically, the training set consists of `70 %` of your data and the test set is the remaining `30 %`.

![](/images/2019/AI/ev_1.png)

###Model Selection and Train/Validation/Test Sets

Just because a learning algorithm fits a training set well, that does not mean it is a good hypothesis. It could over fit and as a result your predictions on the test set would be poor. The error of your hypothesis as measured on the data set with which you trained the parameters will be lower than the error on any other data set.

Given many models with different polynomial degrees, we can use a systematic approach to identify the 'best' function. In order to choose the model of your hypothesis, you can test each degree of polynomial and look at the error result.

One way to break down our dataset into the three sets is:

- Training set: 60%
- Cross validation set: 20%
- Test set: 20%
We can now calculate three separate error values for the three different sets using the following method:

- Optimize the parameters in `Θ` using the training set for each polynomial degree.
- Find the polynomial degree `d` with the least error using the cross validation set.
- Estimate the generalization error using the test set with `Jtest(Θ(d))`, (d = theta from polynomial with lower error);

This way, the degree of the polynomial d has not been trained using the test set.

###Diagnosing Bias vs. Variance

![](/images/2019/AI/ev_2.png)

###Regularization and Bias/Variance

![](/images/2019/AI/ev_3.png)

###Learning Curves

![](/images/2019/AI/ev_4.png)
![](/images/2019/AI/ev_5.png)

###Deciding What to Do Next Revisited

Our decision process can be broken down as follows:

1. Getting more training examples: Fixes high variance
2. Trying smaller sets of features: Fixes high variance
3. Adding features: Fixes high bias
4. Adding polynomial features: Fixes high bias
5. Decreasing λ: Fixes high bias
6. Increasing λ: Fixes high variance.

####Diagnosing Neural Networks
- A neural network with fewer parameters is prone to `underfitting`. It is also computationally cheaper.
- A large neural network with more parameters is prone to `overfitting`. It is also computationally expensive. In this case you can use regularization (increase λ) to address the overfitting.

Using **a single hidden layer** is a good **starting default**. You can train your neural network on a number of hidden layers using your cross validation set. You can then select the one that performs best.

####Model Complexity Effects

- Lower-order polynomials (low model complexity) have high bias and low variance. In this case, the model fits poorly consistently.
- Higher-order polynomials (high model complexity) fit the training data extremely well and the test data extremely poorly. These have low bias on the training data, but very high variance.

In reality, we would want to choose a model somewhere in between, that can generalize well but also fits the data reasonably well.