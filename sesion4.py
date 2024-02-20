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

    # Actividad 2: Usar filtros usando la camara
    contraste = 1.2     # Mantenerlo en el rango de 0.0 a 2.0
    brillo = -20        # Mantenerlo en el rango -100 a 100
    nueva = cv2.convertScaleAbs(frame, alpha=contraste, beta=brillo)

    # Mejorar enfoque
    kernel = -1 * np.ones((5, 5), np.float32)
    kernel[2, 2] = 25
    enfoque = cv2.filter2D(nueva, -1, kernel)
    cv2.imshow('Enfoque', enfoque)

    #--------------------------------------------------------------
    # Crear caricatura de la foto

    # Convertir imagen a grises
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Crea bordes de la imagen binaria
    bordes = cv2.adaptiveThreshold(grises, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('Bordes', bordes)

    # Limpiar Bordes
    kernel = np.ones((3, 3), np.uint8)
    dilatacion = cv2.dilate(bordes, kernel)
    cv2.imshow('Dilatacion', dilatacion)

    #-----------------------------------------------------------------
    # Combinar camara y el cambio de fondo

    # Crear imagen binaria
    _, binaria = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
    binaria = cv2.bitwise_not(binaria)

    # Separar la persona de la imagen original
    persona = np.zeros(frame.shape, np.uint8)
    for i in range(3):
        persona[:, :, i] = cv2.bitwise_and(frame[:, :, i], binaria)
    imshow('Persona', persona)

    #Leer fondo
    fondo = cv2.imread("./img/fondo.jpg")
    fondo = cv2.resize(fondo, binaria.shape[::-1])

    # Obtener el fondo con el espacio de la persona
    for i in range(3):
        fondo[:, :, i] = cv2.bitwise_and(fondo[:, :, i], cv2.bitwise_not(binaria))

    #Combinar la persona con el fondo
    persona += fondo
    imshow('Persona', persona)

    #----------------------------------------------------------
    # Cerrar Ventana cuando se presiona la tecla "q"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.destroyAllWindows()
cap.release()
