# 🐾 Animal Image Classification Using ResNet50

## 📌 Project Overview

This project focuses on building a deep learning-based **Animal Image Classification Model** using **ResNet50 (Residual Neural Network)** and PyTorch.

The model takes an input image and predicts the corresponding animal category. It leverages transfer learning to utilise pretrained ResNet50 weights and fine-tunes the network for multi-class image classification.

The project includes image preprocessing, data augmentation, dataset splitting, model training, and performance evaluation to develop a reliable image classification pipeline.

## 🎯 Objectives

- Develop a deep learning model capable of classifying multiple animal categories.
- Implement transfer learning using pretrained ResNet50.
- Perform image preprocessing and augmentation to improve generalisation.
- Handle class imbalance where necessary.
- Optimise model training using GPU acceleration and Automatic Mixed Precision (AMP).
- Evaluate model performance using classification metrics.

## 🧠 Model Architecture

**ResNet50 (Residual Network with 50 layers)**

ResNet50 is a convolutional neural network architecture that introduces residual connections (skip connections) to address the vanishing gradient problem in deeper neural networks.

### Why ResNet50?

- Pretrained on the ImageNet dataset.
- Residual connections enable effective training of deep networks.
- Extracts meaningful hierarchical image features.
- Transfer learning reduces training time and computational requirements.
- Suitable for complex multi-class image classification tasks.

### Transfer Learning Approach

1. Load pretrained ResNet50 weights.
2. Adapt the final fully connected layer to match the number of animal classes.
3. Train and fine-tune the model on the animal dataset.
4. Evaluate the trained model on unseen validation/test images.

## 📂 Dataset

The dataset contains approximately **18,000 animal images** belonging to multiple animal categories.

The dataset is organised using image paths and corresponding class labels.

Example:

```text
dataset/
│
├── train/
│   ├── cat/
│   ├── dog/
│   ├── elephant/
│   └── ...
│
├── validation/
│   ├── cat/
│   ├── dog/
│   ├── elephant/
│   └── ...
│
└── test/
    ├── cat/
    ├── dog/
    ├── elephant/
    └── ...
```

*Note: The directory structure above is illustrative; adapt it to your actual dataset organisation.*

## ⚙️ Data Preprocessing

The following preprocessing techniques are used to prepare images for model training:

- **Image Resizing:** Resize images to a consistent input dimension compatible with ResNet50.
- **Image Normalization:** Normalize images using ImageNet mean and standard deviation.
- **Data Augmentation:** Apply transformations to introduce image variations and reduce overfitting.
- **Train-Validation-Test Split:** Separate datasets to evaluate model generalisation.
- **Stratified Splitting:** Maintain class distribution across dataset splits.

### Image Normalization

ImageNet normalization parameters:

```python
transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)
```

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Model Architecture | ResNet50 |
| Image Processing | OpenCV, PIL |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| GPU Acceleration | CUDA |
| Development | Jupyter Notebook |

## 📊 Model Evaluation

The model's performance can be evaluated using the following metrics:

- **Accuracy:** Measures the percentage of correctly classified images.
- **Precision:** Measures how many predicted instances of a class are correct.
- **Recall:** Measures how many actual instances of a class are correctly identified.
- **F1-Score:** Provides a balance between precision and recall.
- **Confusion Matrix:** Helps identify misclassifications across animal categories.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/animal-classification.git

cd animal-classification
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

Open the Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebook cells to execute the preprocessing, training, and evaluation pipeline.

## 📁 Project Structure

```text
Animal-Classification/
│
├── dataset/
│
├── notebooks/
│   └── animal_classification.ipynb
│
├── models/
│   └── resnet50.pth
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

## 🔮 Future Improvements

- Experiment with other architectures such as EfficientNet, DenseNet, and Vision Transformers.
- Implement Grad-CAM for model interpretability.
- Develop a web-based interface for real-time image classification.
- Improve performance on underrepresented animal classes.
- Explore object detection models for identifying multiple animals within a single image.

## 👨‍💻 Author

**Rohit Yadav**

IT Engineering Student | Deep Learning & AI Enthusiast

- GitHub: [Your GitHub Profile](https://github.com/your-username)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

⭐ If you find this project interesting, consider giving the repository a star!