from flask import Flask, request, jsonify

app = Flask(__name__)

def fizzbuzz(n):
  return [
    ("Fizz" * (i%3==0) + "Buzz" * (i%5==0) or str(i))
    for i in range (1, n+1)
  ]

@app.route('/')
@app.route('/index')
def index():
  routes = [
    f"{rule}{', '.join(rule.arguments)} - method:{', '.join(rule.methods)}"
    for rule in app.url_map.iter_rules()
  ]

  html = "<h1>"
  hello = ("Hello", "world")
  html += " ".join(hello)
  html +="</h1><h2>Available Routes</h2><ul>"
  for route in routes:
    html+=f"<li>{route}</li>"
  html+="</ul>"
  html+="<p>Fizzbuzz through flask api</p>"
  return html

@app.route('/fizzbuzz', methods=['GET'])
def get_fizzbuzz():
  # http://127.0.0.1:5002/fizzbuzz?num=18
    num = request.args.get("num", type=int)
    
    if num is None:
      return jsonify({"error": "Missing query parameter"}), 400
    
    result = fizzbuzz(num)
    return jsonify({"input": num, "output": result})

@app.route('/buzzfizz/<num>', methods=['GET'])
def get_buzzfizz(num):
  # http://127.0.0.1:5002/buzzfizz/18
  if num is None:
    return jsonify({"error": "Missing query parameter"}), 400
  # url variables are string
  result = fizzbuzz(int(num))
  return jsonify({"input": num, "output": result})
  
@app.route('/fizzing/<int:num>', methods=['GET'])
def get_fizzing(num):
  # http://127.0.0.1:5002/buzzfizz/18
  if num is None:
    return jsonify({"error": "Missing query parameter"}), 400
  # url variables are string
  result = fizzbuzz(num)
  return jsonify({"input": num, "output": result})
  
@app.route('/about', methods=['GET',"POST"])
def a_boat():
  return "boats"

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


if __name__ == '__main__':
    app.run()
