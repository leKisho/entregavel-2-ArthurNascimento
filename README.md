# Entregável 2 — 2a Fase PS Harpia

## Autor: Arthur Nascimento ;  [GitHub: leKisho](https://github.com/leKisho)

Programa desenvolvido em Python para visualizar imagens com *bounding boxes* a partir de anotações fornecidas em um arquivo CSV.

## Objetivo

O programa lê as anotações de `dados/anotacoes.csv`, agrupa as detecções por imagem e desenha as caixas delimitadoras correspondentes sobre as imagens originais.

O conjunto de dados contém 10 imagens e 581 caixas delimitadoras (*bounding boxes*). Cada caixa representa uma abstração de uma detecção, delimitando a região de um objeto na imagem e associando-a a uma classe identificada por um rótulo numérico binário (0 ou 1). As anotações são fornecidas no arquivo CSV, não sendo predições geradas pelo programa.

As caixas são diferenciadas por cor conforme o identificador da classe:
- **Classe 0:** verde.
- **Classe 1:** azul.

As imagens anotadas são salvas na pasta `resultados`, preservando os arquivos originais.

## Dependências

O programa utiliza Python 3 e a biblioteca OpenCV (`opencv-python`). 

Também são utilizados os seguintes módulos da biblioteca padrão do Python:
- **csv:** leitura dos dados de anotação.
- **pathlib:** manipulação de caminhos de arquivos e diretórios.
- **sys:** acesso a funcionalidades do sistema, incluindo o encerramento do programa em caso de erro.

Os módulos da biblioteca padrão já acompanham o Python e não precisam ser instalados separadamente. Para instalar o OpenCV, execute na raiz do repositório

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Execução

Com as dependências instaladas, execute:

```bash
python src/main.py
```

O programa apresenta as imagens anotadas individualmente, em ordem alfabética.

- **Espaço:** avança para a próxima imagem.
- **q:** encerra a visualização.

As caixas são desenhadas na resolução original antes de qualquer redimensionamento para exibição.

### Exemplo de execução

![Execução do programa no terminal](evidencias/terminal.png)

Durante a execução, as imagens são apresentadas em uma janela de visualização, com a identificação da imagem e a legenda das classes.

![Visualização das imagens anotadas](evidencias/visualizador.png)

## Classes

**Deteccao:** representa uma caixa delimitadora, armazenando o identificador da classe e as coordenadas dos seus limites. Também é responsável por desenhar a caixa na imagem com a cor correspondente.

**ImagemAnotada:** representa uma imagem e suas respectivas detecções. Armazena as informações da imagem, reúne as caixas delimitadoras e gera a versão anotada para salvamento e visualização.
