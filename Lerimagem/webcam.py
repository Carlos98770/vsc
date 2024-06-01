import cv2

imagem = cv2.VideoCapture("/dev/video1")

while True:
    ret,frame = imagem.read()

    cv2.imshow("Camera",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

