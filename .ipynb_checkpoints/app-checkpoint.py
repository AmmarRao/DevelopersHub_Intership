from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained Iris model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logistic_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

print("Iris model loaded successfully!")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input from form
        sepal_length = float(request.form.get("sepal_length"))
        sepal_width  = float(request.form.get("sepal_width"))
        petal_length = float(request.form.get("petal_length"))
        petal_width  = float(request.form.get("petal_width"))

        # Convert to array
        x = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Predict
        prediction = model.predict(x)[0]

        return jsonify({"species": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

# --- THIS IS THE CRUCIAL PART ---
if __name__ == "__main__":
    # debug=True shows errors in browser & auto reloads on code changes
    # port=5000 is standard; you can change it if needed
    app.run(debug=True, port=5000)
