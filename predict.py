import tensorflow as tf
import numpy as np

IMG_SIZE = (224, 224)

def predict_plant_disease(image_path, model, class_names):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=IMG_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    preds = model.predict(img_batch)
    pred_idx = np.argmax(preds, axis=1)[0]
    return class_names[pred_idx]

