from implementation.automatas.af import Automata

def glud_parser(glud):
    states= set(glud['variables'])
    alphabet = set(glud['terminals'])
    initial_state = glud['initial_state']
    final_states = set(['F'])
    transitions = {}
    states.add('F')  

    for prod in glud['productions']:
        esquerda, direita = prod.split('->')
        esquerda = esquerda.strip()
        direita = direita.strip()
       
        if direita == 'ε':
            simbolo = 'ε'
            destino = 'F'
        elif len(direita) == 1:
            simbolo = direita
            destino = 'F'
        elif len(direita) == 2:
            simbolo = direita[0]
            destino = direita[1]
        else:
            continue
        if esquerda not in transitions:
            transitions[esquerda] = {}
        if simbolo not in transitions[esquerda]:
            transitions[esquerda][simbolo] = set()
        
        transitions[esquerda][simbolo].add(destino)


    return Automata(states, alphabet, transitions, initial_state, final_states)



