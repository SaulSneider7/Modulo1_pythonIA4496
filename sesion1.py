# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 1 - Introducción a las imágenes digitales
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:
img = cv2.imread('./img/17.jpg')
imshow('Mi imagen', img)

negro = np.zeros(img.shape, np.uint8)
imshow('Negro', negro)

blanco = 255 * np.ones(img.shape, np.uint8)
imshow('Blanco', blanco)

gris = 150 * np.ones(img.shape, np.uint8) #Puedes cambiar el numero entre 0 y 255
imshow('Gris', gris)

azul = np.zeros(img.shape, np.uint8)
azul[:,:,0] = img[:,:,0]
imshow('Azul',azul)

verde = np.zeros(img.shape, np.uint8)
verde[:, :, 1] = img[:,:,1]
imshow('Verde',verde)

rojo = np.zeros(img.shape, np.uint8)
rojo[:, :, 2] = img[:,:,2]
imshow('Rojo',rojo)
# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
