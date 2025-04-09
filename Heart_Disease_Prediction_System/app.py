from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

app = Flask(__name__)

class_labels = ['F', 'N', 'Q', 'S', 'V']

model = load_model('LeNet_model.h5')

img_size = (299, 299)

def test_single_image(image_path):
    img = image.load_img(image_path, target_size=(128, 128), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    return class_labels[predicted_class]

    #return labels[pred_class[0]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    prediction_result = None
    img_path = None

    if request.method == 'POST':
        img = request.files['my_image2']
        img_path = "static/" + img.filename
        img.save(img_path)

        # Get the prediction result
        prediction_result = test_single_image(img_path)

    return render_template('prediction.html', prediction_result=prediction_result, img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
