from flask import Flask, jsonify, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  global state, context
  payload = request.get_json()
  print(payload)

  request_type = None
  if payload['request']:
    request_type = payload['request']['type']

  try:
    request_query = payload['request']['intent']['slots']['query']['value']
  except KeyError:
    request_query = ''

  # We are starting, so we should reset the state
  if request_type == 'LaunchRequest':
    state = 'NO_QUERY'
    context = None
    print('Launched, resetting state')

  elif request_type == 'IntentRequest':
    print(f'Processing {request_query} with ({state}, {context})')

    # Intents will have some input, so we need to process it
    # Change the conversation state based on the message from the user

    state, context, output = on_input(state, context, request_query)
    print(f'Result ({state}, {data})')

  # Do something based on the state
  print(f'Starting on enter ({state}, {data})')
  on_enter_state(state, context)

  # Build our response
  print(f'Giving response {output}')

  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': output
      },
      'shouldEndSession': False,
    },
  })

if __name__ == '__main__':
  app.run()
