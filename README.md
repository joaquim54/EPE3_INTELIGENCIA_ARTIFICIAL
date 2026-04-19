# Clasificador de Tickets con Machine Learning

Proyecto desarrollado por Joaquín Garcés Duarte.

## Descripción

Esta aplicación web permite clasificar tickets de soporte según su nivel de prioridad utilizando Machine Learning.  
La solución fue desarrollada con Python, Scikit-learn, FastAPI y Flask.

El sistema permite:

- entrenar un modelo de clasificación de texto
- predecir la prioridad de tickets de soporte
- consumir predicciones mediante una API REST
- interactuar con el modelo desde una interfaz web

## Tecnologías utilizadas

- Python
- Scikit-learn
- Pandas
- FastAPI
- Flask
- Uvicorn
- Requests
- TailwindCSS

## Estructura del proyecto

```bash
ticket_ml_project/
├── api/
│   └── main.py
├── data/
│   └── tickets.csv
├── model/
│   ├── train_model.py
│   └── predict.py
├── saved_model/
├── web/
│   ├── app.py
│   └── templates/
│       └── index.html
├── requirements.txt
├── README.md
└── .gitignore