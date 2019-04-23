# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:16:14 2019

@author: pe.santos
"""

import cv2

vidcap = cv2.VideoCapture('Video01.mp4')    # Leitura do vídeo original
success,image = vidcap.read()
height, width, layers = image.shape
videoMedia = cv2.VideoWriter('MediaVideo.avi', 0, 25, (width,height))   # Propriedades do video Media
videoMediana = cv2.VideoWriter('MedianaVideo.avi', 0, 25, (width,height))   # Propriedades do video Mediana
count = 0
success = True
while success:
  # Aplicação filtro media e escrita do frame para o videoMedia
  img_filtro_media = cv2.blur(image, ( 5, 5))
  videoMedia.write(img_filtro_media)
  # Aplicação filtro mediana e escrita do frame para o videoMediana
  img_filtro_mediana = cv2.medianBlur(image, 3)
  videoMediana.write(img_filtro_mediana)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
videoMedia.release()
videoMediana.release()
