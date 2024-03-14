from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
model = load_model("./model/ANN.h5")
model.summary()
image = Image.open("제목 없음.png")
image = image.resize((28, 28)).convert("L") #L흑백 28x28로 변환
image = 255 - np.array(image)
plt.imshow(image, cmap='Greys')
plt.show()
x_test_sample = image.reshape(1, 784).astype("float32") / 255
pred = model.predict(x_test_sample)
print(np.argmax(pred, axis=1))