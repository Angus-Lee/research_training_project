import numpy as np
import cv2
import os

res_path = 'D:\\semantic_segmentation\\models-master\\research\\deeplab\\datasets\\yaogan_ADE20K\\ADE20K\\ADEChallengeData2016\\annotations_256_512_1024\\res\\'
src_path = 'D:\\semantic_segmentation\\models-master\\research\\deeplab\\datasets\\yaogan_ADE20K\ADE20K\\ADEChallengeData2016\\annotations_256_512_1024\\validation\\'

for i in range(46):
    for j in range(2501):
        file_name = '{}_{}.png'.format(i,j)
        if os.path.exists(src_path + file_name):
           src_image = cv2.imread(src_path + file_name)
           src_image_copy = src_image.copy()
           src_image_gray = src_image[:,:,0]
           src_image_copy[src_image_gray == 0] = np.array([255, 255, 255])
           src_image_copy[src_image_gray == 1] = np.array([0, 255, 0])
           src_image_copy[src_image_gray == 2] = np.array([255, 0, 0])
           src_image_copy[src_image_gray == 3] = np.array([0, 0, 255])
           src_image_copy[src_image_gray == 4] = np.array([0, 0, 0])
           cv2.imwrite(res_path + file_name, src_image_copy)
