from flask import Flask, render_template, request, jsonify
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Configuración de Azure
AZURE_KEY = "TU_CLAVE_DE_AZURE"
AZURE_ENDPOINT = "TU_ENDPOINT"

# Inicializar Flask
app = Flask(__name__)

# Cliente de Azure
client = TextAnalyticsClient(endpoint=AZURE_ENDPOINT, credential=AzureKeyCredential(AZURE_KEY))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    texto = data.get("text", "")

    if not texto:
        return jsonify({"error": "No se recibió texto"}), 400

    response = client.analyze_sentiment([texto])[0]
    return jsonify({
        "sentimiento": response.sentiment,
        "confianza": response.confidence_scores
    })

if __name__ == "__main__":
    app.run(debug=True)
