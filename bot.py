from conversations import *


"""
Common states
"""

def no_query_on_enter_state(data):
  print('How can I help?')

def no_query_on_input(text, data):
  # No data
  if text == 'how do I plant seeds':
    return 'HOW TO PLANT', None

  # Seed data
  elif text == 'how do I plant tomato seeds':
    return 'HOW TO PLANT SEED', {'seed': 'tomato'}

  # If we don't know what they're talking about, go to no query
  else:
    print('I don\'t know that command yet!')
    # todo
    print('One day I will suggest some things you can do.')
    return 'NO QUERY', None


"""
Register states
"""

def on_enter_state(state, data):
  if state == 'NO QUERY':
    return no_query_on_enter_state(data)

  elif state == 'HOW TO PLANT':
    return how_to_plant.how_to_plant_on_enter_state(data)

  elif state == 'HOW TO PLANT SEED':
    return how_to_plant.how_to_plant_seed_on_enter_state(data)

  else:
    return 'END', None

def on_input(state, text, data):
  # If they're trying to quit, then quit.
  if text == 'quit':
    return 'END', None

  # Otherwise, do the state thing.
  if state == 'NO QUERY':
    return no_query_on_input(text, data)

  elif state == 'HOW TO PLANT':
    return how_to_plant.how_to_plant_on_input(text, data)

  elif state == 'HOW TO PLANT SEED':
    # End state: go back to no query
    return no_query_on_input(text, data)

  else:
    return 'END', None
