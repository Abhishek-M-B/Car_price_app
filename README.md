# Car Price Prediction Web App

## About the Project
This project is an **End-to-End Machine Learning** solution designed to help users estimate the market price of a used car. Instead of guessing, this tool uses a **Tuned Random Forest Regressor** to analyze specific car attributes and provide a data-driven valuation.

### Key Features
* **Real-time Prediction:** Get instant price estimates based on live user input.
* **Interactive UI:** A clean, user-friendly interface built with HTML5 and CSS3.
* **Tuned ML Model:** The backend uses a Scikit-Learn pipeline that handles feature scaling and categorical encoding automatically.
* **Accuracy:** Uses an optimized Random Forest algorithm for high-precision regression.

## Tech Stack
* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend:** HTML5, CSS3
* **Model Deployment:** Joblib/Pickle for model serialization

## 📁 Project Structure
```text
├── app.py                      # Flask Application entry point
├── classifier.py               # Script for model training/logic
├── best_random_forest_tuned.pkl # Trained ML model
├── scaler.pkl                  # Data scaling parameters
├── car_prediction_data.csv     # Dataset used for training
├── static/
│   └── style.css               # Styling for the web UI
└── templates/
    └── index.html              # Main web page



## 🎬 Demo 
> **How to add your video:** > 1. Record your screen while using the app.
> 2. Convert it to a `.gif` or `.mp4`.
> 3. Save it as `demo.gif` inside your `static/` folder.
> 4. If you use a video, GitHub will automatically play it if you drag and drop it into this README!
