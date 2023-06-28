import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

from PIL import Image


def process_image(path):
    img = cv2.imread(path)
    img = np.asarray(img, dtype = "float32")
    img = cv2.resize(img, (540, 420))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img/255.0
    img = np.reshape(img, (420, 540, 1))

    return img


def denoise_image(path: str):
    path_to_model = os.path.abspath(os.curdir) + '\model_learning\model_full.h5'
    model = tf.keras.models.load_model(path_to_model, compile=False)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    size = Image.open(path).size

    predict = [process_image(path)]
    result = model.predict(np.asarray(predict), batch_size=16)

    plt.plot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(result[0][:, :, 0], cmap='gray')

    plt.savefig('1234.png', transparent= True)
    Image.open('1234.png').resize(size).save('1234.png')

    return 0
