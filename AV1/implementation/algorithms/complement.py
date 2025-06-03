from implementation.automatas.af import Automata

def complement(automata: Automata) -> Automata:
    alphabet = automata.alphabet
    initial_state = automata.initial_state
    transitions = automata.transition_function
    states = automata.state_set

    final_states = set()
    for state in states:
        if state not in automata.final_states:
            final_states.add(state)

    return Automata(states, alphabet, transitions, initial_state, final_states, deterministic=True)