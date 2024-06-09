#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
from flask import Flask, request, jsonify
import pandas as pd
from cliente import Cliente
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

app = Flask(__name__)


#━━━━━━━━━━━━━━❮Rota upload❯━━━━━━━━━━━━━━

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            df = pd.read_csv(file)
            
            if 'Valor Monetario' not in df.columns:
                return jsonify({"error": "CSV does not have required 'Valor Monetario' column"}), 400
                
            cliente = Cliente(df)
            stats = cliente.calcular_estatisticas()
            return jsonify(stats)
        except pd.errors.EmptyDataError:
            return jsonify({"error": "File is not a CSV"}), 400
    else:
        return jsonify({"error": "Invalid file type"}), 400


#━━━━━━━━━━━━━━❮Rota Json❯━━━━━━━━━━━━━━

@app.route('/get_json', methods=['POST'])
def get_json():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            df = pd.read_csv(file)
            
            if 'Valor Monetario' not in df.columns:
                return jsonify({"error": "CSV does not have required 'Valor Monetario' column"}), 400
                
            cliente = Cliente(df)
            json_data = cliente.converter_para_json()
            return jsonify(json.loads(json_data))
        except pd.errors.EmptyDataError:
            return jsonify({"error": "File is not a CSV"}), 400
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
