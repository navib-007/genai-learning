# Gradient Descent (batch_size)

## Gradient Descent is an optimization algorithm used to minimize a loss function by iteratively adjusting the model parameters (weights) in the direction that reduces the error.

## You move in the opposite direction of the gradient to minimize the function.

## Type | Description | Use Case
## Batch GD (Vanilla GD) | Uses entire dataset to compute gradients | Stable, but slow for large data | No of epochs = No of times update of weight and bias | batch_size= No. of records

## Stochastic GD (SGD) | Uses one data point at a time | Faster, more noise | No of epochs = No of records * No of epochs to update of weight and bias | batch_size = 1
## It helps algorithm to move out of local minima. sometimes it may not converged on the global minima.

## Mini-batch GD | Uses small batches (e.g., 32, 64 samples) | Balance between speed and stability
## why batch size is provided in multiple of 2?
## To make use of RAM effective as it is made to handle binary values. It is optimization technique to make it faster.


## Learning Rate (η): Too small = slow convergence; too large = overshooting.
## Loss Function: Guides optimization. E.g., MSE for regression, cross-entropy for classification.