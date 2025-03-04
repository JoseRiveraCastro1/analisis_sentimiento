from flask import Flask, render_template, request, jsonify
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Configuración de Azure
AZURE_KEY = "4RMlU5dWZczbAMFT8C8NGIx2cLAcLdi9wqPezoodImoL61vGhOIUJQQJ99BCACYeBjFXJ3w3AAAaACOGBT9c"
AZURE_ENDPOINT = "https://testpty.cognitiveservices.azure.com/"

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
