# Entregável 2 - Anotações de imagens com OpenCV
#
# Programa principal para organizar as anotações e exibir 
# as imagens de forma interativa.
#
# Autor: Arthur Nascimento
# Github.com/leKisho
# ============================================================

import cv2 as cv
from arquivos import carregarAnotacoes 
from modelos import ImagemAnotada

def main():

    img_info: dict #Armazena as caixas que serão criadas, atribuidas a um arquivo de imagem
    sair: bool #condição de quebra do loop - q pressionado para sair
    k: int #valor equivalente da tecla na tabela ASCII
    img_obj: object 

    img_info = carregarAnotacoes()

    for image in sorted(img_info.keys()):
        
        img_obj = ImagemAnotada(image) #cria o objeto, inicializando com o nome da imagem
        
        for itens in img_info[image]:
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
    
    return 0

if __name__ == "__main__":
    main()