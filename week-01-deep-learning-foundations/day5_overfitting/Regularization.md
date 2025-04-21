# Why Overfitting?
## Neural network is very complex model. It tries to capture all patterns in the data as per the neurons.
## When a model is overfitting, it has learned the training data too well and may not perform well on new, unseen data.

# Eliminate Overfitting:
## 1. Adding more data: Data Augmentation, Add more rows
## 2. Reducing complexity of model: Dropout, EarlyStopping, Regularization.

# Regularization: L1 regularization (Lasso), L2 regularization (Ridge), and Elastic Net regularization.
## Loss function will be calculated on single outcome of dataset.
## Cost function will be calculated on batch outcome of dataset.

## L1 the regularization term is the sum of the absolute values of all the weights in the neural network. This encourages sparsity in the model, effectively setting some weights to zero and performing feature selection. L1 regularization helps reduce the model’s complexity and improve its interpretability.
## L1 regularization produces sparse models, which can be advantageous when feature selection is desired.
### Total loss = Original Loss + λ * L1 Regularization Term | L1 Regularization Term = Σ|wi|

## the L2 regularization term is the sum of the squared values of all the weights in the neural network. It penalizes large weight values and encourages smaller weights, preventing any one weight from dominating the model.
## L2 regularization does not force the coefficients to be exactly zero but instead encourages them to be small.
### Total loss = Original Loss + λ * L2 Regularization Term | L2 Regularization Term = Σ(wi^2)

## Finally, elastic Net regularization combines both L1 and L2 regularization.
## The L1 regularization term encourages sparsity and feature selection, driving some coefficients to exactly zero. This helps in selecting the most relevant features and reducing the complexity of the model. On the other hand, the L2 regularization term encourages smaller but non-zero coefficients, preventing any one feature from dominating the model’s predictions and improving the model’s stability.
### Elastic Net regularization = λ1 * Σ|wi| + λ2 * Σ(wi^2)


## Regularization is typically achieved by adding a term to the loss function during training. 

<!-- Regularization Technique	Advantages	Disadvantages
L1 (Lasso) Regularization	– Performs feature selection, driving some coefficients to zero	– Can lead to high sparsity, making the model less interpretable
 	– Helps in dealing with high-dimensional datasets	– Not effective when there are strong correlations between features
 	– Can handle irrelevant or less important features	– Computationally more expensive than L2 regularization
– Useful for building sparse models	
L2 (Ridge) Regularization	– Helps to prevent overfitting and improve generalization	– Doesn’t perform feature selection like L1 regularization
– Effective when there are strong correlations between features	– The resulting model may still contain many small non-zero coefficients
– Computes stable solutions	– May not be suitable for high-dimensional datasets
– Computationally efficient	 -->