
def read_glud():
    path = 'filestxt/in.txt'
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:]
    
    variables = []
    terminals = []
    productions = []
    initial_state = None

    for line in lines: 

        line = line.strip()
        
        if initial_state is None:
            initial_state = line[0]
            variables.append(initial_state)

        productions.append(line)
        
        if '->' in line:
            esquerda, direita = line.split('->', 1)
            esquerda = esquerda.strip()
            direita = direita.strip()

            if esquerda not in variables:
                variables.append(esquerda)

            for char in direita:
                if char == 'ε':
                    pass
                elif char.isupper() and char not in variables:
                    variables.append(char)
                elif char.islower() and char not in terminals:
                    terminals.append(char)

    glud = {
        'variables' : variables,
        'terminals' : terminals,
        'productions' : productions,
        'initial_state': initial_state 
    }

    return glud


        
            
        

