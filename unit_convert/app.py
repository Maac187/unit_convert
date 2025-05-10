from flask import Flask, render_template,request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('length.html')

@app.route('/procesar', methods=['POST'])
def length():
    if request.method == 'POST':
        try:
            length = float(request.form["len"])
            unit_from = request.form["unit_from"]
            unit_to = request.form["unit_to"]
            conversion_factors = {
                'cm': 1,
                'm': 100,
                'km': 100000,
                'in': 2.54,
                'ft': 30.48,
                'yd': 91.44,
                'mi': 160934
             }
            if unit_from in conversion_factors and unit_to in conversion_factors:
                converted = length * (conversion_factors[unit_from] / conversion_factors[unit_to])
            else:
                error = "Invalid unit conversion."
                return render_template('result.html', error=error)
        except ValueError:
            error= "Invalid input. Please enter a valid number."
            return render_template('result.html', error=error)
        
        return render_template('result.html', converted=converted, unit_to=unit_to)
    return render_template('length.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/procesar_weight', methods=['POST'])
def weight_conversion():
    if request.method == 'POST':
        try:
            weight = float(request.form["weight"])
            unit_from = request.form["unit_from"]
            unit_to = request.form["unit_to"]
            conversion_factors = {
                'g': 1,
                'kg': 1000,
                'lb': 453.592,
                'oz': 28.3495
            }
            if unit_from in conversion_factors and unit_to in conversion_factors:
                converted = weight * (conversion_factors[unit_from] / conversion_factors[unit_to])
            else:
                error = "Invalid unit conversion."
                return render_template('result.html', error=error)
        except ValueError:
            error= "Invalid input. Please enter a valid number."
            return render_template('result.html', error=error)
        
        return render_template('result.html', converted=converted, unit_to=unit_to)
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/procesar_temperature', methods=['POST'])
def temperature_conversion():
    if request.method == 'POST':
        try:
            temperature = float(request.form["temperature"])
            unit_from = request.form["unit_from"]
            unit_to = request.form["unit_to"]
            if unit_from == 'c' and unit_to == 'f':
                converted = (temperature * 9/5) + 32
            elif unit_from == 'f' and unit_to == 'c':
                converted = (temperature - 32) * 5/9
            elif unit_from == 'c' and unit_to == 'k':
                converted = temperature + 273.15
            elif unit_from == 'k' and unit_to == 'c':
                converted = temperature - 273.15
            elif unit_from == 'f' and unit_to == 'k':
                converted = (temperature - 32) * 5/9 + 273.15
            elif unit_from == 'k' and unit_to == 'f':
                converted = (temperature - 273.15) * 9/5 + 32
            else:
                error = "Invalid unit conversion."
                return render_template('result.html', error=error)
        except ValueError:
            error= "Invalid input. Please enter a valid number."
            return render_template('result.html', error=error)
        return render_template('result.html', converted=converted, unit_to=unit_to)
    return render_template('temperature.html')



 
@app.route('/result')
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)