import cv2

imagem = cv2.imread("../google.jpg")

#Convertendo para tons de cinzas

imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

cv2.imshow("Imagem em tons de cinza", imagem_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()