from flask import Flask, render_template, request
import pickle
import numpy as np
import yaml

app = Flask(__name__)

with open('config.yaml',"r") as file:
    config = yaml.safe_load(file)

model_Path = config['model_name']
scalar_Path = config['scalar_name']

model = pickle.load(open(model_Path, 'rb'))
scaler = pickle.load(open(scalar_Path, 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. Capture inputs from HTML
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        owner = int(request.form['Owner'])
        
        # 2. Calculate Age (Use 2024 to match your training script)
        input_year = int(request.form['Year'])
        car_age = 2024 - input_year 
        
        # 3. Categorical Encoding
        fuel_type = request.form['Fuel_Type']
        fuel_diesel = 1 if fuel_type == 'Diesel' else 0
        fuel_petrol = 1 if fuel_type == 'Petrol' else 0
        
        seller_type = request.form['Seller_Type']
        seller_individual = 1 if seller_type == 'Individual' else 0
        
        transmission = request.form['Transmission']
        transmission_manual = 1 if transmission == 'Manual' else 0

        # 4. FIXED FEATURE ORDER (Matches your training script perfectly)
        input_data = [
            present_price,      
            kms_driven,        
            owner,            
            car_age,            
            fuel_diesel,        
            fuel_petrol,        
            seller_individual, 
            transmission_manual 
        ]
        
        # 5. Transform and Predict
        input_array = np.array(input_data).reshape(1, -1)
        
        # IMPORTANT: Only use scaler if you used it in your training script!
        # If your training script didn't use StandardScaler, comment out the line below.
        scaled_data = scaler.transform(input_array)
        
        prediction = model.predict(scaled_data)
        
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f"Estimated Resale Value: ₹{output} Lakhs")
    
if __name__ == "__main__":
    app.run(debug=True)