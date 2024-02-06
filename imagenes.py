# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Funciones de apoyo e importación de librerias
# -------------------------------------------------------------------------
# ¡No escribas nada en este archivo!

# Importar bibliotecas que se utilizarán
import os
import cv2
import numpy as np

# Hacer carpeta out si no existe:
if not os.path.exists('./out'):
    os.mkdir('./out')


# Función de apoyo para reescalar las imagenes antes de mostrarlas
def imshow(n, i):
    scale_width = 640 / i.shape[1]
    scale_height = 480 / i.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(i.shape[1] * scale)
    window_height = int(i.shape[0] * scale)
    cv2.namedWindow(n, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(n, window_width, window_height)
    cv2.imshow(n, i)


# Funcion para crear ruido de tipo sal y pimienta en la imagen
def noise(image):
    s_vs_p = 0.5
    amount = 0.05
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[tuple(coords)] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[tuple(coords)] = 0
    return out

# ¡No escribas nada en este archivo!
# -------------------------------------------------------------------------
