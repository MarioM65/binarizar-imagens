import cv2
import numpy as np

imagem_colorida = cv2.imread('minha_imagem.jpg')  # Substitua pelo nome da sua imagem

if imagem_colorida is None:
    print("Erro ao carregar a imagem.")
    exit()

imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagem Original", imagem_colorida)
cv2.imshow("Imagem em Tons de Cinza", imagem_cinza)
cv2.imshow("Imagem Binarizada", imagem_binarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
