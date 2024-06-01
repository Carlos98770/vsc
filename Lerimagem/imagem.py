import cv2

#Função que carrega uma imagem a partir de um arquivo cv2.imread()
imagem = cv2.imread("../Naruto.jpg")

#Funçao que exibe a imagem carregada em uma variavel cv2.imshow()
cv2.imshow("Imagem",imagem)

#Este comando exibe uma janela e espera indefinidamente até que qualquer tecla seja pressionada.
#O argumento 0 indica que a função deve esperar indefinidamente.
cv2.waitKey(0)

#Fecha todas as janelas abertas pelo opencv
cv2.destroyAllWindows()