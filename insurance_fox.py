from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_quote(business_type, revenue, employees):
    """Calculate insurance quote based on business metrics"""
    base_rates = {
        "retail": 0.05,
        "tech": 0.03,
        "manufacturing": 0.08,
        "services": 0.04
    }
    
    rate = base_rates.get(business_type, 0.05)
    annual_quote = revenue * rate + (employees * 100)
    monthly_quote = annual_quote / 12
    
    return {
        "monthly": round(monthly_quote, 2),
        "annual": round(annual_quote, 2)
    }

@app.route('/api/quote', methods=['POST'])
def get_quote():
    data = request.json
    quote = calculate_quote(
        data.get('businessType'),
        data.get('revenue'),
        data.get('employees')
    )
    return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=True)