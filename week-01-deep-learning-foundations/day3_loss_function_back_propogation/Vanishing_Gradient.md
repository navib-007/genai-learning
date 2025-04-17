# Vanishing Gradient

## The Vanishing Gradient problem occurs during the training of deep neural networks when the gradients of the loss function become very small as they are backpropagated through many layers. 
## As a result, early layers learn very slowly or not at all, preventing the model from converging effectively.

## How to find?
## Focus on loss: No changes so VGP
## Epoch vs weight graph 

## To Handle VGP:
## 1. Reduce model complexity. (Use Shallow Neural Network)
## 2. Using Relu Activation Function. value= (0,max)
## 3. Proper weight Initialization
## 4. Batch Normalization
## 5. Residual Network