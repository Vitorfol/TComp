import sys
from utils.io import read_glud
from implementation.automatas.glud_parser import glud_parser
from implementation.algorithms.determinization import determinize
from implementation.algorithms.simulation import simulate_afd


def main():
    glud = read_glud()
    afn = glud_parser(glud)
    afn.save_as_txt()
    afd = determinize(afn)
    afd.save_as_txt()

    string = sys.argv[1] if len(sys.argv) > 1 else ""
    simulation_result = simulate_afd(afd, string)
    
if __name__ == "__main__":
    main()