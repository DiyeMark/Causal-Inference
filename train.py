import dvc.api
import mlflow
import pandas as pd

path = "data/data.csv"
repo = "https://github.com/DiyeMark/Causal-Inference"
version = None

data_url = dvc.api.get_url(path=path, repo=repo, rev=version)

mlflow.set_experiment("Causal Inference")

if __name__ == "__main___":

    data = pd.read_csv(data_url, sep=",")

    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)

    mlflow.log_artifact("data/data.csv")
