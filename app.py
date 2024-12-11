from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the form
    try:
        features = [float(request.form[f'feature{i}']) for i in range(1, 12)]
        # Mock prediction logic (replace with your ML model logic)
        prediction = sum(features)  # Example: Sum of all features as a "prediction"
        result = f"Prediction result: {prediction:.2f}"
    except Exception as e:
        result = f"Error in processing: {str(e)}"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
