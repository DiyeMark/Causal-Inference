from pathlib import Path
import dvc.api
import os
import mlflow
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    plot_confusion_matrix,
    precision_score,
    recall_score,
)

# path = "data/data.csv"
# repo = "https://github.com/DiyeMark/Causal-Inference"
# version = None
#
# data_url = dvc.api.get_url(path=path, repo=repo, rev=version)

mlflow.set_experiment("Causal Inference")

if __name__ == '__main__':
    root_dir = Path().cwd()
    data_dir = root_dir / "data"
    metrics_dir = root_dir / "metrics"
    clean_data = pd.read_csv(data_dir / "data_clean.csv")

    standard_scaler = StandardScaler()
    logreg_clf = LogisticRegression()

    X = clean_data.iloc[:, 2:]
    y = clean_data["diagnosis"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = standard_scaler.fit_transform(X_train)
    X_test = standard_scaler.transform(X_test)

    with mlflow.start_run():
        logreg_clf.fit(X_train, y_train)

        y_pred = logreg_clf.predict(X_test)

        accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
        precision = precision_score(
            y_true=y_test, y_pred=y_pred, average="weighted"
        )
        recall = recall_score(y_true=y_test, y_pred=y_pred, average="weighted")
        f1 = f1_score(y_true=y_test, y_pred=y_pred, average="weighted")

        clf_report = classification_report(y_true=y_test, y_pred=y_pred)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1", f1)

        plot_confusion_matrix(
            logreg_clf, X_test, y_test, normalize="true", cmap=plt.cm.Blues
        )

        if not os.path.exists(metrics_dir):
            metrics_dir.mkdir()

        with open(metrics_dir / "results.txt", "w") as metrics_file:
            metrics_file.write(
                f"Accuracy: {accuracy} \n\nClassification Report: \n{clf_report} \n"
            )

        plt.savefig(metrics_dir / "metrics_plot.png")


