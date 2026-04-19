from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="API Clasificación de Tickets")

model = joblib.load("saved_model/ticket_model.pkl")

class Ticket(BaseModel):
    descripcion: str

# Endpoint de prueba
@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

# Endpoint de predicción
@app.post("/predict")
def predecir(ticket: Ticket):
    prediccion = model.predict([ticket.descripcion])[0]
    return {
        "descripcion": ticket.descripcion,
        "prioridad_predicha": prediccion
    }