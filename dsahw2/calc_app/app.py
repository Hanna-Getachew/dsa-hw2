from flask import Flask, render_template, request
from .circle import Circle
from .helper import convert_to_float, perform_calculation  # using a helper.py file

app = Flask(__name__)

@app.route('/')
@app.route('/home')  # now '/' and '/home' show the same page
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        radius = float(request.form['radius'])
        c = Circle(radius)
        result = {
            'perimeter': round(c.perimeter(), 2),
            'area': round(c.area(), 2)
        }
    return render_template('circle.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)