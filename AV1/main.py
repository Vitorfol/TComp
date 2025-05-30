from utils.io import read_glud
from implementation.automatas.glud_parser import glud_parser
from implementation.algorithms.determinization import determinize


def main():
    glud = read_glud()
    afn = glud_parser(glud)
    afn.save_as_txt()
    afd = determinize(afn)
    afd.save_as_txt()

if __name__ == "__main__":
    main()