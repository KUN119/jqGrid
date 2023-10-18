# app.py
from flask import Flask, render_template, send_from_directory, request, jsonify, make_response, json

#Flask 객체 인스턴스 생성
app = Flask(__name__)

# 아래 코드가 없을 때는 data.json을 flask서버에서 받아오질 못함
# Serve static JSON files from the 'static' directory
@app.route('/static/<path:filename>')
def serve_static(filename):
  return send_from_directory('static', filename)

@app.route('/') 
def index():
  return render_template('index.html')

@app.route('/json_example', methods=['POST'])
def handle_json():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    print('content_type == application/json:', content_type)
  else:
    print('content_type:', content_type)
    return "Content type is not supported."
  
@app.route('/json_example2', methods=['POST'])
def handle_json2():
  if request.is_json:
    print('data:jsonnnnnnnn')
    data = json.loads(request.data, strict=False)
    print('Received Data:', data)
  else:
    print('get data error')

@app.route('/editColumn', methods=['POST']) 
def edit_column():
  try:
    print('##################/editColumn##############')
    data = request.get_json()
    print('Received Data:', data)
    
    # Process the data here as needed
    
    # Return a response, for example:
    return jsonify(result='success')
  except Exception as e:
    # Print the error details
    print('Error:', str(e))
    return jsonify(error='Server error'), 500

@app.route('/addColumn', methods=['GET', 'POST'])
def add_column():
  print('##################/addColumn##############')
  response = make_response(jsonify({'message': 'Custom Status'}))
  response.status_code = 201  # Set the desired HTTP status code, e.g., 201 Created
  return response


#이건 왜 되는거야?
@app.route('/delColumn', methods=['GET', 'POST'])
def del_column():
  print('##################/delColumn##############')
  response = make_response(jsonify({'message': 'Custom Status'}))
  response.status_code = 201  # Set the desired HTTP status code, e.g., 201 Created
  return response

if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  app.run(host="127.0.0.1", port="5000", debug=True)
