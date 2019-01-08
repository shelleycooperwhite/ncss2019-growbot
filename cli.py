from bot import on_enter_state, on_input

state = 'NO QUERY'
data = None

while state != 'END':
  on_enter_state(state, data)

  text = input('> ')
  state, data = on_input(state, text, data)
