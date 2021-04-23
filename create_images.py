import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Obviously, you need to replace gen_final_5000.h5 with whatever model you wish to use
generator = tf.keras.models.load_model('saved_models/gen_final_5000.h5')

# the random generation of (1, 100) is the shape the GAN expects. If you changed it in the code, you will need to change it in here as well
fin = np.random.randn(1, 100,).astype("float32")
generated_images = generator(fin)

print(len(generated_images))

img = (np.array(generated_images[0]) * 255).astype(np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Saving the GAN output as image.png
plt.axis('off')
plt.imshow(img)
plt.savefig('image.png', dpi=500)
plt.show()
plt.clf()
