from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traducir', methods=['POST'])
def traducir():
    data = request.get_json()
    texto = data.get('texto', '')
    origen = data.get('origen', 'es')
    destino = data.get('destino', 'en')
    response = requests.post('http://localhost:5001/translate', json={
        "q": texto, "source": origen, "target": destino
    })
    resultado = response.json()
    return jsonify({"traduccion": resultado.get("translatedText", "")})

if __name__ == '__main__':
    app.run(debug=True)
