import os

class Automata:
    def __init__(self, state_set, alphabet, transition_function, initial_state, final_states, deterministic=False):
        self.state_set = state_set
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_states = final_states
        self.deterministic = deterministic

    def save_as_txt(self, name=None):
        if name is None:
            name = 'afd' if self.deterministic else 'afn'

        filename = f"{name}.txt"
        
        dir_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_filestxt = os.path.abspath(os.path.join(dir_atual, '..', '..', 'filestxt'))
        os.makedirs(pasta_filestxt, exist_ok=True)
        path = os.path.join(pasta_filestxt, filename)
        
        tipo_map = {
            'afn.txt': 'AFN Original',
            'afd.txt': 'AFD Determinizado',
            'comp.txt': 'AFD Complemento',
            'rev.txt': 'AFN Reverso',
        }
        tipo = tipo_map.get(filename.lower(), 'Autômato Finito')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"{tipo}\n\n")
            f.write("Q:\n")
            for estado in self.state_set:
                f.write(f"{estado}\n")
            f.write("\nΣ:\n")
            for simbolo in self.alphabet:
                f.write(f"{simbolo}\n")
            f.write("\nδ:\n")
            for estado in self.transition_function:
                for simbolo in self.transition_function[estado]:
                    destinos = self.transition_function[estado][simbolo]
                    if isinstance(destinos, set):
                        for destino in destinos:
                            f.write(f"δ({estado}, {simbolo}) → {destino}\n")
                    else:
                        f.write(f"δ({estado}, {simbolo}) → {destinos}\n")
            f.write(f"\nq0:\n{self.initial_state}\n")
            f.write("\nF:\n")
            for final in self.final_states:
                f.write(f"{final}\n")

