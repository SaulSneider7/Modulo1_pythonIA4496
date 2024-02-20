# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 4 - Crea tu propio filtro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:
# Actividad 1: Utilizar camara web

# Abrir camara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Utiliza la camara hasta que la tecla "q" sea presionada
while True:
    ret, frame = cap.read()

    #comprobar que exista una imagen
    if not ret:
        break

    #Mostrar la imagen en pantalla
    cv2.imshow('Frame', frame)



# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
