import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/feature_matrix.csv")

x = df.drop(columns=["genome_id", "resistant_phenotype", "label"])
y = df["label"]

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=33, stratify=y
)

models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=33, n_jobs=-1),
    "XGBoost": xgb.XGBClassifier(n_estimators=100, random_state=33, eval_metric="logloss"),
    "SVM": SVC(kernel="linear", probability=True, random_state=33)
}

res = {}

for name, model in models.items():
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    yprob = model.predict_proba(xtest)[:, 1]

    auc = roc_auc_score(ytest, yprob)
    rep = classification_report(ytest, ypred, output_dict=True)

    res[name] = {
        "AUC": round(auc, 4),
        "F1": round(rep["weighted avg"]["f1-score"], 4),
        "Accuracy": round(rep["accuracy"], 4),
        "model": model
    }

    cm = confusion_matrix(ytest, ypred)
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title(f"{name} - Confusion Matrix")
    plt.ylabel("Real")
    plt.xlabel("Predicted")
    plt.show()

for name in res:
    print(f"\n{name}")
    print(f"  AUC:      {res[name]["AUC"]}")
    print(f"  F1:       {res[name]["F1"]}")
    print(f"  Accuracy: {res[name]["Accuracy"]}")

xgb = res["XGBoost"]["model"]
imp = pd.Series(xgb.feature_importances_, index=x.columns)
top = imp.sort_values(ascending=False).head(20)

top.sort_values().plot(kind="barh")
plt.title("Top 20 Important Genes - XGBoost")
plt.xlabel("Feature Importance")
plt.show()

print("done :)")