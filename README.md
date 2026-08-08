# COVID Mortality Prediction App

Ini adalah aplikasi web berbasis Flask yang digunakan untuk memprediksi tingkat kematian (mortality) akibat COVID-19 menggunakan Machine Learning. Model prediksi telah dilatih sebelumnya (menggunakan scikit-learn) dan disimpan dalam format `.pkl`.

## 📂 Struktur Direktori
- `app.py`: File utama aplikasi web (Flask).
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `covid_model.pkl`: Model machine learning yang telah dilatih.
- `scaler.save`: Skalar (StandardScaler) untuk normalisasi data.
- `templates/`: Folder berisi file HTML (`index.html`, `results.html`).
- `static/`: Folder untuk aset statis (CSS, JS, Images).
- `notebooks/`: Folder berisi Jupyter Notebook untuk eksperimen / training model.
- `dataset/`: Folder berisi dataset yang digunakan untuk melatih model.

## 🚀 Cara Menjalankan Aplikasi Lokal

1. **Clone repository ini** (jika sudah di-push ke GitHub):
   ```bash
   git clone <url-repo-anda>
   cd COVID_Mortality
   ```

2. **Buat dan aktifkan Virtual Environment** (disarankan):
   - Di Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Di Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Flask**:
   ```bash
   python app.py
   ```
   Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

## 🛠️ Teknologi yang Digunakan
- **Python** (Backend)
- **Flask** (Web Framework)
- **Scikit-Learn** (Machine Learning)
- **HTML/CSS** (Frontend)
- **Gunicorn** (WSGI Server untuk deployment)
