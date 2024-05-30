# digit-recognition
**Neural network model for classifying handwritten digits.**

Using the [MNIST](http://yann.lecun.com/exdb/mnist/) database, I created a neural network model that recognizes handwritten digits with an accuracy of **99.3%**. That is, it correctly predicted 9,931 out of 10,000 images.

Network architecture:
- Convolutional layer with 20  feature maps, 5 by 5 local receptive fields and a stride length of 1.
- Max-pooling layer that pulls over 2 by 2 regions.
- Convolutional layer with 40 feature maps, 5 by 5 local receptive fields and a stride length of 1.
- Max-pooling layer that pulls over 2 by 2 regions.
- Fully-connected layer with 1000 neurons using RELU activation.
- Fully-connected layer with 1000 neurons using RELU activation.
- Output layer with 10 neurons using softmax activation.

![image](https://github.com/danielsimon4/digit-recognition/assets/155323325/ff8e876c-14a5-4e47-a343-1b9046b027f1)


Reference:
- http://neuralnetworksanddeeplearning.com/index.html
- https://www.tensorflow.org/tutorials/keras/classification
