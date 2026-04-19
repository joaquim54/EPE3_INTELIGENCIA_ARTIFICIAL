#  Clasificador de Tickets con Machine Learning

Proyecto desarrollado por **Joaquín Garcés Duarte**

---

##  Descripción

Este proyecto consiste en el desarrollo de una aplicación web capaz de **clasificar tickets de soporte** según su nivel de prioridad (Alta, Media o Baja) utilizando técnicas de **Machine Learning**.

El sistema permite ingresar una o múltiples descripciones de incidentes, las cuales son procesadas por un modelo previamente entrenado, entregando una predicción automática de prioridad.

---

##  Objetivo

Implementar una solución completa que integre:

- Entrenamiento de un modelo de Machine Learning
- Exposición del modelo mediante una API REST
- Consumo de la API desde una aplicación web
- Interacción con el usuario a través de una interfaz moderna

---

##  ¿Dónde se utiliza Machine Learning?

El Machine Learning se utiliza en dos etapas clave:

###  Entrenamiento del modelo

Se entrena un modelo de clasificación de texto utilizando:

- **TF-IDF** para vectorización
- **Logistic Regression** como algoritmo de clasificación

El modelo aprende patrones a partir de un dataset etiquetado (`tickets.csv`).

###  Predicción

Una vez entrenado, el modelo es utilizado para predecir la prioridad de nuevos tickets que **no existen en el dataset**, lo que demuestra su capacidad de generalización.

---

##  Arquitectura del sistema

El proyecto está dividido en tres capas:

### Modelo (Machine Learning)


model/
├── train_model.py
└── predict.py


- Entrenamiento del modelo
- Evaluación con métricas (accuracy, precision, recall, F1-score)
- Serialización del modelo (`.pkl`)

---

###  API (FastAPI)


api/
└── main.py


- Expone el modelo como servicio REST
- Endpoint principal: `/predict`
- Permite consumir el modelo desde aplicaciones externas

---

###  Aplicación Web (Flask)


web/
├── app.py
└── templates/
└── index.html


- Interfaz de usuario
- Permite ingresar uno o varios tickets
- Consume la API y muestra resultados dinámicamente

---

##  Tecnologías utilizadas

- Python
- Scikit-learn
- Pandas
- FastAPI
- Flask
- Uvicorn
- Requests
- TailwindCSS

---

##  Estructura del proyecto


ticket_ml_project/
├── api/
├── data/
├── model/
├── saved_model/
├── web/
├── requirements.txt
├── README.md
└── .gitignore


---

##  Instalación y ejecución

### 1. Clonar el repositorio

git clone https://github.com/tu_usuario/tu_repo.git
cd ticket_ml_project
2. Instalar dependencias
pip install -r requirements.txt
3. Entrenar el modelo
python model/train_model.py
4. Ejecutar la API
python -m uvicorn api.main:app --reload

Acceder en:

http://127.0.0.1:8000/docs
5. Ejecutar la aplicación web
python web/app.py

Acceder en:

http://127.0.0.1:5000
 Uso
Ingresar uno o más tickets en el formulario
Para múltiples tickets, escribir uno por línea
El sistema analizará cada ticket de forma independiente
Validaciones implementadas
Campo vacío
Descripciones demasiado cortas
Manejo de errores de conexión con la API
Detección de múltiples tickets pegados en una misma línea (advertencia al usuario)
 Evaluación del modelo

El modelo fue evaluado utilizando:

Accuracy
Precision
Recall
F1-score

Estas métricas permiten medir el desempeño del modelo en la clasificación de tickets.

 Ejemplo

Entrada:

El servidor principal está caído
Necesito cambiar mi contraseña
El sistema está lento

Salida:

Ticket 1 → Alta
Ticket 2 → Baja
Ticket 3 → Media
 Autor

Joaquín Garcés Duarte

Proyecto – Inteligencia Artificial
