Este proyecto fue rezlizado para el trabajo de fin de curso de 
análisis y procesamiento de imagenes
Fue realizado con fines netamente educativos
La base de datos de las radiografias torácicas NO son de nuestra
autoría
La base de datos de radiograf´ıa de tórax subministrada
por NIH Clinical Center, consiste en más de 112000
imágenes, de las cuales se estudiaron solo 276 para efectos
prácticos de procesamiento.


Este programa requiere las siguientes librerias:
numpy					v 1.18.1
matplotlib.pyplot			v 3.3.4
os					
skimage.io				v 0.18.1
skimage.color.rgb2gray y rgba2rgb	v 0.18.1
scipy.signal.correlate			v 1.6.0
glob
sklearn.metrics				v 0.24.1
argparse

Versión de Python 3.8

ASEGURESE DE TENER LAS LIBRERIAS DISPONIBLES PARA QUE EL 
PROGRAMA FUNCIONE
** Las librerias fueron ejecutadas con las versiones 
especificadas
---------------------------------------------------------------
El programa hace uso de la libreria disponible y descargada en
este .zip disponible en \libs\trainer.py
---------------------------------------------------------------
El programa genera archivos de texto para consulta de 
resultados en la carpeta de origen del programa así:
\Rodriguez_Ballesteros_code
'pred.txt' es el archivo de texto con las predicciones
organizada de acuerdo a la organizacion de la carpeta 
\Datos\Imágenes
'metricas_pred.txt' es el archivo de texto con las metricas
resultado del programa aplicado a las imágenes en 
\Datos\Imágenes
'test_pred.txt' es el archivo de texto resultado de aplicar
el programa a una imágen seleccionada de \Datos\Imágenes
De igual forma no son necesarios para la funcionalidad de la 
aplicación.
---------------------------------------------------------------
En la carpeta \Datos\Anotaciones encuentra un archivo excel con
nombre Anotaciones por nombre con las anotaciones de cada
imágen
---------------------------------------------------------------
Al correr el programa con el comando python main.py --image
se pide un imagen para evaluar si tiene o no cardiomegalia
para ello puede buscar una imagen disponible en:
\Datos\Imágenes\"número de imagen".png
De igual forma aquí hay una lista de las imagenes disponibles
00000001_000.png
00000001_001.png
00000001_002.png
00000002_000.png
00000005_000.png
00000005_001.png
00000005_002.png
00000005_003.png
00000005_004.png
00000005_005.png
00000006_000.png
00000007_000.png
00000008_000.png
00000008_001.png
00000011_001.png
00000011_002.png
00000011_003.png
00000011_004.png
00000011_008.png
00000013_000.png
00000013_008.png
00000013_014.png
00000013_015.png
00000013_016.png
00000013_017.png
00000013_019.png
00000013_025.png
00000013_026.png
00000013_027.png
00000013_028.png
00000013_029.png
00000013_030.png
00000013_037.png
00000013_038.png
00000013_040.png
00000013_044.png
00000013_045.png
00000014_000.png
00000015_000.png
00000016_000.png
00000017_001.png
00000017_002.png
00000018_000.png
00000022_000.png
00000023_000.png
00000023_001.png
00000023_003.png
00000029_000.png
00000031_000.png
00000032_000.png
00000032_001.png
00000032_004.png
00000032_007.png
00000032_021.png
00000032_027.png
00000032_028.png
00000032_029.png
00000032_030.png
00000032_031.png
00000032_032.png
00000032_037.png
00000032_040.png
00000032_042.png
00000032_044.png
00000032_045.png
00000032_046.png
00000032_048.png
00000032_049.png
00000032_051.png
00000032_053.png
00000032_055.png
00000032_056.png
00000032_059.png
00000032_060.png
00000033_000.png
00000034_001.png
00000035_000.png
00000035_001.png
00000037_000.png
00000038_000.png
00000038_002.png
00000038_003.png
00000038_004.png
00000038_005.png
00000038_007.png
00000039_000.png
00000039_001.png
00000039_002.png
00000039_003.png
00000040_000.png
00000040_002.png
00000041_003.png
00000041_004.png
00000042_000.png
00000042_001.png
00000042_002.png
00000042_003.png
00000042_004.png
00000042_005.png
00000042_007.png
00000042_008.png
00000044_002.png
00000045_000.png
00000046_000.png
00000047_000.png
00000047_001.png
00000047_002.png
00000047_005.png
00000047_007.png
00000048_000.png
00000049_001.png
00000049_002.png
00000050_000.png
00000050_001.png
00000050_002.png
00000050_003.png
00000052_000.png
00000052_001.png
00000054_002.png
00000054_003.png
00000054_004.png
00000054_005.png
00000054_007.png
00000054_008.png
00000054_009.png
00000055_000.png
00000057_000.png
00000057_001.png
00000057_003.png
00000059_000.png
00000059_001.png
00000061_016.png
00000061_019.png
00000061_021.png
00000061_022.png
00000064_000.png
00000065_000.png
00000067_002.png
00000068_000.png
00000069_000.png
00000070_000.png
00000071_003.png
00000073_000.png
00000073_001.png
00000073_003.png
00000073_004.png
00000073_005.png
00000073_006.png
00000073_007.png
00000073_008.png
00000073_009.png
00000075_000.png
00000075_001.png
00000077_000.png
00000078_000.png
00000080_000.png
00000080_002.png
00000080_003.png
00000080_005.png
00000081_000.png
00000082_000.png
00000083_000.png
00000085_000.png
00000086_000.png
00000087_000.png
00000087_001.png
00000088_000.png
00000090_000.png
00000090_001.png
00000090_002.png
00000090_006.png
00000090_007.png
00000090_010.png
00000091_000.png
00000091_006.png
00000091_007.png
00000092_000.png
00000096_000.png
00000096_001.png
00000096_005.png
00000103_001.png
00000116_000.png
00000116_010.png
00000116_013.png
00000116_016.png
00000116_031.png
00000116_032.png
00000116_034.png
00000116_037.png
00000116_040.png
00000123_000.png
00000124_000.png
00000128_000.png
00000131_001.png
00000131_002.png
00000155_000.png
00000156_000.png
00000156_001.png
00000176_001.png
00000176_002.png
00000200_001.png
00000211_001.png
00000211_002.png
00000211_004.png
00000211_005.png
00000211_006.png
00000211_007.png
00000211_008.png
00000211_009.png
00000211_010.png
00000211_011.png
00000211_012.png
00000211_013.png
00000211_014.png
00000211_016.png
00000211_018.png
00000211_019.png
00000211_021.png
00000211_022.png
00000211_024.png
00000211_034.png
00000211_035.png
00000211_037.png
00000211_038.png
00000211_039.png
00000211_041.png
00000211_043.png
00000221_000.png
00000233_000.png
00000240_000.png
00000271_004.png
00000272_000.png
00000284_004.png
00000284_005.png
00000287_000.png
00000294_000.png
00000330_000.png
00000333_000.png
00000338_000.png
00000374_000.png
00000377_000.png
00000377_001.png
00000377_003.png
00000377_004.png
00000398_006.png
00000406_000.png
00000409_001.png
00000432_000.png
00000435_000.png
00000442_000.png
00000442_001.png
00000442_002.png
00000442_003.png
00000448_000.png
00000457_002.png
00000457_003.png
00000457_004.png
00000459_029.png
00000459_032.png
00000459_045.png
00000459_046.png
00000468_029.png
00000498_003.png
00000512_001.png
00000512_002.png
00000547_005.png
00000578_000.png
00000579_001.png
00000607_000.png
00000608_001.png
00000646_006.png
00000661_000.png
00000661_001.png
00000683_002.png
00000688_001.png
00000728_000.png
---------------------------------------------------------------
Las imagenes y anotaciones no son de nuestra autoría.
La base de datos fue obtenida de https:
//nihcc.app.box.com/v/ChestXray-NIHCC
del centro clínico de los NIH.

Agradecemos a los colaboradores por su base de datos.
---------------------------------------------------------------
Referencia:
Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu,
Mohammadhadi Bagheri, Ronald Summers, ChestXray8:
Hospital-scale Chest X-ray Database and
Benchmarks onWeakly-Supervised Classification and
Localization of Common Thorax Diseases, IEEE
CVPR, pp. 3462-3471, 2017. Disponible: https://
nihcc.app.box.com/v/ChestXray-NIHCC
