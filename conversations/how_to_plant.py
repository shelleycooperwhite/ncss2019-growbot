SEED_TYPES = ['tomato', 'lettuce', 'bean']

# How to plant
def how_to_plant_on_enter_state(data):
  print('What are you planting?')

def how_to_plant_on_input(text, data):
  if text in SEED_TYPES:
    return 'HOW TO PLANT SEED', {'seed': text}

  # If we don't understand, let them know and try this state again.
  else:
    print('Hmm, I don\'t know about that type of seed.')
    return 'HOW TO PLANT', None


# How to plant
# + Seed type
def how_to_plant_seed_on_enter_state(data):
  seed = data['seed']
  print('Here are the instructions for planting ' + seed + '! blah blah blah etc')

def how_to_plant_seed_on_input(data):
  return 'NO QUERY', None
