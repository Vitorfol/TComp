from implementation.automatas.af import Automata

def determinize(Automata): 
    alphabet = Automata.alphabet
    initial_state = eclose(Automata.initial_state, Automata.transition_function)
    state_set = set()
    state_set.add(initial_state)
    transiction_function = {}

    for i in Automata.state_set: 
        state_set.add(eclose(i, Automata.transition_function))
    for i in state_set:
        transiction_function.add(transictions(i, Automata.transition_function))
    
        


def eclose(state, transition_function):
    closure = set()
    stack = [state]

    while stack:
        current = stack.pop()
        if current not in closure:
            closure.add(current)
            for next_state in transition_function.get(current, {}).get('ε', set()):
                stack.append(next_state)

    return closure
      
