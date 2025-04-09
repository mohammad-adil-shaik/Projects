# 🩺 ECG Classification Web App (Flask + CNN)

A Flask-based web application that allows users to upload an ECG image and get predictions for cardiac arrhythmia classes using a pre-trained LeNet-based Convolutional Neural Network (CNN) model.

---

## 🚀 Features

- 📷 Upload ECG grayscale images for prediction
- 🧠 Model predicts one of five heartbeat classes:
  - `F` — Fusion of ventricular and normal beat
  - `N` — Normal beat
  - `Q` — Unknown beat
  - `S` — Supraventricular premature beat
  - `V` — Premature ventricular contraction
- 🛠️ Built with Flask for easy deployment
- 🤖 Uses a pre-trained `LeNet_model.h5` (Keras/TensorFlow)

---

## 🛠️ Tech Stack

- 🔙 **Backend:** Python, Flask
- 🧠 **Deep Learning:** TensorFlow, Keras
- 🎨 **Frontend:** HTML, CSS (Jinja templates)
- 🏗️ **Model:** LeNet-5 (custom trained for ECG images)

---

## 📁 Project Structure

ecg-classifier/
├── app.py # Flask app
├── LeNet_model.h5 # Pre-trained CNN model
├── static/ # Uploaded ECG image files
├── templates/ # HTML templates
│ ├── index.html
│ ├── about.html
│ ├── prediction.html
│ └── result.html
└── README.md # Project overview

---

## ▶️ How to Run Locally

### 📦 1. Install Dependencies

Make sure Python 3.x and pip are installed, then run:

```bash
pip install flask tensorflow numpy opencv-python
```

### 📁 2. Place Your Model

```bash
Ensure the `LeNet_model.h5` file is present in the project root directory.
```

### 🚀 3. Start the App

```bash
python app.py
```

### 🌐 4. Open in Browser

```bash
Visit: http://127.0.0.1:5000 to access the app.
```

---

### 🧪 Testing the Model

```bash
Upload a grayscale ECG image via the /prediction page

Recommended input size: 128x128

View your predicted class right after submission!
```

---

### 📬 Contact

```bash
💼 GitHub: @mohammad-adil-shaik

🔗 LinkedIn: Mohammad Adil Shaik

🌐 Portfolio: adilshaik.in

```
