import os
import sys
from utils.input_processor import read_glud
from implementation.automatas.glud_parser import glud_parser
from implementation.algorithms.determinization import determinize
from implementation.algorithms.simulation import simulate_afd
from implementation.algorithms.complement import complement
from implementation.algorithms.reverse import reverse

def main():
    glud = read_glud()
    afn = glud_parser(glud)
    afn.save_as_txt()

    afd = determinize(afn)
    afd.save_as_txt()

    comp = complement(afd)
    comp.save_as_txt("comp")

    rev = reverse(afd)
    rev.save_as_txt("rev") 

    string = sys.argv[1] if len(sys.argv) > 1 else ""
    simulation_result = simulate_afd(afd, string)
    print(f"Cadeia: {string}")
    if(simulation_result): 
        print(f"Cadeia aceita")
    else:
        print(f"Cadeia rejeitada")

    folder = os.path.join(os.path.dirname(__file__), 'filestxt')
    files = [file for file in os.listdir(folder) if file.endswith('.txt') and file != 'in.txt']
    print("Arquivos gerados:", ' '.join(files))
    
if __name__ == "__main__":
    main()