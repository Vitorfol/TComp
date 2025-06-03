# Simulador de Autômato Finito a partir de Gramática Linear Unitária à Direita (GLUD)

Este projeto é um trabalho prático da disciplina **Teoria da Computação** que implementa um simulador de autômato finito gerado a partir de uma **Gramática Linear Unitária à Direita (GLUD)**.

---

## 🔍 Descrição do Projeto

O programa realiza as seguintes etapas:

1. **Conversão da Gramática (GLUD) em AFN** (Autômato Finito Não Determinístico).  
2. **Determinização do AFN para obter um AFD** (Autômato Finito Determinístico).  
3. Aplicação das operações de **reverso** e **complemento** no AFD, resultando em um AFN e um AFD, respectivamente.  
4. **Simulação da execução** de uma cadeia de entrada. 
5. Geração de arquivos `.txt` contendo a formalização do AF de cada etapa.

---

## 🗂 Estrutura do Projeto

```plaintext
automato_simulador/
│
├── main.py                  # Arquivo principal, controla o fluxo geral
├── filestxt/                # Arquivos de entrada e saída
│   ├── in.txt               # Entrada: gramática GLUD e cadeia
│   ├── afn.txt              # AFN gerado após conversão da gramática
│   ├── afd.txt              # AFD após determinização do AFN
│   ├── rev.txt              # AFN reverso
│   ├── comp.txt             # AFD complemento
│
├── implementation/
│   ├── automatas/           # Representação dos autômatos e parser da gramática
│   │   ├── glud_parser.py   # Conversão de GLUD para AFN   
│   │   ├── af.py            # Classe e estrutura de AF's em geral
│   │
│   ├── algoritmos/          # Algoritmos de manipulação dos autômatos
│   │   ├── determinization.py # Algoritmo de determinização: AFN → AFD
│   │   ├── reverse.py       # Algoritmo para reversão do AFD
│   │   ├── complement.py    # Algoritmo para complemento do AFD
│   │   └── simulation.py    # Simulação da cadeia de entrada
│   │
│   └── utils/
│       └── input_processor.py  # Processa e devolve como GLUD o arquivo de entrada
```

---

## ▶️ Como Executar

1. No terminal, navegue até a pasta do projeto:

```powershell
cd AV1
```

2. Execute o arquivo principal passando na cli a cadeia que deseja testar, como por exemplo:

```powershell
python main.py ababa
```

3. O aceite ou rejeite da cadeia será exibido no terminal.

4. Os arquivos de entrada e saída estarão na pasta `filestxt/`.

