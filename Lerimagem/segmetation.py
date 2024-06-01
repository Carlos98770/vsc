import cv2

imagem = cv2.imread("../google.jpg")
#Padrao do opecv é o BGR
blue,green,red = cv2.split(imagem)

cv2.imshow("Canal R" , red)
cv2.imshow("Canal G" , green)
cv2.imshow("Canal B" , blue)

#Podemos mesclar novamente a imagem

imagem = cv2.merge((blue,green,red))

cv2.imshow("Imagem novamente mesclada",imagem)


#Função cv2.imwrite salva a imagem
cv2.imwrite("../imgs/imagem_red.png",red)
cv2.imwrite("../imgs/imagem_green.png",green)
cv2.imwrite("../imgs/imagem_blue.png",blue)

cv2.waitKey(0)
cv2.destroyAllWindows()