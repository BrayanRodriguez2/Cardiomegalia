# Se importan las librerias para la funcion de evaluar una imagen
import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io as io
from skimage.color import rgb2gray, rgba2rgb
from scipy.signal import correlate
import glob
# Se define la funcion para evaluar una imagen
def evaluate(image):
    # Se descargan las imagenes de la carpeta 'Modelos' sana y la segmentacion del corazon de la misma
    sano = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos', '00000042_007.png')))
    sanoseg = rgb2gray(rgba2rgb(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos', 'Sano.png'))))
    # Se halla el corazon segmentado como el kernel
    kernel = (sanoseg * sano)[451:723, 372:708]
    # Se lee la imagen que el usuario ingresa
    imagelei = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Datos', 'Imágenes', image)))
    # Se crean las variables ne y fill que corresponden a las imagenes leida y el kernel normalizadas, respectivamente
    ne = (imagelei - np.mean(imagelei)) / (np.std(imagelei) * imagelei.size)
    fil = (kernel - np.mean(kernel)) / (np.std(kernel) * sano.size)
    # Se realiza la cross-correlacion de el kernel y la imagen normalizadas en modo 'same' y automatico
    cross = correlate(ne, fil, mode='same', method='auto')
    # Se suma el resultado de la cross-correlacion
    resul = [np.sum(cross)]
    # Se define un texto por defecto como 'es sano'
    text = 'es sano'
    final = [0]
    # Si el resultado de la cross-correlacion esta entre 0.015 y 0.03 la imagen es con cardiomegalia
    if resul > 0.03 or resul < 0.015:
        # Se cambia el texto por 'tiene cardiomegalia'
        text = 'tiene cardiomegalia'
        final = [1]
    # Se imprime la imagen solicitada
    plt.imshow(imagelei, cmap='gray')
    # Se cambia el titulo como 'La imagen' + 'tiene cardiomegalia' o 'es sano'
    plt.title('La imagen\n'+text)
    # Se eliminan los bordes del plot
    plt.axis('off')
    # Se guarda el resultado como un archivo de texto con nombre 'test_pred.txt'
    np.savetxt(os.path.join('Rodriguez_Ballesteros_code', 'test_pred.txt'), final)