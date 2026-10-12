# Entregável 2 - Anotações de imagens com OpenCV
#
# Módulo de leitura do arquivo de anotações CSV.
#
# Autor: Arthur Nascimento
# Github.com/leKisho
# ============================================================

import csv
import sys
from pathlib import Path

def carregarAnotacoes():
    
    img_info: dict #Armazena as caixas que serão criadas, atribuidas a um arquivo de imagem
    raiz_projeto: object 
    caminho_csv: str #caminho 

    img_info = {}
    raiz_projeto = Path(__file__).parent.parent #obtem a raiz do arquivo do codigo. Garante que nao haja problema na execução 
                                                #referente ao local em que se executa o codigo
    caminho_csv = str(raiz_projeto / "dados" / "anotacoes.csv")

    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as arq:
            leitor = csv.reader(arq, delimiter=',')

            for leitura in leitor:
                imagem = leitura[0]
                
                if imagem == "imagem" or len(leitura) < 6: # Pula a linha de cabeçalho e ignora linhas vazias ou incompletas
                    continue 
                
                try:
                    for val in leitura[1:6]:
                        int(val) #verifica se todos os valores podem ser convertidos para int
                except ValueError:
                    print("Erro: Campos inválidos no CSV.")
                    sys.exit(-1)

                if imagem in img_info:
                    img_info[imagem].append(leitura[1:]) #adiciona novas caixas ao dict
                else:
                    img_info[imagem] = [leitura[1:]] #cria a key com elementos do dict
                    
        return img_info

    except FileNotFoundError:
        print("Erro: CSV não encontrado no caminho %s." % (caminho_csv))