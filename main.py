import csv
import sys
import cv2 as cv

class Deteccao:
    def __init__(self, class_id, x_min, y_min, x_max, y_max):
        self.class_id = str(class_id)
        self.x_min = int(x_min)
        self.y_min = int(y_min)
        self.x_max = int(x_max)
        self.y_max = int(y_max)

    def desenhar(self, imagem):
        if self.class_id == '0':
            cor = (255, 255, 0)
        else:
            cor = (0, 0, 255)

        cv.rectangle(imagem, (self.x_min, self.y_min), (self.x_max, self.y_max), cor, 1)
        return imagem


class ImagemAnotada:
    def __init__(self, nome_imagem):
        self.nome_imagem = nome_imagem
        self.deteccoes = []

    def adicionar_deteccao(self, class_id, x_min, y_min, x_max, y_max):
        nova_deteccao = Deteccao(class_id, x_min, y_min, x_max, y_max)
        self.deteccoes.append(nova_deteccao)

    def criar_imagem(self):
        caminho_leitura = f"imagens/{self.nome_imagem}"
        img = cv.imread(cv.samples.findFile(caminho_leitura))
        
        if img is None:
            sys.exit(f"Could not read the image: {caminho_leitura}")

        for deteccao in self.deteccoes:
            deteccao.desenhar(img)

        cv.imwrite(f"resultados/{self.nome_imagem}", img)
        cv.imshow("Display window", img)


def main():
    eidict = {}

    with open('dados/anotacoes.csv', mode='r') as arq:
        leitor = csv.reader(arq, delimiter=',')

        imagem = ''
        for leitura in leitor:
            if leitura[0] == imagem:
                eidict[imagem].append(leitura[1:])
            else:
                imagem = leitura[0]
                eidict.update({imagem: [leitura[1:]]})

    if "imagem" in eidict:
        eidict.pop("imagem")

    for image in eidict.keys():
        img_anotada = ImagemAnotada(image)
        
        for itens in eidict[image]:
            img_anotada.adicionar_deteccao(
                class_id=itens[0],
                x_min=itens[1],
                y_min=itens[2],
                x_max=itens[3],
                y_max=itens[4]
            )

        img_anotada.criar_imagem()

        k = cv.waitKey(0)
        if k == ord("q"):
            break
        if k == ord(" "):
            cv.destroyAllWindows()

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()