import cv2
import numpy as np

from tensorflow.keras.models import load_model

model=load_model(
"brain_tumor_model.h5"
)

img=cv2.imread(
"testMRI.jpg"
)

img=cv2.resize(
img,
(128,128)
)

img=img/255

img=np.expand_dims(
img,
axis=0
)

prediction=model.predict(img)

if prediction>0.5:

    print("Tumor detected")

else:

    print("No Tumor")