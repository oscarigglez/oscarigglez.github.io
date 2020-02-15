---
layout: post
title: Multiple linear regression from scratch in Python
description: A rough introduction to machine learning where I explain an implementation of a multiple linear regression model in Python using matrix notation and a gradient descent algorithm.
tags: python data-science
mathjax: true
published: false
---

Linear regression is a statistical approach that may be used to model the relationship between a dependent variable (y) and independent ones (x). It's one of the simplest yet most widely used machine learning algorithms, and even as a chemist I've had my fair share of using linear regression to fit physical equations to the measurements I'd gotten in the lab.

As such an universal tool, linear regression has already been implemented over and over and is readily available in many packages, such as ```scipy```, ```statsmodels``` or ```scikit-learn```. However, I believe that there's a lot to learn from doing things yourself, so I decided to build my own simple linear regression model. Follow me as I break it down!

A linear relationship, in its simplest form, can be formulated as follows:

$$y \approx \beta_0 + \beta_1x$$

Sounds familiar? Here the behavior of the independent variable y is defined as a line dependent on x, where $\beta_0$ is the value that y must have when x is equal to 0 (commonly known as the origin), and $\beta_1$ is the slope of the line.

If we extend this definition to be able to describe systems where y depends on more than one independent variable (let's say p, as in "predictor") and we study each data point individually (from a collection of n points), we could arrive to this expression:

$$y_i \approx \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + ... + \beta_p x_{ip} \quad i=1,...,n$$

Rewriting this to a more comfortable matrix form, where $X$ holds the values of all data points (as well as an additional column of ones to account for the indepentent term $\beta_0$) and $\Beta$ holds their corresponding coefficients:

$$y \approx X \Beta = \begin{bmatrix} y_1 \\ y_2 \\ ... \\ y_n \end{bmatrix} = \begin{bmatrix} 1 & x_{11} & x_{12} & ... & x_{1p} \\ 1 & x_{21} & x_{22} & ... & x_{2p} \\ ... & ... & ... & ... & ... \\ 1 & x_{n1} & x_{n2} & ... & x_{np} \end{bmatrix} \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ ... \\ \beta_p \\ \end{bmatrix}$$

Now, solving the problem is a matter of finding out the best values for $\Beta$ so that the $X\Beta$ product is as close as possible to $y$.

To do this, I chose to use the simple and popular gradient descent algorithm: the coefficients are initialized as arbitrary numbers and the multiplication is computed and compared against the true values to obatain an estimation of the gradient. After each step, the values of the coefficients are corrected, and if everything's gone according to plan, the recomputed product should lie a bit closer to our truth.

In my implementation, the gradient is calculated as $G = X^T(X\Beta-y)$, and is multiplied by an arbitrary chosen constant (commonly called learning rate) before being subtracted from the coefficient matrix. This learning rate defines the length of the steps that are taken in the optimization, and must be chosen accordingly to the magnitudes of each specific problem.

A cost function (defined here as $(X\Beta-y)^2$) is used to evaluate the goodness of the fit at each step. When its stops improving significantly between steps, the loop is broken and the model is considered fitted.

```python
class LinearRegressionCustom:
    """Multiple linear regression model
    """

    def __init__(self, lrp=10e-5, fit_threshold=10e-2):
        self.lrp = lrp # learning rate
        self.fit_threshold = fit_threshold # the maximum value for the cost

    def fit(self, X, y):
        n = X.shape[0] # number of data points
        p = X.shape[1] # number of predictors
        X = np.concatenate((np.ones((n, 1)), X), axis=1) # column of ones
        self.coefs = np.zeros((p + 1, 1)) # all coefficients start as 0
        lastcost = 0
        diff = self.fit_threshold + 1

        while diff > self.fit_threshold:
            h = np.matmul(X, self.coefs) # the X Beta product
            residuals = h - y
            gradient = np.matmul(X.T, residuals)
            self.coefs -= self.lrp/n*gradient

            cost = np.mean(np.square(residuals))
            diff = abs(lastcost - cost)
            lastcost = cost
        return self
```



[//]: # (Now, fitting this raw model to a set of data points is a matter of finding out what value to assign to each $\beta$ coefficient so that the predicted values get as close to the real ones as mathematically possible. To avoid going crazy assessing this manually, we must devise some sort of calculation that clearly measures how good the model performs so that it can be automatically minimized. Here comes the cost function:)
