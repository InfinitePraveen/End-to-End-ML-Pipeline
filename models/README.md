# Models

The training notebooks export the complete scikit-learn pipeline with Joblib.

The saved artifact contains both preprocessing and the trained estimator. This is important because the Flask application can use exactly the same transformations that were used during training.

Generated model files are ignored by Git to keep the repository lightweight.

Run:

```text
notebooks/03_mlflow_tracking_and_export.ipynb
```

to create the local model artifact used by the Flask application.
