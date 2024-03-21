import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import RMSprop

# # Load the trained model
#loaded_model = load_model('/home/pi/Desktop/project/led_classification_model_custom_100x100_emil.h5',custom_objects=custom_objects)
loaded_model = load_model('/home/pi/Desktop/project/led_classification_model_custom_100x100_emil.h5',compile = False)
#loaded_model = load_model('/home/pi/Desktop/project/led_classification_model_custom_100x100_emil.h5')

# Now, you can use the loaded_model to make predictions on new images
# Example: Load a new image and preprocess it

from tensorflow.keras.preprocessing import image
import numpy as np

image_size = (100, 100)

# Pillow processed image
# img_path = '/home/pi/Desktop/project/processed-image/processed_image.jpg' 

# cv2 processed image
img_path = '/home/pi/Desktop/project/processed_image.jpg'  

img = image.load_img(img_path, target_size=image_size)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

# Preprocess the image
#img_array /= 255.0
images = np.vstack([img_array])
#classes2 = loaded_model.predictclasses(images,batchsize=10)
#print(classes2)
# Make predictions
predictions = loaded_model.predict(img_array)

# Get the predicted class (LED category)
predicted_class = np.argmax(predictions)
print("predicted Class:",predicted_class)

# You can map the predicted_class to the corresponding LED label based on your dataset 
# LED 1 for class 0 , LED 2 for class 1 etc. 

led_labels = ['LED 1', 'LED 2','LED 3', 'LED 4','LED 5', 'LED 6','LED 7', 'LED 8','LED 9']
predicted_led = led_labels[predicted_class]

print("The predicted LED is:", predicted_led)
