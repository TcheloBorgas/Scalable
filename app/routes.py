from flask import Blueprint, request, jsonify
import pandas as pd
import numpy as np
from .utils import calculate_median, calculate_additional_insights

main = Blueprint('main', __name__)




@main.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "File is not a CSV"}), 400

    try:
        df = pd.read_csv(file)
        # Ensure the 'Valor Monetário' column exists
        if 'Valor Monetário' not in df.columns:
            return jsonify({"error": "CSV does not have required 'Valor Monetário' column"}), 400

        # Calculate the median
        median_value = calculate_median(df['Valor Monetario'])

        return jsonify({
            "message": "Arquivo recebido com sucesso",
            "mediana": median_value
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500






@main.route('/additional_insights', methods=['POST'])
def additional_insights():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "File is not a CSV"}), 400

    try:
        df = pd.read_csv(file)
        required_columns = ["Email", "Nome", "Idade", "Valor Monetario"]
        if not all(column in df.columns for column in required_columns):
            return jsonify({"error": "CSV does not have required columns"}), 400

        insights = calculate_additional_insights(df['Valor Monetario'])

        return jsonify(insights), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
