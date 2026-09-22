from pathlib import Path

import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = Path("models") / "california_housing_pipeline.joblib"

FEATURE_NAMES = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]


def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            values = [float(request.form[name]) for name in FEATURE_NAMES]
            model = load_model()

            if model is None:
                error = (
                    "The trained model was not found. "
                    "Run the training/export notebook first."
                )
            else:
                prediction = float(model.predict(np.array(values).reshape(1, -1))[0])

        except (TypeError, ValueError):
            error = "Please enter valid numeric values for every field."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        feature_names=FEATURE_NAMES,
    )


if __name__ == "__main__":
    app.run(debug=True)
