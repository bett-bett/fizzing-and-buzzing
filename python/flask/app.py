from flask import Flask, request, jsonify

app = Flask(__name__)

def fizzbuzz(n):
  return None

@app.route('/')
@app.route('/index')
def index():
  return "Hello world"

@app.route('/fizzbuzz', methods=['GET'])
def get_fizzbuzz():
    num = request.args.get("num", type=int)
    
    if num is None:
        return jsonify({"error": "Missing query parameter"}), 400
    
    result = fizzbuzz(num)
    return jsonify({"input": num, "output": result})

@app.route('/buzzfizz', methods=['GET', 'POST'])
def get_buzzfizz():
  return "..."
  
@app.route('/about', methods=['GET'])
def a_boat():
  return "boats"
if __name__ == '__main__':
    app.run(debug=True, port=5002)
