import json
import functools
from flask import (
    Flask,
    make_response,
    render_template,
    request,
)

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def demo():
    # Render the HTML form for GET requests
    return render_template('index.html')


@app.route('/demo', methods=['POST'])
def index():
    if request.method == 'POST':
        # Handle the form submission
        name = request.form.get('name')
        age = request.form.get('age')
        # return f"Hello, {name}! You are {age} years old."
        return render_template("demo.html", name=name, age=age)


@app.route('/api/message', methods=["POST"])
def demo_post():
    payload = request.get_json(force=True)
    if 'name' in payload and 'age' in payload:
        response_data = {
            'message': f"Hello, {payload['name']}! You are {payload['age']} years old."
        }
    else:
        response_data = {
            'error': 'Invalid data format.'
        }

        # Return a JSON response
    return make_response(json.dumps(response_data), 200)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
