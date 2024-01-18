from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    # Perform some action here
    return jsonify({'message': 'FLASK: Btn was clicked!'})

@app.route('/send_msg', methods=['POST'])
def send_msg():
    data = request.get_json()  # Get the request body as JSON
    msg = data['msg']  # Get the message from the request body
    # Perform some action with msg here
    return jsonify({'message': 'FLASK: btn was clicked, message was: ' + msg})

if __name__ == '__main__':
    app.run(debug=True)