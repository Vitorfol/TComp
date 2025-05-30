from implementation.automatas.af import Automata
from collections import deque

def determinize(automata: Automata) -> Automata:

    alphabet = [a for a in automata.alphabet if a != 'ε']
    nfa_transition_function = automata.transition_function

    initial_closure = frozenset(eclose(automata.initial_state, nfa_transition_function))
    unprocessed_states = deque([initial_closure])
    dfa_transition_function = {}
    state_name_map = {initial_closure: "{" + ",".join(initial_closure) + "}"}

    while unprocessed_states:
        current = unprocessed_states.popleft()
        dfa_transition_function[state_name_map[current]] = {}

        for symbol in alphabet:
            reachable = set()
            for substate in current:
                next_states = nfa_transition_function.get(substate, {}).get(symbol, set())
                for ns in next_states:
                    reachable.update(eclose(ns, nfa_transition_function))

            reachable_frozen = frozenset(reachable)
            if reachable_frozen not in state_name_map and reachable:
                state_name_map[reachable_frozen] = "{" + ",".join(reachable_frozen) + "}"
                unprocessed_states.append(reachable_frozen)

            if reachable:
                dfa_transition_function[state_name_map[current]][symbol] = state_name_map[reachable_frozen]

    new_final_states = set()
    for state_set in state_name_map:
        if any(s in automata.final_states for s in state_set):
            new_final_states.add(state_name_map[state_set])

    dead_state = "∅"
    all_states = set(state_name_map.values())
    for state in all_states:
        if state not in dfa_transition_function:
            dfa_transition_function[state] = {}
        for symbol in alphabet:
            if symbol not in dfa_transition_function[state]:
                dfa_transition_function[state][symbol] = dead_state

    dfa_transition_function[dead_state] = {symbol: dead_state for symbol in alphabet}
    state_name_map[dead_state] = "{" + dead_state + "}"

    return Automata(  
        alphabet=alphabet,
        state_set=set(state_name_map.values()),
        initial_state=state_name_map[initial_closure],
        final_states=new_final_states,
        transition_function=dfa_transition_function,
        deterministic=True
    )

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
      
