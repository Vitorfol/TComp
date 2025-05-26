import os

class Automata:
    def __init__(self, state_set, alphabet, transition_function, initial_state, final_states, deterministic=False):
        self.state_set = state_set
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_states = final_states
        self.deterministic = deterministic

    def save_as_txt(self, path=None):
        if path is None:
            nome_arquivo = 'afd.txt' if self.deterministic else 'afn.txt'
            dir_atual = os.path.dirname(os.path.abspath(__file__))
            pasta_filestxt = os.path.abspath(os.path.join(dir_atual, '..', '..', 'filestxt'))
            os.makedirs(pasta_filestxt, exist_ok=True)
            path = os.path.join(pasta_filestxt, nome_arquivo)

        with open(path, 'w', encoding='utf-8') as f:
            tipo = 'AFD Determinizado' if self.deterministic else 'AFN Original'
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
                    for destino in destinos:
                        f.write(f"δ({estado}, {simbolo}) → {destino}\n")
            f.write(f"\nq0:\n{self.initial_state}\n")
            f.write("\nF:\n")
            for final in self.final_states:
                f.write(f"{final}\n")

