# Transfer Learning
## Transfer Learning is when a model trained on one task is reused on a different but related task.

# Types of Transfer Learning

## 1. Feature Extraction: Use a pre-trained model as a fixed feature extractor. | Example: Use VGG or ResNet for image features, then add your own classifier.

## 2. Fine-Tuning: Start with a pre-trained model.| Unfreeze some layers (usually last few) and retrain. | Good for adapting to a new domain.

## 3. Domain Adaptation: Source and target tasks are similar, but data distribution differs. | Adapt the model using methods like adversarial training or regularization. | Used in NLP and cross-language tasks.

## 4. Multi-Task Learning: Train a model on multiple tasks simultaneously, sharing common layers. | Helps one task benefit from another.

## 5. Zero-Shot / Few-Shot Learning (Advanced): Pre-trained model generalizes to unseen tasks or with few examples. | Common in LLMs like GPT-4, CLIP, and Meta’s Segment Anything.

# Hyperparameters in Fine-Tuning:
## 1. Hidden Layers: Have a Multiple Hidden Layers with fewer Neurons, because hidden layer capture heirarchy. until we won't have overfitting we can add HL.
## 2. Neurons per layer: Sufficient. Start with more later as per overfitting we can reduce.
## 3. Learning Rate
## 4. Optimizer
## 5. Batch Size: Large will make training faster. Smaller will make data generalized. So, use Learning rate scheduler. while start of training batch size is smaller afterwards increase it.
## 6. Activation Function
## 7. Epochs: Keep as you want only keep Early Stopping.

# Problems in NN:
## 1. Vanishing/ Exploding Gradient: weight Initialization | Change Activation Function | Batch Normalization | Gradient Clipping
## 2. Not Enough data: Transfer Learning | Unsupervised Pre-Training
## 3. Slow Training: Optimizer | Learning Rate Scheduler
## 4. Overfitting: L1 and L2 Reg | Dropout.