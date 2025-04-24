from flask import Flask, request, jsonify
from utils import (
    get_balance,
    get_balance_batch,
    get_top_holders,
    get_top_holders_with_transactions,
    get_token_info
)

app = Flask(__name__)

# === Level A ===
@app.route('/get_balance')
def balance():
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "Address required"}), 400
    result = get_balance(address)
    return jsonify({"balance": result})

# === Level B ===
@app.route('/get_balance_batch', methods=["POST"])
def balance_batch():
    data = request.get_json()
    addresses = data.get("addresses", [])
    balances = get_balance_batch(addresses)
    return jsonify({"balances": balances})

# === Level C ===
@app.route('/get_top')
def top():
    try:
        n = int(request.args.get("n", 5))
        top_holders = get_top_holders(n)
        return jsonify({"top_holders": top_holders})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Level D ===
@app.route('/get_top_with_transactions')
def top_with_transactions():
    try:
        n = int(request.args.get("n", 5))
        result = get_top_holders_with_transactions(n)
        return jsonify({"top_holders": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Level E ===
@app.route('/get_token_info')
def token_info():
    return jsonify(get_token_info())

if __name__ == '__main__':
    app.run(port=8080)
