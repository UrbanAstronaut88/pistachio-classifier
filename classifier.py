import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("model/pistachio_model.h5")

class_names = ["Kirmizi_Pistachio", "Siirt_Pistachio"]


def prepare_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))
    image = np.array(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)
    return image


def predict_image(image):
    processed_image = prepare_image(image)

    prediction = model.predict(processed_image)
    probability = float(prediction[0][0])

    if probability > 0.5:
        predicted_class = class_names[1]
        confidence = probability
    else:
        predicted_class = class_names[0]
        confidence = 1 - probability

    confidence = round(confidence * 100, 2)

    return predicted_class, confidence
