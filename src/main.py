import cv2 as cv
import sys
from arquivos import carregar_anotacoes
from modelos import ImagemAnotada

def main():
    eidict = carregar_anotacoes()

    for image in sorted(eidict.keys()):
        
        img_obj = ImagemAnotada(image)
        
        for itens in eidict[image]:
            img_obj.adicionarDeteccao(itens[0], itens[1], itens[3], itens[2], itens[4])

        img_obj.criarImagem()

        sair = False
        while True:
            k = cv.waitKey(0)
            if k == ord("q"):
                sair = True
                break
            if k == ord(" "):
                break
                
        if sair:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()