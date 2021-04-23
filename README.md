# General Information
Welcome to my Pokemon drawing GAN. This Project is based off my Adaptive-GAN, which you can find here https://github.com/TrackLab/Adaptive-GAN
I created a video demonstrating the GAN Training process, which you can see here https://www.youtube.com/watch?v=-VwZmGXGNY0&t
There is a pretrained model saved, in the saved_models folder. This one was trained on a single wartortle image only, so the GAN tried to copy it, only outputting wartortle copies.

# Dataset
For the Pokemon dataset I used the Kaggle Pokemon Image Dataset https://www.kaggle.com/kvpratama/pokemon-images-dataset
If you wish to use a different dataset, you can easily use different images.
The Code will resize the image to make them work for the network.

# Usage
Both Grayscale and RGB Images are usable.
Depending on if your dataset is Grayscale or RGB the GAN will train and output as such.
The code includes a simple check wether or not the first Image in the dataset is Grayscale.
Should that check estimate incorrectly, you can overwrite the color mode.
The default image size is 112x112 pixels.
You may change that scale, but then you need to understand how to change the convolutional layers of the generator.

# Important Notes
The code and setup is mostly self explanatory, since most important lines include code for explanation.
If there is something missing or wrong, the code will tell you with simple messages.
During training, the GAN will save its training images after every few epochs. The number of epochs to save a pic after is adjustable.

# Setup
All you need is the python file and a folder called "dataset" containing your images to train on.
Well, you also need the python modules to run the GAN. You can install them using "pip install -r requirements.txt"
The code will resize the images automatically and determine the color space, as mentioned before.
Make sure that the batch size is not more than the amount of images.
The folder "saved_models" and "train_output_images" is created automatically in case it does not exist already.

# Create Images
If you finished training, and wish to create images after training, you can run the create_images.py script, which will let the GAN create as many images as you want.
The code of it is pretty simple.