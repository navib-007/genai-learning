# Hyperparameter Tuning (Keras Tuner)

## 🎯 What is Hyperparameter Tuning?
### Hyperparameters are settings like learning rate, number of layers, units per layer, dropout rate, etc.
### They are NOT learned during training — you have to set them manually.
### Tuning means automatically searching for the best set of hyperparameters that gives lowest validation loss or highest accuracy.


## 🚀 What is Keras Tuner?
### Keras Tuner is a library built to make hyperparameter search easy and automatic in TensorFlow/Keras models.
### It supports:
### Random Search,
### Grid Search,
### Bayesian Optimization,
### Hyperband (fast multi-armed bandit strategy).

## Step | Meaning
### build_model(hp) | Tell tuner what to search (what parameters to tune)
### kt.RandomSearch | Choose search method (can also use Bayesian, Hyperband)
### tuner.search | Start automatic search
### tuner.get_best_models | Get the best found model

## Keras Tuner automates the boring task of manually trying hyperparameters.