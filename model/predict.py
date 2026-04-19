import joblib

# Cargar modelo
model = joblib.load("saved_model/ticket_model.pkl")

# Ejemplos de prueba
tickets = [
    "El servidor no responde y nadie puede ingresar al sistema",
    "Necesito cambiar mi contraseña",
    "El sistema está lento al generar reportes"
]

for ticket in tickets:
    prediccion = model.predict([ticket])[0]
    print(f"Ticket: {ticket}")
    print(f"Prioridad predicha: {prediccion}")
    print("-" * 50)