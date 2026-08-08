from flask import Flask,request,render_template,url_for
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


app = Flask(__name__)
model=joblib.load('covid_model.pkl')
scaler=joblib.load('scaler.save')

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form")
def form():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Mengambil data dan mengubahnya menjadi float
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        
        # Standarisasi data
        normal = scaler.transform(features)
        
        # Melakukan prediksi
        prediction = model.predict(normal)
        
        return render_template('results.html', pred=prediction[0])
    
    except Exception as e:
        # Jika terjadi error (misal form kosong atau format salah), kembalikan ke halaman awal dengan pesan error (jika diimplementasi di frontend) atau sekadar render ulang.
        # Untuk kesederhanaan, kita bisa mengarahkan kembali ke home atau mencetak error.
        print(f"Error during prediction: {e}")
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
