# import matplotlib.pylab as plt
from pathlib import Path
import os
# import tensorflow_hub as hub
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
# from tensorflow.keras.models import Sequential
import PIL
import numpy as np

def predict(image_path, lang, crop):

    image_path = 'temp_images/'+image_path
    size=(600,600)
    im = PIL.Image.open(image_path).convert('RGB')
    im = im.resize(size, resample=PIL.Image.LANCZOS)

        
    probability_model = tf.keras.models.load_model('final_models/{}_model'.format(crop))

    class_names = {
        'soybean': ['Acalypha indica L.', 
                    'Alternanthera philoxeroides (Mart.) Griseb', 
                    'Amaranthus viridis Hook. F.', 
                    'Amaranthus spinosus L.', 
                    'Borreria hispida (L.) K. Schum',
                    'Brachiaria erusiformis (J.E.Smith) Griseb', 
                    'Brachiaria reptans Gard. and Hubb.', 
                    'Celosia argentea L.',
                    'Cleome viscosa L.', 
                    'Commelina benghalensis L.', 
                    'Croton bonplandianum Baill.',
                    'Cyperus difformis L.', 
                    'Dactyloctenium aegyptium (L.) Willd', 
                    'Digera arvensis Forssk.',
                    'Digitaria sanguinalis L. (Scop.)', 
                    'Dinebra retroflexa (Vahl) Panzer.',
                    'Echinochloa colona (L.) Link.', 
                    'Echinochloa crusgalli (L.) Beauv.', 
                    'Eleusine indica (L.) Gaertner.',
                    'Eragrostis pilosa L.', 
                    'Euphorbia geniculata Orteg.', 
                    'Euphorbia hirta L.',
                    'Euphorbia hypersifolia L.', 
                    'Euphorbia microphylla Heyneex. Roth.',
                    'Parthenium hysterophorus L.', 
                    'Phyllanthus niruri L.',
                    'Physalis minima L.', 
                    'Portulaca oleracea L.', 
                    'Stellaria media (L.) Vilt.',
                    'Trianthema portulacastrum L.'],
        'rice': ['Cyperus Difformis L', 'Cyperus Difformis L',
                    'Cyperus Haspan L', 'Cyperus Haspan L', 
                    'Cyperus Iria L', 'Cyperus Iria L', 
                    'Cyperus Rotundus L', 'Cyperus Rotundus L', 
                    'Echinochloa Colona (L.) Link', 'Echinochloa Colona (L.) Link',
                    'Echinochloa Crus-Galli (L.) P. Beauv', 'Echinochloa Crus-Galli (L.) P. Beauv',
                    'Monochoria vaginalis', 
                    'Fimbristylis Miliacea (L.) Vahl', 'Fimbristylis Miliacea (L.) Vahl',
                    'Ipomoea Aquatica Forssk', 
                    'Leptochloa Chinensis (L.) Nees', 'Leptochloa Chinensis (L.) Nees', 
                    'Ludwigia adcendes',
                    'Ludwigia Octovalvis (Jacq.) P.H. Raven', 'Ludwigia Octovalvis (Jacq.) P.H. Raven',
                    'Portulaca Oleracea L', 'Sphenoclea Zeylanica Gaertner'],
        'maize': ['Alternanthera sessilis',
                     'Amaranthus viridis',
                     'Celosia argentea',
                     'Chloris barbata',
                     'Cleome viscosa',
                     'Convolvulus arvensis',
                     'Dactyloctenium aegyptium',
                     'Digera arvensis',
                     'Digitaria sanguinalis',
                     'Echinochloa colona',
                     'Echinochloa crus-galli',
                     'Eleusine indica',
                     'Parthenium hysterophorus',
                     'Physalis minima',
                     'Polygonum aviculare',
                     'Polygonum paronychia',
                     'Portulaca oleracea',
                     'Trianthema portulacastrum',
                     'Xanthium strumarium'],
        'wheat': ['Anagallis arvensis',
                    'Avena fatua',
                    'Chenopodium album',
                    'Chenopodium ficifolium',
                    'Chenopodium nutans',
                    'Coronopus didymus',
                    'Convolvulus arvensis'
                    'Fumaria parviflora',
                    'Malva parviflora',
                    'Melilotus albus Medik',
                    'Phalaris minor',
                    'Poa annua',
                    'Portulaca oleracea',
                    'Rumex spp',
                    'Sonchus arvensis',
                    'Spergula arvensis',
                    'Vicia sativa'],
        'cotton': ['Amaranthus viridis',
                    'Cynodon dactylon',
                    'Cyperus rotundus',
                    'Dactyloctenium aegyptium',
                    'Digitaria sanguinalis',
                    'Echinochloa colona',
                    'Echinochloa crus-galli',
                    'Eleusine indica',
                    'Eragrostis minor',
                    'Euphorbia hirta',
                    'Euphorbia spp',
                    'Portulaca oleracea',
                    'Trianthema portulacastrum']
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

    weed_names = class_names[crop]
    if (conf_score>=0.2):
        result = weed_names[np.argmax(predictions)]
        # print("Weed Name: ", result)

        return {'result': result}
    else:
        msg_return = message(2, lang)
        return {'message': msg_return}