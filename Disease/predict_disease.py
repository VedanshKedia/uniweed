# import matplotlib.pylab as plt
from pathlib import Path
import os
# import tensorflow_hub as hub
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
from Disease.alert import message
# from tensorflow.keras.models import Sequential
import PIL
import numpy as np

def predict(image_path, lang, crop):

    image_path = 'Disease/temp_images/'+image_path
    size=(500,500)
    im = PIL.Image.open(image_path).convert('RGB')
    im = im.resize(size, resample=PIL.Image.LANCZOS)

        
    model = tf.keras.models.load_model('Disease/final_models/{}_model'.format(crop))
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    class_names = {
        'rice': ['Bacterial Leaf Blight', 'Brown Spot', 'False Smut', 'Leaf Blast', 'Neck Blast', 'Sheath Blight']
    }



   
    img_array = np.array(im).astype(float)
    img_array = np.expand_dims(img_array, axis=0).astype(float)
    # print("img_array.shape\n", img_array.shape)
    # img_array.shape

   
    # with graph.as_default():
    # predictions = model.predict(img_array)

    predictions = probability_model.predict(img_array)
    print("\n\nGetting Result from Probability Model\n\n")
    print(predictions)

    conf_score = predictions[0][np.argmax(predictions)]

    print("\nconf_score:\n", conf_score)

    disease_names = class_names[crop]
    if (conf_score>=0.65):
        result = disease_names[np.argmax(predictions)]
        # print("Weed Name: ", result)

        return {'result': result}
    else:
        msg_return = message(2, lang)
        return {'message': msg_return}