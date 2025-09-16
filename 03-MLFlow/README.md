# MLFlow
End-to-End, open-source MLOps platform




1. Core components of MLFlow
2. Why Use MLFlow: Experiment Tracking and Hypothesis Testing
3. Who Uses MLFlow: Data Scientists
4. Usecase of MLFlow

### Lifecycle of DS Project
Data Preperation -> EDA -> FE -> Model Training -> Model Validation -> Deployment -> Monitoring

![lifecycle](/assets/03.00-ds-project-lifecycle.png)

### Data Scientists Leverage MLFlow for:

1. Experimentat tracking and hypothesis testing
2. Code Structuring
3. Model packaging and dependency management
4. Evaluating hyperparameter tuning
5. Compare the results of model's retraining over time (i.e., versioning).


### MLFlow for MLOps Professional
1. Manage the lifecycle of trained models, both pre and post deployment.
2. Deploy models security to the production environment.
3. Manage deployment dependencies.


### Install MLFlow
Create venv.

```py
pip install mlflow
```

### MLFlow Tracking Server
In terminal type `mlflow ui` and hit enter. 


### Learning Roadmap
1. Install
2. mlflow.set_tracking_uri("http://127.0.0.1:5000")
3. mlflow ui
4. mlflow.set_experiment("experiment name")
5. with mlflow.start_run():
6. compare runs
7. mlruns directory
8. delete mlruns directory > nothing to display on mlflow ui 