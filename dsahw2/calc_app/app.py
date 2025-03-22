from flask import Flask, render_template, request
from .circle import Circle  # assuming you're in a package

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome!</h1><p>Go to <a href='/circle'>/circle</a> to use the calculator.</p>"

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    print("Route hit!")  # Check that the route is being accessed
    result = None
    if request.method == 'POST':
        print("Form submitted!")
        radius = float(request.form['radius'])
        print(f"Radius received: {radius}")
        c = Circle(radius)
        result = {
            'perimeter': round(c.perimeter(), 2),
            'area': round(c.area(), 2)
        }
        print(f"Result: {result}")
    return render_template('circle.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)



