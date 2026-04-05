from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("best_random_forest_tuned.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    present_price = float(request.form["Present_Price"])
    kms_driven = int(request.form["Kms_Driven"])
    owner = int(request.form["Owner"])

    # Keep preprocessing aligned with how the model was trained.
    input_year = int(request.form["Year"])
    car_age = 2024 - input_year

    fuel_type = request.form["Fuel_Type"]
    fuel_diesel = 1 if fuel_type == "Diesel" else 0
    fuel_petrol = 1 if fuel_type == "Petrol" else 0

    seller_type = request.form["Seller_Type"]
    seller_individual = 1 if seller_type == "Individual" else 0

    transmission = request.form["Transmission"]
    transmission_manual = 1 if transmission == "Manual" else 0

    # Feature order must match training order exactly.
    input_data = [
        present_price,
        kms_driven,
        owner,
        car_age,
        fuel_diesel,
        fuel_petrol,
        seller_individual,
        transmission_manual,
    ]

    input_array = np.array(input_data).reshape(1, -1)
    scaled_data = scaler.transform(input_array)
    prediction = model.predict(scaled_data)

    output = round(prediction[0], 2)
    return render_template(
        "index.html",
        prediction_text=f"Estimated Resale Value: Rs. {output} Lakhs",
    )


if __name__ == "__main__":
    app.run(debug=True)
