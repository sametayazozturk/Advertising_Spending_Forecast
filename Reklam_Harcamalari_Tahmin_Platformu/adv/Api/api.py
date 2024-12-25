# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

# Flask uygulamasını başlatma
app = Flask(__name__)

# CORS ayarları
CORS(app, resources={r"/predict": {"origins": "http://localhost:5010"}}, supports_credentials=True)


# Model dosya yolu
model_path = 'model.pkl'

# Modeli yükleme (pickle dosyasından)
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model



# API anahtarını kontrol eden fonksiyon
def check_api_key():
    api_key = request.headers.get('API-Key')
    # Gerçek bir API anahtarını burada kontrol edin
    if api_key == 'asdjaslkjdlkasjdlkas':  # Örnek anahtar, gerçek anahtarınızı buraya yazın
        return True
    return False

# /predict endpoint'i
@app.route('/predict', methods=['POST'])
def predict_sales():
    if request.method == 'POST' and request.is_json:
        if not check_api_key():
            return jsonify({'error': 'Unauthorized access'}), 401

        input_data = request.json  # JSON formatındaki veriyi al
        tv = float(input_data['TV'])
        radio = float(input_data['Radio'])
        newspaper = float(input_data['Newspaper'])

        features = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])

        # Modeli yükle
        model = load_model(model_path)

        # Tahmin yap
        prediction = model.predict(features)[0]

        return jsonify({'SalesPrediction': prediction}), 200
    else:
        return jsonify({'error': 'Only POST requests with JSON data are allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
