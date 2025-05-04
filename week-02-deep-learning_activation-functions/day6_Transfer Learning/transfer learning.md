# Transfer Learning

## Transfer learning is a machine learning technique where a pre-trained model (usually trained on a large dataset like ImageNet) is reused or adapted for a new, but related task — typically with less data and computation.

## 🧠 Why Use Transfer Learning?
- Saves training time
- Reduces data requirements
- Improves performance, especially on small datasets
- Leverages rich features learned by deep networks from large datasets

| Approach                  | Description |
|---------------------------|-------------|
| **Feature Extraction**    | Use the convolutional base (without Fully Connected(FC) layers) to extract features from new data |
| **Fine-tuning**           | Unfreeze some deeper layers of the base model and retrain them with a lower learning rate |
| **Full retraining**       | Rare — retrain the whole network with your dataset (only if you have a large dataset) |


| Model       | Trained On  | Use Case                              |
|-------------|-------------|----------------------------------------|
| **ResNet**  | ImageNet    | General vision tasks                   |
| **VGGNet**  | ImageNet    | Easy to use, but large in size         |
| **Inception** | ImageNet  | Efficient, multi-scale feature learning|
| **MobileNet** | ImageNet  | Lightweight, great for mobile devices  |
| **BERT/GPT** | Text corpus| For NLP tasks                          |

```python
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

# Load pre-trained ResNet50 model (without top layers)
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Add custom top layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)

# Create final model
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
```

## 🔍 When to Use Transfer Learning?
- ✅ When you have limited data
- ✅ When your task is similar to the pre-trained model's task
- ✅ When you want faster training with high performance