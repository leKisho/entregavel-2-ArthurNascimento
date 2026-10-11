import cv2 as cv
import sys
from pathlib import Path

class Deteccao:
    def __init__(self, id, x_mn, x_mx, y_mn, y_mx):
        self.class_id = int(id)
        self.x_min = int(x_mn)
        self.x_max = int(x_mx)
        self.y_min = int(y_mn)
        self.y_max = int(y_mx)

    def desenhar(self, imagem):
        if self.class_id == 0:
            cor = (255, 255, 0)
        else:
            cor = (0, 0, 255)

        cv.rectangle(imagem, (self.x_min, self.y_min), (self.x_max, self.y_max), cor, 2)


class ImagemAnotada:
    def __init__(self, caminho_img):
        self.caminho = caminho_img
        self.deteccoes = []
        self.raiz_projeto = Path(__file__).parent.parent

    def adicionarDeteccao(self, id, x_mn, x_mx, y_mn, y_mx):
        novaDetec = Deteccao(id, x_mn, x_mx, y_mn, y_mx)
        self.deteccoes.append(novaDetec)

    def criarImagem(self):
        caminho_leitura = str(self.raiz_projeto / "imagens" / self.caminho)
        caminho_salvar = str(self.raiz_projeto / "resultados" / self.caminho)
        
        img = cv.imread(caminho_leitura)
        
        if img is None:
            sys.exit(f"Erro crítico: A imagem não pôde ser lida no caminho {caminho_leitura}")

        altura, largura = img.shape[:2]
        caixas_desenhadas = 0

        for atual in self.deteccoes:
            if (0 <= atual.x_min < atual.x_max < largura) and (0 <= atual.y_min < atual.y_max < altura):
                atual.desenhar(img)
                caixas_desenhadas += 1

        cv.rectangle(img, (10, 10), (350, 110), (255, 255, 255), -1)
        cv.rectangle(img, (10, 10), (350, 110), (0, 0, 0), 1)
        cv.putText(img, f"Img: {self.caminho}", (20, 35), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv.LINE_AA)
        cv.putText(img, "0: Classe 0", (20, 65), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1, cv.LINE_AA)
        cv.putText(img, "1: Classe 1", (20, 95), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv.LINE_AA)

        cv.imwrite(caminho_salvar, img)
        print(f"[{self.caminho}] {caixas_desenhadas} caixas desenhadas.")

        if altura > 720 or largura > 1280:
            escala = min(1280 / largura, 720 / altura)
            img_exibicao = cv.resize(img, (int(largura * escala), int(altura * escala)))
        else:
            img_exibicao = img

        cv.imshow("Display window", img_exibicao)