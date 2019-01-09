from bot import on_enter_state, on_input

state = 'NO QUERY'
context = None

while state != 'END':
  on_enter_state(state, context)

  text = input('> ')
  state, context = on_input(state, text, context)
