from flask import Flask, request

app = Flask(__name__)

@app.route('/slack/event', methods=['GET', 'POST'])
def slack_event():
  print(request.get_json())
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
