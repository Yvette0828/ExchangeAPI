from flask import Flask, request, jsonify
from exchange_rate_provider import StaticExchangeRateProvider, EXCHANGE_RATES
from currency_converter_service import CurrencyConverterService

# Create Flask application
app = Flask(__name__)

# Initialize exchange rate provider and currency converter service
rate_provider = StaticExchangeRateProvider(EXCHANGE_RATES)
converter_service = CurrencyConverterService(rate_provider)

# Define the route for currency conversion
@app.route('/convert', methods=['GET'])
def convert_currency():
    # Get parameters from the request
    source = request.args.get('source')
    target = request.args.get('target')
    # Check if the amount is a valid number
    try: 
        amount = float(request.args.get('amount'))
    except:
        return jsonify({"msg": "failed", "error": "Invalid parameters, please enter correct format as amount"}), 400

    # Check if currency codes are valid
    if source not in converter_service.exchange_rate_keys() or target not in converter_service.exchange_rate_keys():
        return jsonify({"msg": "failed", "error": "Invalid parameters, please enter "+str(converter_service.exchange_rate_keys())+" as parameter"}), 400

    try:
        # Perform currency conversion
        converted_amount = converter_service.convert(source, target, amount)
        # Format the result to two decimal places and add comma separators
        formatted_number = f'{round(converted_amount, 2):,}'
        return jsonify({
            "msg": "success",
            "amount": formatted_number,
        })
    except KeyError:
        return jsonify({"msg": "failed", "error": "Invalid currency code"}), 400

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
