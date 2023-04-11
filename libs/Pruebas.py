##
import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io as io
from skimage.color import rgb2gray, rgba2rgb
from scipy.signal import correlate
import glob
import sklearn.metrics as mt
import argparse
##
sano = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','00000042_007.png'), as_gray=True))
card = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','00000374_000.png'), as_gray=True))
sanoseg = rgba2rgb(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','Sano.png')))
cardseg = rgba2rgb(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','Cardio.png')))

kernel = (sanoseg*sano)[451:723,372:708]
kernel2 = (cardseg*card)[376:933,373:853]
def corr(imagen):
    ne = (imagen - np.mean(imagen)) / (np.std(imagen) * imagen.size)
    fil = (kernel - np.mean(kernel)) / (np.std(kernel) * kernel.size)
    cross = correlate(ne, fil, mode='same', method='auto')
    return np.sum(cross)

images = os.path.join('Rodriguez_Ballesteros_code', 'Datos', 'Imágenes','*.png')
images_list = list(map(io.imread, glob.glob(images)))
images_black = list(map(rgb2gray, images_list))
resul = list(map(corr, images_black))
##
tiene = np.zeros(len(resul))
for i in range (0, len(resul)):
    if resul[i] > 0.03 or resul[i] < 0.015:
        tiene[i] = 1
#np.savetxt(os.path.join('Rodriguez_Ballesteros_code','pred.txt'), tiene)
anotaciones = np.loadtxt(os.path.join('Rodriguez_Ballesteros_code', 'Datos', 'Anotaciones','anotaciones.txt'))
conf_mat = mt.confusion_matrix(anotaciones, tiene, normalize='all')
precision = mt.precision_score(anotaciones, tiene)
recall = mt.recall_score(anotaciones, tiene)
f_score = mt.f1_score(anotaciones, tiene)
accuracy = mt.accuracy_score(anotaciones, tiene)
jaccard = mt.jaccard_score(anotaciones, tiene)

##
anotaciones = np.loadtxt(os.path.join('Rodriguez_Ballesteros_code', 'Datos', 'Anotaciones','anotaciones.txt'))
umbral = [0, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.045, 0.05]
prec_tot = np.array([])
rec_tot = np.array([])
for z in range(0, len(umbral)):
    tiene = np.zeros(len(resul))
    for i in range(0, len(resul)):
        if resul[i] > umbral[z]:
            tiene[i] = 1
    prec_tot = np.append(prec_tot, mt.precision_score(anotaciones, tiene))
    rec_tot = np.append(rec_tot, mt.recall_score(anotaciones, tiene))
plt.plot(rec_tot, prec_tot)
plt.ylabel('precisión')
plt.xlabel('cobertura')
plt.title('Curva de precisión y cobertura\nkernel sano')
##
sano = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','00000042_007.png')))
card = rgb2gray(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','00000374_000.png')))
sanoseg = rgb2gray(rgba2rgb(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','Sano.png'))))
cardseg = rgb2gray(rgba2rgb(io.imread(os.path.join('Rodriguez_Ballesteros_code', 'Modelos','Cardio.png'))))

kernel = (sanoseg*sano)[451:723,372:708]
kernel2 = (cardseg*card)[376:933,373:853]
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(kernel, cmap="gray")
ax[0].set_title('Corazón sano')
ax[0].set_axis_off()
ax[1].imshow(kernel2, cmap="gray")
ax[1].set_title('Corazón con cardiomegalia')
ax[1].set_axis_off()
plt.savefig("Segmentaciones.png")
##
arc = open(os.path.join('Rodriguez_Ballesteros_code','metricas_pred.txt'), 'w')
arc.write('Matriz de confusion:\n')
arc.write(str(conf_mat) + '\n')
arc.write('Precision :' + str(precision) + '\n')
arc.write('Cobertura: ' + str(recall) + '\n')
arc.write('F medida: ' + str(f_score) + '\n')
arc.close()
##
umbral = 135
segmentacion = sano > umbral
da = segmentacion * sano
plt.imshow(segmentacion, cmap='gray')
