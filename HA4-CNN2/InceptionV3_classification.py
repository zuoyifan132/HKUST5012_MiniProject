from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from tensorflow.keras.layers import Input

input_tensor = Input(shape=(224, 224, 3))

model = InceptionV3(input_tensor=input_tensor, weights='imagenet', include_top=True)

for i in range(1, 11):
	img_path = '/home/parallels/Desktop/Parallels Shared Folders/Home/Desktop/HKUST/first_term/5012/ha/HA4-CNN2/images/' + str(i) + '.png'
	img = image.load_img(img_path, target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

	preds = model.predict(x)
	# decode the results into a list of tuples (class, description, probability)
	# (one such list for each sample in the batch)
	print('Predicted:', decode_predictions(preds, top=3)[0])