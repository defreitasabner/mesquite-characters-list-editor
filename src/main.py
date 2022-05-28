import re

filename = 'matrix.txt'

with open(filename, mode='r', encoding='utf-8') as file:
  
  pattern_description = '([0-9]+)[.][ ](.+)'
  pattern_states = '([0-9]+)[ ](.+)'
  characters_list = []

  lines_raw = file.readlines()

  lines = []

  for line in lines_raw:
    line_treated = line.strip()
    if(line_treated != ''):
      lines.append(line_treated)
  
  character = None

  for line in lines:

    if(character == None):
      character = {'description': line.strip(), 'states': []}

    elif(re.match(pattern_description, line) and len(character['states']) == 0):
      character['description'] = line.strip()

    elif(re.match(pattern_states, line)):
      states_re_group = re.match(pattern_states, line)
      character['states'].append({states_re_group.group(1): states_re_group.group(2)})

    elif(re.match(pattern_description, line) and len(character['states']) != 0):
      characters_list.append(character)
      character = {'description': line.strip(), 'states': []}

  characters_list.append(character)

  with open('output.txt', mode='w', encoding='utf-8') as output_file:
    for character in characters_list:
      character_description = character['description']
      character_states = character['states']
      character_states_string = ''
      for state in character_states:
        state_key, state_value = list(state.items())[0]
        state_string = f'({state_key}) {state_value}, '
        if(character_states.index(state) == len(character_states) - 1):
          state_string = state_string.replace(',', '.')  
        character_states_string += state_string
      line_string = f'{character_description}: {character_states_string}\n'
      output_file.write(line_string)