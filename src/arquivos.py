import csv
import sys
from pathlib import Path

def carregar_anotacoes():
    eidict = {}
    
    raiz_projeto = Path(__file__).parent.parent
    caminho_csv = raiz_projeto / "dados" / "anotacoes.csv"

    try:
        with open(caminho_csv, mode='r') as arq:
            leitor = csv.reader(arq, delimiter=',')

            for leitura in leitor:
                imagem = leitura[0]
                
                if imagem == "imagem" or len(leitura) < 6:
                    continue
                
                try:
                    for val in leitura[1:6]:
                        int(val)
                except ValueError:
                    sys.exit("Erro: Campos inválidos no CSV.")

                if imagem in eidict:
                    eidict[imagem].append(leitura[1:])
                else:
                    eidict[imagem] = [leitura[1:]]
                    
        return eidict

    except FileNotFoundError:
        sys.exit(f"Erro: CSV não encontrado no caminho {caminho_csv}.")