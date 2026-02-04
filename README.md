# 🚗 Car Price Prediction Web Application

An end-to-end Machine Learning web application designed to help users estimate the fair market value of used cars. By analyzing historical data, the app provides data-driven pricing to assist buyers and sellers in making informed decisions.

---

## 📌 Project Overview

Determining the right price for a used car is complex, as it depends on multiple variables like age, usage, and mechanical specs. This project implements a **Supervised Regression Model** to automate this process.

**Key Goals:**
- Deliver high-accuracy price predictions based on user input.
- Provide a seamless, responsive user interface.
- Demonstrate a robust integration between a Machine Learning backend and a web frontend.

---


## ✨ Features

- **✅ Real-time Predictions:** Get instant price estimates based on vehicle specs.
- **✅ Attribute Analysis:** Considers Year, Mileage, Fuel Type, and Transmission.
- **✅ Clean UI/UX:** A minimalist and intuitive web dashboard.
- **✅ Optimized Backend:** Efficient model loading for fast response times.

---

## 🛠️ Tech Stack

### **Machine Learning & Data**
* **Python:** The core programming language.
* **Scikit-Learn:** Used for model training and evaluation.
* **Pandas & NumPy:** For data manipulation and preprocessing.
* **Pickle:** To serialize and save the trained model.

### **Web Framework**
* **Backend:** Flask
* **Frontend:** HTML5, CSS3, JavaScript.

---

## 🧠 How the Model Works

The application uses a **Regression Algorithm** trained on a dataset of thousands of car sales.

1. **Data Preprocessing:** Categorical features (Fuel Type, Transmission) are converted into numerical values using encoding techniques.
2. **Feature Engineering:** The "Age" of the car is calculated from the Manufacturing Year to improve model accuracy.
3. **Training:** The model learns the correlation between these features and the final selling price.
4. **Inference:** When a user submits the form, the data is passed through the `.pkl` model file to generate a prediction.

---

## 📂 Project Structure
```text
CAR_PREDICTION_APP/
│
├── notebooks/
│   └── experiments.ipynb
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   └── result.html
├── venv/                  # local virtual environment (DO NOT push)
│
├── .gitignore
├── app.py                 # Flask entry point
├── best_random_forest_tuned.pkl
├── scaler.pkl
├── car_prediction_data.csv
├── config.yaml
├── requirements.txt
├── README.md
└── demo.mp4

```

### How to Run

### 1. Clone the Repository
```Bash
git clone [https://raw.githubusercontent.com/Abhishek-M-B/Car_price_app/refs/heads/main/demo_video.gif)
cd car-price-prediction
```

###2. Create a Virtual Environment
```Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

###3. Install Dependencies
```Bash
pip install -r requirements.txt
```

### 4. Run the Application
```Bash
# If using Flask:
python app.py
```

## If using Django:
``` Bash
python manage.py runserver
The app will be available at http://127.0.0.1:5000/
```

### Demo Video
<img src="https://raw.githubusercontent.com/Abhishek-M-B/Car_price_app/refs/heads/main/demo_video.gif" alt="Alt text" width=600/>





