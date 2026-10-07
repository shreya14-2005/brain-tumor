# 🧠 Brain Tumor Detection using Deep Learning

An AI-powered computer vision project designed to classify and detect brain tumors from MRI scan images using Convolutional Neural Networks (CNNs) built with TensorFlow/Keras and OpenCV.

---

## 📌 Features

- **Binary Classification**: Identifies presence (`Tumor detected`) or absence (`No Tumor`) from brain MRI images.
- **Image Preprocessing**: Automatic resizing to `128x128` and pixel normalization (`[0, 1]`) using OpenCV.
- **Inference Pipeline**: Simple and fast prediction script (`predict.py`) using pre-trained model weights.

---

## 📁 Project Structure

```text
brain_tumor/
├── dataset/
│   └── archive (2)/
│       ├── yes/         # MRI scans with tumor
│       └── no/          # MRI scans without tumor
├── predict.py           # Inference script for MRI image prediction
├── train.py             # Model training script
├── .gitignore           # Git ignore configuration
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shreya14-2005/brain-tumor.git
   cd brain-tumor
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install tensorflow opencv-python numpy
   ```

---

## 🚀 Usage

### 1. Training the Model
Run `train.py` to train the CNN model on the dataset:
```bash
python train.py
```
*(This saves the trained weights as `brain_tumor_model.h5`)*

### 2. Making Predictions
Place a test MRI image in the project directory (e.g., `testMRI.jpg`) and run:
```bash
python predict.py
```

**Sample Output:**
```text
1/1 [==============================] - 0s 18ms/step
Tumor detected
```

---

## 🛠️ Tech Stack

- **Python 3**
- **TensorFlow / Keras** - Deep learning model architecture and training
- **OpenCV (`cv2`)** - Image processing and manipulation
- **NumPy** - Matrix computations and array handling

---

## 👤 Author

- **Shreya** - [shreya14-2005](https://github.com/shreya14-2005)
