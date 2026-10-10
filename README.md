# Material complementar do entregável 2

Este pacote contém 10 imagens e suas 581 bounding boxes, selecionadas do arquivo visdrone_calib_256.zip fornecido pela organização. As imagens foram apenas renomeadas; seus bytes e sua resolução foram preservados. Todas as anotações das imagens selecionadas foram mantidas, na ordem dos TXT de origem.

## Preparação

Leia Entregavel_2_Fase_2.pdf. Copie as pastas imagens e dados e o arquivo requirements.txt para a raiz do repositório do exercício. Escreva sua própria solução em src; o pacote fornece apenas o enunciado, as imagens e os dados.

Este README.md descreve o pacote. Crie o seu próprio README.md na raiz do repositório para apresentar a solução, as dependências, os comandos de execução e os controles, conforme o enunciado. A pasta anotacoes_originais não precisa entrar na entrega. O mapeamento_imagens.csv pode ficar em dados para conferência, mas o programa deve ler as caixas de dados/anotacoes.csv.

## Entrada obrigatória

O programa deve ler dados/anotacoes.csv com a biblioteca csv do Python. O arquivo usa UTF-8 sem BOM e vírgula como separador. O cabeçalho é:

imagem,classe_id,x_min,y_min,x_max,y_max

Cada linha é uma caixa. imagem é o nome do JPG dentro da pasta imagens. Os outros cinco campos são inteiros. classe_id mantém os IDs 0 e 1 encontrados no arquivo de origem. Use esses IDs na legenda; o ZIP de origem não inclui um dicionário que confirme nomes de classes.

As coordenadas já estão em pixels da imagem original. (x_min, y_min) é o canto superior esquerdo e (x_max, y_max) é o canto inferior direito, ambos inclusivos. x aumenta para a direita, y aumenta para baixo, e a origem (0, 0) está no canto superior esquerdo. Não trate esses valores como centro, largura ou altura, nem os multiplique pelas dimensões da imagem. A largura da caixa em pixels é x_max - x_min + 1 e sua altura é y_max - y_min + 1.

O CSV contém anotações de referência, não predições de um detector. Não há confiança nem filtro de confiança. Agrupe pelo nome da imagem, crie os objetos e desenhe todas as caixas.

## Conferência e origem

dados/mapeamento_imagens.csv registra o nome original de cada imagem, o novo nome, sua resolução e as quantidades de caixas de cada classe. A tabela abaixo resume o conteúdo:

| Imagem | Resolução | Caixas |
| --- | --- | --- |
| cena_01_parque.jpg | 960 × 540 | 61 |
| cena_02_praca_noturna.jpg | 960 × 540 | 60 |
| cena_03_patio.jpg | 1360 × 765 | 64 |
| cena_04_quadra.jpg | 1360 × 765 | 55 |
| cena_05_rua_noturna.jpg | 960 × 540 | 51 |
| cena_06_cruzamento.jpg | 960 × 540 | 63 |
| cena_07_quadras_aereas.jpg | 1400 × 788 | 53 |
| cena_08_avenida_noturna.jpg | 1400 × 1050 | 61 |
| cena_09_avenida_aerea.jpg | 1400 × 788 | 61 |
| cena_10_onibus.jpg | 1400 × 1050 | 52 |

Total: 581 caixas, sendo 431 da classe 0 e 150 da classe 1.

anotacoes_originais contém uma cópia de cada TXT de origem, com o mesmo nome-base da imagem renomeada. Esses TXT estão no formato YOLO de cinco campos: classe_id, x_centro, y_centro, largura e altura, separados por espaços. Os quatro valores geométricos são normalizados. Esses arquivos servem para rastrear a origem dos dados; a solução do exercício deve usar o CSV.

Na preparação do CSV, os limites esquerdo e superior foram obtidos arredondando (centro - tamanho / 2) × dimensão. Os limites direito e inferior foram obtidos arredondando (centro + tamanho / 2) × dimensão e subtraindo 1, para representar o último pixel incluído. Nenhuma das 581 caixas precisou ser recortada ou removida. As coordenadas e as quantidades foram conferidas contra os TXT e as dimensões dos JPGs.

## Ambiente

requirements.txt contém opencv-python. Use Python 3 e um ambiente com suporte a janelas gráficas. O pacote instalado é importado como cv2; a biblioteca csv já acompanha o Python. Em Linux ou WSL com suporte gráfico, uma opção é:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

As teclas do exercício são Espaço para avançar e q para encerrar. Salve as imagens anotadas em resultados, sem sobrescrever os JPGs de entrada. Se precisar diminuir a imagem na tela, desenhe primeiro na resolução original e redimensione apenas a cópia exibida.

Se q for pressionado antes da última imagem, o programa pode encerrar após salvar a imagem atual; as imagens ainda não processadas não precisam ser geradas. Uma execução completa até o fim deve produzir dez arquivos em resultados.

No Windows PowerShell, a partir da raiz do repositório, é possível usar o executável do ambiente virtual diretamente, sem ativá-lo:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\main.py
```

## Documentação

- Biblioteca csv: https://docs.python.org/3/library/csv.html
- Desenho no OpenCV: https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html
- Janelas e teclado no OpenCV: https://docs.opencv.org/4.x/d7/dfc/group__highgui.html
- Instalação do pacote: https://github.com/opencv/opencv-python
- Conjunto VisDrone: https://github.com/VisDrone/VisDrone-Dataset
