import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import yaml
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from mlflow.models import infer_signature
import os 
import mlflow

from sklearn.model_selection import train_test_split, GridSearchCV
from urllib.parse import urlparse

# go to dagshub > remote > experiments > mlflow uri
os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/SagarChhabriya/my-first-repo.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "SagarChhabriya"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "82d61c84a75b08fa1d7ca779ba1d976509e76f00"



def hyperparameter_tuning(X_train, y_train, param_grid):
    rf = RandomForestClassifier()
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    return grid_search.fit(X_train, y_train)


params = yaml.safe_load(open('params.yaml'))['train']

def train(data_path, model_path, random_state, n_estimators, max_depth):
    data = pd.read_csv(data_path)
    X = data.drop(columns=['Outcome'])
    y = data['Outcome']

    mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])

    with mlflow.start_run():

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        signature = infer_signature(X_train, y_train)

        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [5,10, None],
            'min_samples_split': [2,5],
            'min_samples_leaf': [1,2]
        }

        grid_search = hyperparameter_tuning(X_train, y_train, param_grid)


        best_model = grid_search.best_estimator_

        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")

        # Logging
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_param("best_n_estimator", grid_search.best_params_['n_estimators'])
        mlflow.log_param("best_max_depth", grid_search.best_params_['max_depth'])
        mlflow.log_param("best_sample_split", grid_search.best_params_['min_samples_split'])
        mlflow.log_param("best_sample_leaf", grid_search.best_params_['min_samples_leaf'])

        cm = confusion_matrix(y_test, y_pred)
        cr = classification_report(y_test, y_pred)

        mlflow.log_text(str(cm), "confusion_matrix.txt")
        mlflow.log_text(cr, "classification_report.txt")

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Example of input_example (one row of X_train)
        input_example = X_train.iloc[0].to_dict() 

        if tracking_url_type_store!="file":
            mlflow.sklearn.log_model(best_model, "model", registered_model_name="Best Model", signature=signature, input_example=input_example)  
        else:
            mlflow.sklearn.log_model(best_model, "model", signature=signature)

        # Create the directory to save the model
        os.makedirs(os.path.dirname(model_path), exist_ok=True)

        filename = model_path
        pickle.dump(best_model, open(filename, "wb"))

        print(f"Modle save to {model_path}")


if __name__ == "__main__":
    train(params['data'], params['model'], params['random_state'], params['n_estimators'], params['max_depth'])