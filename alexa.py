from flask import Flask, jsonify, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  payload = request.get_json()

  request_type = payload['request']['type']
  if request_type == 'IntentRequest':
    query = payload['request']['intent']['slots']['query']['value']
    response_text = 'You said: ' + query
  else:
    response_text = 'Say something!'

  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': response_text
      }
    },
    'shouldEndSession': False,
  })

if __name__ == '__main__':
  app.run()
