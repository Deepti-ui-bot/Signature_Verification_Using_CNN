from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('signature_verification_model.keras')

# Preprocess the uploaded image
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((128, 128))  # Resize to 128x128
    image_array = np.array(image) / 255.0  # Normalize pixel values
    image_array = image_array.reshape(1, 128, 128, 1)  # Reshape for the model
    return image_array

# Predict whether the signature is forged or genuine
def predict_signature(image):
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)
    return "Genuine" if prediction >= 0.5 else "Forged"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file uploaded", 400

    image = Image.open(io.BytesIO(file.read()))
    result = predict_signature(image)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)