from implementation.automatas.af import Automata

def simulate_afd(automata: Automata, string: str) -> bool:
    current_state = automata.initial_state

    for symbol in string:
        current_state = automata.transition_function.get(current_state, {}).get(symbol)

    return current_state in automata.final_states
