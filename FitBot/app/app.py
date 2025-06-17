from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # <- this looks for templates/index.html
@app.route('/get_response', methods=['POST'])
@app.route('/get_response', methods=['POST'])
def get_response_route():
    try:
        user_input = request.json['message']
        print("User message:", user_input)

        from chatbot.predict import get_response
        bot_response = get_response(user_input)

        print("Bot response:", bot_response)
        return jsonify({'response': bot_response})
    except Exception as e:
        print("❌ ERROR in /get_response:", str(e))
        return jsonify({'response': "Server error: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
