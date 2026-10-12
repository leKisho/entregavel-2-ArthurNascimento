# Entregável 2 - Anotações de imagens com OpenCV
#
# Módulo contendo as classes Deteccao e ImagemAnotada.
#
# Autor: Arthur Nascimento
# Github.com/leKisho
# ============================================================

import cv2 as cv
import sys
from pathlib import Path

class Deteccao: #classe que armazena uma "caixa", uma abstração de deteccão de um objeto
    def __init__(self, id, x_mn, x_mx, y_mn, y_mx):
        self.class_id = int(id)
        self.x_min = int(x_mn)
        self.x_max = int(x_mx)
        self.y_min = int(y_mn)
        self.y_max = int(y_mx)

    def desenhar(self, imagem): #desenha a caixa na imagem segundo os atributos armazenados do objeto
        cor: tuple
        
        if self.class_id == 0: #assume que o class_id é binário
            cor = (255, 255, 0)
        else:
            cor = (0, 0, 255)

        cv.rectangle(imagem, (self.x_min, self.y_min), (self.x_max, self.y_max), cor, 2)


class ImagemAnotada:
    def __init__(self, caminho_img):
        self.caminho = caminho_img
        self.deteccoes = [] #lista de objetos Deteccao (classe acima)
        self.raiz_projeto = Path(__file__).parent.parent

    def adicionarDeteccao(self, id, x_mn, x_mx, y_mn, y_mx):
        novaDetec: object
        
        novaDetec = Deteccao(id, x_mn, x_mx, y_mn, y_mx)
        self.deteccoes.append(novaDetec)

    def criarImagem(self):
        caminho_leitura: str
        caminho_salvar: str
        altura: int
        largura: int
        caixas_desenhadas: int
        escala: float
        texto_img: str

        caminho_leitura = str(self.raiz_projeto / "imagens" / self.caminho)
        caminho_salvar = str(self.raiz_projeto / "resultados" / self.caminho)
        
        img = cv.imread(caminho_leitura)
        
        if img is None:
            print("Erro crítico: A imagem não pôde ser lida no caminho %s" % (caminho_leitura))
            sys.exit(-3)

        altura, largura = img.shape[:2] #pega as dimensões da imagem
        caixas_desenhadas = 0

        for atual in self.deteccoes:
            #Garante que a caixa desenhada fique dentro da imagem de fato
            if (0 <= atual.x_min < atual.x_max < largura) and (0 <= atual.y_min < atual.y_max < altura):
                atual.desenhar(img)
                caixas_desenhadas += 1

        font = cv.FONT_HERSHEY_SIMPLEX
        
        ##Legenda class_id 0
        #cria um retangulo ao lado do texto
        cv.rectangle(img, (10, 15), (25, 30), (255, 255, 0), -1)
        cv.rectangle(img, (10, 15), (25, 30), (0, 0, 0), 1)
        # Texto ao lado do retangulo, em branco com contorno preto
        cv.putText(img, "class_id 0", (35, 28), font, 0.6, (0, 0, 0), 3, cv.LINE_AA)
        cv.putText(img, "class_id 0", (35, 28), font, 0.6, (255, 255, 255), 1, cv.LINE_AA)

        ##Legenda class_id 1
        cv.rectangle(img, (10, 45), (25, 60), (0, 0, 255), -1)
        cv.rectangle(img, (10, 45), (25, 60), (0, 0, 0), 1)
        cv.putText(img, "class_id 1", (35, 58), font, 0.6, (0, 0, 0), 3, cv.LINE_AA)
        cv.putText(img, "class_id 1", (35, 58), font, 0.6, (255, 255, 255), 1, cv.LINE_AA)

        # Nome da imagem na parte inferior da mesma
        texto_img = "Img: %s" % (self.caminho)
        pos_y_inferior = altura - 20
        cv.putText(img, texto_img, (10, pos_y_inferior), font, 0.6, (0, 0, 0), 3, cv.LINE_AA)
        cv.putText(img, texto_img, (10, pos_y_inferior), font, 0.6, (255, 255, 255), 1, cv.LINE_AA)

        cv.imwrite(caminho_salvar, img) #salva a imagem
        print("[%s] %d caixas desenhadas." % (self.caminho, caixas_desenhadas))

        if altura > 720 or largura > 1280: #garante que a imagem caiba na tela do computador, assumindo uma resolução de 
            escala = min(1280 / largura, 720 / altura) #1280x720
            img_exibicao = cv.resize(img, (int(largura * escala), int(altura * escala)))
        else:
            img_exibicao = img

        cv.imshow("Display window", img_exibicao)