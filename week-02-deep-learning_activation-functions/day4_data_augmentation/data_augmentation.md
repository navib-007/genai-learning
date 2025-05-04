# Data Augmentation

## Data augmentation is a technique used to artificially increase the size and diversity of a training dataset by applying random but realistic transformations to the input data — especially useful in image-based tasks like classification, detection, and segmentation.

## 🎯 Why is Data Augmentation Important?
- Improves generalization – Helps the model perform better on unseen data.
- Prevents overfitting – Reduces reliance on specific features.
- Makes small datasets usable – Especially critical when labeled data is limited.
- Encourages invariance – Teaches the model to be robust to shifts, rotations, flips, etc.

## 🖼️ Common Image Augmentation Techniques
| **Type**           | **Description**                                           |
|--------------------|-----------------------------------------------------------|
| **Flip**           | Horizontal/vertical flip (mirror effect)                  |
| **Rotation**       | Rotate image by a random angle (e.g., ±30°)               |
| **Zoom**           | Random zoom-in or zoom-out                                |
| **Shift**          | Translate image along X or Y axis                         |
| **Brightness/Contrast** | Vary image brightness or contrast                    |
| **Shear**          | Apply affine shearing                                     |
| **Noise**          | Add random noise to simulate sensor noise                 |
| **Crop/Resize**    | Randomly crop parts of the image and resize to original   |
| **Color Jitter**   | Random changes to hue, saturation, value (HSV)            |
| **Cutout/Masking** | Randomly mask out patches to force focus on other features|

## 🛠️ How to Perform Data Augmentation
## 📍 Option 1: Manual with OpenCV
- Fully customizable
- Requires writing transformation code manually
- Example: Used for Cats & Dogs dataset (as shared earlier)

## 📍 Option 2: Keras ImageDataGenerator
```python
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=30,
    zoom_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    rescale=1./255
) 
```

## 📍 Option 3: Albumentations (Advanced, Fast, Flexible)
```python
import albumentations as A

transform = A.Compose([
    A.HorizontalFlip(),
    A.RandomBrightnessContrast(),
    A.Rotate(limit=30),
    A.ShiftScaleRotate(),
    A.GaussianBlur(),
])
```
## 📌 Best Practices
- Apply augmentation only on training data, not on validation or test sets.
- Use realistic transformations that match how your input data might vary.
- Augment on-the-fly during training to save disk space (especially with libraries like PyTorch/Keras).
- Too much augmentation may lead to noise if irrelevant transformations are applied.