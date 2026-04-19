import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Cargar datos
df = pd.read_csv("data/tickets.csv")

# Variables
X = df["descripcion"]
y = df["prioridad"]

# Separación entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Entrenar
model.fit(X_train, y_train)

# Evaluar
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n")
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(model, "saved_model/ticket_model.pkl")

print("\nModelo guardado en saved_model/ticket_model.pkl")