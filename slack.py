from flask import Flask, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/slack/event', methods=['GET', 'POST'])
def slack_event():
  global state, context

  payload = request.get_json()
  print(payload)

  if payload:
    event = payload.get('event')

    # While state is not EXIT, talk to the user.
    if state != 'END':
      state, data, output1 = on_input(state, event.get('text'), context)

      # Enter the new state.
      output2 = on_enter_state(state, context)

      return '{}\n{}'.format(output1, output2)

if __name__ == '__main__':
  app.run()
