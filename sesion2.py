# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 2 - Imágenes en blanco y negro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:
# Recordar como leer y mostrar imagenes
img = cv2.imread('./img/14.jpg')
imshow('Mi imagen', img)

#La imagen a escala de grises
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imshow('Gris', grises)

#Histograma
plt.hist(grises.ravel(), 256, [0, 256])
plt.show()

# IMAGEN BINARIA
_, binaria = cv2.threshold(grises, 86, 255, cv2.THRESH_BINARY)
imshow('Binario', binaria)

#Complemento de imagen
complemento = cv2.bitwise_not(binaria)
imshow('Complemento', complemento)

#Operacion de Dilatacion, erosion, apertura y cierre

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binaria, kernel)
imshow('Erosion', erosion)

dilatacion = cv2.dilate(erosion, kernel)
imshow('Dilatacion', dilatacion)

apertura = cv2.morphologyEx(dilatacion, cv2.MORPH_OPEN, kernel)
imshow('Apertura', apertura)

cerradura = cv2.morphologyEx(dilatacion, cv2.MORPH_CLOSE, kernel)
imshow('Cerradura', cerradura)



# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
