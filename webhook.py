from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # 🔍 Ver todo lo que llega desde Dialogflow (debug)
    print("🔍 JSON recibido:")
    print(data)

    # ✅ Extraer parámetros
    session_params = data.get("sessionInfo", {}).get("parameters", {})
    print("📦 Parámetros recibidos:")
    print(session_params)

    nombre = session_params.get("name", "desconocido")
    edad = session_params.get("age", "N/A")
    correo = session_params.get("email", "N/A")

    print(f"📥 Recibido desde Dialogflow: {nombre}, {edad}, {correo}")

    # 📁 Guardar en CSV
    archivo_csv = "datos.csv"
    encabezados = ["Nombre", "Edad", "Correo"]

    # Crear el archivo si no existe
    archivo_nuevo = not os.path.isfile(archivo_csv)

    with open(archivo_csv, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if archivo_nuevo:
            writer.writerow(encabezados)
        writer.writerow([nombre, edad, correo])

    # ✅ Respuesta al agente
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": [
                        f"✅ Datos guardados correctamente: {nombre}, {edad}, {correo}"
                    ]
                }
            }]
        }
    })

if __name__ == "__main__":
    app.run(port=5000)
