# End-to-End ML Pipeline

A lightweight, reproducible machine learning project that demonstrates a complete workflow from data ingestion to model deployment.

The project uses the **California Housing** open-source dataset available through scikit-learn. The workflow covers:

- Data ingestion with `pandas` and `pathlib`
- Basic data inspection and cleaning
- Reproducible preprocessing with `sklearn.pipeline.Pipeline`
- Model training with scikit-learn
- Experiment tracking with MLflow
- Model persistence with `joblib`
- A lightweight Flask web application for predictions
- Notebook-first development so the complete workflow is easy to inspect and explain in interviews

## Project Highlights

This project intentionally avoids a complicated production-style folder structure. There is no `src/`, separate preprocessing module, data-loader module, or utility module.

The notebooks contain the actual ML workflow, while the Flask application is kept small and focused on serving the saved pipeline.

## Dataset

**California Housing Dataset**

The dataset is available through `sklearn.datasets.fetch_california_housing` and is based on the California housing data.

The target is the median house value for California districts.

## Tech Stack

- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- MLflow
- Joblib
- Flask
- Matplotlib
- Seaborn
- Jupyter Notebook
- HTML/CSS

## Repository Structure

```text
End-to-End-ML-Pipeline/
│
├── notebooks/
│   ├── 01_data_ingestion_and_eda.ipynb
│   ├── 02_ml_pipeline_training.ipynb
│   └── 03_mlflow_tracking_and_export.ipynb
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md
```

## How the Pipeline Works

```text
Open Dataset
     ↓
Data Ingestion
     ↓
Data Inspection
     ↓
Train/Test Split
     ↓
Sklearn Preprocessing Pipeline
     ↓
Model Training
     ↓
Evaluation
     ↓
MLflow Experiment Tracking
     ↓
Joblib Model Export
     ↓
Flask Web App
     ↓
Prediction
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter notebook
```

Run the notebooks in order.

## MLflow

The third notebook demonstrates local MLflow tracking.

To open the MLflow dashboard after running the notebook:

```bash
mlflow ui
```

Then open the local address shown by MLflow in your browser.

The project uses local MLflow files, so no cloud account is required.

## Running the Web App

After completing the training/export notebook, run:

```bash
python app.py
```

Open the local Flask address shown in the terminal.

The application provides a simple form where users can enter California housing features and receive a predicted median house value.

If the saved model is not available, the application explains that the training notebook must be run first.

## LinkedIn & GitHub

The web application includes profile links for:

- LinkedIn: https://www.linkedin.com/in/infinitepraveen/
- GitHub: https://github.com/InfinitePraveen

## Interview Talking Points

This project can be explained as an end-to-end ML workflow rather than only a model-training exercise.

Important concepts demonstrated:

1. Reproducible data ingestion
2. Avoiding data leakage with an sklearn pipeline
3. Consistent preprocessing during training and inference
4. Train/test evaluation
5. MLflow experiment tracking
6. Saving the complete preprocessing + model pipeline with Joblib
7. Loading the same artifact in a Flask application
8. Keeping the deployment layer separate from notebook experimentation without creating a large application architecture

## Notes

The dataset is small enough for CPU-based experimentation. No GPU is required.

The application is intended as a portfolio/interview demonstration and is not designed as a production-scale deployment.
