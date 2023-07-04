import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import logging

from PIL import Image

logger = logging.getLogger('main')

def process_image(path):
    img = cv2.imread(path)
    img = np.asarray(img, dtype = "float32")
    img = cv2.resize(img, (540, 420))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img/255.0
    img = np.reshape(img, (420, 540, 1))

    return img

def denoise_image(path: str):
    path_to_model = os.path.abspath(os.curdir) + '\model_learning\model_full_aug.h5'
    model = tf.keras.models.load_model(path_to_model, compile=False)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    path_img = os.path.abspath(os.curdir) + path
    size = Image.open(path_img).size

    predict = [process_image(path_img)]
    result = model.predict(np.asarray(predict), batch_size=16)

    plt.plot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.imshow(result[0][:, :, 0], cmap='gray')

    path_img = path_img + '_denoised.png'

    plt.savefig(path_img, bbox_inches='tight', transparent=True)
    Image.open(path_img).resize(size).save(path_img)

    logger.info('User used denoising')

    return path+'_denoised.png'

