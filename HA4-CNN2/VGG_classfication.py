from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np

model = VGG16(weights='imagenet')
for i in range(1, 11):
	img_path = '/home/parallels/Desktop/Parallels Shared Folders/Home/Desktop/HKUST/first_term/5012/ha/HA4-CNN2/images/' + str(i) + '.png'
	img = image.load_img(img_path, color_mode="rgb", target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

	features = model.predict(x)

	p = decode_predictions(features)

	print(p)