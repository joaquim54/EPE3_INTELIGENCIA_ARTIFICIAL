from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/predict"

def interpretar_prioridad(prioridad: str) -> tuple[str, str]:
    prioridad = prioridad.strip().capitalize()

    if prioridad == "Alta":
        return "El ticket parece requerir atención inmediata.", "alta"
    elif prioridad == "Media":
        return "El ticket presenta una urgencia intermedia y debería revisarse pronto.", "media"
    else:
        return "El ticket parece corresponder a una solicitud de menor urgencia.", "baja"

def parece_ticket_pegado(texto: str) -> bool:
    """
    Detecta de forma simple si parece haber más de una incidencia
    pegada en la misma línea.
    """
    patrones = [
        r"[a-záéíóúñ][A-ZÁÉÍÓÚÑ]",   # ejemplo: laboralNo
        r".{45,}(No\s+\w+)",         # frase larga seguida de 'No ...'
        r".{45,}(Necesito\s+\w+)",   # frase larga seguida de 'Necesito ...'
        r".{45,}(Consulta\s+\w+)",   # frase larga seguida de 'Consulta ...'
        r".{45,}(Problema\s+\w+)",   # frase larga seguida de 'Problema ...'
        r".{45,}(El\s+sistema\s+)",  # frase larga seguida de otro inicio típico
    ]
    return any(re.search(patron, texto) for patron in patrones)

@app.route("/", methods=["GET", "POST"])
def index():
    descripcion = ""
    error = None
    advertencia = None
    resultados = []

    if request.method == "POST":
        descripcion = request.form.get("descripcion", "").strip()

        if not descripcion:
            error = "Debe ingresar al menos una descripción de ticket."
        else:
            tickets = [linea.strip() for linea in descripcion.splitlines() if linea.strip()]

            if len(tickets) == 1 and parece_ticket_pegado(tickets[0]):
                advertencia = (
                    "La entrada parece contener más de un ticket pegado en una misma línea. "
                    "Sepárelos dejando un ticket por línea para obtener resultados independientes."
                )

            if not tickets:
                error = "Debe ingresar al menos una descripción válida."
            else:
                for i, ticket in enumerate(tickets, start=1):
                    if len(ticket) < 10:
                        resultados.append({
                            "indice": i,
                            "descripcion": ticket,
                            "prioridad": "Inválido",
                            "tipo": "error",
                            "mensaje": "La descripción es demasiado corta para analizarla."
                        })
                        continue

                    try:
                        response = requests.post(
                            API_URL,
                            json={"descripcion": ticket},
                            timeout=5
                        )

                        if response.status_code == 200:
                            data = response.json()
                            prioridad = data.get("prioridad_predicha", "Sin resultado")
                            mensaje, tipo = interpretar_prioridad(prioridad)

                            resultados.append({
                                "indice": i,
                                "descripcion": ticket,
                                "prioridad": prioridad,
                                "tipo": tipo,
                                "mensaje": mensaje
                            })
                        else:
                            resultados.append({
                                "indice": i,
                                "descripcion": ticket,
                                "prioridad": "Error",
                                "tipo": "error",
                                "mensaje": f"La API respondió con código {response.status_code}."
                            })

                    except requests.exceptions.ConnectionError:
                        resultados.append({
                            "indice": i,
                            "descripcion": ticket,
                            "prioridad": "Error",
                            "tipo": "error",
                            "mensaje": "No se pudo conectar con la API."
                        })

                    except requests.exceptions.Timeout:
                        resultados.append({
                            "indice": i,
                            "descripcion": ticket,
                            "prioridad": "Error",
                            "tipo": "error",
                            "mensaje": "La API tardó demasiado en responder."
                        })

                    except Exception:
                        resultados.append({
                            "indice": i,
                            "descripcion": ticket,
                            "prioridad": "Error",
                            "tipo": "error",
                            "mensaje": "Ocurrió un error inesperado en la aplicación."
                        })

    return render_template(
        "index.html",
        descripcion=descripcion,
        error=error,
        advertencia=advertencia,
        resultados=resultados
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)