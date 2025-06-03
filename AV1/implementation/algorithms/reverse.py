from implementation.automatas.af import Automata


def reverse(automata: Automata) -> Automata:

    states = set(automata.state_set)
    alphabet = set(automata.alphabet)
    alphabet.add('ε')  

    new_initial_state = 'qF'
    states.add(new_initial_state)

    final_states = {automata.initial_state}

    new_transition_function = {}

    for f in automata.final_states:
        if f not in new_transition_function:
            new_transition_function[new_initial_state] = {}
        if 'ε' not in new_transition_function[new_initial_state]:
            new_transition_function[new_initial_state]['ε'] = set()
        new_transition_function[new_initial_state]['ε'].add(f)

    for origem in automata.transition_function:
        for simbolo in automata.transition_function[origem]:
            destinos = automata.transition_function[origem][simbolo]
            
            if not isinstance(destinos, set):
                destinos = {destinos}
            for destino in destinos:
                if destino not in new_transition_function:
                    new_transition_function[destino] = {}
                if simbolo not in new_transition_function[destino]:
                    new_transition_function[destino][simbolo] = set()
                new_transition_function[destino][simbolo].add(origem)

    return Automata(
        state_set=states,
        alphabet=alphabet,
        transition_function=new_transition_function,
        initial_state=new_initial_state,
        final_states=final_states,
        deterministic=False  
    )
